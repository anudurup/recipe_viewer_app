import streamlit as st
import os
import glob
import find_recipes_based_on_ingredient as fri


if "shared" not in st.session_state:
   st.session_state["shared"] = True
meal_type = 'soup_recipes'
st.title(f"{meal_type}".capitalize())

fpath = r"segregated_recipes" + os.sep + meal_type
files = glob.glob(fpath + os.sep + "*.txt")
types_of_recipes = list()
for file in files:
    file_name = os.path.basename(file)
    option_string = file_name.replace('.txt','').title()
    if option_string != '':
        types_of_recipes.append(option_string)

for i,option in enumerate(types_of_recipes):
    recipe_dict,url_dict,instr_dict = fri.get_ingredients_recipe_url_dict(meal_type,i)      
    st.subheader(f"{option}")
    st.selectbox(f"{option}", options=url_dict.keys(), key=f"{option}")
    st.write(recipe_dict[st.session_state[f"{option}"]])
    st.write(url_dict[st.session_state[f"{option}"]])
    st.write(instr_dict[st.sessin_state[f"{option}"]])
