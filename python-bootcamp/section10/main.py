# Function with Outputs
def format_name(f_name, l_name):
    # docstring
    """Take a first and last name and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    full_name = f"{f_name} {l_name}"
    formated_full_name = full_name.title()
    return formated_full_name


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

formated_name = format_name(first_name, last_name)
print(f"{formated_name}")
