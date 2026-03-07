import pandas as pd
import plotly_express as px
import streamlit as st

# Function Histograms
def create_histograms(x, title):
        """
        Helper function to create histograms
        :param x: str, column name in dataframe
        :param title: str, title of the created chart
        :return: plotly graph object
        """
        hist = px.histogram(
            data_frame=df_plot,
            x=x, color_discrete_sequence=['blue'],
            title=title
        )
        return hist

st.set_page_config(layout='wide')

df = pd.read_csv(r"D:\PROJECT TASHA\PYTHON\learning\streamlit\data\iris.csv")
unique_species = df['species'].unique()

st.title('Iris Dashboard')

# Select Box and Checkbox Control
cola, colb = st.columns([1,1])

selected_species = cola.selectbox(
    label='Species',
    label_visibility='collapsed',
    options=unique_species
)

show_hist = colb.checkbox(label='Show Histogram',
                        key='checkb')

print(selected_species)

# Subset of Dataset
df_plot = df[df['species'] == selected_species]

sl_mean = round(df_plot['sepal_length'].mean(), 2)
sw_mean = round(df_plot['sepal_width'].mean(), 2)
pl_mean = round(df_plot['petal_length'].mean(), 2)
pw_mean = round(df_plot['petal_width'].mean(), 2)

# Add Columns
col1, col2, col3, col4 = st.columns([1,1,1,1])
col1.metric(label='Sepal Length Average', value=sl_mean)
col2.metric(label='Sepal Width Average', value=sw_mean)
col3.metric(label='Petal Length Average', value=pl_mean)
col4.metric(label='Petal Width Average', value=pw_mean)

# color map dictionary
color_map = {'setosa':'gray',
             'versicolor':'gray',
             'virginica':'gray'}

# alter color dictionary based on selected species
color_map[selected_species]='blue'

# Add Scatter Plot
scatter_plot = px.scatter(
    data_frame=df,
    x='sepal_length',
    y='petal_width',
    title='Sepal Length vs Petal Width for {}'.format(selected_species),
    color_discrete_map=color_map,
    color='species',
    size='petal_length'
)
st.plotly_chart(scatter_plot)


if show_hist:
    col5, col6, col7, col8 = st.columns([1,1,1,1])

    # Create Histogram
    hist1 = create_histograms(x='sepal_length', title='Distribution of Sepal Length')
    hist2 = create_histograms(x='sepal_width', title='Distribution of Sepal Width')
    hist3 = create_histograms(x='petal_length', title='Distribution of Petal Length')
    hist4 = create_histograms(x='petal_width', title='Distribution of Petal Width')
   
    col5.plotly_chart(hist1)
    col6.plotly_chart(hist2)
    col7.plotly_chart(hist3)
    col8.plotly_chart(hist4)