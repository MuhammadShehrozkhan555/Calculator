import streamlit as st
st.set_page_config(page_title="Calculator", page_icon="🔢")
st.title("CALCULATOR")

# 1. Create the calculator's "memory" so it doesn't forget the numbers
if "math_equation" not in st.session_state:
    st.session_state.math_equation = ""

# 2. Create simple functions to handle the button clicks
def add_to_calc(value):
    # This adds the clicked number/symbol to our memory string
    st.session_state.math_equation += str(value)

def calculate_result():
    try:
        # 'eval' is a built-in Python tool that automatically calculates a math string (like "7+5")
        result = eval(st.session_state.math_equation)
        st.session_state.math_equation = str(result)
    except:
        st.session_state.math_equation = "Error"

def clear_calc():
    # This empties the memory
    st.session_state.math_equation = ""

# 3. The Calculator Screen (Using st.info for a nice blue box)
st.text_input(label="Calculator Display",
    label_visibility="collapsed",
    value=st.session_state.math_equation,
    key="math_equation",
    on_change=calculate_result,
    placeholder="0")

# 4. The Buttons Grid (Using 4 columns to put buttons side-by-side)
col1, col2, col3, col4 = st.columns(4)

with col1:         
    st.button("𝟳", on_click=add_to_calc, args=("7",))
    st.button("𝟰", on_click=add_to_calc, args=("4",))
    st.button("𝟭", on_click=add_to_calc, args=("1",))
    st.button("𝗖", on_click=clear_calc)

with col2:
    st.button("𝟴", on_click=add_to_calc, args=("8",))
    st.button("𝟱", on_click=add_to_calc, args=("5",))
    st.button("𝟮", on_click=add_to_calc, args=("2",))
    st.button("𝟬 ", on_click=add_to_calc, args=("0",))

with col3:
    st.button("𝟵", on_click=add_to_calc, args=("9",))
    st.button("𝟲", on_click=add_to_calc, args=("6",))
    st.button("𝟯", on_click=add_to_calc, args=("3",))
    st.button("＝", on_click=calculate_result)

with col4:
    st.button("➗", on_click=add_to_calc, args=("/",))
    st.button("✖️", on_click=add_to_calc, args=("*",))
    st.button("➖", on_click=add_to_calc, args=("-",))
    st.button("➕", on_click=add_to_calc, args=("+",))