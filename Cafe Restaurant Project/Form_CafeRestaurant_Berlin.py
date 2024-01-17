import tkinter as tk
from tkinter import ttk
import Class_CafeRestaurant_Berlin as rp
import time
from datetime import date
main_win=tk.Tk()
main_win.title("صفحه اصلی")
window_height = 500
window_width = 900
screen_width = main_win.winfo_screenwidth()
screen_height = main_win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
main_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
main_win.configure(bg="#DCDCDC")
main_win.resizable(False,False)

canvas = tk.Canvas(main_win,width=500, height=900, bg='#FFA500')
canvas.pack(expand=tk.YES, fill=tk.BOTH)
main_image = tk.PhotoImage(file='main_win_image.png')
canvas.create_image(0,0, image=main_image, anchor=tk.NW)


main_menu=tk.Menu(main_win)

about_menu=tk.Menu(main_menu,tearoff=0)

def creat_list(class_name,win_name,row,column,height,width):
    s=class_name.read_file()
    val=tk.StringVar(value=s)
    lst=tk.Listbox(win_name,listvariable=val,justify="right",height=height,width=width,font=("Mj_Heritage Two Bold",18))
    lst.grid(row=row,column=column)
    return lst,s
def creat_Combobox(class_name,win_name,row,column):
    s=class_name.read_file()
    val=tk.StringVar()
    lst=ttk.Combobox(win_name,textvariable=val,justify="right",height=8,width=20,font=("Mj_Heritage Two Bold",18))
    
    lst["values"] = s
   
    lst["state"] = "readonly"
    lst.grid(row=row,column=column)
    return lst,s

def clockWin():
    clock_win=tk.Toplevel()
    clock_win.title("ساعت کاری")
    window_height = 320
    window_width = 500
    screen_width = clock_win.winfo_screenwidth()
    screen_height = clock_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    clock_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    clock_win.resizable(False,False)
    clock_win.configure(bg="#FAA770")
    tk.Label(clock_win,text=":ساعت کاری مجموعه برلین",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(clock_win,text=":ساعت کاری صبح(صبحانه)",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600").pack(fill=tk.X)
    tk.Label(clock_win,text=rp.Restaurant.clock_sobh,font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770").pack(fill=tk.X)
    tk.Label(clock_win,text=":ساعت کاری ظهر(ناهار)",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600").pack(fill=tk.X)
    tk.Label(clock_win,text=rp.Restaurant.clock_zohr,font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770").pack(fill=tk.X)
    tk.Label(clock_win,text=":ساعت کاری شب (شام)",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600").pack(fill=tk.X)
    tk.Label(clock_win,text=rp.Restaurant.clock_shab,font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770").pack(fill=tk.X)
    back_btn=tk.Button(clock_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :clock_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
    
about_menu.add_command(label="ساعت کاری",font=("Mj_Heritage Two Bold",14),command=clockWin)
about_menu.add_separator()

def addressWin():
    address_win=tk.Toplevel()
    address_win.title("آدرس رستوران")
    window_height = 150
    window_width = 500
    screen_width = address_win.winfo_screenwidth()
    screen_height = address_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    address_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    address_win.configure(bg="#FAA770")
    address_win.resizable(False,False)
    tk.Label(address_win,text=":آدرس مجموعه برلین",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)
    tk.Label(address_win,text=rp.Restaurant.address,font=("Mj_Heritage Two Bold",20),justify="right",anchor=tk.E,bg="#FAA770",padx=10).pack(fill=tk.X)
    back_btn=tk.Button(address_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :address_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
about_menu.add_command(label="آدرس رستوران",font=("Mj_Heritage Two Bold",14),command=addressWin)
about_menu.add_separator()
def hisWin():
    his_win=tk.Toplevel()
    his_win.title("تاریخ تاسیس")
    window_height = 200
    window_width = 500
    screen_width = his_win.winfo_screenwidth()
    screen_height = his_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    his_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    his_win.configure(bg="#FAA770")
    his_win.resizable(False,False)
    tk.Label(his_win,text=":تاریخ تاسیس مجموعه برلین",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(his_win,text=rp.Restaurant.tarikh_eftetah,font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600").pack(fill=tk.X)
    tk.Label(his_win,text="مجموعه برلین یک مجموعه تازه تاسیس با نیروی کار جوان و بروز است\n این مجموعه اولین رستوران تمام اتوماتیک استان فارس میباشد.",font=("Mj_Heritage Two Bold",14),justify="right",bg="#FAA770").pack(fill=tk.X)
    back_btn=tk.Button(his_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :his_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
about_menu.add_command(label="تاریخ تاسیس",font=("Mj_Heritage Two Bold",14),command=hisWin)
about_menu.add_separator()


def telWin():
    tel_win=tk.Toplevel()
    tel_win.title("تلفن ثبت سفارش")
    window_height = 220
    window_width = 500
    screen_width = tel_win.winfo_screenwidth()
    screen_height = tel_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    tel_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    tel_win.configure(bg="#FAA770")
    tel_win.resizable(False,False)
    tk.Label(tel_win,text=":تلفن های ثبت سفارش",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)
    tk.Label(tel_win,text=rp.Restaurant.tel1,font=("Mj_Heritage Two Bold",20),justify="left",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(tel_win,text=rp.Restaurant.tel2,font=("Mj_Heritage Two Bold",20),justify="left",bg="#FF6600",padx=10).pack(fill=tk.X)
    tk.Label(tel_win,text=rp.Restaurant.phone,font=("Mj_Heritage Two Bold",20),justify="left",bg="#FAA770",padx=10).pack(fill=tk.X)
    back_btn=tk.Button(tel_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :tel_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
about_menu.add_command(label="تلفن ثبت سفارش",font=("Mj_Heritage Two Bold",14),command=telWin)
about_menu.add_separator()
def socialMediaWin():
    social_media_win=tk.Toplevel()
    social_media_win.title("شبکه های اجتماعی")
    window_height = 300
    window_width = 500
    screen_width = social_media_win.winfo_screenwidth()
    screen_height = social_media_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    social_media_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    social_media_win.configure(bg="#FAA770")
    social_media_win.resizable(False,False)
    tk.Label(social_media_win,text=":آدرس اینستاگرام",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)
    tk.Label(social_media_win,text="@CafeRestuaranBerlin",font=("Mj_Heritage Two Bold",20),justify="left",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(social_media_win,text=":آدرس ایمیل مجموعه",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)
    tk.Label(social_media_win,text="BerlinCafe@gmail.com",font=("Mj_Heritage Two Bold",20),justify="left",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(social_media_win,text=":شماره واتساپ",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)
    tk.Label(social_media_win,text="09309024924",font=("Mj_Heritage Two Bold",20),justify="left",bg="#FAA770",padx=10).pack(fill=tk.X)
    back_btn=tk.Button(social_media_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :social_media_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
about_menu.add_command(label="شبکه های اجتماعی",font=("Mj_Heritage Two Bold",14),command=socialMediaWin)
about_menu.add_separator()

learn_menu=tk.Menu(main_menu,tearoff=0)
sapce_menu=tk.Menu(main_menu,tearoff=0)
def howWin():
    how_win=tk.Toplevel()
    how_win.title("نحوه ثبت سفارش")
    window_height = 500
    window_width = 500
    screen_width = how_win.winfo_screenwidth()
    screen_height = how_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    how_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    how_win.configure(bg="#FAA770")
    how_win.resizable(False,False)
    tk.Label(how_win,text=":نحوه ثبت سفارش",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(how_win,text="........",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)
    back_btn=tk.Button(how_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :how_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
learn_menu.add_command(label="نحوه ثبت سفارش",font=("Mj_Heritage Two Bold",14),command=howWin)
learn_menu.add_separator()
def roleWin():
    role_win=tk.Toplevel()
    role_win.title("قوانین")
    window_height = 500
    window_width = 500
    screen_width = role_win.winfo_screenwidth()
    screen_height = role_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    role_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    role_win.configure(bg="#FAA770")
    role_win.resizable(False,False)
    tk.Label(role_win,text=":قوانین ثبت سفارش",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(role_win,text=".....",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)

    back_btn=tk.Button(role_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :role_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
learn_menu.add_command(label="قوانین",font=("Mj_Heritage Two Bold",14),command=roleWin)
learn_menu.add_separator()

def howReservWin():
    how_reserv_win=tk.Toplevel()
    how_reserv_win.title("شرایط رزرو")
    window_height = 500
    window_width = 500
    screen_width = how_reserv_win.winfo_screenwidth()
    screen_height = how_reserv_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    how_reserv_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    how_reserv_win.configure(bg="#FAA770")
    how_reserv_win.resizable(False,False)
    tk.Label(how_reserv_win,text="شرایط رزرو تلفنی میز",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FAA770",padx=10).pack(fill=tk.X)
    tk.Label(how_reserv_win,text=".....",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)

    back_btn=tk.Button(how_reserv_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :how_reserv_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
learn_menu.add_command(label="شرایط رزور",font=("Mj_Heritage Two Bold",14),command=howReservWin)
learn_menu.add_separator()
main_menu.add_cascade(label=" "*70,menu=sapce_menu)
main_menu.add_cascade(label="اطلاعات بیشتر",menu=about_menu)

main_menu.add_cascade(label=" "*100,menu=sapce_menu)
main_menu.add_cascade(label="آموزش ها",menu=learn_menu)



def menuShow():
    menu_show_win=tk.Toplevel()
    menu_show_win.title("نمایش منو")
    window_height = 500
    window_width = 900
    screen_width = menu_show_win.winfo_screenwidth()
    screen_height = menu_show_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    menu_show_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    menu_show_win.configure(bg="#FAA770")
    menu_show_win.resizable(False,False)
    tk.Label(menu_show_win,text='منو مورد نظر را انتخاب کنید',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).pack()

    def menuShowSobhane():
        menu_sobhane_win=tk.Toplevel()
        menu_sobhane_win.title("منو صبحانه")
        window_height = 500
        window_width = 580
        screen_width = menu_sobhane_win.winfo_screenwidth()
        screen_height = menu_sobhane_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        menu_sobhane_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        menu_sobhane_win.configure(bg="#FAA770")
        menu_sobhane_win.resizable(False,False)
        menu_frame=tk.Frame(menu_sobhane_win,bg="#FAA770")
        menu_frame.grid(row=0,column=0)
        info_frame=tk.Frame(menu_sobhane_win,bg="#FAA770")
        info_frame.grid(row=0,column=1)
        btn_frame=tk.Frame(menu_sobhane_win,bg="#FAA770")
        btn_frame.grid(row=1)
        tk.Label(menu_frame,text='منو صبحانه',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right").grid(row=0,column=0)
        sobhane_list,s=creat_list(rp.FoodSobhane,menu_frame,1,0,"12","49")
        back_btn=tk.Button(btn_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :menu_sobhane_win.destroy())
        back_btn.grid(row=0,column=3)
        tk.Label(info_frame,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            
        txt_name=tk.StringVar(value='###')
        ent_name=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_name)
        ent_name.grid(row=0,column=0)
            
        tk.Label(info_frame,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=1,column=1)
            
        txt_price=tk.StringVar(value='###')
        ent_price=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_price)
        ent_price.grid(row=1,column=0)
            
        tk.Label(info_frame,text=' کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=2,column=1)
        
        txt_code=tk.StringVar(value='###')
        ent_code=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_code)
        ent_code.grid(row=2,column=0)
            
        tk.Label(info_frame,text='موجودی غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=3,column=1)
            
        txt_stock=tk.StringVar(value='###')
        ent_stock=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_stock)
        ent_stock.grid(row=3,column=0)
        item=(0,)
        def selectFoodSobhane(event):
            global item
            try:
                newitem=sobhane_list.curselection()
                if newitem:
                    item=newitem
                    txt_name.set(s[item[0]].name)
                    txt_price.set(s[item[0]].price)
                    txt_code.set(s[item[0]].code)
                    txt_stock.set(s[item[0]].stock)
                    
            except:
                pass
        (sobhane_list).bind("<<ListboxSelect>>",selectFoodSobhane)
    def menuShowNahar():
        menu_nahar_win=tk.Toplevel()
        menu_nahar_win.title("منو ناهار")
        window_height = 500
        window_width = 580
        screen_width = menu_nahar_win.winfo_screenwidth()
        screen_height = menu_nahar_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        menu_nahar_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        menu_nahar_win.configure(bg="#FAA770")
        menu_nahar_win.resizable(False,False)
        menu_frame=tk.Frame(menu_nahar_win,bg="#FAA770")
        menu_frame.grid(row=0,column=0)
        info_frame=tk.Frame(menu_nahar_win,bg="#FAA770")
        info_frame.grid(row=0,column=1)
        btn_frame=tk.Frame(menu_nahar_win,bg="#FAA770")
        btn_frame.grid(row=1)
        tk.Label(menu_frame,text='منو ناهار',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E).grid(row=0,column=0)
        nahar_list,s1=creat_list(rp.FoodNahar,menu_frame,1,0,"12","49")
        back_btn=tk.Button(btn_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :menu_nahar_win.destroy())
        back_btn.grid(row=0,column=3)
        tk.Label(info_frame,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            
        txt_name=tk.StringVar(value='###')
        ent_name=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_name)
        ent_name.grid(row=0,column=0)
            
        tk.Label(info_frame,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=1,column=1)
            
        txt_price=tk.StringVar(value='###')
        ent_price=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_price)
        ent_price.grid(row=1,column=0)
            
        tk.Label(info_frame,text=' کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=2,column=1)
        
        txt_code=tk.StringVar(value='###')
        ent_code=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_code)
        ent_code.grid(row=2,column=0)
            
        tk.Label(info_frame,text='موجودی غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=3,column=1)
            
        txt_stock=tk.StringVar(value='###')
        ent_stock=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_stock)
        ent_stock.grid(row=3,column=0)
        item1=(0,)
        def selectFoodNahar(event):
            global item1
            try:
                newitem=nahar_list.curselection()
                if newitem:
                    item1=newitem
                    txt_name.set(s1[item1[0]].name)
                    txt_price.set(s1[item1[0]].price)
                    txt_code.set(s1[item1[0]].code)
                    txt_stock.set(s1[item1[0]].stock)
                    
            except:
                pass
        (nahar_list).bind("<<ListboxSelect>>",selectFoodNahar)
    def menuShowSham():
        menu_sham_win=tk.Toplevel()
        menu_sham_win.title("منو شام")
        window_height = 500
        window_width = 580
        screen_width = menu_sham_win.winfo_screenwidth()
        screen_height = menu_sham_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        menu_sham_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        menu_sham_win.configure(bg="#FAA770")
        menu_sham_win.resizable(False,False)
        menu_frame=tk.Frame(menu_sham_win,bg="#FAA770")
        menu_frame.grid(row=0,column=0)
        info_frame=tk.Frame(menu_sham_win,bg="#FAA770")
        info_frame.grid(row=0,column=1)
        btn_frame=tk.Frame(menu_sham_win,bg="#FAA770")
        btn_frame.grid(row=1)
        tk.Label(menu_frame,text='منو شام',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E).grid(row=0,column=0)
        sham_list,s2=creat_list(rp.FoodSham,menu_frame,1,0,"12","49")
        back_btn=tk.Button(btn_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :menu_sham_win.destroy())
        back_btn.grid(row=0,column=3)
        tk.Label(info_frame,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            
        txt_name=tk.StringVar(value='###')
        ent_name=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_name)
        ent_name.grid(row=0,column=0)
            
        tk.Label(info_frame,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=1,column=1)
            
        txt_price=tk.StringVar(value='###')
        ent_price=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_price)
        ent_price.grid(row=1,column=0)
            
        tk.Label(info_frame,text=' کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=2,column=1)
        
        txt_code=tk.StringVar(value='###')
        ent_code=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_code)
        ent_code.grid(row=2,column=0)
            
        tk.Label(info_frame,text='موجودی غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=3,column=1)
            
        txt_stock=tk.StringVar(value='###')
        ent_stock=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_stock)
        ent_stock.grid(row=3,column=0)
        item2=(0,)
        def selectFoodSham(event):
            global item2
            try:
                newitem=sham_list.curselection()
                if newitem:
                    item2=newitem
                    txt_name.set(s2[item2[0]].name)
                    txt_price.set(s2[item2[0]].price)
                    txt_code.set(s2[item2[0]].code)
                    txt_stock.set(s2[item2[0]].stock)
                        
            except:
                pass
        (sham_list).bind("<<ListboxSelect>>",selectFoodSham)
    btn_sobhane=tk.Button(menu_show_win,text="منو صبحانه",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",pady=35,command=menuShowSobhane)
    btn_sobhane.pack(fill=tk.X)
    btn_nahar=tk.Button(menu_show_win,text="منو ناهار",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770",pady=35,command=menuShowNahar)
    btn_nahar.pack(fill=tk.X)
    btn_sham=tk.Button(menu_show_win,text="منو شام",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",pady=35,command=menuShowSham)
    btn_sham.pack(fill=tk.X)
    back_btn=tk.Button(menu_show_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770",padx=30,command=lambda :menu_show_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
def menuEdit():
    menu_edit_win=tk.Toplevel()
    menu_edit_win.title("ویرایش منو")
    window_height = 500
    window_width = 900
    screen_width = menu_edit_win.winfo_screenwidth()
    screen_height = menu_edit_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    menu_edit_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    menu_edit_win.configure(bg="#FAA770")
    menu_edit_win.resizable(False,False)
    tk.Label(menu_edit_win,text='منو مورد نظر را انتخاب کنید',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).pack()

    def menuEditSobhane():
        menu_edit_sobhane_win=tk.Toplevel()
        menu_edit_sobhane_win.title("ویرایش منو صبحانه")
        window_height = 500
        window_width = 580
        screen_width = menu_edit_sobhane_win.winfo_screenwidth()
        screen_height = menu_edit_sobhane_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        menu_edit_sobhane_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        menu_edit_sobhane_win.configure(bg="#FAA770")
        menu_edit_sobhane_win.resizable(False,False)
        btn_frame=tk.Frame(menu_edit_sobhane_win,bg="#FAA770")
        btn_frame.grid(row=1)
        menu_frame=tk.Frame(menu_edit_sobhane_win,bg="#FAA770")
        menu_frame.grid(row=0,column=0)
        tk.Label(menu_frame,text="منو صبحانه",font=("Mj_Heritage Two Bold",25),justify="right",bg="#FAA770").grid(row=0,column=0)

        sobhane_list,s=creat_list(rp.FoodSobhane,menu_frame,1,0,"12","45")
            
        info_frame=tk.Frame(menu_edit_sobhane_win,bg="#FAA770")
        info_frame.grid(row=0,column=1)
        tk.Label(info_frame,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            
        txt_name=tk.StringVar(value='###')
        ent_name=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_name)
        ent_name.grid(row=0,column=0)
            
        tk.Label(info_frame,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=1,column=1)
            
        txt_price=tk.StringVar(value='###')
        ent_price=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_price)
        ent_price.grid(row=1,column=0)
            
        tk.Label(info_frame,text=' کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=2,column=1)
        
        txt_code=tk.StringVar(value='###')
        ent_code=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_code)
        ent_code.grid(row=2,column=0)
            
        tk.Label(info_frame,text='موجودی غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=3,column=1)
            
        txt_stock=tk.StringVar(value='###')
        ent_stock=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_stock)
        ent_stock.grid(row=3,column=0)
        item=(0,)
        back_btn=tk.Button(menu_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :menu_edit_sobhane_win.destroy())
        back_btn.grid(row=2,column=0)
        def editFood():
            try:
                name=ent_name.get()
                code=ent_code.get()
                price=int(ent_price.get())
                stock=int(ent_stock.get())
                global item
                s[item[0]].edit(name,code,price,stock)
                tk.messagebox.showinfo('پیام موفقیت','ویرایش با موفقیت انجام شد')
                menu_edit_win.destroy()
            except:
                tk.messagebox.showerror('خطا','ویرایش با خطا مواجعه شد')
                menu_edit_win.destroy()
        def deleteFood():
            try:
                        
                global item
                s[item[0]].delete()
                            
                tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
                menu_edit_win.destroy()
            except:
                tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
                menu_edit_win.destroy()
        def selectFoodSobhane(event):
            global item
            try:
                newitem=sobhane_list.curselection()
                if newitem:
                    item=newitem
                    txt_name.set(s[item[0]].name)
                    txt_price.set(s[item[0]].price)
                    txt_code.set(s[item[0]].code)
                    txt_stock.set(s[item[0]].stock)
                    
            except:
                pass
        (sobhane_list).bind("<<ListboxSelect>>",selectFoodSobhane)
        bntedit=tk.Button(info_frame,text='ویرایش',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=editFood)
        bntedit.grid(row=4,column=0)

        bntdelete=tk.Button(info_frame,text='حذف',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=deleteFood)
        bntdelete.grid(row=4,column=1)
        def addFood():
            add_food_win=tk.Toplevel()
            add_food_win.title('ثبت غذای جدید(صبحانه)')
            window_height = 350
            window_width = 400
            screen_width = add_food_win.winfo_screenwidth()
            screen_height = add_food_win.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            add_food_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            add_food_win.configure(bg="#FAA770")
            add_food_win.resizable(False,False)
            tk.Label(add_food_win,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            ent_name=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_name.grid(row=0,column=0)
            
            tk.Label(add_food_win,text='کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=1,column=1)
            ent_ncode=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_ncode.grid(row=1,column=0)
                
            tk.Label(add_food_win,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=2,column=1)
            ent_price=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_price.grid(row=2,column=0)
                
            tk.Label(add_food_win,text='تعداد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=3,column=1)
            ent_stock=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_stock.grid(row=3,column=0)
                
            def fsave():
                name=ent_name.get()
                code=ent_ncode.get()
                try:
                    price=int(ent_price.get())
                    stock=int(ent_stock.get())
                    
                    f=rp.FoodSobhane(name, code, price,stock)
                    f.save()
                    tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
                    add_food_win.destroy()
                except:
                    tk.messagebox.showerror('خطا','ثبت با خطا مواجعه شد')

                
            bnt_save=tk.Button(add_food_win,text='ذخیره',bg="#FF6600",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=0,padx=62,command=fsave)
            bnt_save.grid(row=5,column=1)
            back_btn=tk.Button(add_food_win,text="بازگشت",bg="#FF6600",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=0,padx=62,command=lambda :add_food_win.destroy())
            back_btn.grid(row=5,column=0)
                
        btn_menu_edit=tk.Button(info_frame,text="افزودن غذا",font=("Mj_Heritage Two Bold",18,"bold"),justify="right",bg="#FF6600",padx=15,pady=10,command=addFood)
        btn_menu_edit.grid(row=5,column=0)

    def menuEditNahar():
        menu_edit_nahar_win=tk.Toplevel()
        menu_edit_nahar_win.title("ویرایش منو ناهار")
        window_height = 500
        window_width = 580
        screen_width = menu_edit_nahar_win.winfo_screenwidth()
        screen_height = menu_edit_nahar_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        menu_edit_nahar_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        menu_edit_nahar_win.configure(bg="#FAA770")
        menu_edit_nahar_win.resizable(False,False)
        menu_frame=tk.Frame(menu_edit_nahar_win,bg="#FAA770")
        menu_frame.grid(row=0,column=0)
        nahar_list,s1=creat_list(rp.FoodNahar,menu_frame,1,0,"12","45")
        info_frame=tk.Frame(menu_edit_nahar_win,bg="#FAA770")
        info_frame.grid(row=0,column=1)
        tk.Label(menu_frame,text='منو ناهار',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right").grid(row=0,column=0)
        tk.Label(info_frame,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",pady=18).grid(row=0,column=1)
        txt_name=tk.StringVar(value='###')
        ent_name=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_name)
        ent_name.grid(row=0,column=0)
            
        tk.Label(info_frame,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=1,column=1)
            
        txt_price=tk.StringVar(value='###')
        ent_price=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_price)
        ent_price.grid(row=1,column=0)
            
        tk.Label(info_frame,text=' کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=2,column=1)
        
        txt_code=tk.StringVar(value='###')
        ent_code=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_code)
        ent_code.grid(row=2,column=0)
            
        tk.Label(info_frame,text='موجودی غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=3,column=1)
            
        txt_stock=tk.StringVar(value='###')
        ent_stock=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_stock)
        ent_stock.grid(row=3,column=0)
        item1=(0,)
        back_btn=tk.Button(menu_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :menu_edit_nahar_win.destroy())
        back_btn.grid(row=2,column=0)
        def editFood():
            try:
                name=ent_name.get()
                code=ent_code.get()
                price=int(ent_price.get())
                stock=int(ent_stock.get())
                global item1
                s1[item1[0]].edit(name,code,price,stock)
                tk.messagebox.showinfo('پیام موفقیت','ویرایش با موفقیت انجام شد')
                menu_edit_win.destroy()
            except:
                tk.messagebox.showerror('خطا','ویرایش با خطا مواجعه شد')
                menu_edit_win.destroy()
        def deleteFood():
            try:
                
                global item1
                s1[item1[0]].delete()
                    
                tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
                menu_edit_win.destroy()
            except:
                tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
                menu_edit_win.destroy()
        def selectFoodNahar(event):
            global item1
            try:
                newitem=nahar_list.curselection()
                if newitem:
                    item1=newitem
                    txt_name.set(s1[item1[0]].name)
                    txt_price.set(s1[item1[0]].price)
                    txt_code.set(s1[item1[0]].code)
                    txt_stock.set(s1[item1[0]].stock)
                    
            except:
                pass
        (nahar_list).bind("<<ListboxSelect>>",selectFoodNahar)
        bntedit=tk.Button(info_frame,text='ویرایش',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=editFood)
        bntedit.grid(row=4,column=0)

        bntdelete=tk.Button(info_frame,text='حذف',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=deleteFood)
        bntdelete.grid(row=4,column=1)
        def addFood():
            add_food_win=tk.Toplevel()
            add_food_win.title('ثبت غذای جدید(ناهار)')
            window_height = 350
            window_width = 400
            screen_width = add_food_win.winfo_screenwidth()
            screen_height = add_food_win.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            add_food_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            add_food_win.configure(bg="#FAA770")
            add_food_win.resizable(False,False)
            tk.Label(add_food_win,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            ent_name=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_name.grid(row=0,column=0)
            
            tk.Label(add_food_win,text='کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=1,column=1)
            ent_ncode=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_ncode.grid(row=1,column=0)
                
            tk.Label(add_food_win,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=2,column=1)
            ent_price=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_price.grid(row=2,column=0)
                
            tk.Label(add_food_win,text='تعداد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=3,column=1)
            ent_stock=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_stock.grid(row=3,column=0)
                
            def fsave():
                name=ent_name.get()
                code=ent_ncode.get()
                try:
                    price=int(ent_price.get())
                    stock=int(ent_stock.get())
                    
                    f=rp.FoodNahar(name, code, price,stock)
                    f.save()
                    tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
                    add_food_win.destroy()
                except:
                    tk.messagebox.showerror('خطا','ثبت با خطا مواجعه شد')

                
            bnt_save=tk.Button(add_food_win,text='ذخیره',bg="#FF6600",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=0,padx=62,command=fsave)
            bnt_save.grid(row=5,column=1)
            back_btn=tk.Button(add_food_win,text="بازگشت",bg="#FF6600",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=0,padx=62,command=lambda :add_food_win.destroy())
            back_btn.grid(row=5,column=0)
        btn_menu_edit=tk.Button(info_frame,text="افزودن غذا",font=("Mj_Heritage Two Bold",18,"bold"),justify="right",bg="#FF6600",padx=15,pady=10,command=addFood)
        btn_menu_edit.grid(row=5,column=0)
    def menuEditSham():
        menu_edit_sham_win=tk.Toplevel()
        menu_edit_sham_win.title("ویرایش منو شام")
        window_height = 500
        window_width = 580
        screen_width = menu_edit_sham_win.winfo_screenwidth()
        screen_height = menu_edit_sham_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        menu_edit_sham_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        menu_edit_sham_win.configure(bg="#FAA770")
        menu_edit_sham_win.resizable(False,False)
        menu_frame=tk.Frame(menu_edit_sham_win,bg="#FAA770")
        menu_frame.grid(row=0,column=0)
        tk.Label(menu_frame,text="منو شام",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770").grid(row=0,column=0)

        sham_list,s2=creat_list(rp.FoodSham,menu_frame,1,0,"12","45")
            
        info_frame=tk.Frame(menu_edit_sham_win,bg="#FAA770")
        info_frame.grid(row=0,column=1)
        tk.Label(info_frame,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            
        txt_name=tk.StringVar(value='###')
        ent_name=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_name)
        ent_name.grid(row=0,column=0)
            
        tk.Label(info_frame,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=1,column=1)
            
        txt_price=tk.StringVar(value='###')
        ent_price=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_price)
        ent_price.grid(row=1,column=0)
            
        tk.Label(info_frame,text=' کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=2,column=1)
        
        txt_code=tk.StringVar(value='###')
        ent_code=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_code)
        ent_code.grid(row=2,column=0)
            
        tk.Label(info_frame,text='موجودی غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=3,column=1)
            
        txt_stock=tk.StringVar(value='###')
        ent_stock=tk.Entry(info_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18),textvariable=txt_stock)
        ent_stock.grid(row=3,column=0)
        item2=(0,)
        back_btn=tk.Button(menu_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :menu_edit_sham_win.destroy())
        back_btn.grid(row=2,column=0)
        def editFood():
            try:
                name=ent_name.get()
                code=ent_code.get()
                price=int(ent_price.get())
                stock=int(ent_stock.get())
                global item2
                s2[item2[0]].edit(name,code,price,stock)
                tk.messagebox.showinfo('پیام موفقیت','ویرایش با موفقیت انجام شد')
                menu_edit_win.destroy()
            except:
                tk.messagebox.showerror('خطا','ویرایش با خطا مواجعه شد')
                menu_edit_win.destroy()
        def deleteFood():
            try:
                    
                global item2
                s2[item2[0]].delete()
                        
                tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
                menu_edit_win.destroy()
            except:
                tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
                menu_edit_win.destroy()
        def selectFoodSham(event):
            global item2
            try:
                newitem=sham_list.curselection()
                if newitem:
                    item2=newitem
                    txt_name.set(s2[item2[0]].name)
                    txt_price.set(s2[item2[0]].price)
                    txt_code.set(s2[item2[0]].code)
                    txt_stock.set(s2[item2[0]].stock)
                        
            except:
                pass

        (sham_list).bind("<<ListboxSelect>>",selectFoodSham)

        bntedit=tk.Button(info_frame,text='ویرایش',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=editFood)
        bntedit.grid(row=4,column=0)

        bntdelete=tk.Button(info_frame,text='حذف',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=deleteFood)
        bntdelete.grid(row=4,column=1)
        def addFood():
            add_food_win=tk.Toplevel()
            add_food_win.title('ثبت غذای جدید(شام)')
            window_height = 350
            window_width = 400
            screen_width = add_food_win.winfo_screenwidth()
            screen_height = add_food_win.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            add_food_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            add_food_win.configure(bg="#FAA770")
            add_food_win.resizable(False,False)
            tk.Label(add_food_win,text='نام غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=18).grid(row=0,column=1)
            ent_name=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_name.grid(row=0,column=0)
            
            tk.Label(add_food_win,text='کد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=1,column=1)
            ent_ncode=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_ncode.grid(row=1,column=0)
                
            tk.Label(add_food_win,text='قیمت غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=2,column=1)
            ent_price=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_price.grid(row=2,column=0)
                
            tk.Label(add_food_win,text='تعداد غذا',bg="#FAA770",font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,pady=10).grid(row=3,column=1)
            ent_stock=tk.Entry(add_food_win,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
            ent_stock.grid(row=3,column=0)
                
            def fsave():
                name=ent_name.get()
                code=ent_ncode.get()
                try:
                    price=int(ent_price.get())
                    stock=int(ent_stock.get())
                    
                    f=rp.FoodSham(name, code, price,stock)
                    f.save()
                    tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
                    add_food_win.destroy()
                except:
                    tk.messagebox.showerror('خطا','ثبت با خطا مواجعه شد')

                
            bnt_save=tk.Button(add_food_win,text='ذخیره',bg="#FF6600",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=0,padx=62,command=fsave)
            bnt_save.grid(row=5,column=1)
            back_btn=tk.Button(add_food_win,text="بازگشت",bg="#FF6600",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=0,padx=62,command=lambda :add_food_win.destroy())
            back_btn.grid(row=5,column=0)
        btn_menu_edit=tk.Button(info_frame,text="افزودن غذا",font=("Mj_Heritage Two Bold",18,"bold"),justify="right",bg="#FF6600",padx=15,pady=10,command=addFood)
        btn_menu_edit.grid(row=5,column=0)
    btn_sobhane=tk.Button(menu_edit_win,text="منو صبحانه",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",pady=35,command=menuEditSobhane)
    btn_sobhane.pack(fill=tk.X)
    btn_nahar=tk.Button(menu_edit_win,text="منو ناهار",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770",pady=35,command=menuEditNahar)
    btn_nahar.pack(fill=tk.X)
    btn_sham=tk.Button(menu_edit_win,text="منو شام",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",pady=35,command=menuEditSham)
    btn_sham.pack(fill=tk.X)
    back_btn=tk.Button(menu_edit_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770",padx=30,command=lambda :menu_edit_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
def panelCustomer():
    panel_customer_win=tk.Toplevel()
    panel_customer_win.title("پنل مشتریان")
    window_height = 500
    window_width = 580
    screen_width = panel_customer_win.winfo_screenwidth()
    screen_height = panel_customer_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    panel_customer_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    panel_customer_win.configure(bg="#FAA770")
    panel_customer_win.resizable(False,False)    
    info_frame=tk.Frame(panel_customer_win,bg="#FAA770")
    info_frame.grid(row=0,column=1)
    btn_frame=tk.Frame(panel_customer_win,bg="#FAA770")
    btn_frame.grid(row=1)
    list_frame=tk.Frame(panel_customer_win,bg="#FAA770")
    list_frame.grid(row=0,column=0)
    customer_list,s=creat_list(rp.Customer,list_frame,1,0,"12","45")
    tk.Label(list_frame,text='لیست مشتریان',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770").grid(row=0,column=0)
    tk.Label(info_frame,text='نام مشتری',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=0,column=1)
    txt_name=tk.StringVar(value='###')
    ent_name=tk.Entry(info_frame,textvariable=txt_name,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_name.grid(row=0,column=0)
    tk.Label(info_frame,text=' فامیل مشتری',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=1,column=1)
    txt_famil=tk.StringVar(value='###')
    ent_famil=tk.Entry(info_frame,textvariable=txt_famil,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_famil.grid(row=1,column=0)
    tk.Label(info_frame,text=' کد مشتری',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=2,column=1)
    txt_code=tk.StringVar(value='###')
    ent_code=tk.Entry(info_frame,textvariable=txt_code,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_code.grid(row=2,column=0)
    tk.Label(info_frame,text='  آدرس مشتری',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=3,column=1)
    txt_adres=tk.StringVar(value='###')
    ent_adres=tk.Entry(info_frame,textvariable=txt_adres,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_adres.grid(row=3,column=0)
    item=(0,)
    def editCustomer():
        try:
            name=ent_name.get()
            famil=ent_famil.get()
            code=ent_code.get()
            adres=ent_adres.get()
            global item
            s[item[0]].edit(name,famil,code,adres)
            tk.messagebox.showinfo('پیام موفقیت','ویرایش با موفقیت انجام شد')
            panel_customer_win.destroy()
        except:
            tk.messagebox.showerror('خطا','ویرایش با خطا مواجعه شد')
            panel_customer_win.destroy()
    
    bnt_edit=tk.Button(info_frame,text='ویرایش',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=editCustomer)
    bnt_edit.grid(row=4,column=0)
    def deleteCustomer():
        try:
            global item
            answer = tk.messagebox.askyesno("حذف مشتری", "آیا مطمئن هستید که میخواهید این مشتری را حذف کنید؟")
            if answer == True:
                s[item[0]].delete()
                tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
                panel_customer_win.destroy()
            else:
                panel_customer_win.destroy()
                return
            
        except:
            tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
            panel_customer_win.destroy()
    
    bnt_save=tk.Button(info_frame,text='حذف',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=deleteCustomer)
    bnt_save.grid(row=4,column=1)
    def selectCustomer(event):
        global item
        try:
            newitem=customer_list.curselection()
            if newitem:
                item=newitem
                txt_name.set(s[item[0]].name)
                txt_famil.set(s[item[0]].last_name)
                txt_code.set(s[item[0]].code)
                txt_adres.set(s[item[0]].address)
        except:
            pass
    customer_list.bind('<<ListboxSelect>>',selectCustomer)


    back_btn=tk.Button(btn_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :panel_customer_win.destroy())
    back_btn.grid(row=0,column=0)
def addCustomer():
    add_customer_win=tk.Toplevel()
    add_customer_win.title('ثبت مشتری جدید')
    window_height = 550
    window_width = 580
    screen_width = add_customer_win.winfo_screenwidth()
    screen_height = add_customer_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    add_customer_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    add_customer_win.configure(bg="#FAA770")
    add_customer_win.resizable(False,False)
    tk.Label(add_customer_win,text='ثبت مشتری جدید',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FAA770").pack(fill=tk.X)

    tk.Label(add_customer_win,text='نام مشتری',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_name=tk.Entry(add_customer_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_name.pack()
       
    tk.Label(add_customer_win,text='فامیل',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_famil=tk.Entry(add_customer_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_famil.pack()
        
    tk.Label(add_customer_win,text='کد مشتری',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_ncode=tk.Entry(add_customer_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_ncode.pack()
        
    tk.Label(add_customer_win,text='آدرس',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_addres=tk.Entry(add_customer_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_addres.pack()  
    def customerSave():
        try:
            name=ent_name.get()
            last_name=ent_famil.get()
            code=ent_ncode.get()
            address=ent_addres.get()
            f=rp.Customer(name,last_name,code,address)
            f.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            add_customer_win.destroy()
        except:
            tk.messagebox.showerror('خطا','ثبت با خطا مواجعه شد')
            add_customer_win.destroy()
    bnt_save=tk.Button(add_customer_win,text='ذخیره',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",command=customerSave)
    bnt_save.pack(fill=tk.X)
        
    back_btn=tk.Button(add_customer_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770",padx=30,pady=10,command=lambda :add_customer_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
def sabtSefaresh():
    sabt_sefaresh_win=tk.Toplevel()
    sabt_sefaresh_win.title('ثبت سفارش')
    window_height = 650
    window_width = 1105
    screen_width = sabt_sefaresh_win.winfo_screenwidth()
    screen_height = sabt_sefaresh_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    sabt_sefaresh_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    sabt_sefaresh_win.configure(bg="#FAA770")
    sabt_sefaresh_win.resizable(False,False)
    info_frame=tk.Frame(sabt_sefaresh_win,bg="#FAA770")
    info_frame.grid(row=0,column=3)
    info_menu_frame=tk.Frame(sabt_sefaresh_win,bg="#FAA770")
    info_menu_frame.grid(row=0,column=1)
    btn_frame=tk.Frame(sabt_sefaresh_win,bg="#FAA770")
    btn_frame.grid(row=2,column=1)
    menu_frame=tk.Frame(sabt_sefaresh_win,bg="#FAA770")
    menu_frame.grid(row=0,column=0)
    customer_frame=tk.Frame(sabt_sefaresh_win,bg="#FAA770")
    customer_frame.grid(row=0,column=2)
    tree_frame=tk.Frame(sabt_sefaresh_win,bg="#FAA770")
    tree_frame.grid(row=1,column=1)
        
    tk.Label(customer_frame,text='مشتریان',bg="#FAA770",font=("Mj_Heritage Two Bold",20),justify="right",anchor=tk.E,pady=13).grid(row=0,column=1)
    customer_list,s_cust=creat_Combobox(rp.Customer,customer_frame, 1, 1)
    
    tk.Label(customer_frame,text='پیک را انتخاب کنید',bg="#FAA770",font=("Mj_Heritage Two Bold",20),justify="right",anchor=tk.E,pady=13).grid(row=5,column=1)
    peik_list,s_peik=creat_Combobox(rp.Peik,customer_frame, 6, 1)    
    tk.Label(menu_frame,text='منو مورد نظر را انتخاب کنید',bg="#FAA770",font=("Mj_Heritage Two Bold",20),justify="right",anchor=tk.E,pady=13).grid(row=0,column=0)
    val=["صبحانه","ناهار","شام"]
    choose_menu=ttk.Combobox(menu_frame,value=val,justify="right",height=8,width=20,font=("Mj_Heritage Two Bold",18))
    choose_menu.grid(row=1,column=0)
    def menuSelect(event):
        val=choose_menu.get()
        if val=="صبحانه":
            sobhane_list,s_food=creat_list(rp.FoodSobhane,menu_frame, 2, 0,"6","30")
            def addFoodSobhane():
                try:
                    item=sobhane_list.curselection()
                    count=ent_count.get()
                    tree.insert('', tk.END, values=([s_food[item[0]].name,s_food[item[0]].price,count]))
                    t=int(s_food[item[0]].price)*int(count)+total.get()
                    lbtotal.config(text=str(total))
                    total.set(value=t)
                    lbtotal.config(text=t)
                except:
                    tk.messagebox.showerror('خطا','غذا انتخاب نشده')
            bnt_add_food=tk.Button(info_menu_frame,text='اضافه کردن غذا',bg="#FF6600",font=("Mj_Heritage Two Bold",18),pady=13,justify="right",command=addFoodSobhane)
            bnt_add_food.grid(row=2,column=0)
        elif val=="ناهار":
            nahar_list,s1_food=creat_list(rp.FoodNahar,menu_frame, 2, 0,"6","30")
            def addFoodNahar():
                try:
                    item1=nahar_list.curselection()
                    count=ent_count.get()
                    tree.insert('', tk.END, values=([s1_food[item1[0]].name,s1_food[item1[0]].price,count]))
                    t1=int(s1_food[item1[0]].price)*int(count)+total.get()
                    lbtotal.config(text=str(total))
                    total.set(value=t1)
                    lbtotal.config(text=t1)
                except:
                    tk.messagebox.showerror('خطا','غذا انتخاب نشده')
            bnt_add_food=tk.Button(info_menu_frame,text='اضافه کردن غذا',bg="#FF6600",font=("Mj_Heritage Two Bold",18),pady=13,justify="right",command=addFoodNahar)
            bnt_add_food.grid(row=2,column=0)
        elif val=="شام":
            sham_list,s2_food=creat_list(rp.FoodSham,menu_frame, 2, 0,"6","30")
            def addFoodSham():
                try:
                    item2=sham_list.curselection()
                    count=ent_count.get()
                    tree.insert('', tk.END, values=([s2_food[item2[0]].name,s2_food[item2[0]].price,count]))
                    t2=int(s2_food[item2[0]].price)*int(count)+total.get()
                    lbtotal.config(text=str(total))
                    total.set(value=t2)
                    lbtotal.config(text=t2)
                except:
                    tk.messagebox.showerror('خطا','غذا انتخاب نشده')
                    sabt_sefaresh_win.destroy()
            bnt_add_food=tk.Button(info_menu_frame,text='اضافه کردن غذا',bg="#FF6600",font=("Mj_Heritage Two Bold",18),pady=13,justify="right",command=addFoodSham)
            bnt_add_food.grid(row=2,column=0)
            
        
    choose_menu.bind('<<ComboboxSelected>>',menuSelect) 
    
    
   
    def factNumber():
        for i in range(100,1001):
            yield i
    tk.Label(info_menu_frame,text='تعداد غذا ',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=1,column=1)
    ent_count=tk.Entry(info_menu_frame,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_count.grid(row=1,column=0)
    
    tk.Label(info_frame,text='نام مشتری',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=1,column=1)
    lbname_customer=tk.Label(info_frame,text='###',font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    lbname_customer.grid(row=1,column=0)
    
    tk.Label(info_frame,text='فامیل مشتری',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=2,column=1)
    lbfamil_customer=tk.Label(info_frame,text='###',font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    lbfamil_customer.grid(row=2,column=0)
    
    tk.Label(info_frame,text='آدرس مشتری',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=3,column=1)
    lbadres_customer=tk.Label(info_frame,text='###',font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    lbadres_customer.grid(row=3,column=0)
    
    tk.Label(info_menu_frame,text=' قیمت کل',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=4,column=1)
    lbtotal=tk.Label(info_menu_frame,text='###',font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    lbtotal.grid(row=4,column=0)
    
    tk.Label(info_frame,text='شماره سفارش',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=0,column=1)
    lbfact_nember=tk.Label(info_frame,text=next(factNumber()),font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    lbfact_nember.grid(row=0,column=0)
    
    tk.Label(customer_frame,text='زمان ثبت سفارش',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=3,column=1)
    lbtime=tk.Label(customer_frame,text=time.strftime("%H:%M:%S"),font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    lbtime.grid(row=3,column=0)
    
    tk.Label(customer_frame,text='تاریخ ثبت سفارش',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=2,column=1)
    lbdate=tk.Label(customer_frame,text=date.today(),font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    lbdate.grid(row=2,column=0)
    
    # tk.Label(peik_frame,text='نام پیک',bg="#FAA770",font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E,pady=13).grid(row=0,column=0)
    # lbname_peik=tk.Label(peik_frame,text='###',font=("Mj_Heritage Two Bold",18),justify="right",anchor=tk.E)
    # lbname_peik.grid(row=1,column=0)
    def sabtAkhar():
        answer = tk.messagebox.askyesno("خروج", "آیا مطمئن هستید که میخواهید ثبت نهایی کنید ؟")
        if answer == True:
            tk.messagebox.showinfo('پیام موفقیت','ثبت نهایی با موفقیت انجام شد')
            sabt_sefaresh_win.destroy()
        else:
            return

        
    bnt_sabt_akhar=tk.Button(sabt_sefaresh_win,text='ثبت نهایی',command=sabtAkhar,font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10)
    bnt_sabt_akhar.grid(row=3,column=3)
    total=tk.IntVar(value=0)

    
    colums=('food_name','food_price','food_count')
    tree=ttk.Treeview(sabt_sefaresh_win,columns=colums,show='headings')
    tree.heading('food_name',text='نام غذا')
    tree.heading('food_price',text='قیمت غذا')
    tree.heading('food_count',text='تعداد غذا')
    
    
    
    
    tree.grid(row=2,columnspan=5, sticky='nsew')
    def flistboxselect(event):
        item=customer_list.current()
       
        # if item:
        lbname_customer.configure(text=s_cust[item].name)
        lbfamil_customer.configure(text=s_cust[item].last_name)
        fullname=s_cust[item].name+" "+s_cust[item].last_name
        lbadres_customer.configure(text=s_cust[item].address)
        return fullname
    customer_list.bind('<<ComboboxSelected>>',flistboxselect)
    # def peikSelect(event):
    #     item=peik_list.current()
       
    #     # if item:
    #     lbname_peik.configure(text=s_peik[item].name+" "+s_peik[item].last_name)
    # peik_list.bind('<<ComboboxSelected>>',peikSelect)
    back_btn=tk.Button(sabt_sefaresh_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :sabt_sefaresh_win.destroy())
    back_btn.grid(row=3,column=0) 
    tk.Label(info_menu_frame,text=rp.Restaurant.name,font=("Mj_Heritage Two Bold",30),justify="right",anchor=tk.E,bg="#FAA770",pady=13).grid(row=0,column=1)

def timeLabel():
    time_label=tk.Label(main_win,text=time.strftime("%H:%M:%S"),font=("Mj_Heritage Two Bold",20),justify="left",bg="#DCDCDC")
    time_label.place(x=795,y=60)
    main_win.after(1000,timeLabel)
main_win.after(1000,timeLabel)
def exitApp():
    answer = tk.messagebox.askyesno("خروج", "آیا مطمئن هستید که میخواهید خارج شوید؟")
    if answer == True:
        main_win.destroy()
    else:
        return
def panelPeik():
    panel_peik_win=tk.Toplevel()
    panel_peik_win.title("پنل پیک")
    window_height = 550
    window_width = 580
    screen_width = panel_peik_win.winfo_screenwidth()
    screen_height = panel_peik_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    panel_peik_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    panel_peik_win.configure(bg="#FAA770")
    panel_peik_win.resizable(False,False)    
    info_frame=tk.Frame(panel_peik_win,bg="#FAA770")
    info_frame.grid(row=0,column=1)
    btn_frame=tk.Frame(panel_peik_win,bg="#FAA770")
    btn_frame.grid(row=1)
    list_frame=tk.Frame(panel_peik_win,bg="#FAA770")
    list_frame.grid(row=0,column=0)
    peik_list,s=creat_list(rp.Peik,list_frame,1,0,"12","45")
    tk.Label(list_frame,text='لیست پیک رستوران',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770").grid(row=0,column=0)
    tk.Label(info_frame,text='نام',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=0,column=1)
    txt_name=tk.StringVar(value='###')
    ent_name=tk.Entry(info_frame,textvariable=txt_name,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_name.grid(row=0,column=0)
    tk.Label(info_frame,text='فامیل',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=1,column=1)
    txt_famil=tk.StringVar(value='###')
    ent_famil=tk.Entry(info_frame,textvariable=txt_famil,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_famil.grid(row=1,column=0)
    tk.Label(info_frame,text='کد ملی',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=2,column=1)
    txt_code=tk.StringVar(value='###')
    ent_code=tk.Entry(info_frame,textvariable=txt_code,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_code.grid(row=2,column=0)
    tk.Label(info_frame,text='آدرس',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=3,column=1)
    txt_adres=tk.StringVar(value='###')
    ent_adres=tk.Entry(info_frame,textvariable=txt_adres,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_adres.grid(row=3,column=0)
    tk.Label(info_frame,text='سن',font=("Mj_Heritage Two Bold",25),justify="right",anchor=tk.E,bg="#FAA770",pady=18).grid(row=4,column=1)
    txt_age=tk.StringVar(value='###')
    ent_age=tk.Entry(info_frame,textvariable=txt_age,width=20,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_age.grid(row=4,column=0)
    item=(0,)
    def editPeik():
        try:
            name=ent_name.get()
            famil=ent_famil.get()
            code=ent_code.get()
            adres=ent_adres.get()
            age=ent_age.get()
            global item
            s[item[0]].edit(name,famil,adres,code,age)
            tk.messagebox.showinfo('پیام موفقیت','ویرایش با موفقیت انجام شد')
            panel_peik_win.destroy()
        except:
            tk.messagebox.showerror('خطا','ویرایش با خطا مواجعه شد')
            panel_peik_win.destroy()
    
    bnt_edit=tk.Button(info_frame,text='ویرایش',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=editPeik)
    bnt_edit.grid(row=5,column=0)
    def deletePeik():
        try:
            global item
            answer = tk.messagebox.askyesno("حذف مشتری", "آیا مطمئن هستید که میخواهید این مشتری را حذف کنید؟")
            if answer == True:
                s[item[0]].delete()
                tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
                panel_peik_win.destroy()
            else:
                panel_peik_win.destroy()
                return
            
        except:
            tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
            panel_peik_win.destroy()
    
    bnt_save=tk.Button(info_frame,text='حذف',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=deletePeik)
    bnt_save.grid(row=5,column=1)
    def selectPeik(event):
        global item
        try:
            newitem=peik_list.curselection()
            if newitem:
                item=newitem
                txt_name.set(s[item[0]].name)
                txt_famil.set(s[item[0]].last_name)
                txt_code.set(s[item[0]].code_meli)
                txt_adres.set(s[item[0]].address)
                txt_age.set(s[item[0]].age)
        except:
            pass
    peik_list.bind('<<ListboxSelect>>',selectPeik)

    back_btn=tk.Button(btn_frame,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,pady=10,command=lambda :panel_peik_win.destroy())
    back_btn.grid(row=0,column=0)
def addPeik():
    add_peik_win=tk.Toplevel()
    add_peik_win.title('ثبت مشتری جدید')
    window_height = 650
    window_width = 580
    screen_width = add_peik_win.winfo_screenwidth()
    screen_height = add_peik_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    add_peik_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    add_peik_win.configure(bg="#FAA770")
    add_peik_win.resizable(False,False)
    tk.Label(add_peik_win,text='ثبت پیک جدید',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FAA770").pack(fill=tk.X)

    tk.Label(add_peik_win,text='نام',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_name=tk.Entry(add_peik_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_name.pack()
       
    tk.Label(add_peik_win,text='فامیل',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_famil=tk.Entry(add_peik_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_famil.pack()
        
    tk.Label(add_peik_win,text='کد ملی',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_ncode=tk.Entry(add_peik_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_ncode.pack()
        
    tk.Label(add_peik_win,text='آدرس',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_addres=tk.Entry(add_peik_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_addres.pack()
    
    tk.Label(add_peik_win,text='سن',font=("Mj_Heritage Two Bold",25),justify="right",bg="#FF6600",pady=10).pack(fill=tk.X)
    ent_age=tk.Entry(add_peik_win,width=100,justify="right",font=("Mj_Heritage Two Bold",18))
    ent_age.pack() 
    def peikSave():
        try:
            name=ent_name.get()
            last_name=ent_famil.get()
            code_meli=ent_ncode.get()
            address=ent_addres.get()
            age=ent_age.get()
            f=rp.Peik(name,last_name,address,code_meli,age)
            f.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            add_peik_win.destroy()
        except:
            tk.messagebox.showerror('خطا','ثبت با خطا مواجعه شد')
            add_peik_win.destroy()
    bnt_save=tk.Button(add_peik_win,text='ذخیره',font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",command=peikSave)
    bnt_save.pack(fill=tk.X)
        
    back_btn=tk.Button(add_peik_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FAA770",padx=30,pady=10,command=lambda :add_peik_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
def segWin():
    seg_win=tk.Toplevel()
    seg_win.title("به زودی")
    window_height = 150
    window_width = 500
    screen_width = seg_win.winfo_screenwidth()
    screen_height = seg_win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    seg_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    seg_win.configure(bg="#FAA770")
    seg_win.resizable(False,False)
    tk.Label(seg_win,text="به زودی",font=("Mj_Heritage Two Bold",20),justify="right",bg="#FF6600",padx=10).pack(fill=tk.X)
    back_btn=tk.Button(seg_win,text="بازگشت",font=("Mj_Heritage Two Bold",18),justify="right",bg="#FF6600",padx=30,command=lambda :seg_win.destroy())
    back_btn.pack(side=tk.BOTTOM,fill=tk.X)
tk.Label(main_win,text=date.today(),font=("Mj_Heritage Two Bold",20),justify="left",anchor=tk.E,bg="#DCDCDC").place(x=770,y=8)

tk.Label(main_win,text=rp.Restaurant.name,font=("Mj_Heritage Two Bold",30),justify="right",anchor=tk.E,bg="#DCDCDC").place(x=330,y=15)

btn_menu=tk.Button(main_win,text="نمایش منو",font=("Mj_Heritage Two Bold",20),bg="#DCDCDC",padx=34,command=menuShow)
btn_menu.place(x=5,y=25)

btn_panel_customer=tk.Button(main_win,text="پنل مشتریان",font=("Mj_Heritage Two Bold",20),bg="#DCDCDC",padx=28,command=panelCustomer)
btn_panel_customer.place(x=5,y=155)

btn_add_customer=tk.Button(main_win,text="افزودن مشتری",font=("Mj_Heritage Two Bold",20),bg="#DCDCDC",padx=17,command=addCustomer)
btn_add_customer.place(x=5,y=220)

btn_sabt_sefaresh=tk.Button(main_win,text="ثبت سفارش",font=("Mj_Heritage Two Bold ",20),bg="#DCDCDC",padx=31,command=sabtSefaresh)
btn_sabt_sefaresh.place(x=5,y=415)


btn_menu_edit=tk.Button(main_win,text="ویرایش منو",font=("Mj_Heritage Two Bold",20),justify="right",bg="#DCDCDC",padx=32,command=menuEdit)
btn_menu_edit.place(x=5,y=90)

btn_nazarat=tk.Button(main_win,text="ثبت نظرات",font=("Mj_Heritage Two Bold",20),justify="right",bg="#DCDCDC",padx=15,command=segWin)
btn_nazarat.place(x=750,y=350)

btn_fact=tk.Button(main_win,text="فاکتور",font=("Mj_Heritage Two Bold",20),justify="right",bg="#DCDCDC",padx=34,command=segWin)
btn_fact.place(x=750,y=285)

btn_admin=tk.Button(main_win,text="پنل ادمین",font=("Mj_Heritage Two Bold",20),justify="right",bg="#DCDCDC",padx=18,command=segWin)
btn_admin.place(x=750,y=220)

btn_exit=tk.Button(main_win,text="خروج",font=("Mj_Heritage Two Bold",20),justify="right",bg="#DCDCDC",padx=35,command=exitApp)
btn_exit.place(x=750,y=415)

btn_peik=tk.Button(main_win,text="پیک رستوران",font=("Mj_Heritage Two Bold",20),justify="right",bg="#DCDCDC",padx=28,command=panelPeik)
btn_peik.place(x=5,y=285)

btn_add_peik=tk.Button(main_win,text="افزودن پیک",font=("Mj_Heritage Two Bold",20),justify="right",bg="#DCDCDC",padx=32,command=addPeik)
btn_add_peik.place(x=5,y=350)

main_win.config(menu=main_menu)

main_win.mainloop()
