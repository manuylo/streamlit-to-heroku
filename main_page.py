import streamlit as st

st.title('My first ml app')

my_text=st.text('A random version')

my_button  =st.button('Run ML')

if my_button:
    st.title('The model is running...')


agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
    
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")