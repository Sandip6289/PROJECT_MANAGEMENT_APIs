from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .models import User, EmpA, EmpS
from .serializers import UserRegisterSerializer, UserLoginSerializer, EmpADetailSerializer, EmpSDetailSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .permissions import SuperUserPermissions, EmpaPermissions, EmpsPermissions, EmpS_Plus_SuperUserPermissions


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.

class EmpSUserRegister(APIView):
    permission_classes=[SuperUserPermissions]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data.get("role") != "Level S":
                return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            employee_s = EmpS(user=user)
            employee_s.save()
            token = get_tokens_for_user(user)
            response = {"username":serializer.data.get("username")}|{"email":serializer.data.get("email")}|{"role":serializer.data.get("role")}|token|{"status":"registration successfull"}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmpAUserRegister(APIView):
    permission_classes=[EmpS_Plus_SuperUserPermissions]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data.get("role") != "Level A":
                return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            employee_a = EmpA(user=user)
            employee_a.save()
            token = get_tokens_for_user(user)
            response = {"username":serializer.data.get("username")}|{"email":serializer.data.get("email")}|{"role":serializer.data.get("role")}|token|{"status":"registration successfull"}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogin(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request._request, user)
                token = get_tokens_for_user(user)
                response = {"username":user.username}|{"email":serializer.data.get("email")}|{"role":user.role}|token|{"status":"login successfull"}
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogout(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            print(request.user)
            logout(request)
            return Response({"msg":"successfully logout"})
        return Response({"msg":"Login first"})
    
class EmpA_AllUserDetails(APIView):
    permission_classes=[IsAuthenticated]
    permission_classes=[EmpS_Plus_SuperUserPermissions]
    def get(self, request):
        if request.user.is_authenticated:
            empa = EmpA.objects.all()
            serializer = EmpADetailSerializer(empa, many=True)
            if serializer.data is not None:
                response = serializer.data
                formated_response = []
                
                for item in response:
                    # print(item)
                    formated_response.append({"username":item["user"]["username"],"email":item["user"]["email"],"role":item["user"]["role"]})
        
                return Response(formated_response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class EmpS_AllUserDetails(APIView):
    permission_classes=[IsAuthenticated]
    permission_classes=[SuperUserPermissions]
    def get(self, request):
        if request.user.is_authenticated:
            emps = EmpS.objects.all()
            serializer = EmpSDetailSerializer(emps, many=True)
            if serializer.data is not None:
                response = serializer.data
                formated_response = []
                
                for item in response:
                    # print(item)
                    formated_response.append({"username":item["user"]["username"],"email":item["user"]["email"],"role":item["user"]["role"]})
        
                print(formated_response)
                return Response(formated_response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    



    