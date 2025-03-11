def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius to convert.
    
    Returns:
        float: Temperature converted to Fahrenheit.
    
    Raises:
        TypeError: If input is not a number.
    """
    # Validate input is a number
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    
    # Conversion formula: F = (C * 9/5) + 32
    return (celsius * 9/5) + 32