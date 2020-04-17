from django.conf.urls import url

from CartApp import views

urlpatterns=[
    url(r'^cart/',views.cart,name='cart'),
#     添加到购物车
    url(r'^addToCart/',views.addToCart),

#     减少数据量
    url(r'^subCart/',views.subCart),

#     改变选中状态
    url(r'^changeStatus/',views.changeStatus),

#     全选
    url(r'^allSelect/',views.allSelect),
]