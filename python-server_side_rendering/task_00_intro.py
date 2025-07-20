import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dicts, got {type(attendees).__name__}")
        return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    placeholders = ["name", "event_title", "event_date", "event_location"]
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            val = attendee.get(key)
            if val is None or (isinstance(val, str) and val.strip() == ""):
                val = "N/A"
            content = content.replace(f"{{{key}}}", str(val))
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
            print(f"Generated {filename}")
        except Exception as e:
            print(f"Failed to write {filename}: {e}")
