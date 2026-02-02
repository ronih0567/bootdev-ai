def run_python_file(working_directory, file_path, args=None):
    import os
    import subprocess

    try:
        abs_dir = os.path.abspath(working_directory)
        target_file = os.path.join(abs_dir, file_path)
        target_file = os.path.normpath(target_file)
        valid_target_file = os.path.commonpath([abs_dir, target_file]) == abs_dir
        if not valid_target_file:
            return f"Error: Cannot run \"{file_path}\" as it is outside the permitted working directory"
        valid_file = os.path.isfile(target_file)
        if not valid_file:
            return f'Error: File not found or is not a regular file: \"{file_path}\"'
        
        command = ["python", target_file]
        if args:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"
        
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"