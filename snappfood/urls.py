from django.urls import path

urlpatterns = [
    path('/customer/ResAtNeigh/<str:res_nei>', ),
    path('/customer/FoodAtRes/<str:res_name>/<str:res_num>/<str:type3>',),
    path('/customer/FoodAtNeighRange/<str:res_nei>',),
    path('/customer/AllOrders/<str:cus_id>',),
    path('/customer/FavoriteFood/<str:phone_num>',),
    path('/customer/FavoriteRes/<str:phone_num>',),
    path('/customer/PersonWatchTransactions/<str:per_id>',),
    path('/customer/CusDiscounts/<str:phone_num>',),
    path('/restaurant/ObserveBestFood/<str:res_num>/<str:res_name>',),
    path('/restaurant/ObserveDeliveries/<str:del_city>',),
    path('/restaurant/ObserveOrders/<str:res_num>/<str:res_name>/',),
    path('/restaurant/Observe_customers/<str:res_num>/<str:res_name>',),
    path('/delivery/ObserveDeliveries/<str:res_num>/<str:res_nei>',),
    path('/delivery/<str:res_num>/<str:res_nei>',),
]
