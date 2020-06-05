from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from .serializers import CreateUserSerializer


@api_view(['POST'])
def signup(request):
    user = CreateUserSerializer(data=request.data)
    if user.is_valid(raise_exception=True):
        user.save()
        return Response(data=user.data)
    return Response(data=user.errors)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
