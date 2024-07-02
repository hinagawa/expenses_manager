from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view
from users.serializers import UsersSerializer


@api_view(["POST"])
def create_user(request):
    if request.method == "POST":
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            refresh.payload.update({"id": user.id, "email": user.email})
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def signIn(request):
    data = request.data
    email = data.get("email", None)
    password = data.get("password", None)
    if email is None or password is None:
        return Response(
            {"error": "Please provide email and password"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=email)
        print(user, UserModel.objects, user.currency_id)
        if not user.check_password(password):
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        refresh.payload.update({"id": user.id, "email": user.email})

        return Response(
            {
                "refresh": str(refresh),    
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )

    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(
            {"error": f"Error generating token: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def logout(request):
    refresh_token = request.data.get("refresh_token")
    if not refresh_token:
        return Response(
            {"error": "No refresh token"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
    except Exception as e:
        return Response(
            {"error": "Wrong refresh token"}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response({"success": "Log out"}, status=status.HTTP_200_OK)
