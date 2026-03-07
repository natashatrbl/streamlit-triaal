# Text Widget in Streamlit
import streamlit as st
import datetime

st.markdown('# Markdown Display 1')
st.markdown('## Markdown Display 2')
st.markdown('### Markdown Display 3')

st.header('This is a Header')
st.subheader('This is a Subheader')
st.text('This is a text')
st.caption('This is a caption')

#display code
code_snippet = """
def greet(name): return f"Hello, {name}!"""
st.code(code_snippet, language='python')

#display latex
#Latex input: Render mathematical expressions
st.latex(r'''a^2 + b^2 = c^2''')
st.latex(r'''y = m*x + c''')

#list and dictionary
my_list = [1,2,3]
my_du = {'a':1, 'b':2}
st.write(my_list)
st.write(my_du)


# Dropdown Widget in streamlit
st.header('All About Dropdown')

car_manufacturer = ['Ford', 'Lexus', 'Toyota', 'VW', 'Audi', 'Porsche', 'BMW']

selected_car = st.selectbox(label='Car Manufacturer',
                            options=car_manufacturer,
                            help='Select Car Brand',
                            key='u1')

# Multiple Select Widget
st.header('All About Multi Select')
my_favs = st.multiselect(
    label='Select Your Favorite Car',
    label_visibility='collapsed',
    placeholder='Select your top 3 car brands',
    options=car_manufacturer,
    help='Select your favorite car brand',
    max_selections=3
)

# Slider Widget
## Basic Slider
st.header('All About Slider')

basic_slider = st.slider(
    label='Basic Label',
    min_value=1, max_value=100,
    value=50
)
st.write('Selected number: {}'.format(basic_slider))

## Range Slider
range_slider = st.slider(
    label='Select a range',
    min_value=1, max_value=100,
    value=(50, 75)
)
st.write('Selected number: {}'.format(range_slider))

## Float Slider
float_slider = st.slider(
    label='Select a decimal range',
    min_value=1.0, max_value=10.0,
    step=0.1,
    value=5.0
)
st.write('Selected number: {}'.format(float_slider))

## Data Slider
date_slider = st.slider(
    label="Select a date",
    min_value=datetime.date(2026, 1, 1),
    max_value=datetime.date(2026, 3, 31),
    value=datetime.date(2026, 3, 3),
    format="MM/DD/YYYY"
)
st.write(f"Selected date: {date_slider}")

# Number Input Widget

number_input = st.number_input(
    label="Enter a number",
    min_value=0,
    max_value=100,
    value=50,
    step=1,
    help="Use this widget to input a number",
    label_visibility='visible'
)

sidebar_number_input = st.sidebar.number_input(
    label='Number input in sidebar',
    min_value=5,
    max_value=100,
    step=5,
    value=30,
    label_visibility='visible'
)
st.write(sidebar_number_input)

# Forms in Streamlit
st.header('All About Forms')

form = st.form(
    key='form1',
    clear_on_submit=False,
    enter_to_submit=True,
    border=True,
)
state_of_origin = form.selectbox(label='Current State', 
                                options=['TX', 'NX', 'NV'])
submit = form.form_submit_button(label='Submit Details')

if submit:
    print('Submit Buttion Value', submit)
    print(state_of_origin)

second_form = st.sidebar.form(key='sidebar_form')
age = second_form.number_input(label='Age', min_value=1, max_value=99)
submit_second_form = second_form.form_submit_button()

if submit_second_form:
    st.markdown('Second form was submitted')
    print(age)
