# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


# Write directly to the app
st.title(":cup_with_straw: Customize your smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothies
    """)




#import streamlit as st

#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)

name_on_order =st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be', name_on_order)

#session = get_active_session()

cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect ('Choose upto 5 ingredients:',
my_dataframe,max_selections = 5)

if ingredients_list:  
    ingredients_string = ''

    for fruit_choosen in ingredients_list:
        ingredients_string += fruit_choosen + ' '



    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""



    time_to_insert = st.button('Submit Order')



    if time_to_insert:
        session.sql(my_insert_stmt).collect()
	  
        st.success('Your Smoothie is ordered!', icon="✅")


