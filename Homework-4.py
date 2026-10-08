web_development = ["Rahul", "Anu", "Vishnu"]
data_science = ["Asha", "Arjun", "Meera"]
ui_ux_design = ["Neha", "Riya", "Kiran"]

all_participants = [web_development, data_science, ui_ux_design]
web_development.append("Akhil")
data_science.insert(1, "Priya")
ui_ux_design.pop()
data_science_copy = data_science.copy()
data_science.clear()

print(web_development[:2])

name_lengths = [len(x) for x in data_science_copy]
print(name_lengths)

if "Asha" in web_development or "Asha" in data_science_copy or "Asha" in ui_ux_design:
    print("Asha is in a workshop")
else:
    print("Asha is not in any workshop")

first_participants = (
    web_development[0],
    data_science_copy[0],
    ui_ux_design[0]
)

print(first_participants)