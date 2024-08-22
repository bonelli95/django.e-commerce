from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(
        label = 'Username',
        required = True,
        max_length = 20,
        widget = forms.TextInput(
            attrs={
                'class' : "form-control form-control-lg",
                "placeholder": "Enter Your Name"
            }
        )
    )

    password = forms.CharField(
        label = "Password",
        required = True,
        max_length = 20,
        widget = forms.PasswordInput(
            attrs = {
                'class' : "form-control form-control-lg",
                'placeholder' : 'Enter your password'
            }
        )
    )

class registerForms(forms.Form):
    register_username = forms.CharField(
        label = 'Username',
        required = True,
        max_length = 20,
        widget = forms.TextInput(
            attrs= {
                'class' :"form-control form-control-lg",
                'placeholder' : 'Register your name'
            }
        )
    )

    email = forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 30,
        widget = forms.EmailInput(
            attrs= {
                'class' :"form-control form-control-lg",
                'placeholder' : 'Register your email'
            }
        )
    )

    password1 = forms.CharField(
        label= 'Password',
        required= True,
        max_length= 20,
        widget= forms.PasswordInput(
            attrs= {
                'class' :"form-control form-control-lg",
                'placeholder' : 'Register your password'
            }
        )
    )

    password2 = forms.CharField(
        label= 'Confirm your password',
        required= True,
        max_length= 20,
        widget= forms.PasswordInput(
            attrs= {
            'class' :"form-control form-control-lg",
            'placeholder' : 'Confirm your password'
            }
        )
    )

    def clean_register_username(self):
        name = self.cleaned_data.get('register_username')

        if name:
            name = name.strip()
            if ' ' in name:
                raise forms.ValidationError('Cannot include space in username')
            else:
                return name
            
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Password are not the same')
            else:
                return password2