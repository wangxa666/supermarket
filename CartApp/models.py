from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class AxfCart(models.Model):
    c_user = models.ForeignKey(AxfUser)
    c_goods = models.ForeignKey(AxfGoods)

    c_goods_num = models.IntegerField(default=1)
    c_is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'axf_cart'
