from django.shortcuts import render, get_object_or_404
from .client import get_categories, get_products,get_product
from cart.forms import CartAddProductForm

#from .models import Category, Product

def product_list(request, category_slug=None):
    
    category = None
    categories = get_categories()
    
    products = get_products()
    products_filtered = []
    ##filter by products
    category_selected = None
    
    for category in categories:
        if category['slug'] == category_slug:
            category_selected = category    

    for product in products:
        if product['available']:
            if (category_slug and product['category'] == category_selected['id']) or (not category_slug):
                products_filtered.append(product)

    return render(request, 'shop/product/list.html',{"categories": categories,"products": products_filtered})


def product_detail(request, id, slug):
    product =  get_product(str(id))
    # Se obtiene la información del producto que se mostrará.
    #product = get_object_or_404(Product, id=id, slug=slug, available=True)

    # Se obtiene el formulario para agregar elementos de este producto al carrito.
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html', {"product" : product,
                                                "cart_product_form":cart_product_form})