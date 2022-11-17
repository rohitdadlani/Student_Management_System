"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib.auth.models import User
from attendence.models import Attendence, Category
from rest_framework import routers

from attendence.views import UserViewSet, AttendenceViewSet, CategoryViewSet, LoginViewSet


## New Code
from rest_framework.authtoken import views

## New Code








# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)

router.register(r'api/attendence', AttendenceViewSet)

router.register(r'api/category', CategoryViewSet)

router.register(r'api/login', LoginViewSet)

## New Code

## New Code



# Video
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#from attendence.views import UserViewSet
from rest_framework.routers import DefaultRouter

#Video






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),    
    path(r'', include(router.urls)),
    #  path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    ## New Code
    path('',include('attendence.urls')),
    path('api-token-auth', views.obtain_auth_token),

    ## New Code



    # Video
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Video

]







# video

router1 = DefaultRouter()
router1.register('user',UserViewSet,basename='user')


urlpatterns += router1.urls

#video

