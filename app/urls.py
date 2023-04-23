from django.urls import path
from app import views


urlpatterns = [
    path('swagger_test_create/', views.SwaggerTestCreateView.as_view())
    , path('swagger_test_edit/<pk>/', views.SwaggerTestEditView.as_view())
    , path('swagger_test_delete/<pk>/', views.SwaggerTestDeleteView.as_view())
]
