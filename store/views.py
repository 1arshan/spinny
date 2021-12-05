from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer, BoxSerializer,BoxNonStaffSerializer,BoxStaffSerializer
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
    message = {"success": "false",
               "status_code": 404,
               "message": "Only Staff Can Add Box"}

    def has_permission(self, request, view):
        username = request.user.username
        return User.objects.get(username=username).is_staff


class BoxAddView(APIView):
    permission_classes = [IsAuthenticated, IsStaff]

    def post(self, request):
        data = request.data
        serializer = BoxSerializer(data=data)
        # print("reach")
        if serializer.is_valid():
            serializer.validated_data['created_by'] = request.user
            serializer.save()
            x = {"msg": "box added"}
            return Response(x, status=status.HTTP_201_CREATED)
        x = {"msg": "something went wrong please retry"}
        return Response(x, status=status.HTTP_400_BAD_REQUEST)


class BoxUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsStaff]
    serializer_class = BoxSerializer

    def update(self, request, *args, **kwargs):
        pk = self.request.GET['pk'] #TODO: make this error prone
        t = Box.objects.get(pk=pk)
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            # change_area_and_volume(serializer)
            serializer.save()
            x = {"msg": "Box Dimention  updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoxListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:

        username=request.user.username
        box = Box.objects.all()
        if User.objects.filter(username=username,is_staff=True).exists():
            serializer = BoxStaffSerializer(box, many=True)
        else:
            serializer = BoxNonStaffSerializer(box, many=True)
        return Response(serializer.data)