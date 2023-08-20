
import torch
import streamlit as st
import pandas as pd
import numpy as np
import os

s = None
st.header("Welcome to BIM team")
st.sidebar.subheader("About BIM team")
st.sidebar.subheader("Check overlap")
st.sidebar.subheader("Contact")
col1, col2,col3 = st.columns(3)


click = st.button("Click me to predict")

if click:
    with st.spinner("Wait a minute..."):
        ###################
        folder_path = './runs/detect'
        subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
        if len(subfolders)>0:
            for subfolder in subfolders:
                try:
                    if subfolder=='exp':
                        os.remove(subfolder)  # Remove the subfolder
                        print(f"Removed subfolder: {subfolder}")
                except Exception as e:
                    print(f"Failed to remove subfolder: {subfolder}. Error: {e}")

        
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='./runs/train/exp/weights/best.pt', force_reload=True)
        results = model('./data/images/pre1.jpg',)
        results.save(save_dir='./',exist_ok=True)
        
        ###################
        st.success("Process complete!")

        clickOK = st.button("OK")
        if clickOK:
            if s is not None:
                s.empty()