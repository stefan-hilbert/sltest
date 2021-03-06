import streamlit as st
import pandas as pd

import logging

st.title("SL Demonstrator")

uploaded_file = st.file_uploader(
    "upload data",
    # type=['tdms'],
    type=['csv'],
    accept_multiple_files=False,
    key="data_uploader",
    help=None)

if uploaded_file is not None:

    st.write("reading data...")
    logging.info(f"reading data...")
    # data = TdmsFile(uploaded_file)
    data = pd.read_csv(uploaded_file)
    logging.info(f"data read.")
    
    st.write("displaying data...")
    logging.info(f"displaying data...")
    st.write(data)
