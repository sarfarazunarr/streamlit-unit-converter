Units = {
    "length": {
        "mm": 0.001,       # Millimeter to meter
        "cm": 0.01,        # Centimeter to meter
        "in": 0.0254,      # Inch to meter
        "ft": 0.3048,      # Foot to meter
        "yd": 0.9144,      # Yard to meter
        "m": 1,            # Meter (base unit)
        "km": 1000,        # Kilometer to meter
        "mi": 1609.34      # Mile to meter
    },
    "temperature": {
        "C_to_F": lambda c: (c * 9/5) + 32,   # Celsius to Fahrenheit
        "F_to_C": lambda f: (f - 32) * 5/9,   # Fahrenheit to Celsius
        "C_to_K": lambda c: c + 273.15,       # Celsius to Kelvin
        "K_to_C": lambda k: k - 273.15,       # Kelvin to Celsius
        "F_to_K": lambda f: (f - 32) * 5/9 + 273.15,  # Fahrenheit to Kelvin
        "K_to_F": lambda k: (k - 273.15) * 9/5 + 32   # Kelvin to Fahrenheit
    },
    "time": {
        "sec": 1,         # Second (base unit)
        "min": 60,        # Minute to seconds
        "hr": 3600,       # Hour to seconds
        "day": 86400      # Day to seconds
    },
    "volume": {
        "ml": 0.001,      # Milliliter to liter
        "cl": 0.01,       # Centiliter to liter
        "l": 1,           # Liter (base unit)
        "m3": 1000,       # Cubic meter to liter
        "fl_oz": 0.0295735,  # Fluid ounce to liter
        "cup": 0.236588,  # Cup to liter
        "pint": 0.473176, # Pint to liter
        "gallon": 3.78541 # Gallon to liter
    },
    "mass": {
        "mg": 0.000001,   # Milligram to kilogram
        "g": 0.001,       # Gram to kilogram
        "kg": 1,          # Kilogram (base unit)
        "lb": 0.453592,   # Pound to kilogram
        "oz": 0.0283495,  # Ounce to kilogram
        "ton": 1000       # Metric ton to kilogram
    }
}