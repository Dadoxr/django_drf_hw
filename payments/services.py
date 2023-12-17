from django.conf import settings
from django.shortcuts import get_object_or_404
import stripe
from payments import models as m


def _save_payment(pid):
    m.Payment.objects.get_or_create(pid=pid)
    return


def get_payment(pk):
    stripe.api_key = settings.STRIPE_API_KEY

    payment = get_object_or_404(m.Payment, pk=pk)
    response = stripe.PaymentIntent.retrieve(payment.pid)
    return response


def create_payment(amount):
    stripe.api_key = settings.STRIPE_API_KEY

    response = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    _save_payment(response.get("id"))
    return response


def check_status(pk):
    stripe.api_key = settings.STRIPE_API_KEY

    payment = get_object_or_404(m.Payment, pk=pk)
    response = stripe.PaymentIntent.retrieve(payment.pid)

    return response.status if response else None
