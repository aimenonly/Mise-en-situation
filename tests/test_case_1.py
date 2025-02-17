from utils.functions import execute_ssh_commands
from data.test_data import REMOTE,  USERNAME, PASSWORD, COMMAND_TO_EXECUTE ,REMOTE_LOGS_PATH

def test_case_1():
    """
    Test Case 1: Execute a command on the remote server via SSH and verify the existence of /var/log/auth.log.
    """
    # Command to check if /var/log/auth.log exists
    command = f"{COMMAND_TO_EXECUTE} {REMOTE_LOGS_PATH}"

    # Execute the command on the remote server
    output = execute_ssh_commands(REMOTE, USERNAME, PASSWORD, [command])

    # Verify that the file exists by checking the output
    assert REMOTE_LOGS_PATH in output, f"File {REMOTE_LOGS_PATH} not found on the remote server. Output: {output}"
