from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
import stripe

stripe.api_key = "sk_test_your_stripe_secret_key"

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=200)
    sum_assurance = models.PositiveIntegerField()
    premium = models.PositiveIntegerField()
    tenure = models.PositiveIntegerField()
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.policy_name

class PolicyRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Pending')
    creation_date = models.DateField(auto_now=True)
    payment_status = models.CharField(max_length=100, default='Not Paid')
    payment_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.policy)

    def process_payment(self, token):
        try:
            charge = stripe.Charge.create(
                amount=self.policy.premium * 100,  # amount in cents
                currency="usd",
                source=token,
                description="Payment for policy: {}".format(self.policy.policy_name),
            )
            self.payment_status = 'Paid'
            self.payment_id = charge.id
            self.save()
            return True
        except stripe.error.StripeError as e:
            # Handle error
            print("Stripe Error:", e)
            return False

class Question(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    admin_comment = models.CharField(max_length=200, default='Nothing')
    asked_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.description












































































# from django.db import models
# from django.contrib.auth.models import User
# from customer.models import Customer

# class Category(models.Model):
#     category_name =models.CharField(max_length=20)
#     creation_date =models.DateField(auto_now=True)
#     def __str__(self):
#         return self.category_name

# class Policy(models.Model):
#     category= models.ForeignKey('Category', on_delete=models.CASCADE)
#     policy_name=models.CharField(max_length=200)
#     sum_assurance=models.PositiveIntegerField()
#     premium=models.PositiveIntegerField()
#     tenure=models.PositiveIntegerField()
#     creation_date =models.DateField(auto_now=True)
#     def __str__(self):
#         return self.policy_name

# class PolicyRecord(models.Model):
#     customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
#     Policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
#     status = models.CharField(max_length=100,default='Pending')
#     creation_date =models.DateField(auto_now=True)
#     def __str__(self):
#         return self.policy

# class Question(models.Model):
#     customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
#     description =models.CharField(max_length=500)
#     admin_comment=models.CharField(max_length=200,default='Nothing')
#     asked_date =models.DateField(auto_now=True)
#     def __str__(self):
#         return self.description