from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from account.models import User
from shoppingapp.forms import *
from shoppingapp.models import *
from shoppingapp.permission import *
from onsale import sale
User = get_user_model()

name,discount,percent,price = sale.calculate_discounted_price("JD sports", 50000, 50)

def home_view(request):

    published_shops = Shop.objects.filter(is_published=True).order_by('-timestamp')
    shops = published_shops.filter(is_closed=False)
    total_companies = User.objects.filter(role='employer').count()
    paginator = Paginator(shops, 15)
    page_number = request.GET.get('page',None)
    page_obj = paginator.get_page(page_number)

    if request.is_ajax():
        shop_lists=[]
        shop_objects_list = page_obj.object_list.values()
        for shop_list in shop_objects_list:
            shop_lists.append(shop_list)
        

        next_page_number = None
        if page_obj.has_next():
            next_page_number = page_obj.next_page_number()

        prev_page_number = None       
        if page_obj.has_previous():
            prev_page_number = page_obj.previous_page_number()

        data={
            'shop_lists':shop_lists,
            'current_page_no':page_obj.number,
            'next_page_number':next_page_number,
            'no_of_page':paginator.num_pages,
            'prev_page_number':prev_page_number
        }    
        return JsonResponse(data)
    
    context = {

    'total_floors': 5,
    'total_companies': total_companies,
    'total_shops': len(shops),
    'total_completed_shops':len(published_shops.filter(is_closed=True)),
    'page_obj': page_obj
    }
    print('ok')
    return render(request, 'shoppingapp/index.html', context)


def shop_list_View(request):
    shop_list = Shop.objects.filter(is_published=True,is_closed=False).order_by('-timestamp')
    paginator = Paginator(shop_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    

    context = {

        'page_obj': page_obj,
        'name':name,
        'discount':discount,
        'percent':percent,
        'price':price,

    }
    return render(request, 'shoppingapp/shop-list.html', context)


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def create_shop_View(request):
    form = ShopForm(request.POST or None, request.FILES or None)

    user = get_object_or_404(User, id=request.user.id)
    categories = Category.objects.all()

    if request.method == 'POST':

        if form.is_valid():

            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            # for save tags
            form.save_m2m()
            messages.success(
                    request, 'Your Store has been successfully created! Please wait for approval.')
            return redirect(reverse("shoppingapp:single-shop", kwargs={
                                    'id': instance.id
                                    }))

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'shoppingapp/post-shop.html', context)


def single_shop_view(request, id):
    shop = get_object_or_404(Shop, id=id)
    related_shop_list = shop.tags.similar_objects()

    paginator = Paginator(related_shop_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'shop': shop,
        'page_obj': page_obj,
        'total': len(related_shop_list),
        'name':name,
        'discount':discount,
        'percent':percent,
        'price':price,

    }
    return render(request, 'shoppingapp/shop-single.html', context)


def search_result_view(request):
    shop_list = Shop.objects.order_by('-timestamp')

    # Keywords
    if 'shop_title' in request.GET:
        shop_title_or_company_name = request.GET['shop_title']

        if shop_title_or_company_name:
            shop_list = shop_list.filter(title__icontains=shop_title_or_company_name) | shop_list.filter(
                company_name__icontains=shop_title_or_company_name)

    # location
    if 'location' in request.GET:
        floors = request.GET['location']
        if floors:
            shop_list = shop_list.filter(location__icontains=floors)

    # Shop Type
    if 'shop_type' in request.GET:
        shop_type = request.GET['shop_type']
        if shop_type:
            shop_list = shop_list.filter(shop_type__iexact=shop_type)

    # Shop Type
    if 'tags' in request.GET:
        tags = request.GET['tags']
        if tags:
            shop_list = shop_list.filter(tags__iexact=tags)

    paginator = Paginator(shop_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {

        'page_obj': page_obj,

    }
    return render(request, 'shoppingapp/result.html', context)


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def delete_shop_view(request, id):

    shop = get_object_or_404(Shop, id=id, user=request.user.id)

    if shop:

        shop.delete()
        messages.success(request, 'Your Store  was successfully deleted!')

    return redirect('shoppingapp:dashboard')


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def shop_edit_view(request, id=id):

    shop = get_object_or_404(Shop, id=id, user=request.user.id)
    categories = Category.objects.all()
    form = ShopEditForm(request.POST or None, instance=shop)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # for save tags
        # form.save_m2m()
        messages.success(request, 'Your Store Was Successfully Updated!')
        return redirect(reverse("shoppingapp:single-shop", kwargs={
            'id': instance.id
        }))
    context = {

        'form': form,
        'categories': categories
    }

    return render(request, 'shoppingapp/shop-edit.html', context)
