import os
version = os.getenv('VERSION')
print(f"Version is {version}")
version_line_index = 5

with open('setup.py', 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith('version'):
        version_line_index = i
        break

new_version_line = f'version="{version}",\n'

lines[version_line_index] = new_version_line

with open('setup.py', 'w') as file:
    file.writelines(lines)
