import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title(':gold[Iris Flower Dashboard]')
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR,os.pardir)
dir_of_interest = os.path.join(PARENT_DIR,'resources')
IMAGE_PATH = os.path.join(dir_of_interest,'images','flower.jpg')
DATA_PATH = os.path.join(dir_of_interest,'data','iris_n.csv')

img = image.imread(IMAGE_PATH)
st.image(img)

data = pd.read_csv(DATA_PATH)
st.dataframe(data)

species = st.selectbox('select a species:',data['Species'].unique())
column1,column2 = st.columns(2)
img1 = px.histogram(data[data['Species']==species], x='SepalLengthCm')
column1.plotly_chart(img1,use_container_width = True)

img2 = px.box(data[data['Species']==species],y='SepalLengthCm')
column2.plotly_chart(img2,use_container_width=True)
st.snow()
