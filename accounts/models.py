from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class User(AbstractUser):
    USER_TYPES = (
        ('CUSTOMER', 'Customer'),
        ('FUNDI', 'Fundi'),
        ('CONTRACTOR', 'Contractor'),
        ('PROFESSIONAL', 'Professional'),
        ('HARDWARE', 'Hardware Supplier'),
        ('ADMIN', 'System Admin'),
    )

    user_type = models.CharField(max_length=12, choices=USER_TYPES, default='CUSTOMER')
    phone_number = PhoneNumberField(_("phone number"), blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    preferred_communication = models.CharField(
        max_length=20,
        choices=[
            ('EMAIL', 'Email'),
            ('SMS', 'SMS'),
            ('WHATSAPP', 'WhatsApp'),
            ('CALL', 'Phone Call')
        ],
        default='EMAIL'
    )

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Fundi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fundi_profile')
    skills = models.ManyToManyField(Skill, blank=True)
    hourly_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0.0
    )
    experience_years = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]  # Now properly imported
    )

    def __str__(self):
        return self.user.username

class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contractor_profile')
    company_name = models.CharField(max_length=255, default='')
    license_number = models.CharField(max_length=50, default='PENDING')
    certifications = models.FileField(upload_to='certifications/contractors/', blank=True, null=True)
    portfolio = models.FileField(upload_to='portfolios/contractors/', blank=True, null=True)
    specialization = models.CharField(max_length=100, default='General')
    years_in_business = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.company_name

class Professional(models.Model):
    PROFESSION_TYPES = (
        ('ARCHITECT', 'Architect'),
        ('ENGINEER', 'Engineer'),
        ('QS', 'Quantity Surveyor'),
        ('INTERIOR_DESIGNER', 'Interior Designer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professional_profile')
    profession = models.CharField(max_length=20, choices=PROFESSION_TYPES, default='ENGINEER')
    license_number = models.CharField(max_length=50, default='PENDING')
    certifications = models.FileField(upload_to='certifications/professionals/', blank=True, null=True)
    portfolio = models.FileField(upload_to='portfolios/professionals/', blank=True, null=True)
    hourly_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.0,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.profession} - {self.user.username}"

class Hardware(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hardware_profile')
    business_name = models.CharField(max_length=255, default='')
    business_license = models.CharField(max_length=50, default='PENDING')
    delivery_available = models.BooleanField(default=False)
    delivery_radius_km = models.PositiveIntegerField(default=0)
    opening_hours = models.CharField(max_length=100, default='9:00 AM - 5:00 PM')

    def __str__(self):
        return self.business_name

class MaterialCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    supplier = models.ForeignKey(Hardware, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(MaterialCategory, on_delete=models.SET_NULL, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity_in_stock = models.PositiveIntegerField(default=0)
    minimum_order_quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='materials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (${self.unit_price})"

    @property
    def is_available(self):
        return self.is_active and self.quantity_in_stock > 0

class Project(models.Model):
    PROJECT_STATUS = (
        ('PLANNING', 'Planning'),
        ('IN_PROGRESS', 'In Progress'),
        ('ON_HOLD', 'On Hold'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='PLANNING')
    contractors = models.ManyToManyField(Contractor, blank=True)
    fundis = models.ManyToManyField(Fundi, blank=True)
    professionals = models.ManyToManyField(Professional, blank=True)
    materials = models.ManyToManyField(Material, through='ProjectMaterial')

    def __str__(self):
        return self.name

class ProjectMaterial(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Hardware, on_delete=models.SET_NULL, null=True)
    date_purchased = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project', 'material'], name='unique_project_material')
        ]

class Task(models.Model):
    TASK_STATUS = (
        ('NOT_STARTED', 'Not Started'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('DELAYED', 'Delayed'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='NOT_STARTED')
    depends_on = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.project})"

class ChatbotConversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    started_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

class ChatbotMessage(models.Model):
    conversation = models.ForeignKey(ChatbotConversation, on_delete=models.CASCADE, related_name='messages')
    message_text = models.TextField()
    is_user = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    intent = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['timestamp']
