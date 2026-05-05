from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username or Email",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email or username',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900',
        })
    )
    
    password = forms.CharField(
        label="Password",
        max_length=150,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900',
        })
    )
    
    
    
class SignupForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'username',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900',
        })
    )
    
    email = forms.EmailField(
        label= 'Email',
        max_length=150,
        widget=forms.EmailInput(attrs={
            'placeholder': 'email',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900',
        })
    )
    email_confirm = forms.EmailField(
        label= 'Confirm Email',
        max_length=150,
        widget=forms.EmailInput(attrs={
            'placeholder': 'confirm email',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900',
        })
    )
    
    password = forms.CharField(
        label='Password',
        max_length=150,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'password',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900',
        })
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        max_length=150,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'confirm password',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900',
        })
    )
    
    policy_confirm = forms.BooleanField(
        label= 'I agree to the terms and conditions',
        required=True,
      widget=forms.CheckboxInput(attrs={
          'class': 'form-checkbox h-5 w-5 text-blue-600 transition duration-150 ease-in-out',
      })  
    )
    