from django.urls import path
from payment import views

app_name = "payment"

urlpatterns = [
    path('payment/', views.PaymentView.as_view(), name="payment"),
    path('payment/ok/', views.payment_ok, name="payment_ok"),
    path('payment/fail/', views.payment_fail, name="payment_fail"),
    path('payment/callback/', views.payment_callback, name="payment_callback"),
]
