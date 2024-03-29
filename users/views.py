from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserLoginView(ObtainAuthToken):
	"""
	Handle creating user authentication tokens
	"""
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
