from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from ecom.models import Product


from .models import*

# Create your views here.
def home(request):
    return render(request,'ecom/index.html')
def product(request):
    return render(request,'ecom/product.html')
def ab1(request):
    return render(request,'ecom/about1.html')
def shopping(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'ecom/shopping.html', context)
def contact(request):
    return render(request,'ecom/contact1.html')
def login(request):
    return render(request,'ecom/login.html')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
       
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request,'ecom/cart.html')

def pro(request):
    return render(request,'ecom/pro.html')

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request,'ecom/checkout.html', context)

def main(request):
    return render(request,'ecom/main.html')

def updateitem(data):
    action = data['action']
    print('action:', action)
    return action

def updateitem(request):
    data =json.loads(request.body)

    product_Id = request.POST.get('product_Id')
    product_obj = Product.objects.get(id=product_Id)

    productId = data['productId']
   
    print('productId:', productId)

    #customer = request.user.customer
    product = Product.objects.get_or_create(id=product_Id)
    product = Product.objects.get(id=productId)


    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
     
    return JsonResponse('Item was added', safe=False)
