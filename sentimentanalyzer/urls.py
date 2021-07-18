
from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('message/', views.MessageViewSet, basename='Message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classify/', views.call_model.as_view()),
    path('api/', include(router.urls)),
    path('register/', views.register, name="register"),
    path('register/register', views.register, name="register"),
]
