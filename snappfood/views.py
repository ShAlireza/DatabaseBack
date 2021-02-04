from django.shortcuts import render
from django.db import connection
from django.http.response import JsonResponse

from .quries import *


def CustomerResAtNeigh(request, res_nei):
    sql = CustomerResAtNeighSql.format(res_nei=res_nei)

    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def FoodAtRes(request, res_name, res_num, type3):
    sql = CustomerFoodAtResSql.format(res_name=res_name, res_num=res_num,
                                      type3=type3)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def FoodAtNeighRange(request, res_nei):
    sql = CustomerFoodAtNeighRangeSql.format(res_nei=res_nei)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def AllOrders(request, cus_id):
    sql = CustomerResAtNeighSql.format(cus_id=cus_id)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def FavoriteFood(request, phone_num):
    sql = CustomerFavoriteFoodSql.format(phone_num=phone_num)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def FavoriteRes(request, phone_num):
    sql = CustomerFavoriteResSql.format(phone_num=phone_num)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def PersonWatchTransactions(request, per_id):
    sql = PersonWatchTransactionsSql.format(per_id=per_id)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def CusDiscounts(request, phone_num):
    sql = CusDiscountsSql.format(phone_num=phone_num)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def ObserveBestFood(request, res_num, res_name):
    sql = RestaurantObserveBestFoodSql.format(res_num=res_num,
                                              res_name=res_name)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def ObserveDeliveries(request, del_city):
    sql = RestaurantObserveDeliveriesSql.format(del_city=del_city)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def ObserveOrders(request, res_num, res_name):
    sql = RestaurantObserveOrderSql.format(res_name=res_name)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def ObserveCustomers(request, res_num, res_name):
    sql = RestaurantObserveCussSql.format(res_num=res_num, res_name=res_name)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)


def Delivery(request, res_num, res_nei):
    sql = CusDiscountsSql.format(res_num=res_num, res_nei=res_nei)
    cursor = connection.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    return JsonResponse(data={'rows': rows}, status=200)
