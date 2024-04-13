from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Category, Currency, Finances, Goals, Users
from .serializers import (CategorySerializer, CurrencySerializer,
                          FinancesSerializer, GoalsSerializer, UsersSerializer)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            # category = serializer.save()
            return Response({'message': 'Category created successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_category(request):
    try:
        category = Category.objects.filter()
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({'category': serializer.data})
        else:
            return Response({'error': 'Category not found'}, status=404)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)


@api_view(['GET'])
def get_category_by_user(request, user_id):
    try:
        category = Category.objects.filter(id=user_id)
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({'category': serializer.data})
        else:
            return Response({'error': 'Category not found'}, status=404)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)


@api_view(['GET'])
def get_custom_category(request):
    try:
        category = Category.objects.filter(is_custom=True)
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({'category': serializer.data})
        else:
            return Response({'error': 'Category not found'}, status=404)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)


@api_view(['GET'])  # we can only get currency
def get_currency(request):
    try:
        currency = Currency.objects.all()
        if currency.exists():
            serializer = CurrencySerializer(currency, many=True)
            return Response({'currency': serializer.data})
        else:
            return Response({'error': 'Currency not found'}, status=404)
    except Currency.DoesNotExist:
        return Response({'error': 'Currency not found'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_finance(request):
    if request.method == 'POST':
        serializer = FinancesSerializer(data=request.data)
        if serializer.is_valid():
            # finance = serializer.save()
            return Response({'message': 'Finance created successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_finances_by_user(request, user_id):
    try:
        finances = Finances.objects.filter(id=user_id)
        if finances.exists():
            serializer = FinancesSerializer(finances, many=True)
            return Response({'finances': serializer.data})
        else:
            return Response({'error': 'Finances not found'}, status=404)
    except Finances.DoesNotExist:
        return Response({'error': 'Finances not found'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_goal(request):
    if request.method == 'POST':
        serializer = GoalsSerializer(data=request.data)
        if serializer.is_valid():
            # goal = serializer.save()
            return Response({'message': 'Goal created successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_goals_by_user(request, user_id):
    try:
        goal = Goals.objects.filter(id=user_id)
        if goal.exists():
            serializer = GoalsSerializer(goal, many=True)
            return Response({'goals': serializer.data})
        else:
            return Response({'error': 'Goals not found'}, status=404)
    except Goals.DoesNotExist:
        return Response({'error': 'Goals not found'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            # user = serializer.save()
            return Response({'message': 'User created successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response({'users': serializer.data})


@api_view(['GET'])
def get_user_by_id(request, user_id):
    try:
        user = Users.objects.filter(id=user_id)
        if user.exists():
            serializer = UsersSerializer(user, many=True)
            return Response({'user': serializer.data})
        else:
            return Response({'error': 'User not found'}, status=404)
    except Users.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
