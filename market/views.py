from django.shortcuts import render, redirect
from django.contrib import auth
from market.forms import AddItemForm
from market.models import Item, TradeItems, BlackBox

def start(request):
    return redirect('/market/')

def home(request):
    args = {}
    args['username'] = auth.get_user(request).username
    if auth.get_user(request).username:
        user = request.user
        args['items'] = Item.objects.filter(user=user)
    return render(request, 'home.html', args)

def addItem(request):
    if request.POST:
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            form.save()
        return redirect('/market/')
    else:
        args = {}
        args['form'] = AddItemForm
        args['username'] = auth.get_user(request).username
        return render(request, 'addItem.html', args)

def search(request):
    args = {}
    args['username'] = auth.get_user(request).username
    if auth.get_user(request).username:
        user = request.user
        all_items = Item.objects.exclude(user=user)
        items_in_black_box = BlackBox.objects.filter(user=user)
        items_bb = []
        for item in items_in_black_box:
            items_bb.append(item.item.id)
        args['items'] = all_items.exclude(id__in=items_bb)
    return render(request, 'search.html', args)

def offer(request):
    args = {}
    args['username'] = auth.get_user(request).username
    if auth.get_user(request).username:
        user = request.user
        args['offers'] = TradeItems.objects.filter(userFirst=user)
    return render(request, 'offer.html', args)

item1_id = 0

def choice(request, item_id):
    args = {}
    args['username'] = auth.get_user(request).username
    args['itemnum'] = item_id
    if auth.get_user(request).username:
        user = request.user
        args['items'] = Item.objects.filter(user=user)
    request.session['it'] = item_id
    global item1_id
    item1_id = item_id
    return render(request, 'choice.html', args)



def trade(request, item_id):
    args={}
    args['username'] = auth.get_user(request).username
    item1 = Item.objects.get(id=item1_id)
    user1 = item1.user
    item2 = Item.objects.get(id=item_id)
    user2 = item2.user
    new_trade = TradeItems(itemFirst=item1, userFirst=user1, itemSecond=item2, userSecond=user2)
    new_trade.save()
    return redirect('/market/')

def accept(request, offer_id):
    offer = TradeItems.objects.get(id=offer_id)
    itemFirst_id = offer.itemFirst.id
    itemSecond_id = offer.itemSecond.id
    offers = TradeItems.objects.all()
    for offerDel in offers:
        if offerDel.itemFirst.id == itemFirst_id or offerDel.itemFirst.id == itemSecond_id or offerDel.itemSecond.id == itemFirst_id or offerDel.itemSecond.id == itemSecond_id:
            offerDel.delete()
    offer.delete()
    item = Item.objects.get(id=itemFirst_id)
    item.delete()
    item = Item.objects.get(id=itemSecond_id)
    item.delete()
    return redirect('/market/')

def deny(request, offer_id):
    offer = TradeItems.objects.get(id=offer_id)
    new_black_box = BlackBox(user=offer.userFirst, item=offer.itemSecond)
    new_black_box.save()
    offer.delete()
    return redirect('/market/')