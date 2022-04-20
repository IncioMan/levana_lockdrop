import os
import random
import requests
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st


st.set_page_config(
    page_title="Levana - Lockdrop Calculator",
    page_icon=Image.open(
        requests.get(
            "https://raw.githubusercontent.com/IncioMan/levana_lockdrop/master/images/favicon.ico",
            stream=True,
        ).raw
    ),
    layout="wide",
)

st.markdown(
    f"""
    <div class="banner" style=\"width: 100%;padding-bottom:48px;float: left;z-index: 1;display: flex;justify-content:center;\">
        <a href="https://www.levana.finance/">
            <img src="https://raw.githubusercontent.com/IncioMan/levana_lockdrop/master/images/logo.svg" style=\"margin-left: 5px;\" width=\"200px\">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# main body
col0, col1, col3, col6, col9, col12, col15, col18, col00 = st.columns(
    [0.5, 2, 2, 2, 2, 2, 2, 2, 1]
)
with col1:
    st.markdown("##### My Lockup", unsafe_allow_html=True)
with col3:
    ml3m = st.number_input("3 Months", key="ml3m", step=10, min_value=0)
with col6:
    ml6m = st.number_input("6 Months", key="ml6m", step=10, min_value=0)
with col9:
    ml9m = st.number_input("9 Months", key="ml9m", step=10, min_value=0)
with col12:
    ml12m = st.number_input("12 Months", key="ml12m", step=10, min_value=0)
with col15:
    ml15m = st.number_input("15 Months", key="ml15m", step=10, min_value=0)
with col18:
    ml18m = st.number_input("18 Months", key="ml18m", step=10, min_value=0)
col0, col1, col3, col6, col9, col12, col15, col18, col00 = st.columns(
    [0.5, 2, 2, 2, 2, 2, 2, 2, 1]
)
with col1:
    st.markdown("##### Everyone elses", unsafe_allow_html=True)
with col3:
    ee3m = st.number_input(
        "3 Months", value=3_000_000, key="ee3m", step=10, min_value=0
    )
with col6:
    ee6m = st.number_input("6 Months", value=250_000, key="ee6m", step=10, min_value=0)
with col9:
    ee9m = st.number_input("9 Months", value=250_000, key="ee9m", step=10, min_value=0)
with col12:
    ee12m = st.number_input(
        "12 Months", value=250_000, key="ee12m", step=10, min_value=0
    )
with col15:
    ee15m = st.number_input(
        "15 Months", value=250_000, key="ee15m", step=10, min_value=0
    )
with col18:
    ee18m = st.number_input(
        "18 Months", value=10_000_000, key="ee18m", step=10, min_value=0
    )

st.text("")
st.text("")

weights = [1, 2.8, 5.2, 8.00, 11.20, 14.70]
col0, col1, col3, col6, col9, col12, col15, col18, col00 = st.columns(
    [0.5, 2, 2, 2, 2, 2, 2, 2, 1]
)
with col1:
    st.markdown("##### Weight", unsafe_allow_html=True)
with col3:
    st.text(weights[0])
with col6:
    st.text(weights[1])
with col9:
    st.text(weights[2])
with col12:
    st.text(weights[3])
with col15:
    st.text(weights[4])
with col18:
    st.text(weights[5])

st.text("")
st.text("")

total_deposit_ust = (
    ml3m
    + ml6m
    + ml9m
    + ml12m
    + ml15m
    + ml18m
    + ee3m
    + ee6m
    + ee9m
    + ee12m
    + ee15m
    + ee18m
)

my_total_deposit_ust = ml3m + ml6m + ml9m + ml12m + ml15m + ml18m

my_total_deposit_ust_weighted = (
    ml3m * weights[0]
    + ml6m * weights[1]
    + ml9m * weights[2]
    + ml12m * weights[3]
    + ml15m * weights[4]
    + ml18m * weights[5]
)
others_total_deposit_ust_weighted = (
    ee3m * weights[0]
    + ee6m * weights[1]
    + ee9m * weights[2]
    + ee12m * weights[3]
    + ee15m * weights[4]
    + ee18m * weights[5]
)
total_deposit_ust_weighted = (
    my_total_deposit_ust_weighted + others_total_deposit_ust_weighted
)

total_lvn = 35_000_000

st.text("")
st.text("")
st.text("")
st.text("")

col0, col1, col36, col912, col1518, col3, col00 = st.columns([0.5, 2, 4, 4, 4, 4, 1])
with col36:
    lvn_price = st.number_input(
        "LVN Price",
        key="lvnprice",
        value=1.0,
        step=0.1,
        min_value=0.1,
    )

my_percent_weighted = my_total_deposit_ust_weighted / total_deposit_ust_weighted

my_lvn_tokens = my_percent_weighted * total_lvn

my_lvn_tokens_ust = my_lvn_tokens * lvn_price

try:
    my_roi = my_lvn_tokens_ust / my_total_deposit_ust
except ZeroDivisionError:
    my_roi = 0
with col912:
    st.metric("Your Deposit (UST)", value=f"${my_total_deposit_ust:,.0f}")

with col1518:
    st.metric("Total Deposit (UST)", value=f"${total_deposit_ust:,.0f}")

with col3:
    st.metric(
        "Total Weighted Deposit (UST)",
        value=f"${total_deposit_ust_weighted:,.0f}",
    )

st.text("")
st.text("")

col0, col1, col36, col9, col1215, col18, col00 = st.columns([0.5, 2, 4, 4, 4, 4, 1])
with col36:
    st.metric(
        "Your LVN Tokens",
        value=f"{my_lvn_tokens:,.0f}",
    )
with col9:
    st.metric(
        "Your LVN Tokens (UST)",
        value=f"${my_lvn_tokens_ust:,.0f}",
    )

with col1215:
    st.metric(
        "Your Share Of Weighted Deposit",
        value=f"{my_percent_weighted*100:,.3f}%",
    )

with col18:

    st.metric(
        "Your ROI",
        value=f"{my_roi:,.2f}x",
    )


#
total_lvn_tokens = 35_000_000

st.markdown(
    """
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
    .css-1ht1j8u{
        font-family: sans-serif;
        text-align: center;
    }
    .css-18l8pcm{
        justify-content: center;
        color: #e085d9;
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
    .css-183lzff{
        text-align: center;
        color: #e085d9;
    }
    [data-testid="stMetricLabel"]{
        font-size: 15px
    }
    [data-testid="stMetricValue"]{
        font-size: 20px
    }
    </style>
    """,
    unsafe_allow_html=True,
)
