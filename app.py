import streamlit as st
from data import Units

st.set_page_config("Unit Converter", layout="centered")
st.title("Convert Units Instantly")

unit_heads = tuple(Units.keys())
dimension = st.selectbox("Select Dimension", unit_heads)

def unit_converter(dimension, unit_from, unit_to, value):
    if not unit_from or not unit_to:
        st.warning("Please Select Units")
        return None

    try:
        value = float(value)  # Convert input to float
    except ValueError:
        st.error("Invalid input! Please enter a numerical value.")
        return None

    if dimension in Units:
        # Check if the units exist in the selected dimension
        if unit_from in Units[dimension] and unit_to in Units[dimension]:
                base_value = value * Units[dimension][unit_from]  # Convert to base unit
                converted_value = base_value / Units[dimension][unit_to]  # Convert to target unit
                return converted_value
        else:
            st.error("Selected units are not available for this dimension!")
            return None
    else:
        st.error("Invalid dimension selected!")
        return None

if dimension:
    col1, col2 = st.columns(2)
    unit_from = None
    from_value = None
    unit_to = None
    result = None

    with col1:
        try:
            unit_from = st.selectbox("Convert From", tuple(Units[dimension].keys()))
            from_value = st.text_input("Enter Value")
        except ValueError:
            st.error("Value should be numerical")
    
    with col2:
        unit_to = st.selectbox("Convert To", tuple(Units[dimension].keys()))
        if from_value:
            result = unit_converter(dimension, unit_from, unit_to, from_value)
            if result is not None:
                st.text_input(label="Output Value", value=f"{from_value} {unit_from} = {result:.2f} {unit_to}")
            elif result is None:
                st.text("Output will be displayed here...")
