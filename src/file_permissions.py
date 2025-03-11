import os
import stat

def change_file_permissions(file_path, permissions):
    """
    Change the permissions of a file.

    Args:
        file_path (str): Path to the file whose permissions will be modified.
        permissions (int): Octal representation of desired file permissions 
                           (e.g., 0o755 for read/write/execute for owner, 
                           read/execute for group and others).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the current user lacks permission to modify the file.
        TypeError: If invalid arguments are provided.
        ValueError: If permissions are outside valid range.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(permissions, int):
        raise TypeError("permissions must be an integer")
    
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate permissions are in valid octal range
    if permissions < 0 or permissions > 0o777:
        raise ValueError("Permissions must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, permissions)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error changing permissions: {str(e)}")
    
    return True  # Indicate successful permission change