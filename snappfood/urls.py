from django.urls import path
from .views import *

urlpatterns = [
    path('/customer/ResAtNeigh/<str:res_nei>', CustomerResAtNeigh),
    path('/customer/FoodAtRes/<str:res_name>/<str:res_num>/<str:type3>',
         FoodAtRes),
    path('/customer/FoodAtNeighRange/<str:res_nei>', FoodAtNeighRange),
    path('/customer/AllOrders/<str:cus_id>', AllOrders),
    path('/customer/FavoriteFood/<str:phone_num>', FavoriteFood),
    path('/customer/FavoriteRes/<str:phone_num>', FavoriteRes),
    path('/customer/PersonWatchTransactions/<str:per_id>',
         PersonWatchTransactions),
    path('/customer/CusDiscounts/<str:phone_num>', CusDiscounts),
    path('/restaurant/ObserveBestFood/<str:res_num>/<str:res_name>',
         ObserveBestFood),
    path('/restaurant/ObserveDeliveries/<str:del_city>', ObserveDeliveries),
    path('/restaurant/ObserveOrders/<str:res_num>/<str:res_name>/',
         ObserveOrders),
    path('/restaurant/ObserveCustomers/<str:res_num>/<str:res_name>',
         ObserveCustomers),
    path('/delivery/<str:res_num>/<str:res_nei>', Delivery),
]
