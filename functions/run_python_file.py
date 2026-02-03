def run_python_file(working_directory, file_path, args=None):
    import os
    import subprocess

    try:
        abs_dir = os.path.abspath(working_directory)
        target_file = os.path.join(abs_dir, file_path)
        target_file = os.path.normpath(target_file)
        valid_target_file = os.path.commonpath([abs_dir, target_file]) == abs_dir
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        valid_file = os.path.isfile(target_file)
        if not valid_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if result.stdout is None and result.stdout.strip() == "":
            return "No output produced"
        return f"STDOUT: {result.stdout.strip()}. STDERR: {result.stderr.strip()}"
    except Exception as e:
        return f"Error: {str(e)}"