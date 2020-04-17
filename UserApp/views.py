from io import BytesIO

from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL import ImageFont

import re




from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from UserApp.models import AxfUser
from UserApp.view_constaint import send_email
import uuid

from axf import settings


def register(request):
    if request.method == 'GET':
        return render(request,'axf/user/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        password = make_password(password)


        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        user = AxfUser()

        user.u_name = name
        user.u_password = password
        user.u_email = email
        user.u_icon = icon

        token = uuid.uuid4()
        user.u_token = token

        user.save()


        send_email(name,email,token)

        cache.set(token,user.id,timeout=45)



        return redirect(reverse('axfuser:login'))


def checkName(request):

    name = request.GET.get('name')

    users = AxfUser.objects.filter(u_name=name)

    data = {
        'msg': 'ok',
        'status': 200
    }

    if users:
        data['msg'] = '用户名字已经被注册'
        data['status'] = 201
    else:
        data['msg'] = '用户名字可以使用'

    return JsonResponse(data=data)


def testEmail(request):
    # subject 邮件的主题
    # message 邮件内容
    # from_email 发送者
    # recipient_list 收件人 是一个列表


    subject = '天气变冷'
    html_message = '<h1>上海的冬天来了，很痛苦，非常痛苦</h1>'
    message = '<h1>大家注意穿秋裤</h1>'

    from_email = 'yulin_ljing@163.com'
    recipient_list = ['yulin_ljing@163.com']


    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)


    return HttpResponse('发送成功')


def account(request):

    # 获取当前注册对象 然后修改状态为true
    token = request.GET.get('token')

    user_id = cache.get(token)

    if user_id:
        user= AxfUser.objects.get(pk=user_id)

        user.u_active = True
        user.save()
        # 激活一次之后清空缓存
        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('链接失效，请重新发送邮件')


def login(request):
    if request.method == 'GET':
        return render(request,'axf/user/login.html')
    elif request.method == 'POST':

        imgcode = request.POST.get('imgcode')

        verify_code = request.session.get('verify_code')

        b = re.match(verify_code,imgcode,re.IGNORECASE)

        if b:
            name = request.POST.get('name')
            password = request.POST.get('password')

            users = AxfUser.objects.filter(u_name=name)

            if users.count() > 0:
                user = users.first()

                if check_password(password,user.u_password):
                    if user.u_active == True:
                        # session不允许绑定一个对象
                        request.session['user_id']=user.id
                        return redirect(reverse('axfmine:mine'))
                    else:
                        context = {
                            'msg': '帐号未激活，请去邮箱激活'
                        }
                        return render(request, 'axf/user/login.html', context=context)
                else:
                    context = {
                        'msg': '密码不正确'
                    }
                    return render(request, 'axf/user/login.html', context=context)
            else:
                context = {
                    'msg':'用户不存在'
                }
                return render(request,'axf/user/login.html',context=context)

        else:
            context = {
                'msg':'验证码错误'
            }
            return render(request,'axf/user/login.html',context=context)






def get_code(request):

    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 60)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 50)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")



import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def logout(request):
    request.session.flush()
    return redirect(reverse('axfmine:mine'))