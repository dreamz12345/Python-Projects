

def format_name(f_name, l_name):

    f_name = f_name.lower()
    f_name_list = list(f_name)
    f_name_list[0] = f_name_list[0].upper()

    l_name = l_name.lower()
    l_name_list = list(l_name)
    l_name_list[0] = l_name_list[0].upper()

    full_name = "".join(f_name_list) + " " + "".join(l_name_list)
    return full_name

def format_name_easy(f_name, l_name):
    full_name = (f_name + " " + l_name).title()
    return full_name

f_name = "anNA"
l_name = "qWErTY"
fixed_name = format_name_easy(f_name, l_name)
print(fixed_name)