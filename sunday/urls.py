"""
URL configuration for sunday project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from users.views import UserLoginView

schema_view = get_schema_view(
	openapi.Info(
		title="Sunday",
		default_version='v1',
		description="Sundays Iteration of Payment API",
		contact=openapi.Contact("kalenshi@gmail.com")
	),
	public=True,
	permission_classes=[permissions.AllowAny, ]
)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('api/', include('api.urls')),
	path('login/', UserLoginView.as_view()),
	#path('accounts/', include('rest_framework.urls')),
]
