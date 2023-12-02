

from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url
from notes.views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
route = routers.DefaultRouter()
route.register("",NoteView,basename='noteview')

from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
    path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
    path('', include(route.urls)),
    # path('', NoteView.as_view(),name="anything"),
    # path('item/<int:pk>/', NoteDetail.as_view(),name='delete'),
    ]