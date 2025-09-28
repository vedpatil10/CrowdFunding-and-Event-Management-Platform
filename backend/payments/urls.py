from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'payments', views.PaymentViewSet)
router.register(r'refunds', views.RefundViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('razorpay/create-order/', views.create_razorpay_order, name='create_razorpay_order'),
    path('razorpay/verify-payment/', views.verify_razorpay_payment, name='verify_razorpay_payment'),
]
