from django.db import models
from django.conf import settings


class Campaign(models.Model):
    """Model for crowdfunding campaigns"""
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_campaigns')
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='campaign_images/', blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    @property
    def progress_percentage(self):
        if self.target_amount > 0:
            return (self.current_amount / self.target_amount) * 100
        return 0
    
    @property
    def days_remaining(self):
        from django.utils import timezone
        if self.end_date > timezone.now():
            return (self.end_date - timezone.now()).days
        return 0
    
    class Meta:
        db_table = 'campaigns'
        ordering = ['-created_at']


class CampaignDonation(models.Model):
    """Model for campaign donations"""
    
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='donations')
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100)
    payment_status = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    message = models.TextField(blank=True)
    donation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.donor.username} - {self.campaign.title} - ₹{self.amount}"
    
    class Meta:
        db_table = 'campaign_donations'
        ordering = ['-donation_date']
