import os
import random
import requests
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st


st.set_page_config(page_title="Levana - Lockdrop Calculator",\
        page_icon=Image.open(requests.get('https://raw.githubusercontent.com/IncioMan/levana_lockdrop/master/images/favicon.ico',stream=True).raw),\
        layout='wide')

st.markdown(f"""
<div class="banner" style=\"width: 100%;padding-bottom:48px;float: left;z-index: 1;display: flex;justify-content:center;\">
    <a href="https://app.neb.money/">
        <img src="https://raw.githubusercontent.com/IncioMan/levana_lockdrop/master/images/logo.svg" style=\"margin-left: 5px;\" width=\"200px\">
    </a>
</div>
""", unsafe_allow_html=True)

# main body
col0,col1,col3,col6,col9,col12,col15,col18,col00 = st.columns([0.5,2,2,2,2,2,2,2,1])
with col1:
    st.markdown("##### My Lockup", unsafe_allow_html=True)
with col3:
    st.number_input('3 Months', key='ml3m', step=10, min_value=0)
with col6:
    st.number_input('6 Months', key='ml6m', step=10, min_value=0)
with col9:
    st.number_input('9 Months', key='ml9m', step=10, min_value=0)
with col12:
    st.number_input('12 Months', key='ml12m', step=10, min_value=0)
with col15:
    st.number_input('15 Months', key='ml15m', step=10, min_value=0)
with col18:
    st.number_input('18 Months', key='ml18m', step=10, min_value=0)
col0,col1,col3,col6,col9,col12,col15,col18,col00 = st.columns([0.5,2,2,2,2,2,2,2,1])
with col1:
    st.markdown("##### Everyone elses", unsafe_allow_html=True)
with col3:
    st.number_input('3 Months', key='ee3m', step=10, min_value=0)
with col6:
    st.number_input('6 Months', key='ee6m', step=10, min_value=0)
with col9:
    st.number_input('9 Months', key='ee9m', step=10, min_value=0)
with col12:
    st.number_input('12 Months', key='ee12m', step=10, min_value=0)
with col15:
    st.number_input('15 Months', key='ee15m', step=10, min_value=0)
with col18:
    st.number_input('18 Months', key='ee18m', step=10, min_value=0)

st.markdown("""
    <style>
    .css-1nnn0hm input {
        text-align: center;
    }
    .st-cl {
        background: transparent;
        border: none;
        text-align: center;
    }
    .st-ck {
        background: transparent;
        border: none;
        border-bottom: solid;
        border-radius: 0px;
        text-align: center;
    }
    .st-bv{
        background:none;
    }
    .st-bw{
        border: none;
        border-bottom: solid;
        border-radius: 0px;
        background:none;
    }
    .st-bt{
        border: none;
        border-bottom: solid;
        border-radius: 0px;
        background:none;
    }
    .css-1nnn0hm {
        display: flex;
        flex-flow: row nowrap;
        -webkit-box-align: center;
        align-items: center;
        background: transparent;
    }
    .css-u3o8cc {
        display: none;
    }
    .css-18l8pcm{
        justify-content: center;
    }
    .css-hamoxu{
        display: flex;
        justify-content: center;
    }
    .css-ryg8tv{
        display: flex;
    }
    .css-wttdo9{
        justify-content: center;
    }
    .css-1uubtht{
         justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)
