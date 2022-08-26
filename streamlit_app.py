import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('🥣 My parents New Healthy Diner')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🐔 Omega 3 & Oatmeal')
streamlit.text('🥑 Kale, Spinach & Smoothie')
streamlit.text('🍞 Hard-boiled free range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
  return streamlit.dataframe(fruityvice_normalized)

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
        streamlit.error("Please select fruit")
  else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
                                      streamlit.error()

#streamlit.write('The user entered ', fruit_choice)
# streamlit.text(fruityvice_response)

#streamlit.stop()
streamlit.header("The fruit load list contains:")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM fruit_load_list")
    return my_cur.fetchall()
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("Insert into fruit_load_list values ('from streamlit')")
    return "Thank you for adding" + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

#streamlit.write('The user entered ', fruit_choice_snowflake)
