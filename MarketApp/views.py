from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods
from MarketApp.view_helper import COM_SORT_RULE, SORT_RULE_BY_PRICE_UP, SORT_RULE_BY_PRICE_DOWN, SORT_RULE_BY_NUM_UP, \
    SORT_RULE_BY_NUM_DOWN


def market(request):

    foodtypes = AxfFoodType.objects.all()

    typeid = request.GET.get('typeid','104749')

    goods_list = AxfGoods.objects.filter(categoryid=typeid)

    # 全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540


    # AxfFoodType.objects.filter(typeid=typeid)  【object】
    # 【object】[0] ===>object
    # object.childtypenames

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames

    # 必须使用.语法来获取汉字以及数字
    # ['全部分类:0', '酸奶乳酸菌:103537', '牛奶豆浆:103538', '面包蛋糕:103540']
    childtypename_list = childtypenames.split('#')

    # [['全部分类', '0'], ['酸奶乳酸菌', '103537'], ['牛奶豆浆', '103538'], ['面包蛋糕', '103540']]
    childtype_list = []

    for childtypename in childtypename_list:
        childtype = childtypename.split(':')
        childtype_list.append(childtype)


    childcid = request.GET.get('childcid','0')

    # childcid有2中情况   （1）是0的时候  商品不变  （2）如果不是0  就做2级联动

    if childcid == '0':
        pass
    else:
        goods_list = goods_list.filter(childcid=childcid)


    sort_rule_list = [
        ['综合排序',COM_SORT_RULE],
        ['价格升序',SORT_RULE_BY_PRICE_UP],
        ['价格降序',SORT_RULE_BY_PRICE_DOWN],
        ['销量升序',SORT_RULE_BY_NUM_UP],
        ['销量降序',SORT_RULE_BY_NUM_DOWN],
    ]

    s_rule = request.GET.get('s_rule',COM_SORT_RULE)

    if s_rule == COM_SORT_RULE:
        pass

    elif s_rule == SORT_RULE_BY_PRICE_UP:
        goods_list = goods_list.order_by('price')

    elif s_rule == SORT_RULE_BY_PRICE_DOWN:
        goods_list = goods_list.order_by('-price')

    elif s_rule == SORT_RULE_BY_NUM_UP:
        goods_list = goods_list.order_by('productnum')

    elif s_rule == SORT_RULE_BY_NUM_DOWN:
        goods_list = goods_list.order_by('-productnum')


    context = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'childtype_list':childtype_list,
        'childcid':childcid,
        'sort_rule_list':sort_rule_list,
        's_rule':s_rule,
    }

    return render(request,'axf/main/market/market.html',context=context)