from django.conf.urls import url

from UserApp import views

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^checkName/',views.checkName,name='checkName'),
#     激活
    url(r'^account/',views.account),
#     登录
    url(r'^login/',views.login,name='login'),
#     验证码
    url(r'^get_code/',views.get_code),

#     退出
    url(r'^logout/',views.logout,name='logout'),


#     发送邮件
    url(r'^testEmail/',views.testEmail),


]