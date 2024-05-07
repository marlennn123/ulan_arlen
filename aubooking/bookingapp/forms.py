from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile
from phonenumber_field import formfields


class CustomSignUpForm(SignupForm):
    phone_number = formfields.PhoneNumberField()

    class Meta:
        model = UserProfile
        fields = ('phone_number',)

    def save(self, request):
        user = super().save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
