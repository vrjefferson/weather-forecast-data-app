import streamlit as st
import plotly.express as px

st.title("Weather Forecast For The Next 5 Days")
place = st.text_input("Place: ").title()
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days forecasted")
option = st.selectbox("Select data to view.", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}.")


def get_data(days):
    dates = ["2022-10-25", "2022-10-26", "2022-10-27"]
    temperature = [10, 11, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
