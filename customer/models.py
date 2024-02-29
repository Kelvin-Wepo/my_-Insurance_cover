from django.db import models
from django.contrib.auth.models import User
import stripe

stripe.api_key = "sk_test_your_stripe_secret_key"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Customer/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    payment_status = models.CharField(max_length=100, default='Not Paid')
    payment_id = models.CharField(max_length=100, blank=True, null=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def process_payment(self, token, amount):
        try:
            charge = stripe.Charge.create(
                amount=amount * 100,  # amount in cents
                currency="usd",
                source=token,
                description="Payment for customer: {}".format(self.get_name),
            )
            self.payment_status = 'Paid'
            self.payment_id = charge.id
            self.save()
            return True
        except stripe.error.StripeError as e:
            # Handle error
            print("Stripe Error:", e)
            return False

    def __str__(self):
        return self.user.first_name






# from django.db import models
# from django.contrib.auth.models import User

# class Customer(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic= models.ImageField(upload_to='profile_pic/Customer/',null=True,blank=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=False)
   
#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_instance(self):
#         return self
#     def __str__(self):
#         return self.user.first_name