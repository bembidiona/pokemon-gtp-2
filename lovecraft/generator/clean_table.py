import os

mypath = os.getcwd()

# -----------------
# CLEAN CSV
# -----------------
file_csv = open(mypath + "/raw_wiki.csv", "r", encoding="utf-8").read().split("\n")
monster_text = ""
for monster in file_csv:
	inside_multy = False
	for char in monster:
		if char == '"':
			inside_multy = not inside_multy
		elif char == "," and not inside_multy:
			monster_text += "|"
		else:
			monster_text += char
	monster_text += "\n"

monster_text = monster_text[0:-1] #remove last linebreak
temp_list = monster_text.split("\n")
new_file_text = ""
names_list = []
for monster in temp_list:
	name, alias, description = monster.split("|")
	name = name.split("[")[0]

	if alias in ["—", "--", "−"]:
		alias = "???"
	#just grab the first alias
	alias = alias.split(",")[0]
	alias = alias.split("[")[0]
	new_file_text += f"{name}|{alias}\n"
	names_list.append(f"{name}")
new_file_text = new_file_text[0:-1] #remove last linebreak


with open(mypath + "/monster_data.txt", "w", encoding="utf-8") as output:
	output.write(new_file_text)

print(names_list)