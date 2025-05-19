import streamlit as st

USER_CREDENTIALS = {
    "user1": "password1",
    "admin": "admin123",
    "test": "test123"
}

st.title(" 🔐 Login Page")

username=st.text_input("Username")
password=st.text_input("Password ",type="password")

if st.button("Login"):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username]==password:
        st.success(f'Welcome,{username} !')
        st.balloons()

        st.write("🎉 You have access to the app content now!")
        st.image("https://picsum.photos/400", caption="Random image for logged-in users")
    else:
        st.error("invalid username or password ")    