import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


# Display Menu
streamlit.title('My Mom''s New Health Diner!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bliueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Soothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Pull list of fruits from aws bucket and show it as selector of fruit name
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# show option to the user prefille with 2 fruit choices and let allow user to choose as many as
fruits_selected = streamlit.multiselect("Pick Some Fruits : ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display selected fruits information to the screen
streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice Fruit Advice!')
# Show Fruit Kiwi
fruit_choice = streamlit.text_input('what fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)


# pull from website api with fruit as Kiwi
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice);

# Parse website output from json to table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# display normalized information in a table
streamlit.dataframe(fruityvice_normalized)
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("Hellow from Snowflake:")
streamlit.header("The fruit list contains:")
streamlit.dataframe(my_data_rows)

fruit_add = streamlit.text_input('What Fruit You Would Like To Add ?')
streamlit.write('The user entered ', fruit_add)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
