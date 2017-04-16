# django-payments-stripe-sources

To configure Ideal and credit cards through Stripe:

PAYMENT_VARIANTS = {
    'default': ('payments_stripe_sources.StripeSourcesProvider', {
        'secret_key': 'sk_test_example',
        'public_key': 'pk_test_example',
        'name': 'Your Web'}),
    'credit_card': ('payments.stripe.StripeProvider', {
        'secret_key': 'sk_test_example',
        'public_key': 'pk_test_example',
        'name': 'Your Web'}),
}

CHECKOUT_PAYMENT_CHOICES = [('default', 'Ideal'), ('credit_card', 'Credit Card')]


You also need to configure a webhook for a callback by stripe when the payment has ended. For an example, see:
https://github.com/CarstVaartjes/saleor/blob/cheese/saleor/order/urls.py
