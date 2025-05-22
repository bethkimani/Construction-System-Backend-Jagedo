from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SignupView, CustomTokenObtainPairView,
    LocationViewSet, CustomerViewSet, SkillViewSet, FundiViewSet,
    ContractorViewSet, ProfessionalViewSet, HardwareViewSet,
    MaterialCategoryViewSet, MaterialViewSet, ProjectViewSet,
    ProjectMaterialViewSet, TaskViewSet,
    ChatbotConversationViewSet, ChatbotMessageViewSet,
)
from rest_framework_simplejwt.views import TokenRefreshView

# Create a router and register all your viewsets
router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'fundis', FundiViewSet)
router.register(r'contractors', ContractorViewSet)
router.register(r'professionals', ProfessionalViewSet)
router.register(r'hardware', HardwareViewSet)
router.register(r'material-categories', MaterialCategoryViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-materials', ProjectMaterialViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'chatbot-conversations', ChatbotConversationViewSet)
router.register(r'chatbot-messages', ChatbotMessageViewSet)

# Combine router URLs with your custom views
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include all registered API endpoints from the router
    path('', include(router.urls)),
]
