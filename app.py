# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own API key from https://openweathermap.org/api
API_KEY = "269ee17023aaa4f9dbf0dd12f5ab9311"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        time = data['dt']
        humidity = data["main"]["humidity"]
        icon_id = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/w/{icon_id}.png"
        weather_data = {'icon_url': icon_url}
        
        
        # icon = data["weather"][0]["icon"]
        return render_template("weather.html", city=city,time=time,weather=weather,weather_data=weather_data, temp=temp, feels_like=feels_like, humidity=humidity)
    else:
        error = data["message"]
        return render_template("error.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)