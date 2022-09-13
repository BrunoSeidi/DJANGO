from http.client import HTTPResponse
from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from store.models import Product

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()

def add_cart(request, product_id):
    product = Product.objects.get(id = product_id) #get the product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) #get cart by id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return HTTPResponse(cart_item.quantity)
    exit()
    return redirect('cart')



def cart(request):
    return render(request, 'store/cart.html')
