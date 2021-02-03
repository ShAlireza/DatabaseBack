from django.shortcuts import render

# Create your views here.

from .quries import *


def CustomerResAtNeigh(request, res_nei):
    sql = CustomerResAtNeighSql.format(res_nei=res_nei)
    # client = psql.client()
    # answers = client.run(sql)

    return


def FoodAtRes(request, res_name, res_num, type3):
    sql = CustomerFoodAtResSql.format(res_name=res_name, res_num=res_num,
                                      type3=type3)
    # client = psql.client()
    # answers = client.run(sql)

    return


def FoodAtNeighRange(request, res_nei):
    sql = CustomerFoodAtNeighRangeSql.format(res_nei=res_nei)
    # client = psql.client()
    # answers = client.run(sql)

    return


def AllOrders(request, cus_id):
    sql = CustomerResAtNeighSql.format(cus_id=cus_id)
    # client = psql.client()
    # answers = client.run(sql)

    return


def FavoriteFood(request, phone_num):
    sql = CustomerFavoriteFoodSql.format(phone_num=phone_num)
    # client = psql.client()
    # answers = client.run(sql)

    return


def FavoriteRes(request, phone_num):
    sql = CustomerFavoriteResSql.format(phone_num=phone_num)
    # client = psql.client()
    # answers = client.run(sql)

    return


def PersonWatchTransactions(request, per_id):
    sql = PersonWatchTransactionsSql.format(per_id=per_id)
    # client = psql.client()
    # answers = client.run(sql)

    return


def CusDiscounts(request, phone_num):
    sql = CusDiscountsSql.format(phone_num=phone_num)
    # client = psql.client()
    # answers = client.run(sql)

    return


