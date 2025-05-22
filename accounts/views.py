from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

from .models import (
    Location, Customer, Skill, Fundi, Contractor, Professional,
    Hardware, MaterialCategory, Material, Project,
    ProjectMaterial, Task, ChatbotConversation, ChatbotMessage
)
from .serializers import (
    UserSignupSerializer, LocationSerializer, CustomerSerializer, SkillSerializer,
    FundiSerializer, ContractorSerializer, ProfessionalSerializer, HardwareSerializer,
    MaterialCategorySerializer, MaterialSerializer, ProjectSerializer, ProjectMaterialSerializer,
    TaskSerializer, ChatbotConversationSerializer, ChatbotMessageSerializer
)

User = get_user_model()

# --- Authentication Views ---

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSignupSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer

# --- API ViewSets ---

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class FundiViewSet(viewsets.ModelViewSet):
    queryset = Fundi.objects.all()
    serializer_class = FundiSerializer

class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

class HardwareViewSet(viewsets.ModelViewSet):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer

class MaterialCategoryViewSet(viewsets.ModelViewSet):
    queryset = MaterialCategory.objects.all()
    serializer_class = MaterialCategorySerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectMaterialViewSet(viewsets.ModelViewSet):
    queryset = ProjectMaterial.objects.all()
    serializer_class = ProjectMaterialSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ChatbotConversationViewSet(viewsets.ModelViewSet):
    queryset = ChatbotConversation.objects.all()
    serializer_class = ChatbotConversationSerializer

class ChatbotMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatbotMessage.objects.all()
    serializer_class = ChatbotMessageSerializer
