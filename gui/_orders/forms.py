from django import forms


class OrderCreateForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    address = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=100)

   