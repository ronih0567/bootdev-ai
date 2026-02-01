import os

def get_files_info(working_directory, directory="."):
    try:
        abs_dir = os.path.abspath(working_directory)
        # print(f"Working directory (absolute): {abs_dir}")  # Debugging line
        target_directory = os.path.join(abs_dir, directory)
        target_directory = os.path.normpath(target_directory)
        # print(f"Target directory (absolute): {target_directory}")  # Debugging line
        valid_target_dir = os.path.commonpath([abs_dir, target_directory]) == abs_dir
        if not valid_target_dir:
            return (f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory")
        valid_dir = os.path.isdir(target_directory)   
        if not valid_dir:
            return (f"Error: \"{directory}\" is not a directory")
        dir_list = os.listdir(target_directory)
        # print(f"dir_list: {dir_list}") # Debugging line
        lines = []
        for name in dir_list:
            full_path = os.path.join(target_directory, name)
            is_dir = os.path.isdir(full_path)
            size = os.path.getsize(full_path)
            line = f"- {name}: file_size={size} bytes, is_dir={is_dir}"
            lines.append(line)
        print(f"Generated lines: {lines}")  # Debugging line
        result = "\n".join(lines)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
