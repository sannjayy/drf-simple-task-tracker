from rest_framework.response import Response
from rest_framework import permissions, status, generics, views
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from .permissions import IsUser
from .serializers import LoginSerializer, UserAccountSerializer, LogoutSerializer
User = get_user_model()

# USER LIST VIEW
class UsersListAPIView(generics.ListAPIView):
    serializer_class = UserAccountSerializer
    queryset = User.objects.all()
    throttle_classes = [UserRateThrottle]
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['^first_name','^last_name', 'username', 'email', '^role']
    filterset_fields = ['role']



# USER AUTHENTICATION VIEW
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    throttle_classes = [AnonRateThrottle]
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# USER ACCOUNT VIEW
class UserAccountView(generics.GenericAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = (IsAuthenticated, IsUser)

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# LOGOUT SINGLE DEVICE
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_205_RESET_CONTENT)


# LOGOUT ALL DEVICES
class LogoutAllView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

