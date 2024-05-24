from rest_framework.response import Response
from rest_framework.decorators import api_view

# from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Category, Finances, Goals
from .serializers import (
    CategorySerializer,
    FinancesSerializer,
    GoalsSerializer,
)

# category endpoints


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_user_category(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(
                {
                    "message": "Category created successfully",
                    "category": CategorySerializer(category).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_category(request):
    try:
        category = Category.objects.filter()
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({"category": serializer.data})
        else:
            return Response({"error": "Category not found"}, status=404)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)


@api_view(["GET"])
def get_category_by_user(request, user_id):
    try:
        category = Category.objects.filter(id=user_id)
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({"category": serializer.data})
        else:
            return Response({"error": "Category not found"}, status=404)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)


@api_view(["GET"])
def get_custom_category(request):
    try:
        category = Category.objects.filter(is_custom=True)
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({"category": serializer.data})
        else:
            return Response({"error": "Category not found"}, status=404)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)


@api_view(["PUT"])
def edit_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"category": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# finances endpoints


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_finance(request):
    if request.method == "POST":
        serializer = FinancesSerializer(data=request.data)
        if serializer.is_valid():
            finance = serializer.save()
            return Response(
                {
                    "message": "Finance created successfully",
                    "category": FinancesSerializer(finance).data,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_finances_by_user(request, user_id):
    try:
        finances = Finances.objects.filter(id=user_id)
        if finances.exists():
            serializer = FinancesSerializer(finances, many=True)
            return Response({"finances": serializer.data})
        else:
            return Response({"error": "Finances not found"}, status=404)
    except Finances.DoesNotExist:
        return Response({"error": "Finances not found"}, status=404)


@api_view(["PUT"])
def edit_finance(request, pk):
    try:
        finance = Finances.objects.get(pk=pk)
    except Finances.DoesNotExist:
        return Response(
            {"error": "Finance not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = FinancesSerializer(finance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"finance": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# goal endpoints


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_goal(request):
    if request.method == "POST":
        serializer = GoalsSerializer(data=request.data)
        if serializer.is_valid():
            goal = serializer.save()
            return Response(
                {
                    "message": "Goal created successfully",
                    "category": GoalsSerializer(goal).data,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_goals_by_user(request, user_id):
    try:
        goal = Goals.objects.filter(id=user_id)
        if goal.exists():
            serializer = GoalsSerializer(goal, many=True)
            return Response({"goals": serializer.data})
        else:
            return Response({"error": "Goals not found"}, status=404)
    except Goals.DoesNotExist:
        return Response({"error": "Goals not found"}, status=404)


@api_view(["PUT"])
def edit_goal(request, pk):
    try:
        goal = Goals.objects.get(pk=pk)
    except Goals.DoesNotExist:
        return Response({"error": "Goal not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = GoalsSerializer(goal, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"goal": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
