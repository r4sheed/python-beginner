"""
File Search Script

This script is designed to search for files in the current directory based on a provided search pattern. It uses the 'ls' command in a shell environment to list files that match the given pattern. The script is useful for quickly finding files without manually navigating through directories or using more complex file search tools.

Usage:
    python findFiles.py [search pattern] [backup directory (optional)]

Example:
    python findFiles.py "*.txt" backup

This command will list all .txt files in the current directory and compress them into a backup file in the 'backup' directory.

The script uses the 'subprocess.Popen' class to execute the 'ls' command in the shell. The 'shell=True' parameter allows the use of wildcard characters in the search pattern, and the 'stdout=subprocess.PIPE' parameter captures the command's output for printing. The 'communicate()' method is used to execute the command and retrieve the output.

Please note that using 'shell=True' can be a security risk if untrusted input is used, as it allows for shell injection. Always sanitize and validate input when using 'shell=True'.

The documentation was created by the Phind-34B model.
"""

import os
import time
import sys
import subprocess
    
def make_dir(path):
    """
    Creates a new directory at the specified path if it does not already exist.

    Parameters:
    path (str): The path where the new directory should be created. Default is 'backup'.

    Returns:
    bool: True if the directory was successfully created, False if it already exists.
    """
    # Construct the absolute path of the directory to be created
    currentPath = os.path.abspath(path + '/')

    # Check if the directory already exists
    if os.path.exists(currentPath):
        return False
    else:
        # Command to create the directory
        args = ['mkdir', path]
        # Execute the command
        subprocess.Popen(args, stdout=subprocess.PIPE).wait()
        return True

# Check if the correct number of arguments is provided
if len(sys.argv) <  2:
    print('Invalid arguments! Usage: findFiles.py [search pattern] [backup directory (optional)]')
    sys.exit(1)

# Read the command-line arguments and sanitize the search pattern to prevent shell injection
search_pattern = sys.argv[1].replace("'", "\\'")

# Default value if no target directory is provided
target_directory = 'backup'

# Check if the target directory is provided
if len(sys.argv) >  2:
    target_directory = sys.argv[-1]  # The last argument is the target directory

# Combine the command and parameters
command = f'ls {search_pattern}'

# Run the command and read the stdout
# Create a 'subprocess.Popen' object that runs the 'ls' command in the shell.
# The 'shell=True' parameter allows the use of wildcard characters in the search pattern.
# The 'stdout=subprocess.PIPE' parameter means that the command's output is passed to the Python program,
# so it can be printed to the console.
# The 'communicate()' method handles the execution of the command and returns the output.
popen = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
stdout, stderr = popen.communicate()

# Store the stdout
# The 'stdout.decode('utf-8')' call converts the 'stdout' byte data to text, making it readable.
files_str = stdout.decode('utf-8')

# Convert the string to a list of files.
files = files_str.splitlines()

# Create the target directory if it does not exists.
make_dir(target_directory)

# Generate a timestamp string in the format YYYY-MM-DD_HH-MM
# This is used to create a unique name for the backup file.
date_time = str(time.strftime("%Y-%m-%d_%H-%M"))

# Use the timestamp to create a backup file name, including the word "backup",
# the timestamp, and the .gz extension indicating a gzip-compressed archive.
# The format is 'backup_YYYY-MM-DD_HH-MM.gz', where YYYY-MM-DD_HH-MM is the current date and time.
backup_file = f'backup_{date_time}.gz'

# Attempt to execute the tar command to compress the found files into an archive.
# This block is wrapped in a try-except to handle any errors that may occur during the execution of the tar command.
try:
    # Construct the tar command with the target directory and archive name
    # The '-czvf' options are used:
    # - '-c': Create a new archive
    # - '-z': Compress the archive using gzip
    # - '-v': Verbose output, listing the files being archived
    # - '-f': Specify the archive file name
    args = ['tar', '-czvf', f'{target_directory}/{backup_file}'] + files
    # Execute the tar command using subprocess.Popen
    # The stdout=subprocess.PIPE argument captures the command's output, which can be useful for debugging
    # The wait() method is called to wait for the command to complete
    subprocess.Popen(args, stdout=subprocess.PIPE).wait()
except Exception as e:
    # If an error occurs during the execution of the tar command, log the error message
    # This helps in identifying and troubleshooting issues with the command execution
    print(f"Failed to create archive: {e}")