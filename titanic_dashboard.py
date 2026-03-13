import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(layout='wide')
st.title("Titanic Dashboard")

df = pd.read_csv("titani_data.csv")

df['Embarked'] = df['Embarked'].fillna('Unknown')

embarked_port = list(df['Embarked'].unique())
gender = list(df['Sex'].unique())

col1, col2 = st.columns([1,1])
selected_port = col1.selectbox(
    options=embarked_port,
    label='Select a port'
)
selected_gender = col2.selectbox(
    options=gender,
    label='Select gender'
)

df_plot = df[df['Embarked'] == selected_port]
df_plot = df_plot[df_plot['Sex'] == selected_gender]

df_plot_pie = df_plot.loc[:, ['PassengerId', 'Survived']].groupby(['Survived']).count().reset_index()
df_plot_pie.rename({'PassengerId': 'Count of Passengers'}, axis='columns', inplace=True)

# Plot Graph Histogram
hist_plot = px.histogram(data_frame=df_plot,
                    template='seaborn',
                    color='Survived',
                    title='Distribution of Age',
                    facet_col='Survived',
                    x='Age')
col1.plotly_chart(hist_plot)

# Plot Pie Chart
pie_plot = px.pie(data_frame=df_plot_pie,
                  template='seaborn',
                  title='Count of Survived Passengers',
                  values='Count of Passengers',
                  names='Survived')
col2.plotly_chart(pie_plot)

# Plot Box Plot
box_plot = px.box(data_frame=df_plot,
                  y='Fare',
                  template='seaborn',
                  color='Survived',
                  title='Distribution of Fare Across Survival Status',
                  x='Survived')
st.plotly_chart(box_plot)