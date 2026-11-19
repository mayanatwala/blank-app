import streamlit as st
st.title("🎈 Mayana Twala Hiking club")
st.header("Explore Nature With Us")
st.subheader("weekend is for Hiking")
st.write("One journey, one team, endless adventures! ❤️,")
st.image("IMG_9335.jpeg")
st.markdown("2km 5km 10km")
st.image("IMG_9156.jpeg")
st.code ("for Booking")
name = st.text_input("What is your Name")
surname = st.text_input("what is your surname")
address = st.text_input("home address")
selected = main_menu(
        menu_title="Main Menu",
        options=["Home", "About", "Services", "Contact"],
        icons=["house", "person", "gear", "envelope"],
        menu_icon="cast",
        default_index=0
    )

if selected == "Home":
    st.title("Welcome Home")

elif selected == "About":
    st.title("About Us")

elif selected == "Services":
    st.title("Our Services")

elif selected == "Contact":
    st.title("Contact Us")
