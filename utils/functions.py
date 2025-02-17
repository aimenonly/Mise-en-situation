# -*- coding: utf-8 -*-
import os
import glob
import paramiko
import json
from datetime import datetime 




def verify_ssh_connectivity(hostname, username, port, key=None, password=None):
    """
    Verify SSH connectivity to a remote server.

    Args:
        hostname (str): The remote server's hostname or IP address.
        username (str): The SSH username.
        port (int): The SSH port.
        key (str, optional): Path to the private key file for authentication.
        password (str, optional): The SSH password.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if key:
            # Use key-based authentication
            private_key = paramiko.RSAKey.from_private_key_file(key)
            client.connect(hostname, port=port, username=username, pkey=private_key)
        else:
            # Use password-based authentication
            client.connect(hostname, port=port, username=username, password=password)
        return True
    except Exception as e:
        print(f"SSH connection failed: {e}")
        return False
    finally:
        client.close()




def execute_ssh_commands(hostname, username, password,  commands):
    """
    Execute a list of commands on a remote server via SSH.

    Args:
        hostname (str): The remote server's hostname or IP address.
        username (str): The SSH username.
        password (str): The SSH password.
        commands (list): A list of commands to execute.

    Returns:
        str: The combined output of all commands.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, username=username, password=password)

        output_string = ""
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            stdin.write(password + "\n")  # Send sudo password if required
            stdin.flush()
            stdout.channel.recv_exit_status()  # Wait for command to complete
            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                output_string += output
            if error:
                output_string += error
                print(f"Error executing command '{command}': {error}")

        return output_string

    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e), ""

    finally:
        client.close()




def sftp_get_file_from_remote(host, username, password, remote_file_path, local_path):
    """
    Retrieve a file from the remote server using SFTP.

    Args:
        host (str): Hostname or IP address of the remote server.
        port (int): SSH port of the remote server.
        username (str): Username for the SSH connection.
        password (str): Password for the SSH connection.
        remote_file_path (str): Path to the remote file to be retrieved.
        local_path (str): Local path to save the retrieved file.

    Returns:
        str: A message indicating the outcome of the operation.
    """
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Establish SSH connection
        ssh.connect(host, username=username, password=password)

        # Start an SFTP session
        sftp = ssh.open_sftp()

        # Retrieve the file from remote to local path
        sftp.get(remote_file_path, local_path)

        sftp.close()
        ssh.close()

        return "File retrieved successfully."

    except Exception as e:
        return f"An error occurred while retrieving the file: {e}"




def clean_directory(directory, file_type):
    """
    Remove files of a specific type from a directory.

    Args:
        directory (str): Path of the directory to clean.
        file_type (str): File extension type (e.g., 'txt', 'jpg', etc.).
    """
    # Create a pattern for the file type
    pattern = os.path.join(directory, f'*.{file_type}')

    # Find all files in the directory with the specified file type
    files = glob.glob(pattern)

    # Remove each file
    for file in files:
        try:
            os.remove(file)
            print(f'Removed file: {file}')
        except OSError as e:
            print(f'Error removing file {file}: {e}')



def generate_report_json(results, file_path):
    """
    Generate a JSON report from test results.

    Args:
        results (dict): A dictionary containing test results.
        file_path (str): Path to save the JSON report.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as json_file:
            json.dump(results, json_file, indent=4)
        print(f"Report saved as {file_path}")
    except Exception as e:
        print(f"Error generating JSON report: {e}")

def generate_report_markdown(results, file_path):
    """
    Generate a Markdown report from test results.

    Args:
        results (dict): A dictionary containing test results.
        file_path (str): Path to save the Markdown report.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as md_file:
            md_file.write(f"# Test Report\n")
            md_file.write(f"Date: {datetime.now()}\n")
            md_file.write(f"\n## Test Results\n")
            for test, result in results.items():
                md_file.write(f"### {test}\n")
                md_file.write(f"Result: {result}\n")
        print(f"Report saved as {file_path}")
    except Exception as e:
        print(f"Error generating Markdown report: {e}")