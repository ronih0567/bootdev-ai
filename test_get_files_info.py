from functions.get_files_info import get_files_info

test_dot = get_files_info("calculator", ".")
print("Result for current directory:")
print("  " + test_dot.replace("\n", "\n  "))
print("\n")

test_pkg = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print("  " + test_pkg.replace("\n", "\n  "))
print("\n")

test_slashbin = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print("  " + test_slashbin.replace("\n", "\n  "))
print("\n")

test_dotdotslash = get_files_info("calculator", "../")
print("Result for '../' directory:")
print("  " + test_dotdotslash.replace("\n", "\n  "))
print("\n")