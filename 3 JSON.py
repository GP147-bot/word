import json

# Load the JSON data from your full file path
json_path = r"sha.json"  # Use raw string for Windows paths

with open(json_path, 'r') as f:
    students = json.load(f)

target_names = ['Shaheen', 'Sameeha']

for student in students:
    if student.get('name') in target_names:
        name = student['name']
        student_id = student['id']
        marks = student.get('marks', {})
        math = marks.get('math', 0)
        science = marks.get('science', 0)
        english = marks.get('english', 0)

        total = math + science + english
        average = total / 3

        print(f"Student: {name} (ID: {student_id})")
        print(f"  Math: {math}")
        print(f"  Science: {science}")
        print(f"  English: {english}")
        print(f"  Total: {total}")
        print(f"  Average: {average:.2f}\n")
