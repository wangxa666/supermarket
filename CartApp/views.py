from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart
from CartApp.views_constaint import get_total_price


def cart(request):

    user_id =request.session.get('user_id')


    # 查询当前帐号的购物车的数据
    carts = AxfCart.objects.filter(c_user_id=user_id)

    # 判断数据库中是否有未被选中的数据
    is_all_select = not AxfCart.objects.filter(c_is_select=False).filter(c_user_id=user_id).exists()


    context = {
        'carts':carts,
        'is_all_select':is_all_select,
        'get_total_price':get_total_price(user_id)
    }

    return render(request,'axf/main/cart/cart.html',context=context)


def addToCart(request):
    user_id = request.session.get('user_id')
    data = {

    }

    if user_id:
        goodsid = request.GET.get('goodsid')

        carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodsid)

        if carts.exists():
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = AxfCart()
            cart.c_user_id = user_id
            cart.c_goods_id = goodsid

        cart.save()
        data['status'] = 200
        data['msg']='添加成功'
        data['c_goods_num'] = cart.c_goods_num

        return JsonResponse(data=data)

    else:
        data['status'] = 201
        data['msg'] = '未登录'
        return JsonResponse(data=data)
        # return redirect(reverse('axfuser:login'))

@csrf_exempt
def subCart(request):

    user_id = request.session.get('user_id')

    cartid = request.POST.get('cartid')

    cart = AxfCart.objects.get(pk=cartid)



    data = {
        'msg': 'ok',
    }

    if cart.c_goods_num > 1:
        cart.c_goods_num = cart.c_goods_num - 1
        cart.save()
        data['status']=200
        data['c_goods_num']=cart.c_goods_num
    else:
        data['status']=204
        cart.delete()

    data['total_price']=get_total_price(user_id)

    is_all_select = not AxfCart.objects.filter(c_is_select=False).filter(c_user_id=user_id).exists()

    data['is_all_select']=is_all_select


    return JsonResponse(data=data)


def changeStatus(request):

    cartid = request.GET.get('cartid')

    cart = AxfCart.objects.get(pk=cartid)

    cart.c_is_select = not cart.c_is_select

    cart.save()

    user_id = request.session.get('user_id')

    is_all_select = not AxfCart.objects.filter(c_is_select=False).filter(c_user_id=user_id).exists()


    data = {
        'msg':'ok',
        'status':200,
        'c_is_select':cart.c_is_select,
        'is_all_select':is_all_select,
        'total_price':get_total_price(user_id)
    }

    return JsonResponse(data=data)


def allSelect(request):
    user_id = request.session.get('user_id')

    cartlist = request.GET.get('cartlist')

    cartid_list = cartlist.split('#')

    carts = AxfCart.objects.filter(id__in = cartid_list)


    for cart in carts:
        cart.c_is_select = not cart.c_is_select
        cart.save()


    data = {
        'msg':'ok',
        'status':200,
        'total_price':get_total_price(user_id)
    }
    return JsonResponse(data=data)