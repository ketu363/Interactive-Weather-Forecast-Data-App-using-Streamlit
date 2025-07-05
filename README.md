# 🌦️ Weather Forecast App

A simple and interactive weather forecast web app built with **Streamlit** and **OpenWeatherMap API**.  
Users can enter a city name and select the number of forecast days (1–5), and the app will display either:

- 📈 A line plot of temperature over time  
- ☁️ Weather condition icons (sunny, clouds, rain, snow)

---

## 🚀 Features

- 🔍 City-based forecast using OpenWeatherMap API  
- 📅 Forecast up to 5 days (3-hour intervals)  
- 📈 Dynamic line plot for temperature  
- ☁️ Weather icons for sky conditions  
- 🧠 Cleanly separated **frontend** and **backend** logic

---

## 📁 Project Structure

```
weather_forecast_app/
│
├── main.py            # Frontend (Streamlit UI)
├── backend.py         # Backend (data fetching and processing)
├── images/            # Icons for sky conditions
│   ├── clear.png
│   ├── clouds.png
│   ├── rain.png
│   └── snow.png
└── requirements.txt   # Python dependencies
```

---

## 🛠️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key:**
   - Get a free API key from [OpenWeatherMap](https://openweathermap.org/forecast5)
   - In `backend.py`, replace the placeholder with your key:
     ```python
     API_KEY = "your_api_key_here"
     ```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 📸 Screenshots

### Temperature Plot

 ![image](https://github.com/user-attachments/assets/1d97b40e-850e-431d-acce-5385d936e8ee)

### Sky Conditions 
![image](https://github.com/user-attachments/assets/341674b8-b442-4dad-8c15-af9ac77ce912)
 

---

## 📦 Dependencies

- `streamlit`
- `requests`
- `plotly`

Install all with:
```bash
pip install -r requirements.txt
```

---

## 💡 Future Improvements

- 🌍 Add support for multiple units (Fahrenheit/Celsius)
- 🗺️ Map view with geo-coordinates
- 💾 Caching API responses
- 📱 Mobile responsiveness

---

## 📜 License

MIT License – Use this project freely for learning and development.

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenWeatherMap API](https://openweathermap.org/)
