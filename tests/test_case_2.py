from utils.functions import sftp_get_file_from_remote
from data.test_data import REMOTE, USERNAME, PASSWORD, REMOTE_LOGS_PATH, LOCAL_TMP_PATH, PROCESS_TO_CHECK
import os


def test_case_2():
    """
    Test Case 2: Retrieve file from the remote server and verify that 'CRON' exists in the file.
    """
    # Define the local path for the retrieved log file
    local_log_path = os.path.join(LOCAL_TMP_PATH, "tmp.log")

    # Retrieve the log file from the remote server
    result = sftp_get_file_from_remote(REMOTE, USERNAME, PASSWORD, REMOTE_LOGS_PATH, local_log_path)

    # Check if file was retrieved successfully
    assert "successfully" in result, f"Failed to retrieve the log file: {result}"
    print(f"Successfully retrieved log file to {local_log_path}")

    # Read the log file and check for CRON process occurrences
    with open(local_log_path, "r") as log_file:
        log_lines = log_file.readlines()

  # printing the file contents
    print("Log file content preview:")
    print("".join(log_lines[:10]))


    cron_found = False
    for line in log_lines:
        if PROCESS_TO_CHECK.lower() in line.lower():  # Case-insensitive check
            cron_found = True
            break  # Exit the loop once a match is found


    assert cron_found, f"No '{PROCESS_TO_CHECK}' process found in the log file."

    # Clean up the retrieved log file
    try:
        os.remove(local_log_path)
        print(f"Cleaned up log file {local_log_path}")
    except Exception as e:
        print(f"Error cleaning up log file: {str(e)}")
