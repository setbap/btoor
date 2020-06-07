from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .serializers import CreateUserSerializer, UserActivationSerializer, UserSerializer
from .models import User
from django.core.mail import send_mail
import secrets


@api_view(['POST'])
def signup(request):
    user = CreateUserSerializer(data=request.data)
    if user.is_valid(raise_exception=True):
        token = secrets.token_urlsafe(7)

        user.save(activation_token=token)
        print(user.validated_data.get("email"))
        send_mail(
            subject='That’s your subject',
            message=f'activation token is : {token}',
            from_email=settings.EMAIL_HOST_USER_EMAIL,
            recipient_list=[user.validated_data.get("email")],
        )
        return Response(data=user.validated_data.get("email"))
    return Response(data=user.errors)


class UserActivate(APIView):

    def post(self, reqest):
        info = UserActivationSerializer(data=reqest.data)
        if info.is_valid(raise_exception=True):
            user = User.objects.filter(email=reqest.data["email"])
            if user.exists():
                user = user.first()
                if user.is_active:
                    return Response(data={
                        "status": "you are active now."}, status=status.HTTP_200_OK)
                if user.activation_token == reqest.data["activation_token"]:
                    user.is_active = True
                    user.activation_token = ""
                    user.save()
                    return Response(data={"status": "user activated"}, status=status.HTTP_200_OK)
        return Response(
            data={"status": "wrong info make sure your request include 'activation_token' and 'email' and right info "},
            status=status.HTTP_400_BAD_REQUEST)


class HelloView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class HelloView2(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
