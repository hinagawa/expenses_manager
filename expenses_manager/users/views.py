from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Users, Currency
from .serializers import UsersSerializer, CurrencySerializer

# user endpoints


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_user(request):
    if request.method == "POST":
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User created successfully",
                    "category": UsersSerializer(user).data,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response({"users": serializer.data})


@api_view(["GET"])
def get_user_by_id(request, user_id):
    try:
        q = Users.objects.filter(id=user_id)
        if q.exists():
            user = q.get()
            serializer = UsersSerializer(user)
            result = {"user": serializer.data}

            currency = Currency.objects.get(pk=result["user"]["currency"])
            currency_serializer = CurrencySerializer(currency)
            result["user"]["currency"] = currency_serializer.data
            return Response(result)
        else:
            return Response({"error": "User not found"}, status=404)
    except Users.DoesNotExist:
        return Response({"error": "User not found"}, status=404)


@api_view(["PUT"])
def edit_user(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# currency endpoints


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_currency(request):
    if request.method == "POST":
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            currency = serializer.save()
            return Response(
                {
                    "message": "Currency created successfully",
                    "category": CurrencySerializer(currency).data,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_currency(request):
    try:
        currency = Currency.objects.all()
        if currency.exists():
            serializer = CurrencySerializer(currency, many=True)
            return Response({"currency": serializer.data})
        else:
            return Response({"error": "Currency not found"}, status=404)
    except Currency.DoesNotExist:
        return Response({"error": "Currency not found"}, status=404)


@api_view(["PUT"])
def edit_currency(request, pk):
    try:
        currency = Currency.objects.get(pk=pk)
    except Currency.DoesNotExist:
        return Response(
            {"error": "Currency not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = CurrencySerializer(currency, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"currency": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
