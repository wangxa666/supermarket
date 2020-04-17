from django.conf.urls import url

from OrderApp import views

urlpatterns=[
    url(r'^makeOrder/',views.makeOrder),
#     订单详情表
    url(r'^orderDetail/',views.orderDetail),

#     支付
    url(r'^testpay/',views.testpay),
]