CustomerResAtNeighSql = """
select ResName, Phone
	from Res natural join ResPhon
	where Res.ResNei = '{res_nei}'
"""
CustomerFoodAtResSql = """
select * 
	from Food as Fo
 	where Fo.ResName = '{res_name}' and
  	Fo.ResNum = {res_num} and
  	Fo.type3 = '{type3}'
"""

CustomerFoodAtNeighRangeSql = """
select * 
 	 from Food as Fo
 	 where Fo.Price < 100 and
	 Fo.Price > 20 and
	 (Fo.FoName,Fo.ResName,Fo.RCID, Fo.ResNum) in 
	 (select FoName, ResName, RCID, ResNum from
	 Food natural join Res
	 where Food.FoName = Fo.FoName and
	  Food.ResName = Fo.ResName and
	  Food.RCID = Fo.RCID and
	  Food.ResNum = Fo.ResNum and
	  Res.ResNei = '{res_nei}')
"""

CustomerAllOrdersSql = """
 select * from
     OrdFood natural join Order3 natural join Cus as Tab
    where OrdFood.CusID = '{cus_id}'
"""

CustomerFavoriteFoodSql = """
 	select * from 
 	FavoriteFoo natural join Cus
 	Where Cus.PhoneNumber = '{phone_num}'
"""
CustomerFavoriteResSql = """
Select * from
 	FavoriteRes natural join Cus
 	Where Cus.PhoneNumber = '{phone_num}'
"""
PersonWatchTransactionsSql = """
 Select * from 
 Transaction3 natural join Person
 Where person.PerID  = '{per_id}'
"""
CusDiscountsSql = """
 Select * 
 From Discount natural join Cus
 Where Cus.PhoneNumber = '{phone_num}'
 And Discount.Used = False
"""

RestaurantObserveBestFoodSql = """
select * from Food
	where Food.ResNum = '{res_num}' and Food.ResName = '{res_name}'
	order by Food.Seen
"""

RestaurantObserveDeliveriesSql = """
select Delivery.DelPhone, Delivery.DelName
	from Delivery
	where Delivery.DelCity = '{del_city}'
"""

RestaurantObserveOrderSql = """
Select Status
	from Order3 natural join OrdFood as Ta
	where Ta.ResName = '{res_name}' and
		Ta.ResNum = '{res_num}'
"""

RestaurantObserveCussSql = """
select CusName, PhoneNumber
	from Cus natural join ordFood
	where ResName = "{res_name}" and ResNum = "{res_num}"
"""
DeliverySql = """
select OrderId, Time3, CusID, DeliveryCost
	from order3 natural join ordFood natural join res
	where ordFood.ResNum = "{res_num}"
		and Res.ResNei = "{res_nei}"
"""
