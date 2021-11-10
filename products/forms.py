from django.forms import ModelForm
from products.models import Product


class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'price', 'quantity']
