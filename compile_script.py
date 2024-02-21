import os
import re

def compile_contents_to_file(output_filename, script_filename, ignore_patterns=[]):
    # Compile regex patterns for efficiency
    compiled_patterns = [re.compile(pattern) for pattern in ignore_patterns]

    def should_ignore(path):
        """Check if the path matches any of the ignore patterns."""
        return any(pattern.search(path) for pattern in compiled_patterns)

    # Get the current directory
    current_directory = os.getcwd()
    output_lines = []

    for root, dirs, files in os.walk(current_directory):
        # Filter directories to ignore
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]
        
        for file in files:
            # Construct the file path
            file_path = os.path.join(root, file)
            # Create a relative path for files inside directories
            relative_path = os.path.relpath(file_path, start=current_directory)
            # Replace backslashes with forward slashes for consistency
            relative_path_formatted = relative_path.replace("\\", "/")

            # Skip the script file itself or any ignored files
            if file == script_filename or file == output_filename or should_ignore(relative_path_formatted):
                continue

            # Read the contents of each file
            try:
                with open(file_path, 'r') as f:
                    contents = f.read()
                    # Append the file name (with folder prefix if applicable) and its contents to the list
                    output_lines.append(f"{relative_path_formatted}:\n{contents}\n\n")
            except Exception as e:
                # Handle files that cannot be read (binary files, permissions issues, etc.)
                print(f"Error reading file {file_path}: {e}")

    # Write the compiled contents to the output file
    with open(output_filename, 'w') as output_file:
        output_file.writelines(output_lines)
    print(f"Contents compiled into {output_filename}")

# Customize the output file name and the script file name
output_filename = "compiled_contents.txt"
script_filename = "compile_script.py" # Change this to the name of your script file

# List of regex patterns for files/directories to ignore
ignore_patterns = [
    r'\.git', # Ignore .git directories
    r'\.history', # Ignore .history directories
    r'\.vscode', # Ignore .vscode directories
    r'\.png$', # Ignore PNG files
    # Add more patterns as needed
]

compile_contents_to_file(output_filename, script_filename, ignore_patterns)
