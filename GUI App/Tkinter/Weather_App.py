#Link do Video -> https://www.youtube.com/watch?v=Sz0_2fp27Q0

#Módulos
import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    #Link
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    #Transforma o link em json
    json_data = requests.get(api).json()
    #Extrai do json os dados que necessitamos
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    #Indicação se está sol, núvens ... e a temperatura
    final_info = condition + "\n" + str(temp) + "°C" 
    #Informações sobre o tempo
    final_data = "\n"+ "Temperatura Minima: " + str(min_temp) + "°C" + "\n" + "Temperatura Máxima: " + str(max_temp) + "°C" +"\n" + "Pressão: " + str(pressure) + "\n" +"Humidade: " + str(humidity) + "\n" +"Velocidade do Vento: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    #Mostrar na janela
    label1.config(text = final_info)
    label2.config(text = final_data)

#Inicializar a janela
canvas = tk.Tk()
#Tamanho da janela
canvas.geometry("600x500")
#Cor def
canvas.configure(background='#c299ff')
#Titulo da janela
canvas.title("Weather App")
#Informação para a TextBox
f = ("poppins", 15, "bold")
#Informação para a Label(Onde vai aparecer a informação sobre o tempo)
t = ("poppins", 35, "bold")

#TextBox
textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
#O texto a retornar(Que será o tempo)
textField.focus()
textField.bind('<Return>', getWeather)

#Labels
label1 = tk.Label(canvas, font=t,bg='#c299ff')
label1.pack()
label2 = tk.Label(canvas, font=f,bg='#c299ff')
label2.pack()

#Mainloop - Inicializar a janela
canvas.mainloop()