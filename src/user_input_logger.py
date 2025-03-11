import sys
import logging
import os
from typing import Optional

def log_user_input(log_file: Optional[str] = None) -> str:
    """
    Logs user input from the command line.

    Args:
        log_file (Optional[str]): Path to the log file. 
                                  If None, uses default logging to console.

    Returns:
        str: The user input that was logged.

    Raises:
        ValueError: If input is empty or contains only whitespace.
    """
    # Ensure log file directory exists if log_file is specified
    if log_file:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(log_file)), exist_ok=True)
        
        # Configure file logging
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - User Input: %(message)s'
        )
    else:
        # Configure console logging
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - User Input: %(message)s'
        )

    # Prompt and read user input
    try:
        user_input = input("Enter your input: ").strip()
        
        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty")
        
        # Log the input
        logging.info(user_input)
        
        return user_input
    except Exception as e:
        logging.error(f"Error logging input: {e}")
        raise