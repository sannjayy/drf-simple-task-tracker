from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import get_user_model
import ast
from .models import Team, Task
User = get_user_model()

# USER ACCOUNTS SERIALIZER
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'username', 'role') # FIXME: REMOVE ROLE
        extra_kwargs = {
            'full_name': {'read_only': True},
            'username': {'read_only': True},
        }


# TASK SERIALIZER
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'team', 'title', 'slug', 'description', 'priority', 'assigned_to', 'status',  'started_at', 'completed_at', 'created_by', 'updated_by', 'updated_at', 'created_at')
        read_only_fields = ('slug', 'id', 'started_at', 'completed_at', 'updated_by', 'updated_at', 'created_by', 'created_at')
    
    def to_representation(self, obj):
        # representation = super().to_representation(obj)
        return {            
            'id': obj.id,
            'title': obj.title,
            'slug': obj.slug,
            'description': obj.description,
            'priority': obj.priority,
            'current_status': obj.status,
            'assigned_to': obj.assigned_to.full_name if obj.assigned_to else None,
            'started_at': obj.started_at, 
            **({'completed_at': obj.completed_at} if obj.is_completed else {}), # If status is `Done`
            'last_modified_by': obj.updated_by.full_name if obj.updated_by else None,     

            'info': {
                'created_by': obj.created_by.full_name or None,                    
                'updated_at': obj.updated_at,
                'created_at': obj.created_at,
            },
            'team': {
                'id': obj.team.id,
                'name': obj.team.name,
                'slug': obj.team.slug,
            },  
        }

    def create(self, validated_data):
        request = self.context.get("request")
        if request.user.role != 'user':
            raise serializers.ValidationError({'error': 'You do not have permission to create a Task.'})    
        try:
            return Task.objects.create(created_by=request.user, **validated_data)

        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error) from e


    def update(self, instance, validated_data):
        request = self.context.get("request")
        title = validated_data.get('title')
        description = validated_data.get('description')
        assigned_to = validated_data.get('assigned_to')
        status = validated_data.get('status')

        if request.user.role == 'leader':
            instance.assigned_to = assigned_to
            
        if request.user.role == 'user':
            instance.title = title
            instance.description = description

        if request.user.role == 'member':
            instance.status = status
      
        instance.save()
        return instance



# TEAM SERIALIZER
class TeamSerializer(serializers.ModelSerializer):
    leader = AccountSerializer(read_only=True)
    leader_id = serializers.IntegerField(write_only=True)
    members = AccountSerializer(many=True, read_only=True)
    member_ids = serializers.CharField(write_only=True, required=False)
    created_by = serializers.StringRelatedField()
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'slug', 'leader', 'leader_id', 'members', 'member_ids',  'created_by', 'created_at', 'updated_at', 'tasks')
        read_only_fields = ('slug', )
        extra_kwargs = {
            'leader_id': {'required': True},
        }
    

    def validate(self, attrs):
        leader_id = attrs.get('leader_id', '')
        leader = User.objects.filter(role='leader', id=leader_id)
        if not leader:
            raise serializers.ValidationError('Invalid ID passed or user not a team leader.')
        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        if request.user.role != 'user':
            raise serializers.ValidationError({'error': 'You do not have permission to create a team.'})       

        validated_data.pop('member_ids') if validated_data.get('member_ids') else None  # Comment this line if want error creating data with member_ids!

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
    