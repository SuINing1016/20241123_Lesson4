from tools import taipei
import streamlit as st
@st.dialog('Cause your vote')
def vote(error):
    st.write(error)
try:
    youbike_data:list[dict]=taipei.get_youbikes()
except Exception as error:
    print(error)
    st.stop()
else:
    st.write
    (youbike_data)


