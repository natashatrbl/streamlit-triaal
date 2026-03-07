import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(layout='wide')
st.title('Auto MPG Dashboard')

df = pd.read_csv(r"D:\PROJECT TASHA\PYTHON\learning\streamlit\data\clean_auto_mpg.csv")
unique_origin = list(df['origin'].unique())
unique_origin.sort()

unique_origin_str = ['Origin: ' + str(origin) for origin in unique_origin]
print(unique_origin_str)

# Add Tabs
tab1, tab2, tab3 = st.tabs([unique_origin_str[0], unique_origin_str[1], unique_origin_str[2]])

with tab1:
    st.subheader(unique_origin_str[0])
    # Metric Columns
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    df_tab = df[df['origin'] == unique_origin[0]]
    avg_mpg = round(df_tab['mpg'].mean(),1)
    avg_disp = round(df_tab['displacement'].mean(),1)
    avg_hp = round(df_tab['horsepower'].mean(),1)
    avg_wt = round(df_tab['weight'].mean(),1)
    col1.metric(label='Average MPG', value=avg_mpg)
    col2.metric(label='Average Displacement', value=avg_disp)
    col3.metric(label='Average Horsepower', value=avg_hp)
    col4.metric(label='Average Weight', value=avg_wt)

    # Scatter Plot & Histogram Columns
    col5,col6 = st.columns([4,1])

    scatter = px.scatter(
        data_frame=df_tab,
        x='weight',
        y='horsepower',
        size='displacement',
        hover_name='car name',
        color='cylinders',
        title='Weight vs HP for Cars from {}'.format(unique_origin[0])
    )
    col5.plotly_chart(scatter)

    histogram_plot = px.histogram(
        data_frame=df_tab,
        x='mpg',
        title='MPG Distribution'
    )
    col6.plotly_chart(histogram_plot)

with tab2:
    st.subheader(unique_origin_str[1])
    # Metric Columns
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    df_tab = df[df['origin'] == unique_origin[1]]
    avg_mpg = round(df_tab['mpg'].mean(),1)
    avg_disp = round(df_tab['displacement'].mean(),1)
    avg_hp = round(df_tab['horsepower'].mean(),1)
    avg_wt = round(df_tab['weight'].mean(),1)
    col1.metric(label='Average MPG', value=avg_mpg)
    col2.metric(label='Average Displacement', value=avg_disp)
    col3.metric(label='Average Horsepower', value=avg_hp)
    col4.metric(label='Average Weight', value=avg_wt)

    # Scatter Plot & Histogram Columns
    col5,col6 = st.columns([4,1])

    scatter = px.scatter(
        data_frame=df_tab,
        x='weight',
        y='horsepower',
        size='displacement',
        hover_name='car name',
        color='cylinders',
        title='Weight vs HP for Cars from {}'.format(unique_origin[1])
    )
    col5.plotly_chart(scatter)

    histogram_plot = px.histogram(
        data_frame=df_tab,
        x='mpg',
        title='MPG Distribution'
    )
    col6.plotly_chart(histogram_plot)

with tab3:
    st.subheader(unique_origin_str[2])
    # Metric Columns
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    df_tab = df[df['origin'] == unique_origin[2]]
    avg_mpg = round(df_tab['mpg'].mean(),1)
    avg_disp = round(df_tab['displacement'].mean(),1)
    avg_hp = round(df_tab['horsepower'].mean(),1)
    avg_wt = round(df_tab['weight'].mean(),1)
    col1.metric(label='Average MPG', value=avg_mpg)
    col2.metric(label='Average Displacement', value=avg_disp)
    col3.metric(label='Average Horsepower', value=avg_hp)
    col4.metric(label='Average Weight', value=avg_wt)

    # Scatter Plot & Histogram Columns
    col5,col6 = st.columns([4,1])

    scatter = px.scatter(
        data_frame=df_tab,
        x='weight',
        y='horsepower',
        size='displacement',
        hover_name='car name',
        color='cylinders',
        title='Weight vs HP for Cars from {}'.format(unique_origin[2])
    )
    col5.plotly_chart(scatter)

    histogram_plot = px.histogram(
        data_frame=df_tab,
        x='mpg',
        title='MPG Distribution'
    )
    col6.plotly_chart(histogram_plot)