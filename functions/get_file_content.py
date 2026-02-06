import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads the content of a specified file relative to the working directory, with a maximum character limit",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            required=["file_path"],
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="File path to read content from, relative to the working directory",
                ),
            },
        ),
    )

def get_file_content(working_directory, file_path):
    try:
        abs_dir = os.path.abspath(working_directory)
        target_file = os.path.join(abs_dir, file_path)
        target_file = os.path.normpath(target_file)
        valid_target_file = os.path.commonpath([abs_dir, target_file]) == abs_dir
        if not valid_target_file:
            return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
        valid_file = os.path.isfile(target_file)
        if not valid_file:
            return f'Error: File not found or is not a regular file: \"{file_path}\"'
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {str(e)}"