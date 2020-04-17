from alipay import AliPay
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from CartApp.models import AxfCart
from CartApp.views_constaint import get_total_price
from OrderApp.models import AxfOrder, AxfOrderGoods
from axf.settings import PUBLIC_KEY, PRIVATE_KEY


def makeOrder(request):

    user_id = request.session.get('user_id')
    # 创建order对象的原因是因为ordergoods需要
    order = AxfOrder()

    order.o_user_id = user_id

    order.o_price = get_total_price(user_id)

    order.save()

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    for cart in carts:

        aog = AxfOrderGoods()

        aog.aog_order = order

        aog.aog_goods = cart.c_goods

        aog.aog_num = cart.c_goods_num

        aog.save()

        cart.delete()

    data = {
        'msg':'ok',
        'status':200,
        'order_id':order.id
    }

    return JsonResponse(data=data)


def orderDetail(request):
    order_id = request.GET.get('order_id')
    order = AxfOrder.objects.get(pk=order_id)

    context = {
        'order':order
    }
    return render(request,'axf/order/order_detail.html',context=context)


def testpay(request):

    alipay = AliPay(
        appid="2016093000627735",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False,  # 默认False
    )

    subject = "华为matepro30"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="20161112",
        total_amount=6800,
        subject=subject,
        return_url="http://www.1000phone.com",
        notify_url="http://www.1000phone.com"  # 可选, 不填则使用默认notify url
    )


    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)
