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
    # Clear any existing loggers
    logging.getLogger().handlers.clear()
    
    # Get root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - User Input: %(message)s'))
    logger.addHandler(console_handler)

    # Handle file logging if log_file is provided
    if log_file:
        # Ensure log file directory exists
        os.makedirs(os.path.dirname(os.path.abspath(log_file)), exist_ok=True)
        
        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - User Input: %(message)s'))
        logger.addHandler(file_handler)

    # Prompt and read user input
    try:
        user_input = input("Enter your input: ").strip()
        
        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty")
        
        # Log the input
        logger.info(user_input)
        
        return user_input
    except Exception as e:
        logger.error(f"Error logging input: {e}")
        raise