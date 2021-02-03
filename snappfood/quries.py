CustomerResAtNeighSql = """
select ResName, Phone
	from Res natural join ResPhon
	where Res.ResNei = {res_nei}
"""
CustomerFoodAtResSql = """
select * 
	from Food as Fo
 	where Fo.ResName = {res_name} and
  	Fo.ResNum = {res_num} and
  	Fo.type3 = {type3};
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
	  Res.ResNei = {res_nei});
"""

CustomerAllOrdersSql = """
 select * from
     OrdFood natural join Order3 natural join Cus as Tab
    where OrdFood.CusID = {cus_id};
"""

CustomerFavoriteFoodSql = """
 	select * from 
 	FavoriteFoo natural join Cus
 	Where Cus.PhoneNumber = {phone_num};
"""
CustomerFavoriteResSql = """
Select * from
 	FavoriteRes natural join Cus
 	Where Cus.PhoneNumber = {phone_num};
"""
PersonWatchTransactionsSql = """
 Select * from 
 Transaction3 natural join Person
 Where person.PerID  = {per_id};
"""
CusDiscountsSql = """
 Select * 
 From Discount natural join Cus
 Where Cus.PhoneNumber = {phone_num}
 And Discount.Used = False
"""

