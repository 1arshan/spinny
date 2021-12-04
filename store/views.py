from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer, BoxSerializer
from .models import Box
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        x = {"success": "true",
             "status": 200,
             "message": "Operation performed successfully"}
        return Response(x, status=status.HTTP_200_OK)


# ---For teacher
class IsStaff(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        try:
            User.objects.get(username=username)
            return True
        except Exception:
            x = {"msg": "Only Staff can add box"}
        return Response(x, status=status.HTTP_400_BAD_REQUEST)


# class BoxView(generics.CreateAPIView):
#     serializer_class = BoxSerializer
#     permission_classes = [IsAuthenticated, IsStaff]
#     queryset = Box

class BoxView(APIView):
    permission_classes = [IsAuthenticated, IsStaff]

    def post(self,request):
        data=request.data
        # print(data)
        serializer = BoxSerializer(data=data)
        if serializer.is_valid():
            serializer.validated_data['area']=2*(serializer.validated_data['length']+serializer.validated_data['width']
                                                 +serializer.validated_data['height'])
            serializer.validated_data['volume'] = serializer.validated_data['length'] * \
                                                  serializer.validated_data['width']* serializer.validated_data['height']
            serializer.validated_data['created_by']=request.user
            print(serializer.validated_data)
            serializer.save()
            x = {"msg": "otp sent"}
            return Response(x, status=status.HTTP_201_CREATED)
        x = {"msg": "something went wrong please retry"}
        return Response(x, status=status.HTTP_400_BAD_REQUEST)
