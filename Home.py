import requests
import streamlit as st
import gspread as gs
from PIL import Image
from streamlit_lottie import st_lottie
import base64

# ---- TITLE & PAGE ICON ----
st.set_page_config(page_title="IAU - Ormoc Air Portal", page_icon="🛬", layout="wide")

# streamlit_app.py
# ---- ASSET SETUP ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json


# ---- Use Local CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_plane = "https://lottie.host/5a4b9f88-85ab-402a-b356-a44afd4239b5/QGPRPCbUny.json"
img_IAUlogo = Image.open("images/IAUlogo.png")
lottie_files = "https://lottie.host/ee518360-2650-4b44-9501-e6b1a3cf3e05/dmGsOjVNTg.json"
img_OrmocAirlogo = Image.open("images/OrmocAirlogo.png")
#gc = gs.service_account(filename='.streamlit/ormoc-air-08dff0666421.json')
#sh = gc.open("Sample-Maintenance-Log")
#worksheet = sh.sheet1


# ---- HEADER SECTION ----
with st.container():
    left_column, middle_column, right_column = st.columns([1, 2, 1])
    with left_column:
        #st.image(img_IAUlogo, use_column_width="auto")
        st.markdown(
            """<a href="https://iau.com.ph/">
            <img src="data:image/png;base64,{}" width="300">
            </a>""".format(
                base64.b64encode(open("images/IAUlogo.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with middle_column:
        st.subheader("IAU - Ormoc Air Portal")
        st.title("Seamless Maintenance Log and Inventory Portal")
        st.write("This page is used to communicate maintenance logs for aircrafts owned by IAU and Ormoc Air")
        #st.write("[IAU >](https://iau.com.ph/)")
        #st.write("[Ormoc Air >](https://www.facebook.com/OrmocAir/)")

    with right_column:
        #st.image(img_OrmocAirlogo, use_column_width="auto")
        st.markdown(
            """<a href="https://www.facebook.com/OrmocAir/">
            <img src="data:image/png;base64,{}" width="300">
            </a>""".format(
                base64.b64encode(open("images/OrmocAirlogo.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )


# ---- DESCRIPTION ----
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:

            st.header("What IAU does")
            st.write("")
            st.write(
                """
                At Indiana Aerospace University, we’re committed to excellence in education and holistic development. 
                Our mission is to provide top-tier basic and tertiary education, fostering academic prowess and universal 
                values. We produce globally competitive graduates with a lifelong dedication to aerospace knowledge and skills.
                """
            )
            st.write("##")

            st.header("What Ormoc Air does")
            st.write("")
            st.write(
                """
                Ormoc Air is a Private Plane Charter Company owned by Indiana Aerospace University.
                It is also where student pilots of Indiana Aerospace University grind their hours.
                Ormoc Air operates as a sister company of Indiana Aerospace University.
                """
            )

    with right_column:
        st_lottie(lottie_plane, height=400, key="plane")


# ---- Projects ----
with st.container():
    st.write("----")
    st.header("What does this Portal do?")
    st.write("##")

    image_column, text_column = st.columns((1, 2))

    with image_column:
        st_lottie(lottie_files, height=400, key="files")

    with text_column:
        st.subheader("Maintenance Logging")
        st.write(
            """
            Transferring Maintenance Logs from Ormoc Air to Indiana Aerospace University.
            Maintenance Logs are sensitive information and must be transferred safely.
            Encryption is crucial with this type of information.
            """
        )
        st.markdown("[Watch Video...](https://www.facebook.com/share/v/gWSQrxopAubkreeK/)")


# ---- Contact ----
with st.container():
    st.write("----")
    st.header("For concerns please contact")
    st.write("")
    contact_form = """
    <form action="https://formsubmit.co/9776a830cb57cd3c08ef15538d71269e" method="POST">
        <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()