import streamlit as st

#Function to convert units with expanded conversion options
def convert_unit(value, unit_from, unit_to):
    #Conversion factors dictionary
    conversion = {
        #length conversion (bas unit: meters)
        "meters_kilometers":  0.001,    # 1 meter = 0.001 kilometers
        "killometers_meters": 1000,     # 1 kilometer = 1000 meters
        "meters_centimeters": 100,      # 1 meter = 100 centimeters
        "centimeters_meters": 0.01,     # 1 centimeter = 0.01 meters
        "meters_inches": 39.3701,       # 1 meter = 39.3701 inches
        "inches_meters": 0.0254,        # 1 inch = 0.0254 meters

        # Weight conversion (bas unit: kilograms)
        "grams_kilograms": 0.001,       # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,        # 1 kilogram = 1000 grams
        "kilograms_pounds": 2.20462,        # 1 gram = 2.20462 pounds
        "pounds_kilograms": 0.453592,       # 1 pound = 0.453592 kilograms

        #Temperature conversions (special cases)
        "celsius_fahrenheit": lambda x: (x * 9/5) + 32,  # Celsius to Fahrenheit
        "fahrenheit_celsius": lambda x: (x - 32) * 5/9,  # Fahrenheit to Celsius
    }

    # Handle same-unit case
    if unit_from == unit_to:
        return value

    # Generate conversion key
    key = f"{unit_from}_{unit_to}"

    # Perform conversion if supported
    if key in conversion:
        conversion = conversion[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return None # Return None for unsupported conversions

# Streamlit UI setup
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

# Hander with custom styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📏 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>Convert units easily and quickly</h1>", unsafe_allow_html=True)

# Organize UI into colums for better layout
col1, col2 = st.columns(2)

# Unit categories
unit_categories = {
    "Length📏": ["meters", "kilometers", "centimeters", "inches"],
    "Weight⚖️": ["grams", "kilograms", "pounds"],
    "Temperature🌡️": ["celsius", "fahrenheit"]
}

# Sidebar for category selection
category = st.sidebar.selectbox("Choose Category", list(unit_categories.keys()))

# Input fields
with col1:
    value = st.number_input("Enter Value", min_value=0.0, step=0.1, format="%.2f")
    unit_from = st.selectbox("➡️From", unit_categories[category], key="unit_from")

with col2:
    unit_to = st.selectbox("To➡️", unit_categories[category], key="unit_to")

# Convert  button with centered alignment
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("🔄Convert", key="convert_btn"):
    result = convert_unit(value, unit_from, unit_to)
    if result is not None:
        st.success(f"✅ {value:.2f} {unit_from} = {result:.2f} {unit_to}")
    else:
        st.error(f"❌ Conversion from {unit_from} to {unit_to} is not supported.")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Built by Umer Ali💖 | © 2025</p>", unsafe_allow_html=True)
