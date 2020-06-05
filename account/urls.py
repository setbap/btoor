from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .apis import HelloView, signup,UserActivate

# base url : /api/account/

urlpatterns = [
    # Your URLs...
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('hello/', HelloView.as_view(), name='hello'),
    path('activation/', UserActivate.as_view(), name='activate user'),
    path('test/', HelloView.as_view(), name='hello'),
    path('signup/', signup, name='signup'),
]
