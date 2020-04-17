from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class AxfOrder(models.Model):
    o_user = models.ForeignKey(AxfUser)
    o_price = models.FloatField()

    class Meta:
        db_table = 'axf_order'


class AxfOrderGoods(models.Model):
    aog_order = models.ForeignKey(AxfOrder)
    aog_goods = models.ForeignKey(AxfGoods)

    aog_num = models.IntegerField(default=1)


    class Meta:
        db_table = 'axf_ordergoods'





