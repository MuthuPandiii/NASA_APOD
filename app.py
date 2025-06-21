import streamlit as st
import requests
from datetime import date

st.title("NASA APOD Viewer")

API_KEY = st.secrets["nasa"]["API_KEY"]

selected_date = st.date_input("Select a Date",value=date.today(),max_value = date.today())

API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={selected_date}"

print(API_URL)

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json();
    
    st.subheader("Date : " + data["date"])
    st.title(data["title"])
    st.write(data["explanation"])

    if(data["media_type"]) == "image":
        st.image(data["url"],caption = "Astronomical Photo")
    
    elif(data["media_type"]) == "video":
        st.video(data["url"])
    else:
        st.error("Unsupported Media Type")

else:
    st.error("NO DATA FROM NASA")
    
