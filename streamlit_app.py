import streamlit
import pandas

streamlit.title('My Mom''s New Health Diner!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bliueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Soothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick Some Fruits : ",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
