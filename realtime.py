import json
import re

# Read JSON
with open("progress.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Progress table
progress_table = "| Item | Status | Progress |\n"
progress_table += "|------|--------|----------|\n"
for item in data["process"]:
    progress_table += f"| {item['list']} | {item['status']} | {item['percent']}% |\n"

# Skills table
skills_table = "| Skill | Level |\n"
skills_table += "|-------|-------|\n"
for item in data["skills"]:
    skills_table += f"| {item['skills']} | {item['percent']}% |\n"

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Content to insert
new_content = f"""## Project Progress

*Last updated: {data['updated']}*

### Progress

{progress_table}

### My Skills

{skills_table}
"""

# Replace between markers
pattern = r"<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->"
replacement = f"<!-- PROGRESS:START -->\n{new_content}\n<!-- PROGRESS:END -->"

new_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print("README updated successfully.")