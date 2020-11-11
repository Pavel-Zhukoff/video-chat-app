from django import forms


class PasswordRoomEnterForm(forms.Form):
    password = forms.CharField(required=True)
