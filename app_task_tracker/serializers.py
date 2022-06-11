from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import Team, Task
User = get_user_model()
import ast
# USER ACCOUNTS SERIALIZER

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'username', 'role') # FIXME: REMOVE ROLE
        extra_kwargs = {
            'full_name': {'read_only': True},
            'username': {'read_only': True},
        }

# TEAM SERIALIZER
class TeamSerializer(serializers.ModelSerializer):
    leader = AccountSerializer(read_only=True)
    leader_id = serializers.IntegerField(write_only=True)
    members = AccountSerializer(many=True, read_only=True)
    member_ids = serializers.CharField(write_only=True, required=False)
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Team
        fields = ('name', 'slug', 'leader', 'leader_id', 'members','member_ids',  'created_by', 'created_at', 'updated_at')
        read_only_fields = ('slug', )
        extra_kwargs = {
            'leader_id': {'required': True},
        }
    # def to_representation(self, obj):
    #     return {
    #         'name': obj.name,
    #         'slug': obj.slug,
    #     }


    def create(self, validated_data):
        request = self.context.get("request")
        if request.user.role != 'user':
            raise serializers.ValidationError({'error': 'You do not have permission to create a team.'})        

        try:
            return Team.objects.create(created_by=request.user, **validated_data)

        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error) from e

    
    def update(self, instance, validated_data):
        request = self.context.get("request")

        # Flexible Multi ID Input
        member_ids = ast.literal_eval(validated_data.pop('member_ids')) if validated_data.get('member_ids') else None
        members_id_list = [member_ids] if type(member_ids) == int else member_ids
        
        if member_ids and request.user.role == 'leader':           
            members = User.objects.filter(role='member', id__in=members_id_list)
        else:
            raise serializers.ValidationError({'error': 'You do not have permission to update the team.'})
        
        instance.members.set(members)
        return instance
    

    

    # def validate(self, data):
    #     data['slug'] = slugify(data['name'])
    #     return data