from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Item, Cart, Order, OrderDetails
from django.db.models import Q
import datetime
from django.utils.crypto import get_random_string
from django.contrib import messages


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request,'core/home.html',context)

def about(request):
    return render(request, 'core/about.html')

def menu(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/menu.html', context)

def contact(request):
    return render(request, 'core/contact.html')

#CART FUNCTION
@login_required(login_url='login')
def cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user) 
    total_amount = 0
    for p in cart:
        value = p.quantity * p.item.price
        total_amount = total_amount + value
    return render(request,'core/cart.html',locals())

def add_to_cart(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    user = request.user
    item_id = request.GET.get('item_id')
    item = Item.objects.get(id=item_id)
    if Cart.objects.filter(user=user, item=item).first():
        cart_item = Cart.objects.get(user=user, item=item)
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart(user=user,item=item).save()
        
    return redirect('/cart')

def plus_cart(request):
    if request.method == "GET":
        item_id=request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id)&Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        total_amount = 0
        for p in cart:
            value = p.quantity * p.item.price
            total_amount = total_amount + value
            data={
                'quantity':c.quantity,
                'total_amount':total_amount,
                'amount':c.quantity*c.item.price
            }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == "GET":
        item_id=request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id)&Q(user=request.user))
        c.quantity-=1
        c.save()
        if c.quantity == 0:
            c.delete()
            return redirect(reverse('cart'))
        user = request.user
        cart = Cart.objects.filter(user=user)
        total_amount = 0
        for p in cart:
            value = p.quantity * p.item.price
            total_amount = total_amount + value
            data={
                'quantity':c.quantity,
                'total_amount':total_amount,
                'amount':c.quantity*c.item.price
            }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == "GET":
        item_id = request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id)&Q(user=request.user))
        print(c)
        c.delete()
        return redirect(reverse('cart'))

@login_required(login_url='login')
def checkout(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    if not cart:
        messages.error(request,'Nothing in the cart!')
        return redirect('cart')
    total_amount = 0
    for p in cart:
        value = p.quantity * p.item.price
        total_amount = total_amount + value

    year = datetime.date.today().year
    years =[]
    for i in range(0,20):
        years.append(year + i)
    
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        address = request.POST['address']
        zipcode = request.POST['zipcode']
        print(fullname,email,address,zipcode)

        card_number = request.POST['card_num']
        cvc = request.POST['cvc']

        if len(card_number) != 16 or len(cvc) != 3:
            messages.error(request,'Card details not valid. Try again')
            return redirect('checkout')
        else:
            order_id = get_random_string(8, allowed_chars='0123456789')
            OrderDetails(order_number=order_id, user=user, name=fullname,email=email,address=address,zipcode=zipcode).save()

            for c in cart:
                Order(order_number=order_id, user=user, item=c.item, quantity=c.quantity,ordered=True).save()
                c.delete()
            
            request.session['order_id'] = order_id
            return redirect('ordered')
            
    return render(request, 'core/checkout.html',locals())


def ordered(request):
    order_id = request.session['order_id']
    print(order_id)
    order_placed = Order.objects.filter(user=request.user, order_number=order_id)
    total_amount = 0
    for order in order_placed:
        value = order.quantity * order.item.price
        total_amount = total_amount + value
    return render(request, 'core/ordered.html', locals())