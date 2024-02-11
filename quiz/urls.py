from django.urls import path
from . import views

# appends in /api/quiz/

urlpatterns = [
    path('', views.QuizView.as_view(), name="get-quiz"),
    path('<int:quiz_id>/', views.QuizAnswerView.as_view(), name="answer-quiz"),
    path('category/', views.CategoryListView.as_view(), name="get-category"),
    path('category/all/', views.CategoryListAllView.as_view(), name="get-category-all"),
    # path('category/<int:pk>/', views.QuizCategoryRetrieveView.as_view()),
    path('script/', views.ScriptView.as_view(), name="get-script"),
]
