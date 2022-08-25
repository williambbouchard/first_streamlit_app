import streamlit
import pandas

streamlit.title('🥣 My parents New Healthy Diner')

streamlit.header('🥗 Breakfast Menu')
streamlit.text('🐔 Omega 3 & Oatmeal')
streamlit.text('🥑 Kale, Spinach & Smoothie')
streamlit.text('🍞 Hard-boiled free range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
