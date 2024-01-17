class Entity:
    def get_att(self):
        d=self.__dict__
        s=''
        for v in d.values():
            s+=str(v)+'$'
        s=s[:len(s)-1]
        s+='#'
        return s
    
    def save(self,filename):
        att=self.get_att()
        f=open(filename,'a+',encoding='utf-8')
        f.write(att)
        f.close()
    def edit(self,filename,t)   :
       
        old=self.get_att()
        new=''
        for v in t:
             new+=str(v)+'$'
        new=new[:len(new)-1]
        new+='#'
        f=open(filename,'r',encoding='utf-8')
        s=f.read()
        f.close()
        s=s.replace(old,new)
        f=open(filename,'w',encoding='utf-8')
        f.write(s)
        f.close()
        
    def delete(self,filename):
        att=self.get_att()
        f=open(filename,'r',encoding='utf-8')
        s=f.read()
        f.close()
        s=s.replace(att,'')
        f=open(filename,'w',encoding='utf-8')
        f.write(s)
        f.close()
class Restaurant:
    filename='Restaursant.txt'
    name="کافه رستوران برلین"
    tel1="0713-6325434"
    tel2="0713-6325535"
    phone="09309265234"
    address="شیراز - معالی آباد - خیابان خلبانان - جنب کوچه 7"
    clock_sobh="8-11"
    clock_zohr="12-16"
    clock_shab="19-23"
    tarikh_eftetah="1401/10/07"
    @classmethod
    def editName(cls,name):
        Restaurant.name=name
    @classmethod
    def editTel(cls,tel1,tel2):
        Restaurant.tel=tel1
        Restaurant.tel=tel2
    @classmethod
    def editPhone(cls,phone):
        Restaurant.phone=phone
    @classmethod
    def editAddress(cls,address):
        Restaurant.address=address
    @classmethod
    def save(cls):
        f=open("Restaurant_info.txt","w")
        f.write("name:"+Restaurant.name+"\n"+"tel:"+Restaurant.tel+"\n"+"phone:"+Restaurant.phone+"\n"+"address:"+Restaurant.address)
        f.close()
    @classmethod
    def read(cls):
        f=open("Restaurant_info.txt","rt")
        print(f.read())
        f.close() 


class Person(Entity):
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
        
class Peik(Person):
    filename="Peik.txt"
    def __init__(self,name,last_name,address,code_meli,age):
        Person.__init__(self,name,last_name)
        self.address=address
        self.code_meli=code_meli
        self.age=age
    # @property    
    # def code_meli(self):
    #     return self.__code_meli
    # @code_meli.setter
    # def code_meli(self,value):
    #     if len(value)==10:
    #         self.__code_meli=value
    #     else:
    #         raise ValueError("invalid")
    # @property    
    # def age(self):
    #     return self.__age
    # @age.setter
    # def age(self,value):
    #     if value>18:
    #         self.__age=value
    #     else:
    #         raise ValueError("invalid")
    def __str__(self):
        return self.name+'  '+self.last_name
    def save(self):
        super().save(Peik.filename)
    def edit(self,*t) :
        super().edit(Peik.filename,t)    
    def delete(self):
        super().delete(Peik.filename)
        
    @classmethod
    def read_file(cls):
        f=open(Peik.filename,'r',encoding='utf-8')
        s=f.read().split('#')
        lst=[]
        s.pop()
        
        for v in s:
            t=v.split('$')
            lst.append(Peik(t[0],t[1],t[2],t[3],t[4]))
        f.close()
        return lst

class Customer(Person):
    filename="customer.txt"
    def __init__(self,name,last_name,code,address):
        Person.__init__(self,name,last_name)
        self.code=code
        self.address=address
    # @property    
    # def code(self):
    #     return self.__code
    # @code.setter
    # def code(self,value):
    #     if value>0:
    #         self.__code=value
        # else:
        #     raise ValueError("invalid")
    def __str__(self):
        return self.name+'  '+self.last_name
    def save(self):
        super().save(Customer.filename)
    def edit(self,*t) :
        super().edit(Customer.filename,t)    
    def delete(self):
        super().delete(Customer.filename)
        
    @classmethod
    def read_file(cls):
        f=open(Customer.filename,'r',encoding='utf-8')
        s=f.read().split('#')
        lst=[]
        s.pop()
        
        for v in s:
            t=v.split('$')
            lst.append(Customer(t[0],t[1],t[2],t[3]))
        f.close()
        return lst
    

class Food(Entity):
    def __init__(self,name,code,price,stock):
        self.name=name
        self.code=code
        self.price=price
        self.stock=stock
    @property    
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if value>0:
            self.__price=value
        else:
            raise ValueError("invalid")
    @property    
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,value):
        if value>=0:
            self.__stock=value
        else:
            raise ValueError("invalid")
class FoodSobhane(Food):
    filename="Food_Sobhane.txt"
    def __init__(self,name,code,price,stock):
        Food.__init__(self,name,code,price,stock)

    def edit(self,*t) :
        super().edit(FoodSobhane.filename,t)
        
    def delete(self):
        super().delete(FoodSobhane.filename)
       
    def reduce_stock(self,count) :
        if self.stock>=count:
            self.stock-=count
        else:
            raise ValueError('موجودی  کافی نیست')
            
    def __str__(self):
        return self.name+'  '+str(self.price)
    def save(self):
        super().save(FoodSobhane.filename)
    
    @classmethod
    def read_file(cls):
        f=open(FoodSobhane.filename,'r',encoding='utf-8')
        s=f.read().split('#')
        lst=[]
        s.pop()
        for v in s:
            t=v.split('$')
            lst.append(FoodSobhane(t[0],t[1],int(t[2]),int(t[3])))
        f.close()
        return lst
class FoodNahar(Food):
    filename="Food_Nahar.txt"
    def __init__(self,name,code,price,stock):
        Food.__init__(self,name,code,price,stock)


    def edit(self,*t) :
        super().edit(FoodNahar.filename,t)
        
    def delete(self):
        super().delete(FoodNahar.filename)
       
    def reduce_stock(self,count) :
        if self.stock>=count:
            self.stock-=count
        else:
            raise ValueError('موجودی  کافی نیست')
            
    def __str__(self):
        return self.name+'  '+str(self.price)
    def save(self):
        super().save(FoodNahar.filename)
    
    @classmethod
    def read_file(cls):
        f=open("Food_Nahar.txt",'r',encoding='utf-8')
        s=f.read().split('#')
        lst=[]
        s.pop()
        for v in s:
            t=v.split('$')
            lst.append(FoodNahar(t[0],t[1],int(t[2]),int(t[3])))
        f.close()
        return lst
class FoodSham(Food):
    filename="Food_Sham.txt"
    def __init__(self,name,code,price,stock):
        Food.__init__(self,name,code,price,stock)
    def edit(self,*t) :
        super().edit(FoodSham.filename,t)
        
    def delete(self):
        super().delete(FoodSham.filename)
       
    def reduce_stock(self,count) :
        if self.stock>=count:
            self.stock-=count
        else:
            raise ValueError('موجودی  کافی نیست')
            
    def __str__(self):
        return self.name+'  '+str(self.price)
    def save(self):
        super().save(FoodSham.filename)
    
    @classmethod
    def read_file(cls):
        f=open(FoodSham.filename,'r',encoding='utf-8')
        s=f.read().split('#')
        lst=[]
        s.pop()
        for v in s:
            t=v.split('$')
            lst.append(FoodSham(t[0],t[1],int(t[2]),int(t[3])))
        f.close()
        return lst

# class Factor:
#     def __init__(self,number,date_of_order,order):
#         self.number=number
#         self.date_of_order=date_of_order
#         self.order=order
#     def showFactor(self):
#         pass
# class Order:
#     filename='food.txt'
#     def __init__(self,menu,time_of_order,customer):
#         self.order_list=[]
#         self.menu=menu
#         self.customer=customer
    

#     def addFood(self,food,count):
#         if food.name in self.menu:
#             if self.menu[food]["mojodi"]>0:
#                 price=self.menu[food]["price"]
#                 self.order_list.append([food,count,price])
#             else:
#                 print("Tamam kardim!")
#         else:
#             print("invalid food!")
#     def __str__(self):
#         return self.name+'  '+str(self.price)
#     def save(self):
        # super().save(Food.filename)
# if '__main__'==__name__:
#     f2=FoodSobhane("sdaas", 78, 97)
#     f2.save()
#     f3=FoodNahar("sdaas", 67, 97)
#     f3.save()
#     f4=FoodSham("sdaas", 67, 97)
#     f4.save()
#     c1=Customer("ali","hamidi",1213,"pasdaran")
#     c1.save()
#     p1=Peik("ali","karimi","avini",1212,23)
