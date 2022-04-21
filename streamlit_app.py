import os
import random
import requests
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt

def simulation_apr_chart(df, color='redpurple'):
    ust_duration_chart = alt.Chart(df).mark_bar().encode(
                        y=alt.Y(field="ROI", type="quantitative"),
                        x=alt.X(field="Lockup period", type="nominal", axis=alt.Axis(labelAngle=0),
                                sort=['3 months','6 months',
                                      '9 months','12 months',
                                      '15 months','18 months']),
                        color=alt.Color(field="Lockup period", type="nominal",
                                sort=['3 months','6 months',
                                      '9 months','12 months',
                                      '15 months','18 months'],
                                scale=alt.Scale(scheme=color),
                                legend=None),
                            tooltip=["ROI x","Lockup period"]
                        )
    text = ust_duration_chart.mark_text(
            align='center',
            baseline='middle',
            dy=-15,  # Nudges text to right so it doesn't appear on top of the bar
            fontSize=25
        ).encode(
            text='ROI x:N'
        )

    return (ust_duration_chart + text).properties(width=400).configure_view(strokeOpacity=0)


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

my_percent_weighted = my_total_deposit_ust_weighted / total_deposit_ust_weighted
my_lvn_tokens = my_percent_weighted * total_lvn

col0, col1, col36, col912, col2, col00 = st.columns([0.5, 2,4,4,8, 1])
with col36:
    lvn_price = st.number_input(
        "LVN Price",
        key="lvnprice",
        value=1.0,
        step=0.1,
        min_value=0.1,
    )
    st.text("")
    st.metric(
        "Your LVN Tokens",
        value=f"{my_lvn_tokens:,.0f}",
    )
    st.text("")
    st.metric("Your Deposit (UST)", value=f"${my_total_deposit_ust:,.0f}")

my_lvn_tokens_ust = my_lvn_tokens * lvn_price
try:
    my_roi = my_lvn_tokens_ust / my_total_deposit_ust
except ZeroDivisionError:
    my_roi = 0

with col912:
    st.text("")
    st.metric(
        "Your LVN Tokens (UST)",
        value=f"${my_lvn_tokens_ust:,.0f}",
    )
    st.text("")
    st.metric("Total Deposit (UST)", value=f"${total_deposit_ust:,.0f}")
    st.text("")
    st.text("")
    st.metric(
        "Your ROI",
        value=f"{my_roi:,.2f}x",
    )


with col2:
    total_points = total_deposit_ust_weighted
    points = [(ml3m+ee3m) * weights[0],
    (ml6m+ee6m) * weights[1],
    (ml9m+ee9m) * weights[2],
    (ml12m+ee12m) * weights[3],
    (ml15m+ee15m) * weights[4],
    (ml18m+ee18m) * weights[5]]
    print(points, total_deposit_ust_weighted, sum(points))
    roi =[((pp/total_points)*total_lvn*lvn_price)/(pp/weights[i]) for i,pp in enumerate(points)]
    df = pd.DataFrame([[round(roi[0]),'3 mmonths',f"{round(roi[0],2)}x"],
            [round(roi[1]),'6 mmonths',f"{round(roi[1],2)}x"],
            [round(roi[2]),'9 mmonths',f"{round(roi[2],2)}x"],
            [round(roi[3]),'12 mmonths',f"{round(roi[3],2)}x"],
            [round(roi[4]),'15 mmonths',f"{round(roi[4],2)}x"],
            [round(roi[5]),'18 mmonths',f"{round(roi[5],2)}x"],], columns=['ROI','Lockup period','ROI x'])
    st.altair_chart(simulation_apr_chart(df), use_container_width=True)


st.markdown(
    """
    <style>
    .block-container
    {
        padding-bottom: 0rem;
        padding-top: 4rem;
    }
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
    [data-testid="stHeader"]{
        display:none
    }    
    </style>
    """,
    unsafe_allow_html=True,
)
