import sys

NOTES_FILE = "notes.txt"


def add_note(text):
    with open(NOTES_FILE, "a") as f:
        f.write(text + "\n")
    print("Added:", text)


def list_notes():
    try:
        with open(NOTES_FILE) as f:
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No notes yet.")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "add":
        add_note(" ".join(sys.argv[2:]))
    elif len(sys.argv) == 2 and sys.argv[1] == "list":
        list_notes()
    else:
        print("Usage: python3 notes.py add <text> | list")
