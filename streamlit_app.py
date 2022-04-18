import os
import random
import requests
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import seaborn as sns
from replit.database import Database


st.set_page_config(page_title="Levana - Lockdrop Calculator",\
        page_icon=Image.open(requests.get('https://raw.githubusercontent.com/IncioMan/levana_lockdrop/master/images/favicon.ico',stream=True).raw),\
        layout='wide')

st.markdown(f"""
<div class="banner" style=\"max-width: 200px;float: left;z-index: 1; padding-top: 20px;\">
    <a href="https://app.neb.money/">
        <img src="https://raw.githubusercontent.com/IncioMan/levana_lockdrop/master/images/logo.svg" style=\"margin-left: 5px;\" width=\"200px\">
    </a>
</div>
""", unsafe_allow_html=True)

# main body
st.markdown("### My Lockup", unsafe_allow_html=True)
col0,col3,col6,col9,col12,col15,col18,col00 = st.columns([1,2,2,2,2,2,2,1])
with col3:
    st.number_input('3 Months', step=10, min_value=0)
with col6:
    st.number_input('6 Months', step=10, min_value=0)
with col9:
    st.number_input('9 Months', step=10, min_value=0)
with col12:
    st.number_input('12 Months', step=10, min_value=0)
with col15:
    st.number_input('15 Months', step=10, min_value=0)
with col18:
    st.number_input('18 Months', step=10, min_value=0)
st.markdown("### Everyone Elses", unsafe_allow_html=True)
col0,col3,col6,col9,col12,col15,col18,col00 = st.columns([1,2,2,2,2,2,2,1])
with col3:
    st.number_input('3 Months_', step=10, min_value=0)
with col6:
    st.number_input('6 Months_', step=10, min_value=0)
with col9:
    st.number_input('9 Months_', step=10, min_value=0)
with col12:
    st.number_input('12 Months_', step=10, min_value=0)
with col15:
    st.number_input('15 Months_', step=10, min_value=0)
with col18:
    st.number_input('18 Months_', step=10, min_value=0)