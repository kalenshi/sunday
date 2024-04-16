from rest_framework import status, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from users.serializers import UserSerializer, TokenSerializer


class CreateUserView(APIView):
	"""Create a new user in the system"""
	serializer_class = UserSerializer
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (permissions.IsAdminUser,)

	@swagger_auto_schema(
		request_body=UserSerializer,
		responses={"201": UserSerializer, "400": openapi.Response("UserSerializer.errors")}
	)
	def post(self, request):
		"""Create a new user in the system"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateTokenView(ObtainAuthToken):
	"""Create a new auth token for user"""
	serializer_class = TokenSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
