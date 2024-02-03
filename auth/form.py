from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "class": "form-control",
            "id": "exampleFormControlInput1",
            "placeholder": "username",
            "name": "username"
        })
        self.fields['password1'].widget.attrs.update({
            "class": "form-control",
            "id": "inputPassword1",
            "placeholder": "password",
            "name": "password1"
        })
        self.fields['password2'].widget.attrs.update({
            "class": "form-control",
            "id": "inputPassword2",
            "placeholder": "confirm password",
            "name": "password2"
        })


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "class": "form-control",
            "id": "exampleFormControlInput1",
            "placeholder": "username",
            "name": "username"
        })
        self.fields['password'].widget.attrs.update({
            "class": "form-control",
            "id": "inputPassword",
            "placeholder": "password",
            "name": "password"
        })