from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from catalog.client import get_product


@require_POST
def cart_add(request, product_id):
    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)
    # Se obtiene la información del producto a agregar y los datos del formulario.
    #product = get_object_or_404(Product, id=product_id)
    product = get_product(str(product_id))

    form = CartAddProductForm(request.POST)
    # Se verifica si el formulario es válido, si es así se procede a agregar el producto.
    if form.is_valid():
        cd = form.cleaned_data
        
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        
    return redirect('cart_detail')


def cart_detail(request):
    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información de cada item del carrito para mostrarla
    for item in cart:
        print(item)
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_remove(request, product_id):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información del producto a remover y se procede a eliminarlo del carrito.
    #product = get_object_or_404(Product, id=product_id)
    product = get_product(str(product_id))
    cart.remove(product)
    return redirect('cart_detail')
