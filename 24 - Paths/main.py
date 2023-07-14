with open("24 - Paths/invitation.txt", "r") as invitation_file:
    invitation_template = invitation_file.read()
with open("24 - Paths/names.txt", "r") as names_file:
    names = names_file.read().splitlines()
for name in names:
    new_invitation_file_name = f"24 - Paths/{name}_invitation.txt"
    with open(new_invitation_file_name, "w") as new_invitation:
        personal_invitation = invitation_template.replace("[name]", name)
        new_invitation.write(personal_invitation)
