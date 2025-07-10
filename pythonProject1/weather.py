from tkinter import *
from tkinter import ttk
import requests
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8900951e839cf6699ff65b2d7c94113f").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Nikitha app")
win.config(bg = "sky blue")
win.geometry("500x570")
# giving the title name to the window as name_label
name_label = Label(win,text="Nikitha Weather App",
                   font=("Times New Roman",25,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
# now for the use of combo box we should write the 2nd line
#after writing the combox, all the states names we should in one box. so we use list_name here and give the state names
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Nikitha Weather App",values=list_name,
                   font=("Times New Roman",20,"bold"),textvariable=city_name)
com.place(x=50,y=120,height=50,width=400)
# now keep the done button
#now we should do the below part. for that . copy and paste title part and edit it.
w_label = Label(win,text="Weather Climate",
                   font=("Times New Roman",18,"bold"))
w_label.place(x=25,y=270,height=50,width=200)
#duplicate of 1
w_label1 = Label(win,text="",
                   font=("Times New Roman",18,"bold"))
w_label1.place(x=250,y=270,height=50,width=200)
#2nd
wb_label = Label(win,text="Weather Description",
                   font=("Times New Roman",15,"bold"))
wb_label.place(x=25,y=340,height=50,width=200)
#duplicate of 2
wb_label1 = Label(win,text="",
                   font=("Times New Roman",15,"bold"))
wb_label1.place(x=250,y=340,height=50,width=200)
#3rd
temp_label = Label(win,text="Temperature",
                   font=("Times New Roman",18,"bold"))
temp_label.place(x=25,y=410,height=50,width=200)
#duplicate of 3
temp_label1 = Label(win,text="",
                   font=("Times New Roman",18,"bold"))
temp_label1.place(x=250,y=410,height=50,width=200)
#4th
per_label = Label(win,text="Pressure",
                   font=("Times New Roman",18,"bold"))
per_label.place(x=25,y=480,height=50,width=200)
#after the 4th go to w_label and do the duplicate of it as w_label1
#duplicate of 4
per_label1 = Label(win,text="",
                   font=("Times New Roman",18,"bold"))
per_label1.place(x=250,y=480,height=50,width=200)
#after the step of duplicates go to top (above win = Tk())
#done button
done_button = Button(win,text="Done",
                   font=("Times New Roman",25,"bold"),command=data_get)
done_button.place(x=180,y=190,height=50,width=140)
win.mainloop()
