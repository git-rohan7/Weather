# from tkinter import *
# from tkinter import ttk
# import requests
#
# def get_data():
#     city_name = city.get()
#     data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=1583c818415a229f09fb3f11a7e99051").json()
#
#     w1.config(text=data["weather"][0]["main"])
#     T1.config(text=str(int(data["main"]["temp"]-273.15)))
#     H1.config(text=data["main"]["humidity"])
#     Pr1.config(text=data["main"]["pressure"])
#     min1.config(text=str(int(data["main"]["temp_min"]-273.15)))
#     max1.config(text=str(int(data["main"]["temp_max"]-273.15)))
#     P1.config(text=str(int(data["main"]["feels_like"]-273.15)))
#
#
#
#
#
#
# win = Tk()
# win.title("Your Local Weather App")
# win.config(bg="skyblue")
# win.geometry("700x700")
# city = StringVar()
#
# name_label = Label(win, text="Your Local Weather App", font=("Time New Roman", 25, "bold"))
# name_label.place(x=100, y=50, height=30, width=500)
# list_state = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
#
# com = ttk.Combobox(win,values=list_state, textvariable=city)
# com.place(x=100, y=100, height=30, width=500)
# done_button = ttk.Button(win, text="Done", command = get_data)
# done_button.place(x=300, y=150, height=30, width=100)
#
# w = Label(win, text="Weather")
# w.place(x=50, y=200, height=30, width=150)
# w1 = Label(win, text="")
# w1.place(x=250, y=200, height=30, width=150)
#
# T = Label(win, text="Temperature")
# T.place(x=50, y=250, height=30, width=150)
# T1 = Label(win, text="")
# T1.place(x=250, y=250, height=30, width=150)
#
# minT = Label(win, text="Minimum Temperature")
# minT.place(x=50, y=300, height=30, width=150)
# min1 = Label(win, text="")
# min1.place(x=250, y=300, height=30, width=150)
#
# maxT = Label(win, text="Maximum Temperature")
# maxT.place(x=50, y=350, height=30, width=150)
# max1 = Label(win, text="")
# max1.place(x=250, y=350, height=30, width=150)
#
# H = Label(win, text="Humidity")
# H.place(x=50, y=450, height=30, width=150)
# H1 = Label(win, text="")
# H1.place(x=250, y=450, height=30, width=150)
#
# P = Label(win, text="Feels Like")
# P.place(x=50, y=400, height=30, width=150)
# P1 = Label(win, text="")
# P1.place(x=250, y=400, height=30, width=150)
#
# Pr = Label(win, text="Pressure")
# Pr.place(x=50, y=500, height=30, width=150)
# Pr1 = Label(win, text="")
# Pr1.place(x=250, y=500, height=30, width=150)
#
# exit_button = ttk.Button(win, text="Exit", command=lambda: win.destroy())
# exit_button.place(x=300, y=600, height=30, width=100)
#
# win.mainloop()
#
#
#

from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk


def get_data():
    city_name = city.get()

    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=1583c818415a229f09fb3f11a7e99051").json()

    weather_main = data["weather"][0]["main"].lower()
    w1.config(text=data["weather"][0]["main"])


    T1.config(text=str(int(data["main"]["temp"] - 273.15)) + "°C")
    H1.config(text=str(data["main"]["humidity"]) + "%")
    Pr1.config(text=str(data["main"]["pressure"]) + "hpa")
    min1.config(text=str(int(data["main"]["temp_min"] - 273.15)) + "°C")
    max1.config(text=str(int(data["main"]["temp_max"] - 273.15)) + "°C")
    P1.config(text=str(int(data["main"]["feels_like"] - 273.15)) + "°C")

    icon_label.config(text=get_weather_icon(weather_main))



def get_weather_icon(weather):
    icons = {
        "clear": "☀️",
        "clouds": "☁️",
        "rain": "🌧️",
        "snow": "❄️",
        "thunderstorm": "⛈️",
        "drizzle": "🌦️",
        "mist": "🌫️",
        "fog": "🌫️",
        "haze": "🌫️"
    }
    return icons.get(weather, "🌤️")



win = Tk()
win.title("Your Local Weather App")
win.config(bg="lightblue")
win.geometry("800x750")
city = StringVar()



bg_image = Image.open("/Users/rohankumar/Desktop/PythonProject/1p.jpeg")
bg_image = bg_image.resize((800, 750), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(win, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

name_label = Label(win, text="Your Local Weather App", font=("Arial", 28, "bold"),
                   bg="white", fg="navy", relief="raised", bd=2)
name_label.place(x=150, y=20, height=40, width=500)





com = ttk.Combobox(win, textvariable=city, font=("Arial", 12))
com.place(x=150, y=80, height=35, width=500)
done_button = ttk.Button(win, text="Get Weather", command=get_data, style="Accent.TButton")
done_button.place(x=350, y=130, height=35, width=150)


info_frame = Frame(win, bg="lightblue", relief="groove", bd=15)
info_frame.place(x=100, y=180, width=600, height=500)



w = Label(info_frame, text="Weather:", font=("Arial", 12, "bold"), bg="lightblue", fg="darkblue")
w.grid(row=0, column=0, padx=10, pady=10, sticky="w")
icon_label = Label(info_frame, text="", font=("Arial", 24), bg="lightblue")
icon_label.grid(row=0, column=1, padx=10, pady=10)
w1 = Label(info_frame, text="", font=("Arial", 12), bg="lightblue", fg="navy")
w1.grid(row=0, column=2, padx=10, pady=10, sticky="w")


T = Label(info_frame, text="Temperature:", font=("Arial", 12, "bold"), bg="lightblue", fg="darkblue")
T.grid(row=1, column=0, padx=10, pady=5, sticky="w")
T1 = Label(info_frame, text="", font=("Arial", 12), bg="lightblue", fg="red")
T1.grid(row=1, column=2, padx=10, pady=5, sticky="w")


minT = Label(info_frame, text="Min Temperature:", font=("Arial", 12, "bold"), bg="lightblue", fg="darkblue")
minT.grid(row=2, column=0, padx=10, pady=5, sticky="w")
min1 = Label(info_frame, text="", font=("Arial", 12), bg="lightblue", fg="blue")
min1.grid(row=2, column=2, padx=10, pady=5, sticky="w")


maxT = Label(info_frame, text="Max Temperature:", font=("Arial", 12, "bold"), bg="lightblue", fg="darkblue")
maxT.grid(row=3, column=0, padx=10, pady=5, sticky="w")
max1 = Label(info_frame, text="", font=("Arial", 12), bg="lightblue", fg="orange")
max1.grid(row=3, column=2, padx=10, pady=5, sticky="w")


P = Label(info_frame, text="Feels Like:", font=("Arial", 12, "bold"), bg="lightblue", fg="darkblue")
P.grid(row=4, column=0, padx=10, pady=5, sticky="w")
P1 = Label(info_frame, text="", font=("Arial", 12), bg="lightblue", fg="purple")
P1.grid(row=4, column=2, padx=10, pady=5, sticky="w")


H = Label(info_frame, text="Humidity:", font=("Arial", 12, "bold"), bg="lightblue", fg="darkblue")
H.grid(row=5, column=0, padx=10, pady=5, sticky="w")
H1 = Label(info_frame, text="", font=("Arial", 12), bg="lightblue", fg="green")
H1.grid(row=5, column=2, padx=10, pady=5, sticky="w")


Pr = Label(info_frame, text="Pressure:", font=("Arial", 12, "bold"), bg="lightblue", fg="darkblue")
Pr.grid(row=6, column=0, padx=10, pady=5, sticky="w")
Pr1 = Label(info_frame, text="", font=("Arial", 12), bg="lightblue", fg="gray")
Pr1.grid(row=6, column=2, padx=10, pady=5, sticky="w")

exit_button = ttk.Button(win, text="Exit", command=lambda: win.destroy())
exit_button.place(x=350, y=700, height=35, width=100)




win.mainloop()

