from django.urls import path
from .views import (
    RegisterView, UserDetailView, CategoryListCreateView,
    QuestionListCreateView, AttemptCreateView, MyAttemptsView, AllAttemptsView,
    CategoryRetrieveUpdateDestroyView, 
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),

  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'), 


    path('questions/<int:category_id>/', QuestionListCreateView.as_view(), name='question-list-create'),


    path('attempt/', AttemptCreateView.as_view(), name='attempt-create'),
    path('my-attempts/', MyAttemptsView.as_view(), name='my-attempts'),
    path('all-attempts/', AllAttemptsView.as_view(), name='all-attempts'),  # Admin only
]
