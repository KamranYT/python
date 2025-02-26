import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversions = {
        'meters': 1,
        'kilometers': 1000,
        'inches': 0.0254,
        'feet': 0.3048,
        'miles': 1609.34,
        'centimeters': 0.01,
        'millimeters': 0.001
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495,
        'stones': 6350.29,
        'milligrams': 0.001
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # Same unit conversion (if applicable)

def convert_area(value, from_unit, to_unit):
    conversions = {
        'square meters': 1,
        'square kilometers': 1e6,
        'hectares': 1e4,
        'acres': 4046.86,
        'square feet': 0.092903,
        'square inches': 0.00064516
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic meters': 1000,
        'cubic centimeters': 0.001,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_speed(value, from_unit, to_unit):
    conversions = {
        'meters per second': 1,
        'kilometers per hour': 0.277778,
        'miles per hour': 0.44704,
        'feet per second': 0.3048
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_time(value, from_unit, to_unit):
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    return value * conversions[to_unit] / conversions[from_unit]

# Initialize session state to keep track of history
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("MK_Unit Converter")

conversion_type = st.selectbox("Select Conversion Type", 
                                 ("Length", "Weight", "Temperature", "Area", "Volume", "Speed", "Time"))

value = st.number_input("Enter the value to convert", min_value=0.0)

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", ["meters", "kilometers", "inches", "feet", "miles", "centimeters", "millimeters"])
    to_unit = st.selectbox("To Unit", ["meters", "kilometers", "inches", "feet", "miles", "centimeters", "millimeters"])
    
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.6f} {to_unit}")
        st.session_state.history.append(f"{value} {from_unit} = {result:.6f} {to_unit}")

elif conversion_type == "Weight":
    from_unit = st.selectbox("From Unit", ["grams", "kilograms", "pounds", "ounces", "stones", "milligrams"])
    to_unit = st.selectbox("To Unit", ["grams", "kilograms", "pounds", "ounces", "stones", "milligrams"])
    
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.6f} {to_unit}")
        st.session_state.history.append(f"{value} {from_unit} = {result:.6f} {to_unit}")

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.6f} {to_unit}")
        st.session_state.history.append(f"{value} {from_unit} = {result:.6f} {to_unit}")

elif conversion_type == "Area":
    from_unit = st.selectbox("From Unit", ["square meters", "square kilometers", "hectares", "acres", "square feet", "square inches"])
    to_unit = st.selectbox("To Unit", ["square meters", "square kilometers", "hectares", "acres", "square feet", "square inches"])
    
    if st.button("Convert"):
        result = convert_area(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.6f} {to_unit}")
        st.session_state.history.append(f"{value} {from_unit} = {result:.6f} {to_unit}")

elif conversion_type == "Volume":
    from_unit = st.selectbox("From Unit", ["liters", "milliliters", "cubic meters", "cubic centimeters", "gallons", "quarts", "pints"])
    to_unit = st.selectbox("To Unit", ["liters", "milliliters", "cubic meters", "cubic centimeters", "gallons", "quarts", "pints"])
    
    if st.button("Convert"):
        result = convert_volume(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.6f} {to_unit}")
        st.session_state.history.append(f"{value} {from_unit} = {result:.6f} {to_unit}")

elif conversion_type == "Speed":
    from_unit = st.selectbox("From Unit", ["meters per second", "kilometers per hour", "miles per hour", "feet per second"])
    to_unit = st.selectbox("To Unit", ["meters per second", "kilometers per hour", "miles per hour", "feet per second"])
    
    if st.button("Convert"):
        result = convert_speed(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.6f} {to_unit}")
        st.session_state.history.append(f"{value} {from_unit} = {result:.6f} {to_unit}")

elif conversion_type == "Time":
    from_unit = st.selectbox("From Unit", ["seconds", "minutes", "hours", "days"])
    to_unit = st.selectbox("To Unit", ["seconds", "minutes", "hours", "days"])
    
    if st.button("Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.6f} {to_unit}")
        st.session_state.history.append(f"{value} {from_unit} = {result:.6f} {to_unit}")

# Display conversion history
st.subheader("Conversion History")
for entry in st.session_state.history:
    st.write(entry)

# Clear history button
if st.button("Clear History"):
    st.session_state.history.clear()
    st.success("History cleared!")