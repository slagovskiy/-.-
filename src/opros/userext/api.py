from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import UserSerializer, ChangePasswordSerializer, AvatarSerializer, UserInfoSerializer, NewUserSerializer, RestoreUserSerializer
from .models import User


class APIUser(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    # permission_classes = [permissions.AllowAny,]

    def get(self, request):
        # email = request.GET.get('email')
        email = request.user.email
        user = User.objects.filter(email=email)
        serializer = UserSerializer(user, many=True)
        return Response({
            'data': serializer.data
        })

    def put(self, request):
        data = JSONParser().parse(request)
        user = UserSerializer(request.user, data=data)

        if user.is_valid():
            user.save()
            return Response({
                'data': user.data
            })
        else:
            return Response({
                'status': 'error'
            })
