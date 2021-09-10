#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
#config
st.set_page_config(page_title="India",page_icon=":smiley:",
                   initial_sidebar_state="collapsed")

st.sidebar.success("Menu")


# In[2]:


st.title("India")
st.title("Delhi")


#text
st.text("I will go")
st.text("I am good")
st.text("Hello India")
st.text("This is so cool")

#header
st.header("'Cool")
st.header("This is a Header")

#subheader
st.subheader("Okay")
st.subheader("I will")
st.markdown("will go there")

#new

st.success("wawo")

st.warning("not good today")

st.info("I am Ajay")

st.error("here there is error")

st.exception("error")


#Dealing with Pandas

import pandas as pd
data=pd.read_csv("binary_classification_data.csv")
st.dataframe(data)

#st.table(data)
st.dataframe(data.head(2))
name="Rai"

#button

#

if st.button("Submit"):
    st.write(name)
    

if st.button("Submit",key='new01'):
    st.write("idea")


##radio
    

status=st.radio("What is your Status",("active","Inactive"))
if status=="active":
    st.write("your are active")
elif status=="Inactive":
    st.write("You are Not Active")


#
if st.checkbox("show/hide"):
    st.text("showing Something")

###
    
with st.expander("python"):
    st.write("Okay")

    

with st.expander("lEARN mORE"):
    st.write("Okay")
    st.write("Not Okay")




###
L=["Python","Java","C","c++"]
choice=st.selectbox("Pro Lang",L)


Lang=["Hindi","English","Urdu","Sanskrit","Spanish"]
mylag=st.multiselect("My Lan",Lang)




#slider
age=st.slider("Age",1,100)

st.select_slider("Choose State",options=["UP","DELHI","Bihar","UK","MP"])


#Image
from PIL import Image
img=Image.open("a.jpg")
st.image(img)

st.image(img,use_column_width=True)


#Input
fname=st.text_input("Enter Your Name")
st.title(fname)


msg=st.text_area("Enter your Msg")
st.write(msg)


#number
x=st.number_input("Enter your Value")
st.write(x+10)
#range
x=st.number_input("Enter your Value",1,10)
#Date Input

st.date_input("Enter ur DOB")
#tIME
st.time_input("Enter time")


##plot
import plotly.express as epz
import pandas as pd
data=pd.read_csv("binary_classification_data.csv")

st.dataframe(data.head(3))

fig=epz.pie(data,values=data["0"],names="Label")
st.plotly_chart(fig)


fig2=epz.line(data,x=data["0"],y=data["1"])
st.plotly_chart(fig2)


data1=pd.read_csv("Sal-data.csv")
st.dataframe(data1.head(2))

fig3=epz.bar(data1,x=data1["Name"],y=data1["Sales Amount"])
st.plotly_chart(fig3)

####

data3=pd.read_csv("iris.csv",header=None)
st.dataframe(data3.head())
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
#here we will get some error as its remove
data3[4].value_counts().plot(kind="bar")
st.pyplot()

st.write("recommended")
fig=plt.figure()
data3[4].value_counts().plot(kind="bar")
st.pyplot(fig)

#lets go for seaburm
import seaborn as sns
st.write("seaborn")

fig=plt.figure()
sns.countplot(data3[4])
st.pyplot(fig)

st.write("go to streamlit")

st.bar_chart(data3[2])

st.bar_chart(data3[[2,3]])


#Loading files
import pandas as pd 
import docx2txt
# import textract
from PyPDF2 import PdfFileReader
#import pdfplumber
st.title("Upload Your File")

from PIL import Image
def load_image(image_file):
	img = Image.open(image_file)
	return img

menu = ["Image","Dataset","DocumentFiles"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Image":
    st.subheader("Image")
    data = st.file_uploader("Upload Images",type=["png","jpg","jpeg"])
    if data is not None:
        st.image(load_image(data),width=250)


elif choice == "Dataset":
    st.subheader("Dataset")
    data_file = st.file_uploader("Upload CSV",type=["csv"])
    if data_file is not None:
        df = pd.read_csv(data_file)
	#st.dataframe(df.head(5))
        st.dataframe(df.head())




























# In[ ]:


#streamlit run k.py

