from rest_framework.generics import CreateAPIView


from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



