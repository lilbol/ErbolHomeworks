from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models



ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPClient, 'VIPClient'),
    (CLIENT, 'CLIENT')
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER')
)

BATKEN = 1
CHUY = 2
OSH = 3
TALAS = 4
NARYN = 5
DJALAL_ABAD = 6
ISSYK_KOL = 7

REGION_TYPE = (
    (BATKEN, 'BATKEN'),
    (CHUY, 'CHUY'),
    (OSH, 'OSH'),
    (TALAS, 'TALAS'),
    (NARYN, 'NARYN'),
    (DJALAL_ABAD, 'DJALAL-ABAD'),
    (ISSYK_KOL, 'ISSYK-KOL')
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    address1 = forms.CharField(required=True)
    address2 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    region = forms.ChoiceField(choices=REGION_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'address1',
            'address2',
            'city',
            'region'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username', 'id': 'hello'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'hi',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'email',
               'id': 'salute'}
    ))