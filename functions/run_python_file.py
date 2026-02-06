import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes a specified Python file relative to the working directory, with optional command-line arguments, and returns the output or any errors",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            required=["file_path"],
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="File path of the Python file to execute, relative to the working directory",
                ),
                "args": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(type=types.Type.STRING),
                    description="Optional list of command-line arguments to pass to the Python script",
                ),
            },
        ),
    )

def run_python_file(working_directory, file_path, args=None):

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