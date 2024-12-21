# Import libraries
import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

import plotly.graph_objects as go

# matplotlib dark mode
plt.style.use('dark_background')

# styling
plt.rcParams.update({
    "font.size": 10
})

# App Description
with st.expander('About this app'):
    st.markdown('**What can this app do?**')
    st.info('This app shows the data analysis and ML models for SRAMA II dataset.')
    st.markdown('**How to use the app?**')
    st.warning('To engage with the app:\n1. Select features of your interest in the drop-down selection box.\n2. Select the target.\n3. Specify the number of plots and configure each plot.\n4. The result will generate side-by-side plots.')

st.sidebar.header('Filter Tools')
core_path = "asteroid_taxonomy/data"
asteroids_df = pd.read_pickle(os.path.join(core_path, "lvl2/asteroids.pkl"))


# Create a dropdown menu for target selector in the sidebar
asteroids_df_col_list = asteroids_df.Main_Group.unique()
asteroids_df_col_selection = st.sidebar.multiselect("Select target", asteroids_df_col_list)

asteroids_filtered_df = asteroids_df[asteroids_df.Main_Group.isin(asteroids_df_col_selection)]

with st.expander("Filtered by target"):
    st.write(asteroids_filtered_df)

with st.sidebar.expander(f'Configure Plot'):
    # Plot-specific configuration
    alpha_scatter = st.slider(f"Select transparency of points for Plot", min_value=0.0, max_value=1.0, value=0.05, key=f"alpha_scatter")
    color = st.color_picker(f"Select color of points for Plot", "#759675", key=f"color_")

with st.expander("EDA plots"):

    if 'asteroids_filtered_df' in locals() and not asteroids_filtered_df.empty:

        fig, ax = plt.subplots()


        for _, row in asteroids_filtered_df.iterrows():
            ax.plot(
                row["SpectrumDF"]["Wavelength_in_microm"],
                row["SpectrumDF"]["Reflectance_norm550nm"],
                color=color,
                alpha=alpha_scatter
            )   # transparencey and opacity of the graph plots

        ax.set_xlabel("Wavelength in micrometer")
        ax.set_ylabel("Reflectance_norm550nm")

        ax.grid(linestyle="dashed", alpha = 0.3)


        st.pyplot(fig)

    else:
        st.warning("No data available to plot")
