from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, UserLoginSerializer


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
            'user': serializer.data['id'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


# @api_view(['GET'])
# def current_user(request):
#     """
#     Determine the current user by their token, and return their data
#     """
#
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)
#
# class UserList(APIView):
#
#     permission_classes = (permissions.AllowAny,)
#
#     # Create new user
#     def post(self, request, format=None):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # class Login(APIView):
# #     permission_classes = (permissions.AllowAny,)
# #
# #     def post(self, request):
# #         TokenObtainPairView()
#
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Add custom claims
#         token['name'] = str(user)
#         # ...
#
#         return token
#
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
