from django import forms
from appThree.models import User
class NewUser(forms.ModelForm):
    class Meta:
        model = User()
        fields='__all__'
