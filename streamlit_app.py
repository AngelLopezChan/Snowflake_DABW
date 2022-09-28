import streamlit
import pandas

streamlit.title('My Parents New Healty Diner')
streamlit.header('This is how it starts with streamlit/python/snowflake')

streamlit.subheader('Menu')
streamlit.text('🦈 Tuna Sandwich')
streamlit.text('🐔 chicken breast Sandwich')
streamlit.text('🦈🥗Tuna Salad')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocato Toast')

#new tittle
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#getting file from site and show it
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add selection into a variable and then lets use that
fruits_selected = streamlit.multiselect("Select some fruits: ", list(my_fruit_list.index),['Apple','Banana','Kiwifruit','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#show as a list, only mentioned columns
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#New section to display fruittyvice api response
streamlit.header("Fruityvice Fruit Advice!")
#fruit selected by user
fruit_choice = streamlit.text_input('What fruit do you like info about?','kiwi')
streamlit.write('The user is asking for',fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# pasing json data to show it better
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display containt in dataframe
streamlit.dataframe(fruityvice_normalized)

#adding snowflake connection
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake, again:")
streamlit.text(my_data_row)

#query fruit list
my_cur2 = my_cnx.cursor()
my_cur2.execute("SELECT * FROM fruit_load_list")
my_data_row2 = my_cur2.fetchone()
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row2)
streamlit.haeder("The fruit load list contains:")
streamlit.dataframe(my_data_row2)

