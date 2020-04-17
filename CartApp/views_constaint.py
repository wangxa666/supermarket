from CartApp.models import AxfCart


def get_total_price(user_id):

    total_price = 0

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)


    for cart in carts:

        total_price = total_price + cart.c_goods_num * cart.c_goods.price

    return total_price