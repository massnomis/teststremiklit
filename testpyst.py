import streamlit as st
!pip import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

# Basic setup and app layout
st.set_page_config(layout="wide")
st.title("AAVE VERSION MIGRATION")
st.markdown(
    """
    YEET
    """
)


st.header("DAI MIGRATION")
# load tax query into pandas
query_id = "d507c67b-9962-4308-a634-1b66df53ad4f"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df)
st.write("TVL")

dai1 = px.bar(
    df,
    x="DATE",
    y=["AMM_TVL_SHARE",	"VONE_TVL_SHARE","VTWO_TVL_SHARE"]
)
st.plotly_chart(dai1, use_container_width=True)

st.write("SUPPLY")

dai2 = px.bar(
    df,
    x="DATE",
    y=["AMM_SUPPLY_SHARE",	"VONE_SUPPLY_SHARE","VTWO_SUPPLY_SHARE"]
)
st.plotly_chart(dai2, use_container_width=True)

st.header("USDT")
# load tax query into pandas
query_id = "07ed5e15-9d63-458e-bf7f-c21b5c449e8a"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df)
st.write("TVL")

USDT1 = px.bar(
    df,
    x="DATE",
    y=["AMM_TVL_SHARE",	"VONE_TVL_SHARE","VTWO_TVL_SHARE"]
)

st.plotly_chart(USDT1, use_container_width=True)
st.write("SUPPLY")

USDT2 = px.bar(
    df,
    x="DATE",
    y=["AMM_SUPPLY_SHARE",	"VONE_SUPPLY_SHARE","VTWO_SUPPLY_SHARE"]
)
st.plotly_chart(USDT2, use_container_width=True)




st.header("USDC MIGRATION")
# load tax query into pandas
query_id = "c9ec4820-97ac-4ca9-8014-d7e2d4e3e3c3"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df)
st.write("TVL")

USDC1 = px.bar(
    df,
    x="DATE",
    y=["AMM_TVL_SHARE",	"VONE_TVL_SHARE","VTWO_TVL_SHARE"]
)

st.plotly_chart(USDC1, use_container_width=True)
st.write("SUPPLY")

USDC2 = px.bar(
    df,
    x="DATE",
    y=["AMM_SUPPLY_SHARE",	"VONE_SUPPLY_SHARE","VTWO_SUPPLY_SHARE"]
)
st.plotly_chart(USDC2, use_container_width=True)
