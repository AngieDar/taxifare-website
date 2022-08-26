from cProfile import label
from time import time
import streamlit as st
import requests
import pytz
import pandas as pd
from datetime import *



st.header('Best Taxi Fare Predictor in Europe (for NYC)')


'''
Check your fare cost in advance, and show to your taxi driver if he tries to scam you. 😅
'''

url = 'https://taxifare.lewagon.ai/predict'

dt = st.date_input(label='Enter date')
tm = st.time_input(label='Enter time')

pickup_datetime = datetime.combine(dt, tm)
pickup_longitude = st.text_input(label='Enter pickup lon', value=float)
pickup_latitude = st.text_input(label='Enter pickup lat', value=float)
dropoff_longitude = st.text_input(label='Enter drop lon', value=float)
dropoff_latitude = st.text_input(label='Enter drop lat', value=float)
passenger_count = st.text_input(label='Enter passengers', value=int)


params = {
    'key':'0000-00-00 00:00:00',
    'pickup_datetime':pickup_datetime,
    'pickup_longitude':float(pickup_longitude),
    'pickup_latitude':float(pickup_latitude),
    'dropoff_longitude':float(dropoff_longitude),
    'dropoff_latitude':float(dropoff_latitude),
    'passenger_count':int(passenger_count)}


response = requests.get(url, params=params)
st.write('## Fare Cost:', response.json()['fare'])
