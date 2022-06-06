import streamlit as st
import time

# Setup functions for both use cases:
def PDF():
    st.text_input("Your recipe's web link")
    with st.expander("See templates"):
        st.image(['https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_1.png',
            'https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_2.png'],
            width=300)
    st.radio('Would you like to choose a template for your recipe?', options=['Template 1', 'Template 2'])
    st.checkbox('Choosing this box you allow us to store this recipe in our data base.')
    st.button('Generate PDF')

def recommendation():
    ingr = st.text_input('Type in ingredients:')
    if st.button('Inspire me!'):
        if ingr == '':
            st.markdown('Please enter some ingredients for a recommendation.')
        elif ingr != '':
            with st.spinner('Magic is happening...'):
                time.sleep(3)
            st.balloons()
            st.markdown('Found recommendations: *Name of some amazing recipe as hyperlink.*')
            col1, col2, col3 = st.columns(3)
            with col1:
                with st.expander('Download PDF'):
                    st.markdown('*Note: PDF will open in a new browser tab*')

# arrange header area of the page
st.image('https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/streamlit_header_image.jpg')
col1, col2, col3 = st.columns(3)
with col2:
    st.title('Recipe2PDF')

<<<<<<< HEAD
# create sidebar to choose, which use case user wants to use
page = st.sidebar.selectbox('Choose, what you want to do:', ('Generate PDF', 'Generate recommendation'))

# setup pages for each use case
if page == 'Generate PDF':
    st.markdown('How often did it happen to you, that now is exactly the perfect moment to cook that cool veggie-tofu-penang curry you read about just couple of days ago, or those banana oatmeal pancakes are the fast and easy solution for a Sunday breakfast, but you don’t seem to find the recipes again.')
    st.markdown("Problem solved! With recipe2pdf you are 2 clicks away from being a person, who never misses an interesting new recipe. Just copy the link to the website, click on 'Generate PDF' - and voila, chef, the recipe is ready to be saved in your library, so that the moment you're up to some experiments the stage is set to make your creativity fly - and hopefully your tastebuds as happy, as they can get.")
    PDF()

elif page == 'Generate recommendation':
    st.markdown("Do you fall into the trap of cooking same and same dishes every time? You usually have everything you need in the cupboard, it's familiar, tested - and oh so boring! \
    What if it is possible to make of those same ingredients something, that is going to become your new got-to dinner? Or maybe fall into a new routine - having no food routine at all and looking forward to any meal.")
    st.markdown("Just type in the suff you have in your cupboard and see, what yummy recipe will inspire your cooking talents today!")
    recommendation()
=======
st.text_input("Your recipe's Web link")
with st.expander("See templates"):
    st.image(['https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_1.png',
        'https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_2.png'],
        width=300)
st.radio('Please choose a template for your recipe.', options=['Template 1', 'Template 2'])
st.checkbox('Choosing this box you allow us to store your recipe in our data base.')
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
>>>>>>> a3c219a3cfe3959f4f34e11e0a8cdf663322ca1a
