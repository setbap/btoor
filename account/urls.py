from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .apis import HelloView, signup, UserActivate, HelloView2

# base url : /api/account/

urlpatterns = [
    # Your URLs...
    path('signup/', signup, name='signup'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('activation/', UserActivate.as_view(), name='activate user'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', HelloView.as_view(), name='hello'),
    path('test/<int:pk>/', HelloView2.as_view(), name='hello'),
]
