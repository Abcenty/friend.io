from django.contrib.auth.forms import UserChangeForm
from users.models import User
from django import forms


"""class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, 'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('username', )
"""