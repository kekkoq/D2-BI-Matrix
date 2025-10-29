import re
import csv

# Load and clean the raw discussion text
with open("discussion.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# Normalize line endings and strip leading/trailing spaces
lines = raw_text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
lines = [line.strip() for line in lines if line.strip()]

# Split responses by "Your preferred name:"
response_blocks = []
current_block = []

for line in lines:
    if line.startswith("Your preferred name:") and current_block:
        response_blocks.append(current_block)
        current_block = [line]
    else:
        current_block.append(line)

if current_block:
    response_blocks.append(current_block)

# Prepare CSV rows
csv_rows = [["Name", "Activity 1", "Activity 2", "Activity 3", "Tool"]]

for block in response_blocks:
    name = ""
    activities = ["", "", ""]
    tool = ""

    for line in block:
        if line.startswith("Your preferred name:"):
            name = line.split(":", 1)[1].strip()
        elif "Your preferred activity 1:" in line:
            activities[0] = line.split(":", 1)[1].strip()
        elif "Your preferred activity 2:" in line:
            activities[1] = line.split(":", 1)[1].strip()
        elif "Your preferred activity 3:" in line:
            activities[2] = line.split(":", 1)[1].strip()
        elif "Tool YOU want to learn:" in line:
            tool = line.split(":", 1)[1].strip()

    csv_rows.append([name] + activities + [tool])

# Write to CSV
with open("discussion.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_rows)

print("✅ discussion.csv created successfully.")