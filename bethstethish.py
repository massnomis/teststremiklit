import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

st.set_page_config(
        layout="wide",
        page_title="Ex-stream-ly Cool App",
        page_icon="🧊",
)
st.title("bETH back to ETH")

st.markdown(
    """
So bETH is now on Terra. Nice! Lets look into the numbers
    """
)

query_id = "770c4049-a3b7-45b0-9977-88df8f197ed9"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df)

st.markdown(
    """
Lets start with the the hourly shuttle sums of Terra to ETH (bETH to stETH)
    """
)



linechart = px.scatter(
    df,
    x="DAYZ",
    y=["SUM(AMOUNTZ)"]  
)
st.plotly_chart(linechart, use_container_width=True)

st.markdown(
    """
Average and Median amounts
    """
)

linechart = px.scatter(
    df,
    x="DAYZ",
    y=["AVG(AMOUNTZ)","MEDIAN(AMOUNTZ)"]  
)
st.plotly_chart(linechart, use_container_width=True)



st.subheader('median and average')



linechart = px.bar(
    df,
    x="DAYZ",
    y=["WHOMZ_COUNT"]
)
st.plotly_chart(linechart, use_container_width=True)




st.subheader('tx a day')
linechart = px.bar(
    df,
    x="DAYZ",
    y=["TX_COUNT"]
  
)
st.plotly_chart(linechart, use_container_width=True)





st.title("ETH to Terra bETH")

st.markdown(
    """
The following are bETH deposits to Terra during the same time period (from ETH).
    """
)
st.subheader('bETH SENT TO TERRA SUM')
linechart = px.scatter(
    df,
    x="DAYZZ",
    y=["BETHSHUTTLESUM"]
  
)
st.plotly_chart(linechart, use_container_width=True)



st.markdown(
    """
MEDIAN and AVERAGE
    """
)



linechart = px.scatter(
    df,
    x="DAYZZ",
    y=["BETHSHUTTLEAVG","BETHSHUTTLEMED" ]
  
)
st.plotly_chart(linechart, use_container_width=True)

st.markdown(
    """
Unique senders a day and total sends
    """
)



linechart = px.scatter(
    df,
    x="DAYZZ",
    y=["COUNTSENDERBETH","COUNTTX_IDBETHETH" ]
)
st.plotly_chart(linechart, use_container_width=True)


st.markdown(
    """
LETS LOOK AT THE STETH PRICE ON CURVE AT THE SAME TIME
    """
)


query_id = "7a5f2ddb-e8f0-4f90-aee7-220264b8f958"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df)


st.markdown(
    """
Price of stETH to ETH
    """
)

linechart = px.line(
    df,
    x="DAYZZZ",
    y=
    [
    "AVG(STETH_WETH)", 
    "AVG(MADAYLSTETH_WETH)" ,
    "AVG(MA3DAYLSTETH_WETH)",
    "AVG(MAWEEKLSTETH_WETH)"
    ] 
)
st.plotly_chart(linechart, use_container_width=True)






query_id = "7a5f2ddb-e8f0-4f90-aee7-220264b8f958"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)  




st.markdown(
    """
VOLUME ON CURVE FOR THE SAME THING
    """
)




linechart = px.bar(
    df,
    x="DAYZZZ",
    y=
    [
    "AVG(INSUMSTETH)",
    "AVG(OUTSUMWETH)",
    "AVG(OUTSUMSTETH)",
    "AVG(INSUMWETH)"
    ] 
)
st.plotly_chart(linechart, use_container_width=True)

st.markdown(
    """
CURVE INVARIANT AS WELL
    """
)



linechart = px.scatter(
    df,
    x="DAYZZZ",
    y=
    [
    "AVG(INV)"
    ] 
)
st.plotly_chart(linechart, use_container_width=True)

