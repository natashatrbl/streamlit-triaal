import streamlit as st
import pandas as pd
import plotly_express as px

# Setting Page Config
st.set_page_config(layout='wide')

# Title Page
st.markdown('# Gapminder Dashboard')

df = pd.read_csv(r"D:\PROJECT TASHA\PYTHON\learning\streamlit\data\gapminder_data_graphs.csv")

# Section Top Computation
unique_years = df['year'].unique()

# Add Dropdown
selected_year = st.selectbox(
    label='Year',
    options=unique_years
)

# Metric Computation
df_plot = df[df['year'] == selected_year]
average_gdp = round(df_plot['gdp'].mean(),2)
average_life_exp = round(df_plot['life_exp'].mean(),2)
average_hdi = round(df_plot['hdi_index'].mean(), 2)

# Add Column
col1,col2,col3 = st.columns([1,1,1])
col1.metric(label='Average GDP', value=average_gdp)
col2.metric(label='Average Life Expectancy', value=average_life_exp)
col3.metric(label='Average HDI', value=average_hdi)

# Add Scatter Plot
title = 'GDP vs Life Expectancy for Year {}'.format(selected_year)
scatter_plot = px.scatter(
    data_frame=df_plot,
    x='gdp',
    y='life_exp',
    color='continent',
    title=title
)
st.plotly_chart(scatter_plot)

# Section Bottom
title_gdp = 'Distribution of GDP Across Continent for Year {}'.format(selected_year)
box_GDP = px.box(
    data_frame=df_plot,
    x='continent',
    y='gdp',
    title=title_gdp
)
histogram_GDP = px.histogram(
    data_frame=df_plot,
    x='gdp',
    nbins=9,
    title=title_gdp
)

title_lifeexp = 'Distribution of Life Expectancy Across Continent for Year {}'.format(selected_year)
box_lifeexp = px.box(
    data_frame=df_plot,
    x='continent',
    y='life_exp',
    title=title_lifeexp
)
histogram_lifeexp = px.histogram(
    data_frame=df_plot,
    x='life_exp',
    nbins=9,
    title=title_lifeexp
)

title_HDI = 'Distribution of HDI Across Continent for Year {}'.format(selected_year)
box_hdi = px.box(
    data_frame=df_plot,
    x='continent',
    y='hdi_index',
    title=title_HDI
)
histogram_hdi = px.histogram(
    data_frame=df_plot,
    x='hdi_index',
    nbins=9,
    title=title_HDI
)

# Add Bottom Column
col3,col4 = st.columns([1,1])
col3.plotly_chart(box_GDP)
col3.plotly_chart(box_lifeexp)
col3.plotly_chart(box_hdi)
col4.plotly_chart(histogram_GDP)
col4.plotly_chart(histogram_lifeexp)
col4.plotly_chart(histogram_hdi)

