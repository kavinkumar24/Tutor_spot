from tokenize import Name
from urllib.request import urlopen
import requests
from googletrans import Translator
from pytube.exceptions import RegexMatchError
import requests
import speech_recognition as sr 
import moviepy.editor as mp
import webbrowser
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
from pytube import YouTube
import urllib
import os
import youtube_dl
import speech_recognition as sr
import moviepy.editor as mp
import json
import requests,sys,webbrowser,bs4

from youtube_transcript_api import YouTubeTranscriptApi,NoTranscriptFound,VideoUnavailable
import nltk
import string
from heapq import nlargest
import pywhatkit as pwt
from streamlit_option_menu import option_menu
from gtts import gTTS
from googletrans import Translator

import base64


import string
import sys
import time
import PyPDF2
import base64


hide_st_style = """
<style>
#MainMenu{visibility:hidden;}

footer {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
with st.sidebar:
    st.title("Tutor Spot")
    select = option_menu(
        menu_title="Main Menu",
        options = ["Scraping data in youtube","Text summarization ","English Translator","MP4/MP3 to Text","Find best books","read the language","Contact"],
        menu_icon="cast"
        )
    page_bg_img = f"""
    <style>
    [data-testid="stSidebar"] {{

    background-color:#abd1ed;
    color:white;    
    }}
   
    </style>
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)
    

if select == "Text summarization ":
    

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-color: #c8d8e4;
    background-size: 180%;
    background-position: top left;  
    background-attachment: local;
    
    }}
    [data-testid="stHeader"]{{
        background-color:rgba(0,0,0,0);
    }}
    </style>
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # summarize the given text
    st.title("Enter the text below and Summarize the Text")
    with st.container():  
        try:        
            text = st.text_area("Enter Text to Summarize", height=200)
            if st.button("Summarize"):
                if text.count(". ") > 20:
                    length = int(round(text.count(". ")/10, 0))
                else:
                    length = 1

                nopuch =[char for char in text if char not in string.punctuation]
                nopuch = "".join(nopuch)

                processed_text = [word for word in nopuch.split() if word.lower() not in nltk.corpus.stopwords.words('english')]

                word_freq = {}
                for word in processed_text:
                    if word not in word_freq:
                        word_freq[word] = 1
                    else:
                        word_freq[word] = word_freq[word] + 1

                max_freq = max(word_freq.values())
                for word in word_freq.keys():
                    word_freq[word] = (word_freq[word]/max_freq)

                sent_list = nltk.sent_tokenize(text)
                sent_score = {}
                for sent in sent_list:
                    for word in nltk.word_tokenize(sent.lower()):
                        if word in word_freq.keys():
                            if sent not in sent_score.keys():
                                sent_score[sent] = word_freq[word]
                            else:
                                sent_score[sent] = sent_score[sent] + word_freq[word]

                summary_sents = nlargest(length, sent_score, key=sent_score.get)
                summary = " ".join(summary_sents)
                st.write(summary)
        except ValueError:
            st.write(" ")
            
elif select=="English Translator":
    import base64
    import plotly.express as px

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-color: #c8d8e4;
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    [data-testid="stHeader"]{{
        background-color:rgba(0,0,0,0);
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    image = Image.open('trans.png')
    st.image(image,  width=90)

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.header("Translator:")
    text = st.text_area("enter any language it will tranlate into english:",height=130)
    if st.button("Translate"):
        translator = Translator()
        translated_text = translator.translate(text)
        st.write(translated_text.text)
        
        
elif select == "Contact":
    st.image("test.jpg")
    page_bg_img=f"""
    <style>
    [data-testid="stImage"] {{
        border-radius:200px;
        background-color: #c8d8e4;
        }}
    
    </style>
    """
    
    new_title = '<p style="font-family:serif; color:Green; font-size: 42px;">This WebTool  was developed by AI lab students for student use </p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
    original_title = '<p style="font-family:courier; color:Blue; font-size: 32px;">Main_Role: KAVIN KUMAR P</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    original_title = '<p style="font-family:courier; color:Blue; font-size: 27px;">Sub_Role: PRAVEEN A, PRAGUSHPATHI P, KANISHKAN S</p>'
    st.markdown(original_title, unsafe_allow_html=True)

elif select== "Find best books":
            st.title("Now-a-days, we prefer e-book rather than offline books")
            st.subheader("Click the below option of google book.com get more books")
            if st.button("Click here"):
                url='https://books.google.co.in/'
                webbrowser.open_new_tab(url)
            with st.container():
                def load_lottiefile(filepath:str):
                    with open(filepath,"r") as f:
                        return json.load(f)
                def load_lottieurl(url:str):
                    r = requests.get(url)
                    if r.status_code !=200:
                        return None 
                    return r.json()
                lottie_hello1 =load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_wh5alaq6.json")
                st_lottie (
                lottie_hello1,
                speed=1,
                quality = "low",
                height=200,
                width=550,
                key=None,
                )
            page_bg_img = f"""
            <style>
            [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://www.itl.cat/pngfile/big/148-1487799_education-wallpaper-hd-learning-backgrounds.jpg");
            background-size: 140%;
            background-position: top left;
            background-repeat: no-repeat;
            background-attachment: local;
            }}
            [data-testid="stHeader"]{{
                background-color:rgba(0,0,0,0);
            }}
            </style>
            """

            st.markdown(page_bg_img, unsafe_allow_html=True)
            
    


