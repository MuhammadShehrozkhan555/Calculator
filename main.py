import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Calculator", layout="wide")

# ---------------- TITLE ----------------
st.markdown("""
<h1 style='
text-align:center;
font-size:65px;
color:#00ffcc;
font-weight:bold;
text-shadow: 2px 2px 10px #00ffcc;'>
DI Calculator 🧮
</h1>
""", unsafe_allow_html=True)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 1.2rem;
        border-radius: 8px;
        background-color: #262730;
        color: white;
        border: 1px solid #464646;
    }
    .stButton > button:hover {
        border: 1px solid #00ffcc;
        color: #00ffcc;
    }
    .main-display {
        font-size: 3rem;
        text-align: right;
        padding: 20px;
        background: #0e1117;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 1px solid #333;
        color: #00ffcc;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if 'expression' not in st.session_state:
    st.session_state.expression = ""

if 'history' not in st.session_state:
    st.session_state.history = []

# ---------------- CALC FUNCTION ----------------
def process_calc(key):
    expr = st.session_state.expression

    if key == "C":
        st.session_state.expression = ""

    elif key == "⌫":
        st.session_state.expression = expr[:-1]

    elif key == "=":
        try:
            result = eval(expr)
            result = round(result, 8) if isinstance(result, float) else result
            st.session_state.history.insert(0, f"{expr} = {result}")
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"

    else:
        operators = "+-*/"
        if expr and key in operators and expr[-1] in operators:
            st.session_state.expression = expr[:-1] + key
        else:
            st.session_state.expression += str(key)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([3, 1])

with col1:
    display_text = st.session_state.expression if st.session_state.expression else "0"
    st.markdown(f'<div class="main-display">{display_text}</div>', unsafe_allow_html=True)

    grid = [
        ["7", "8", "9", "Div /"],
        ["4", "5", "6", "Mul *"],
        ["1", "2", "3", "Sub -"],
        ["C", "0", ".", "Add +"],
        ["⌫", "="]
    ]

    for row in grid:
        cols = st.columns(len(row))
        for i, label in enumerate(row):
            if cols[i].button(label, key=f"{label}_{grid.index(row)}"):
                process_calc(label)
                st.rerun()



# ---------------- KEYBOARD INPUT ----------------
with st.expander("⌨️ Keyboard Input"):
    manual_input = st.text_input("Type expression (e.g. 5*5+2)")
    if st.button("Calculate Typed"):
        st.session_state.expression = manual_input
        process_calc("=")
        st.rerun()