from django.forms import ModelForm, widgets, TextInput, FileInput,EmailInput
from .models import User

class RegisterForm(ModelForm):
   
    class Meta:
        model = User 
        fields = ["gender","first_name", "last_name", "email","phone_number","avatar_url","username"]
        widgets = {
            'first_name':TextInput(),
            'last_name':TextInput(),
            'email':EmailInput(),
            'phone_number':TextInput(),
            'avatar_url': FileInput(attrs={
                'type': "file",
                'name': 'image',
                }),
             'username':TextInput(),    
        }