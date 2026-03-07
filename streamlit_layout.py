import streamlit as st

# Learning Tab
tab1,tab2,tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

with tab1:
    st.header('I am in Tab 1')

with tab2:
    st.header('I am in Tab 2')
    st.text('This is a tab 2')

with tab3:
    st.header('I am in Tab 3')
    range_slider = st.slider(
    label='Select a range',
    min_value=1, max_value=100,
    value=(50, 75))
    st.write('Selected number: {}'.format(range_slider))


# Learning Columns
col1,col2,col3 = st.columns(3, gap='small', vertical_alignment='top')

with col1:
    st.header('Column 1') 

with col2:
    st.header('Column 2')

with col3:
    st.header('Column 3')

col4,col5 = st.columns([3,4], gap='medium', vertical_alignment='top')

col4.header('Column 4')
col5.header('Column 5')


# Learning Sidebar
st.sidebar.subheader('Sidebar')
st.sidebar.selectbox(label='Options', options=['a', 'b', 'c'])