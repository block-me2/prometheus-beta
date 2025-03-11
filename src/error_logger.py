"""
Module for logging error messages to the console.
"""

def log_error(message: str) -> None:
    """
    Log an error message to the console.

    Args:
        message (str): The error message to be logged.

    Raises:
        TypeError: If the message is not a string.
        ValueError: If the message is an empty string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    # Strip whitespace and check for empty string
    stripped_message = message.strip()
    if not stripped_message:
        raise ValueError("Error message cannot be empty")
    
    # Log the error message to console
    print(f"ERROR: {stripped_message}")