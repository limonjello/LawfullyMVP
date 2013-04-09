from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=75,
        label="",
        widget=forms.TextInput(attrs={'class': 'required', 'placeholder': 'Email Address'}),
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'required', 'placeholder': 'Password'},
            render_value=False))


    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_(u'This email already exists. Please choose another.'))

    def clean(self):
        self.cleaned_data['username'] = '' #createUniqueDjangoUsername()
        return self.cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'required', 'placeholder': 'Email Address'}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'required', 'placeholder': 'Password'}),
        label=_(u'Password'),
        required=True)

    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
            return self.cleaned_data['email']
        except User.DoesNotExist:
            raise forms.ValidationError(_(u'There is no account with this email'))

    def clean(self):
        if 'password' in self.cleaned_data and 'email' in self.cleaned_data:
            user = authenticate(username=self.cleaned_data['email'], password=self.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    return self.cleaned_data
                else:
                    raise forms.ValidationError(_(u'This account has been disabled'))
            else:
                raise forms.ValidationError(_(u'You have entered an invalid password'))
        return self.cleaned_data