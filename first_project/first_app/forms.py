from django import forms
from first_app.models import Users
class NewUser(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'
