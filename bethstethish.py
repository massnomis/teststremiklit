import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

# Basic setup and app layout
st.set_page_config(
        layout="wide",
        page_title="Ex-stream-ly Cool App",
        page_icon="🧊",
)
st.title("bETH back to ETH")
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
st.caption('This is a small text')


query_id = "770c4049-a3b7-45b0-9977-88df8f197ed9"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)


st.write(df)

linechart = px.line(
    df,
    x="DAYZ",
    y=["SUM(AMOUNTZ)"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZ",
    y=["AVG(AMOUNTZ)"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZ",
    y=["MEDIAN(AMOUNTZ)"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZ",
    y=["WHOMZ_COUNT"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZ",
    y=["TX_COUNT"]
  
)
st.plotly_chart(linechart, use_container_width=True)


#cc127604-ba31-4ce6-a78d-3b4e0e7e4e84

st.title("ETH to Terra bETH")
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
st.caption('This is a small text')
# DAYZZ	
# COUNTTX_IDBETHETH	
# CDOABETHETH	
# BETHSHUTTLESUM	
# BETHSHUTTLEAVG
# BETHSHUTTLEMED
linechart = px.line(
    df,
    x="DAYZZ",
    y=["BETHSHUTTLESUM"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZZ",
    y=["BETHSHUTTLEAVG"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZZ",
    y=["BETHSHUTTLEMED"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZZ",
    y=["CDOABETHETH"]
  
)
st.plotly_chart(linechart, use_container_width=True)
linechart = px.line(
    df,
    x="DAYZZ",
    y=["COUNTTX_IDBETHETH"] 
)
st.plotly_chart(linechart, use_container_width=True)

st.title("stETH Prices on Ethereum")
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
st.caption('This is a small text')

query_id = "7a5f2ddb-e8f0-4f90-aee7-220264b8f958"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
#DAYZZZ STETH_WETH MADAYLWETH_STETH MA3DAYLWETH_STETH INV MADAYLSTETH_WETH MA3DAYLSTETH_WETH MAWEEKLSTETH_WETH WETH_STETH

st.write(df)
linechart = px.line(
    df,
    x="DAYZZZ",
    y=
    [
    "AVG(STETH_WETH)", 
    "AVG(MADAYLSTETH_WETH)" ,
    "AVG(MA3DAYLSTETH_WETH)",
    "AVG(MAWEEKLSTETH_WETH)"
    # "AVG(MADAYLWETH_STETH)",  
    # "AVG(MA3DAYLWETH_STETH)",  
    # "AVG(MADAYLSTETH_WETH)" ,
    # "AVG(MA3DAYLSTETH_WETH)	",
    # "AVG(MAWEEKLSTETH_WETH)",
    # "AVG(WETH_STETH)"
    ] 
)
st.plotly_chart(linechart, use_container_width=True)


st.subheader('My sub')




query_id = "7a5f2ddb-e8f0-4f90-aee7-220264b8f958"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
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



