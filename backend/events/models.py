from django.db import models
from django.conf import settings


class Event(models.Model):
    """Model for technical fest events"""
    
    EVENT_TYPES = [
        ('technical', 'Technical'),
        ('cultural', 'Cultural'),
        ('sports', 'Sports'),
        ('workshop', 'Workshop'),
        ('competition', 'Competition'),
    ]
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_participants = models.PositiveIntegerField(default=100)
    current_participants = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    registration_deadline = models.DateTimeField()
    venue = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    requirements = models.TextField(blank=True)
    prizes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'events'
        ordering = ['-created_at']


class EventRegistration(models.Model):
    """Model for event registrations"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event_registrations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    registration_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
    
    class Meta:
        db_table = 'event_registrations'
        unique_together = ['event', 'user']
