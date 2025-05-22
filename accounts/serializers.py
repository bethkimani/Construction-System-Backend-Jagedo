from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import (
    Location, Customer, Skill, Fundi, Contractor, Professional,
    Hardware, MaterialCategory, Material, Project,
    ProjectMaterial, Task, ChatbotConversation, ChatbotMessage
)

User = get_user_model()

class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class FundiSerializer(ModelSerializer):
    class Meta:
        model = Fundi
        fields = '__all__'

class ContractorSerializer(ModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'

class ProfessionalSerializer(ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'

class HardwareSerializer(ModelSerializer):
    class Meta:
        model = Hardware
        fields = '__all__'

class MaterialCategorySerializer(ModelSerializer):
    class Meta:
        model = MaterialCategory
        fields = '__all__'

class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectMaterialSerializer(ModelSerializer):
    class Meta:
        model = ProjectMaterial
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ChatbotConversationSerializer(ModelSerializer):
    class Meta:
        model = ChatbotConversation
        fields = '__all__'

class ChatbotMessageSerializer(ModelSerializer):
    class Meta:
        model = ChatbotMessage
        fields = '__all__'
