# api/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Question, Attempt, User
from .serializers import (
    RegisterSerializer, UserSerializer,
    CategorySerializer, QuestionSerializer, AttemptSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Registration View - allows anyone to register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# User Info View - Authenticated users can view their own details
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# Category List and Create View
# GET: List all categories (authenticated users)
# POST: Create a new category (admin users only)
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUser()]
        return [IsAuthenticated()]

# NEW VIEW ADDED: Category Retrieve, Update, and Destroy View
# GET: Retrieve a single category (authenticated users)
# PUT/PATCH: Update a category (admin users only)
# DELETE: Delete a category (admin users only)
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        # Allow any authenticated user to retrieve (GET) a single category
        # For update (PUT/PATCH) and delete (DELETE), require admin privileges
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsAdminUser()]
        return [IsAuthenticated()] # For GET, only authentication is needed


# Questions by Category View
# GET: List questions for a specific category (authenticated users)
# POST: Add a new question to a category (admin users only)
class QuestionListCreateView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUser()]
        return [IsAuthenticated()]

    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
            
        questions = Question.objects.filter(category=category)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, category_id):
        data = request.data.copy()
        data['category'] = category_id
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Quiz Attempt Submission View
class AttemptCreateView(generics.CreateAPIView):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Student's own attempts - Authenticated users can view their own attempts
class MyAttemptsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = Attempt.objects.filter(user=request.user).order_by('-timestamp')
        serializer = AttemptSerializer(attempts, many=True)
        return Response(serializer.data)

# Admin - View all attempts - Only admin users can view all attempts
class AllAttemptsView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        attempts = Attempt.objects.all().order_by('-timestamp')
        serializer = AttemptSerializer(attempts, many=True)
        return Response(serializer.data)