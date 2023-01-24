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
import json
import requests,sys,webbrowser,bs4
from youtube_transcript_api import YouTubeTranscriptApi,NoTranscriptFound,VideoUnavailable
import nltk
import string
from heapq import nlargest 
from streamlit_option_menu import option_menu
from gtts import gTTS
from googletrans import Translator
import base64
import string
import sys
import time
import PyPDF2 
import base64 
with st.sidebar:
    st.title("Tutor Spot")
    select = option_menu(
        menu_title="Main Menu",
        options = ["Scraping data in youtube","Text summarization ","English Translator","MP4/MP3 to Text","Find best books","read the language","Contact"],
        menu_icon="cast")
    page_bg_img = f"""
    <style>
    .menu .container-xxl[data-v-4323f8ce]{{
        background-color:white;
        color:black; 
    }} 
    [data-testid="stSidebar"] {{
    background-color:#faeae8;
    color:white;    
    }}
    </style>
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)
    base='light'  
    
if select == "Text summarization ":
    page_bg_img = f"""
   <style>
    .st-bx{{
        border:2px solid #e8d2c3;
    }}
    *{{
    color:black;
     }}
    [data-testid="stAppViewContainer"] > .main {{
    background-color:#f3f0ec;
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
            st.write("")
            
elif select=="English Translator":
    page_bg_img = f"""
    <style>
    .st-bx{{
        border:2px solid #e8d2c3;
    }}
    *{{
    color:black;
     }}
    [data-testid="stAppViewContainer"] > .main {{
    background-color: #f3f0ec;
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

elif select=="Scraping data in youtube":
    st.caption('Tutor Spot')
    st.title("Welcome to Our webpage (learn everywhere)")
    def load_lottiefile(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
    def load_lottieurl(url:str):
        r = requests.get(url)
        if r.status_code !=200:
            return None 
        return r.json()
    lottie_load1 =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_p4q9ra7d.json")
    st_lottie (
        lottie_load1,
        speed=1,
        quality = "low",
        height=500,
        width=700,
        key=None
    )
    with st.container():
        st.subheader('This webpage tells about web scrabbing by using AI')
        st.title('web extracting data in social media videos')
    with st.container():
        try:
            url = st.text_input('The URL link', placeholder = "type your url")
            yt =  YouTube(url)
        except RegexMatchError:
            st.write("press enter key and than proceed")
        st.markdown(
        """
       <style>
         .st-bx{
        border:2px solid #e8d2c3;
        background-color:white;
            }
            .stButton > button{
                border-radius:12%;
                background-color:#DAFDF4;
                border-color: green;
                color:black;
            }  
            .stTextInput>div>div>TextInput {
                color: #4F8BF9;
                border-color: green;
             }
            [data-testid="stAppViewContainer"] > .main {
               background-color: #f3f0ec;
             }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    base = "light"
    if st.button("Click To view the details of the video"):
        try:
            with st.container():
                st.write("Title :", yt.title)
                # To get number of views
                st.write("Views :", yt.views)
                # To get the length of video
                st.write("Duration :", yt.length)
                # To get description
                st.write("Description :", yt.description)
                # To get ratings
                st.write("Ratings :", yt.rating)
        except NameError:
            st.warning("Paste the url and proceed",icon="⚠️")

    if st.button('Download MP4'):
        try:
            stream = yt.streams.get_highest_resolution()
            stream.download('Downloads')
            st.header("Download completed!!")
            with st.container():
                def load_lottiefile(filepath:str):
                    with open(filepath,"r") as f:
                        return json.load(f)
                def load_lottieurl(url:str):
                    r = requests.get(url)
                    if r.status_code !=200:
                        return None 
                    return r.json()
            lottie_do =load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_o8dma9lg.json")
            st_lottie (
                lottie_do,
                speed=1,
                quality = "low",
                height=200,
                width=700,
                key=None,
            )
                    
        except NameError:
            st.warning('enter the url and proceed', icon="⚠️")
    if st.checkbox("Show the subtitles"):
                try:
                    a2 = url.replace("https://www.youtube.com/watch?v=",'')
                    print(a2)
                    srt = YouTubeTranscriptApi.get_transcript(a2)
                    text = ""
                    for i in srt:
                        text += i["text"] + "..."
                    st.write(text)
                except NoTranscriptFound:
                    st.warning("sorry this video does not contain the subtitles")
                except VideoUnavailable:
                    st.warning("Paste the url in the given box",icon="⚠️")
                        
elif select=="MP4/MP3 to Text":
    #mp4 to text
    st.header("This option is support only in PC so please try in PC")
    st.caption("We will update soon")
    page_bg_img = f"""
    <style>
    .st-bx{{
        border:2px solid #e8d2c3;
    }}
    *{{
    color:black;
     }}
    [data-testid="stAppViewContainer"] > .main {{
    background-color: #f3f0ec;
    background-size: cover;
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
    st.markdown(
        """
        <style>
            .stButton > button{
                border-radius:10%;
                background-color:#fc6762;
                color:black;
                position:relative;
                left:200px;
                bottom:-10px;
                
            }
             .stButton > button:hover{
                 background-color:#fa817d;
                 color:black;
             }
            
    
        </style>
        """,
        unsafe_allow_html=True
    )
    def load_lottiefile(filepath:str):
            with open(filepath,"r") as f:
                    return json.load(f)
    def load_lottieurl(url:str):
        r = requests.get(url)
        if r.status_code !=200:
            return None 
        return r.json()
    lottie_video =load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wvlpcbl8.json")

    st_lottie (
        lottie_video,
        speed=1,
        quality = "low",
        height=200,
        width=420,
        key=None
    )
    path_input =st.text_input("Enter the relative path of mp4 file:",placeholder="give the path of mp4 file")
    path = ""
    for i in path_input:
        if i!='"':
            path=path+i
    if st.button("Convert MP4 into text"):
        try:

            clip = mp.VideoFileClip(r"{}".format(path))
            clip.audio.write_audiofile("ai.wav")
            recognizer = sr.Recognizer()
            audio = sr.AudioFile("ai.wav")
            with audio as source:
                audio_file = recognizer.record(source,duration=150)
                st.write(recognizer.recognize_google(audio_file))
    
        except OSError:
            st.write("please give the path of mp4 file")

        def load_lottiefile(filepath:str):
            with open(filepath,"r") as f:
                    return json.load(f)
    def load_lottieurl(url:str):
        r = requests.get(url)
        if r.status_code !=200:
            return None 
        return r.json()
    lottie_txt =load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_tuarzhkt.json")

    st_lottie (
        lottie_txt,
        speed=1,
        quality = "low",
        height=200,
        width=400,
        key=None
    )
    #mp3 to text

    path1 = st.text_input("Enter the path of mp3 or wav file:",placeholder="Give the total relative path of Mp3 or wav file only")
    updated_path1=""
    for j in path1:
        if j!='"':
            updated_path1=updated_path1+j
    # the below algorithm is used to convert the audio into text
    if st.button("mp3 to text"):
        try:
            audio_path = mp.AudioFileClip(r"{}".format(updated_path1)) 
            audio_path.write_audiofile("cplusplus.wav")
            audio1 = sr.AudioFile("cplusplus.wav")
            recognizer = sr.Recognizer()
            with audio1 as source:
                audio_file1 = recognizer.record(source,duration=120)
                st.write(recognizer.recognize_google(audio_file1))
        except OSError:
            st.write("Give the path of the mp3")
    try:
        os.remove(r'cplusplus.wav')
    except FileNotFoundError:
        st.write(" ")
    
elif select=='read the language':
        
    try:
        os.mkdir("temp")
    except:
        pass
    st.title("Text to speech")
    translator = Translator()
    text = st.text_area("Enter Text ", height=150,placeholder="type the text here....")
    in_lang = st.selectbox(
        "Select your input language",
        ("Afrikaans","Arabic","Bengali","Czech","Chinese","Danish","Dutch","English","Finnish","French","German","Greek","Hindi","Hungarian","Italian",  "Japanese", "Kannada","korean","Malayalam","Russian","Tamil","Telugu","Spanish","Urdu"),
    )
    if in_lang == "Afrikaans":
        input_language = "af"
    elif in_lang == "Arabic":
        input_language = "ar"
    elif in_lang =="Bengali":
        input_language = "bn"
    elif in_lang =="Czech":
        input_language = "cs"
    elif in_lang =="Chinese":
        input_language = "zh-cn"
    elif in_lang =="Danish":
        input_language = "da"
    elif in_lang =="Dutch":
        input_language = "nl"
    elif in_lang =="English":
        input_language = "en"
    elif in_lang =="Finnish":
        input_language = "fi"
    elif in_lang =="French":
        input_language = "fr"
    elif in_lang =="German":
        input_language = "de"
    elif in_lang =="Greek":
        input_language = "el"
    elif in_lang =="Hindi":
        input_language = "hi"
    elif in_lang =="Hungarian":
        input_language = "hu"
    elif in_lang =="Italian":
        input_language = "it"
    elif in_lang =="Japanese":
        input_language = "ja"
    elif in_lang =="Kannada":
        input_language = "kn"
    elif in_lang =="korean":
        input_language = "ko"
    elif in_lang =="Malayalam":
        input_language = "ml"
    elif in_lang =="Russian":
        input_language = "ru"
    elif in_lang =="Tamil":
        input_language = "ta"
    elif in_lang =="Telugu":
        input_language = "te"
    elif in_lang =="Spanish":
        input_language = "es"
    elif in_lang =="Urdu":
        input_language = "ur"
    out_lang = st.selectbox(
        "Select your output language",
        ("Afrikaans","Arabic","Bengali","Czech","Chinese","Danish","Dutch","English","Finnish","French","German","Greek","Hindi","Hungarian","Italian",  "Japanese", "Kannada","korean","Malayalam","Russian","Tamil","Telugu","Spanish","Urdu"),
    )
    if out_lang == "Afrikaans":
        output_language = "af"
    elif out_lang == "Arabic":
        output_language = "ar"
    elif out_lang =="Bengali":
        output_language = "bn"
    elif out_lang =="Czech":
        output_language = "cs"
    elif out_lang =="Chinese":
        output_language = "zh-cn"
    elif out_lang =="Danish":
        output_language = "da"
    elif out_lang =="Dutch":
        output_language = "nl"
    elif out_lang =="English":
        output_language = "en"
    elif out_lang =="Finnish":
        output_language = "fi"
    elif out_lang =="French":
        output_language = "fr"
    elif out_lang =="German":
        output_language = "de"
    elif out_lang =="Greek":
        output_language = "el"
    elif out_lang =="Hindi":
        output_language = "hi"
    elif out_lang =="Hungarian":
        output_language = "hu"
    elif out_lang =="Italian":
        output_language = "it"
    elif out_lang =="Japanese":
        output_language = "ja"
    elif out_lang =="Kannada":
        output_language = "kn"
    elif out_lang =="korean":
        output_language = "ko"
    elif out_lang =="Malayalam":
        output_language = "ml"
    elif out_lang =="Russian":
        output_language = "ru"
    elif out_lang =="Tamil":
        output_language = "ta"
    elif out_lang =="Telugu":
        output_language = "te"
    elif out_lang =="Spanish":
        output_language = "es"
    elif out_lang =="Urdu":
        output_language = "ur"
    
    english_accent = st.selectbox(
        "Select your english accent",
        (
            "Default",
            "India",
            "United Kingdom",
            "United States",
            "Canada",
            "Australia",
            "Ireland",
            "South Africa",
        ),
    )
    if english_accent == "Default":
        tld = "com"
    elif english_accent == "India":
        tld = "co.in"
    elif english_accent == "United Kingdom":
        tld = "co.uk"
    elif english_accent == "United States":
        tld = "com"
    elif english_accent == "Canada":
        tld = "ca"
    elif english_accent == "Australia":
        tld = "com.au"
    elif english_accent == "Ireland":
        tld = "ie"
    elif english_accent == "South Africa":
        tld = "co.za"
        
        
    def text_to_speech(input_language, output_language, text, tld):
        translation = translator.translate(text, src=input_language, dest=output_language)
        trans_text = translation.text
        tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
        try:
            my_file_name = text[0:20]
        except:
            my_file_name = "audio"
        tts.save(f"temp/{my_file_name}.mp3")
        return my_file_name, trans_text
    display_output_text = st.checkbox("Display output text")

    if st.button("convert"):
        result, output_text = text_to_speech(input_language, output_language, text, tld)
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Your audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)

        if display_output_text:
            st.markdown(f"## Output text:")
            st.write(f" {output_text}")

    def remove_files():
        mp3_files = "temp/*mp3"
        try:
            if len(mp3_files) != 0:
                for f in mp3_files:
                    os.remove(f)
                    print("Deleted ", f)
        except PermissionError:
            st.write(" ")

    
    page_bg_img = f"""
    <style>
    .st-bx{{
        border:2px solid #e8d2c3;
    }}
    *{{
    color:black;
     }}
     
    [data-testid="stAppViewContainer"] > .main {{
    background-color: #f3f0ec;  
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    .st-cd{{
         border:2px solid #e8d2c3;
    }}
    .css-po3vlj{{
         border:2px solid #e8d2c3;
        
    }}
    [data-testid="stHeader"]{{
        background-color:rgba(0,0,0,0);
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.header("(OR)")
    st.title(" Upload the pdf file in below")
    try:
        os.mkdir("temp")
    except:
        pass
    translator = Translator()
    
    pdf = st.file_uploader("Enter upload the pdf file from your device:",type=["pdf"])
    st.subheader("Click enter and than proceed")
    try:
        reading = PyPDF2.PdfFileReader(pdf)
        pages = reading.numPages

        for num in range(0,pages):
            choose = reading.getPage(num)
            text = choose.extractText()
        st.write(text)
        in_lang = st.selectbox(
            " select the Input language ",
            ("Afrikaans","Arabic","Bengali","Czech","Chinese","Danish","Dutch","English","Finnish","French","German","Greek","Hindi","Hungarian","Italian",  "Japanese", "Kannada","korean","Malayalam","Russian","Tamil","Telugu","Spanish","Urdu",))
        if in_lang == "Afrikaans":
            input_language = "af"
        elif in_lang == "Arabic":
            input_language = "ar"
        elif in_lang =="Bengali":
            input_language = "bn"
        elif in_lang =="Czech":
            input_language = "cs"
        elif in_lang =="Chinese":
            input_language = "zh-cn"
        elif in_lang =="Danish":
            input_language = "da"
        elif in_lang =="Dutch":
            input_language = "nl"
        elif in_lang =="English":
            input_language = "en"
        elif in_lang =="Finnish":
            input_language = "fi"
        elif in_lang =="French":
            input_language = "fr"
        elif in_lang =="German":
            input_language = "de"
        elif in_lang =="Greek":
            input_language = "el"
        elif in_lang =="Hindi":
            input_language = "hi"
        elif in_lang =="Hungarian":
            input_language = "hu"
        elif in_lang =="Italian":
            input_language = "it"
        elif in_lang =="Japanese":
            input_language = "ja"
        elif in_lang =="Kannada":
            input_language = "kn"
        elif in_lang =="korean":
            input_language = "ko"
        elif in_lang =="Malayalam":
            input_language = "ml"
        elif in_lang =="Russian":
            input_language = "ru"
        elif in_lang =="Tamil":
            input_language = "ta"
        elif in_lang =="Telugu":
            input_language = "te"
        elif in_lang =="Spanish":
            input_language = "es"
        elif in_lang =="Urdu":
            input_language = "ur"
        out_lang = st.selectbox(
            "Select the output language",
            ("Afrikaans","Arabic","Bengali","Czech","Chinese","Danish","Dutch","English","Finnish","French","German","Greek","Hindi","Hungarian","Italian",  "Japanese", "Kannada","korean","Malayalam","Russian","Tamil","Telugu","Spanish","Urdu"),
        )
        if out_lang == "Afrikaans":
            output_language = "af"
        elif out_lang == "Arabic":
            output_language = "ar"
        elif out_lang =="Bengali":
            output_language = "bn"
        elif out_lang =="Czech":
            output_language = "cs"
        elif out_lang =="Chinese":
            output_language = "zh-cn"
        elif out_lang =="Danish":
            output_language = "da"
        elif out_lang =="Dutch":
            output_language = "nl"
        elif out_lang =="English":
            output_language = "en"
        elif out_lang =="Finnish":
            output_language = "fi"
        elif out_lang =="French":
            output_language = "fr"
        elif out_lang =="German":
            output_language = "de"
        elif out_lang =="Greek":
            output_language = "el"
        elif out_lang =="Hindi":
            output_language = "hi"
        elif out_lang =="Hungarian":
            output_language = "hu"
        elif out_lang =="Italian":
            output_language = "it"
        elif out_lang =="Japanese":
            output_language = "ja"
        elif out_lang =="Kannada":
            output_language = "kn"
        elif out_lang =="korean":
            output_language = "ko"
        elif out_lang =="Malayalam":
            output_language = "ml"
        elif out_lang =="Russian":
            output_language = "ru"
        elif out_lang =="Tamil":
            output_language = "ta"
        elif out_lang =="Telugu":
            output_language = "te"
        elif out_lang =="Spanish":
            output_language = "es"
        elif out_lang =="Urdu":
            output_language = "ur"
        english_accent = st.selectbox(
            "Select your english",
            (
               "Default",
                "India",
                "United Kingdom",
                "United States",
                "Canada",
                "Australia",
                "Ireland",
                "South Africa",
            ),)
        if english_accent == "Default":
            tld = "com"
        elif english_accent == "India": 
            tld = "co.in"
        elif english_accent == "United Kingdom":
            tld = "co.uk"
        elif english_accent == "United States":
            tld = "com"
        elif english_accent == "Canada":
            tld = "ca"
        elif english_accent == "Australia":
            tld = "com.au"
        elif english_accent == "Ireland":
            tld = "ie"
        elif english_accent == "South Africa":
            tld = "co.za"
            
            
        def text_to_speech(input_language, output_language, text, tld):
            translation = translator.translate(text, src=input_language, dest=output_language)
            trans_text = translation.text
            tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
            try:
                my_file_name = text[0:20]
            except:
                my_file_name = "audio"
            tts.save(f"temp/{my_file_name}.mp3")
            return my_file_name, trans_text

        display_output_text = st.checkbox("Display output ")
        if st.button("convert here"):
            result, output_text = text_to_speech(input_language, output_language, text, tld)
            audio_file = open(f"temp/{result}.mp3", "rb")
            audio_bytes = audio_file.read()
            st.markdown(f"## Your audio:")
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
            
            if display_output_text:
                st.markdown(f"## Output text:")
                st.write(f" {output_text}")
                
        def remove_files(n):
                mp3_files = glob.glob("temp/*mp3")
                if len(mp3_files) != 0:
                    now = time.time()
                    n_days = n * 86400
                    for f in mp3_files:
                        if os.stat(f).st_mtime < now - n_days:
                            os.remove(f)
                            print("Deleted ", f)
    except:
        pass
