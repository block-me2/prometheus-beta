import os
import stat
import pytest
import tempfile

from src.file_permissions import change_file_permissions

def test_change_file_permissions():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Initial check - default permissions
        original_mode = os.stat(temp_path).st_mode
        
        # Test changing to read-only
        change_file_permissions(temp_path, 0o444)
        new_mode = os.stat(temp_path).st_mode
        assert stat.S_IMODE(new_mode) == 0o444, "Failed to set read-only permissions"
        
        # Test changing to full permissions
        change_file_permissions(temp_path, 0o777)
        new_mode = os.stat(temp_path).st_mode
        assert stat.S_IMODE(new_mode) == 0o777, "Failed to set full permissions"
    
    finally:
        # Clean up temporary file
        os.unlink(temp_path)

def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        change_file_permissions("/path/to/nonexistent/file", 0o644)

def test_invalid_permission_type():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        with pytest.raises(TypeError):
            change_file_permissions(temp_path, "not an int")
        
        with pytest.raises(TypeError):
            change_file_permissions(123, 0o644)
    finally:
        os.unlink(temp_path)

def test_invalid_permission_value():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, -1)
        
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, 0o1000)
    finally:
        os.unlink(temp_path)

def test_permission_change_return_value():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        result = change_file_permissions(temp_path, 0o644)
        assert result is True, "Function should return True on successful permission change"
    
    finally:
        os.unlink(temp_path)