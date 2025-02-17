import pytest
from utils.functions import execute_ssh_commands
from data.test_data import REMOTE, PORT, USERNAME, PASSWORD, FILES_TO_CHECK

def test_case_3():
    """
    Test Case 3: Verify the presence and size of predefined files on the remote server.
    """
    for file_path, expected_size in FILES_TO_CHECK.items():
        # Command to check file existence and size
        command = f"stat -c%s {file_path}"

        # Execute the command on the remote server
        output = execute_ssh_commands(REMOTE, USERNAME, PASSWORD, [command])

        # Verify the file exists and its size matches the expected size
        assert output.strip().isdigit(), f"File {file_path} not found on the remote server."
        assert int(output.strip()) == expected_size, f"File {file_path} size mismatch. Expected: {expected_size}, Actual: {output.strip()}"