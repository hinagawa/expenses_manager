from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Category, Finance, Goal
from .serializers import (
    CategorySerializer,
    FinanceSerializer,
    GoalSerializer,
)

# category endpoints


@api_view(["POST"])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def get_all_category(request):
    try:
        category = Category.objects.filter()
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({"category": serializer.data})
        else:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )
    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_category_by_user(request, user_id):
    try:
        category = Category.objects.filter(id=user_id)
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({"category": serializer.data})
        else:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )
    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_custom_category(request):
    try:
        category = Category.objects.filter(is_custom=True)
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            return Response({"category": serializer.data})
        else:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )
    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def edit_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"category": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# finances endpoints


@api_view(["POST"])
@permission_classes([IsAuthenticated])
# @permission_classes([IsAuthenticated])
def create_finance(request):
    if request.method == "POST":
        serializer = FinanceSerializer(data=request.data)
        if serializer.is_valid():
            finance = serializer.save()
            return Response(
                {
                    "message": "Finance created successfully",
                    "category": FinanceSerializer(finance).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_finances_by_user(request, user_id):
    try:
        finances = Finance.objects.filter(user_id=user_id)
        if finances.exists():
            serializer = FinanceSerializer(finances, many=True)
            result = {"finances": serializer.data}

            for finance_item in result["finances"]:
                category = Category.objects.get(pk=finance_item["category"])
                category_serializer = CategorySerializer(category)
                finance_item["category"] = category_serializer.data

            return Response({"finances": serializer.data})
        else:
            return Response(
                {"error": "Finances not found"}, status=status.HTTP_404_NOT_FOUND
            )
    except Finances.DoesNotExist:
        return Response(
            {"error": "Finances not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def edit_finance(request, finance_id):
    try:
        finance = Finance.objects.get(pk=finance_id)
    except Finance.DoesNotExist:
        return Response(
            {"error": "Finance not found"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "PUT":
        serializer = FinanceSerializer(finance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"finance": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        finance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# goal endpoints


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_goal(request):
    if request.method == "POST":
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            goal = serializer.save()
            return Response(
                {
                    "message": "Goal created successfully",
                    "category": GoalSerializer(goal).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_goals_by_user(request, user_id):
    try:
        goal = Goal.objects.filter(user_id=user_id)
        if goal.exists():
            serializer = GoalSerializer(goal, many=True)
            return Response({"goals": serializer.data})
        else:
            return Response(
                {"error": "Goals not found"}, status=status.HTTP_404_NOT_FOUND
            )
    except Goals.DoesNotExist:
        return Response({"error": "Goals not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_goal(request, goal_id):
    try:
        goal = Goal.objects.get(pk=goal_id)
    except Goal.DoesNotExist:
        return Response({"error": "Goal not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = GoalSerializer(goal, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"goal": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
