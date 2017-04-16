# django-payments-stripe-sources

To configure Ideal and credit cards through Stripe:


STRIPE_SECRET_KEY = 'sk_test_example'
STRIPE_PUBLIC_KEY = 'pk_test_example'

PAYMENT_VARIANTS = {
    'default': ('payments_stripe_sources.StripeSourcesProvider', {
        'secret_key': STRIPE_SECRET_KEY,
        'public_key': STRIPE_PUBLIC_KEY,
        'name': 'Your Web'}),
    'credit_card': ('payments.stripe.StripeProvider', {
        'secret_key': STRIPE_SECRET_KEY,
        'public_key': STRIPE_PUBLIC_KEY,
        'name': 'Your Web'}),
}

CHECKOUT_PAYMENT_CHOICES = [('default', 'Ideal'), ('credit_card', 'Credit Card')]


You also need to configure a webhook for a callback by stripe when the payment has ended. For an example, see:
https://github.com/CarstVaartjes/saleor/blob/cheese/saleor/order/urls.py
