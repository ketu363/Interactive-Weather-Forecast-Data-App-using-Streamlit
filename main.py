import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input , slider, selectbox, and subheader
st.title("Weather Forcast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option =st.selectbox("Selection data to view ",
                     ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}" )

if place:
    # Get the temperature/skey data
    try:
        filtered_data = get_data(place, days)


        # Creating a temperature plot
        if option =="Temperature":
            # Filtering the temperature data
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates =[dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option =="Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            # Filtering the sky data
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width= 115)
    except Exception:
        st.write("That Place does not exist.")



