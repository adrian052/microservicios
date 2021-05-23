from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .client import post_order,post_orderitem
import json
from correos.correos import mandar_correo



def order_create(request):
    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)
    # Si la llamada es por método POST, es una creación de órden.
    if request.method == 'POST':
        # Se obtiene la información del formulario de la orden,
        # si la información es válida, se procede a crear la orden.
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.data)
            order = post_order(data)
            params = json.dumps(form.data)
            id_order = order['id']
            
            for item in cart:

                data = json.dumps({
                    'product_id':item['product']['id'] ,
                    'price':float(item['price']) ,
                    'quantity':item['quantity'],
                    'order':id_order
                })
                post_orderitem(data)
        
            # Se limpia el carrito con ayuda del método clear()
            cart.clear()

            # Llamada al método para enviar el email.
            send(form.data['email'], cart)
            return render(request, 'orders/order/created.html',{'cart': cart,'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})

def send(email,cart):
    print(email)
    total = 0.0
    message = ""
    for item in cart:
        message += "-"+item['product']['name']+" * "+str(item['quantity'])+" $"+str(item['price'])+"="+str(item['quantity']*item['price'])+"\n"
        total+=(float(item['quantity'])*float(item['price']))

    message += "Total = $"+str(total)

    data = json.dumps({
        "subject":"Confirmacion de compra",
        "email":email,
        "message":message
    })
    mandar_correo(data)
    