from django.db import models
from django.conf import settings


class Payment(models.Model):
    """Model for payment transactions"""
    
    PAYMENT_TYPES = [
        ('event_registration', 'Event Registration'),
        ('campaign_donation', 'Campaign Donation'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    payment_type = models.CharField(max_length=30, choices=PAYMENT_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='INR')
    razorpay_order_id = models.CharField(max_length=100, unique=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    razorpay_signature = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=50, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    failure_reason = models.TextField(blank=True)
    
    # Foreign keys for different payment types
    event_registration = models.ForeignKey('events.EventRegistration', on_delete=models.CASCADE, null=True, blank=True)
    campaign_donation = models.ForeignKey('campaigns.CampaignDonation', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - ₹{self.amount} - {self.status}"
    
    class Meta:
        db_table = 'payments'
        ordering = ['-payment_date']


class Refund(models.Model):
    """Model for refund transactions"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        ('failed', 'Failed'),
    ]
    
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='refund')
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_refund_id = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reason = models.TextField()
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='refund_requests')
    requested_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Refund for {self.payment} - ₹{self.refund_amount}"
    
    class Meta:
        db_table = 'refunds'
        ordering = ['-requested_at']
