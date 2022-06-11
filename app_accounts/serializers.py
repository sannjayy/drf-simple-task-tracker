from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import get_user_model
User = get_user_model()


# LOGIN SERIALIZER
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=3)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email = obj['email'])
        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh'],
        }

    class Meta:
        model = User
        fields=['id', 'first_name', 'last_name', 'username', 'email', 'role', 'password', 'tokens']
        read_only_fields = ('first_name', 'last_name', 'email', 'role', )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, please contact admin')

        # if not user.is_email_verified:
        #     '''
        #         We can do this validation here.
        #     '''
        #     raise AuthenticationFailed('User email is not verified')
            
        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'role': user.role,
            'tokens': user.tokens
        }


# USER ACCOUNT SERIALIZER
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'role', 'email', 'is_email_verified', )
        

# LOGOUT SERIALIZER
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')