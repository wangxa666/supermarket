from django.core.cache import cache
from django.core.mail import send_mail
from django.template import loader


def send_email(name,email,token):


    subject = '红浪漫洗浴优惠活动'

    message = ''



    context = {
        'name':name,
        'url':'http://127.0.0.1:8000/axfuser/account/?token='+str(token)
    }

    hm = loader.get_template('axf/user/active.html').render(context=context)

    html_message = hm

    from_email = 'yulin_ljing@163.com'

    recipient_list = [email]


    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,
              recipient_list=recipient_list)

