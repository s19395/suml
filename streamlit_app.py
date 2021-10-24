import streamlit as st
from transformers import pipeline
from PIL import Image

def translate(text):
    translator = pipeline("translation_en_to_de")
    return translator(text)

image = Image.open('Flag_of_the_United_Kingdom_and_Germany.png')
st.image(image)

st.title('English2German')
st.header('Tłumacz na język niemiecki.')

st.markdown('Ta aplikacja tłumaczy tekst wprowadzony w pole tekstowe z języka angielskiego na język niemiecki. '
            'W przypadku błędu należy sprawdzić poprawność wpisanego zdania / słowa.')

st.header('Translate:')

text = st.text_area(label="Wpisz tekst do przetłumaczenia")

if text:
    with st.spinner(text='Tłumaczenie w trakcie...'):
        answer = translate(text)
        for item in answer:
            if(item["translation_text"] == text):
               st.info('Chyba coś poszło nie tak w tłumaczeniu...')
               st.write('Rezultat: ' + item["translation_text"])
            else:
                st.write(item["translation_text"])
                st.success('Gotowe!')
                st.balloons()

st.subheader('Made by:')
st.write('S19395 Oskar Tybura')
