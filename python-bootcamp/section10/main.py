# Function with Outputs
def format_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    formated_full_name = full_name.title()
    return formated_full_name


formated_name = format_name("first", "LAST")
print(f"hello, {formated_name}")
