import streamlit as st
import time

st.image('https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/streamlit_header_image.jpg')
col1, col2, col3 = st.columns(3)
with col2:
    st.title('Recipe2PDF')
st.markdown('How often did it happen to you, that now is exactly the perfect moment to cook that cool veggie-tofu-penang curry you read about just couple of days ago, or those banana oatmeal pancakes are the fast and easy solution for a Sunday breakfast, but you don’t seem to find the recipes again.')
st.markdown('Problem solved! With recipe2pdf you are 2 clicks away from being a person, who never misses an interesting new recipe. Just copy the link to the website, click on “generate PDF” - and voila, chef, the recipe is ready to be saved in your library, so that the moment you get in to experimentative state of mind the stage is set to make your creativity fly - and hopefully your tastebuds as happy, as they can get.')

st.text_input("Your recipe's Web link")
with st.expander("See templates"):
    st.image(['https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_1.png',
        'https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_2.png'],
        width=300)
st.radio('Would you like to choose a template for your recipe?', options=['Template 1', 'Template 2'])
st.checkbox('May we store this recipe in our data base?')
st.button('Generate PDF')

st.text_input('Type in ingridients')
if st.button('Inspire me!'):
    with st.spinner('Magic is happening...'):
        time.sleep(3)
    st.balloons()
    st.markdown('Found recommendations:')
    st.markdown('*Name of some amazing recipe as hyperlink.*')
    with st.expander('Download PDF'):
        st.markdown('*Note: PDF will open in another browser tab*')