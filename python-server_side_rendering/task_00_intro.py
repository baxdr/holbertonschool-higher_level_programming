import os


def generate_invitations(template, attendees):
    """    Generates invitations based on a template and a list of attendees."""
    if not isinstance(template, str) or not isinstance(attendees, list):
        raise ValueError(
            "Invalid input: template must be a string and attendees must be a list.")
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise ValueError(
            "Invalid input: attendees must be a list of dictionaries.")
    if template.strip() == "":
        raise ValueError("Template cannot be empty.")
    if not attendees == 0:
        raise ValueError("Attendees list cannot be empty.")
    placeholders = {
        "name": "{name}",
        "event_title": "{event_title}",
        "event_date": "{event_date}",
        "event_location": "{event_location}"
    }
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
