import json

from . models import *

def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)             # Product Name
            total = (product.price * cart[i]["quantity"])   # Accessing Quantity-value pair * to price = total

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product' :{
                    'id' : product.id,
                    'name' : product.name,
                    'price' : product.price,
                    'new_image': product.imageURL
                    },
                'quantity': cart[i]["quantity"],
                'is_digital': False,
                'get_total': total,
                }
            items.append(item)

            if product.is_digital == False:
                order['shipping'] = True
        except:
            pass

    return {'cartItems':cartItems, 'order':order, 'items':items}

def cart_data(request):
    if request.user:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()   #Parent-Child querying
        cartItems = order.get_cart_items
    else:
        cookie_data = cookie_cart(request)
        cartItems = cookie_data['cartItems']
        order = cookie_data['order']
        items = cookie_data['items']
        
    return {'cartItems':cartItems, 'order':order, 'items':items}

def guest_order(request, data):
    name = data['form']['name']
    email = data['form']['email']
    
    cookie_data = cookie_cart(request)
    items = cookie_data['items']
    
    customer, created = Customer.objects.get_or_create(
        email=email,
        )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
        )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    
    return customer, order
        