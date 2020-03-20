from django import forms


class ProductSearchForm(forms.Form):
    category_number = forms.CharField(label='Category Number')
    product_number = forms.CharField(label='Number of Product')
