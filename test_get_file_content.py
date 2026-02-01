from functions.get_file_content import get_file_content
from config import MAX_CHARS

test_lorem = get_file_content("calculator", "lorem.txt")
print("Result for lorem.txt:")
if "truncated at" in test_lorem:
    print(f"File was greater than {MAX_CHARS} characters and was truncated.")
    print("\n")
elif "Error: " in test_lorem:
    print(test_lorem)
    print("\n")
else:
    print("File content within limit:")
    print("\n")

test_main = get_file_content("calculator", "main.py")
print("Result for main.py:")
if "truncated at" in test_main:
    print(f"File was greater than {MAX_CHARS} characters and was truncated.")
    print("\n")
elif "Error: " in test_main:
    print(test_main)
    print("\n")
else:
    print("File content within limit")
    print("\n")

test_pkg_calc = get_file_content("calculator", "pkg/calculator.py")
print("Result for pkg/calculator.py:")
if "truncated at" in test_pkg_calc:
    print(f"File was greater than {MAX_CHARS} characters and was truncated.")
    print("\n")
elif "Error: " in test_pkg_calc:
    print(test_pkg_calc)
    print("\n")
else:
    print("File content within limit")
    print("\n")

test_bin_cat = get_file_content("calculator", "/bin/cat")
print("Result for /bin/cat:")
if "truncated at" in test_bin_cat:
    print(f"File was greater than {MAX_CHARS} characters and was truncated.")
    print("\n")
elif "Error: " in test_bin_cat:
    print(test_bin_cat)
    print("\n")
else:
    print("File content within limit")
    print("\n")

test_dne = get_file_content("calculator", "pkg/does_not_exist.py")
print("Result for pkg/does_not_exist.py:")
if "truncated at" in test_dne:
    print(f"File was greater than {MAX_CHARS} characters and was truncated.")
    print("\n")
elif "Error: " in test_dne:
    print(test_dne)
    print("\n")
else:
    print("File content within limit")
    print("\n")