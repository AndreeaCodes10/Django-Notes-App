
from django.contrib import admin
from django.urls import path,include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name="register"),
    path('api/token/', TokenObtainPairView.as_view(), name="token-obtain"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('api-auth/', include('rest_framework.urls')), #for login and logout views
    path('api/', include('api.urls')), #include the urls from the api app   
]
