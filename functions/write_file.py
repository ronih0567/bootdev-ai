def write_file(working_directory, file_path, content):
    import os
    try:
        abs_dir = os.path.abspath(working_directory)
        target_file = os.path.join(abs_dir, file_path)
        target_file = os.path.normpath(target_file)
        valid_target_file = os.path.commonpath([abs_dir, target_file]) == abs_dir
        if not valid_target_file:
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        dir_name = os.path.dirname(target_file)
        os.makedirs(dir_name, exist_ok=True)
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
