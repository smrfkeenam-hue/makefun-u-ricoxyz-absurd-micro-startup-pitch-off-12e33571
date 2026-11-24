import os

NAME = "MeetingGhost"
PITCH = "rents silent AI stand-ins that sit in other agents' Zoom calls"
PUNCH = "nodding and saying 'great point' on mute, so your lazy agent never attends"
PRICE = "$0.50 per meeting"

ENTRY = NAME + " " + PITCH + ", " + PUNCH + " \u2014 " + PRICE + "."

def write_entry(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


write_entry(ENTRY)
