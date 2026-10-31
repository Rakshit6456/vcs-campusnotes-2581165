import sys

NOTES_FILE = "notes.txt"


def add_note(text):
    with open(NOTES_FILE, "a") as f:
        f.write(text + "\n")
    print("Added:", text)


def list_notes():
    try:
        with open(NOTES_FILE) as f:
            notes = f.readlines()

        if not notes:
            print("No notes yet.")
            return

        for i, line in enumerate(notes, 1):
            print(f"{i}. {line.strip()}")

    except FileNotFoundError:
        print("No notes yet.")


def delete_note(number):
    try:
        with open(NOTES_FILE) as f:
            notes = f.readlines()

        if number < 1 or number > len(notes):
            print("Invalid note number.")
            return

        deleted = notes.pop(number - 1)

        with open(NOTES_FILE, "w") as f:
            f.writelines(notes)

        print("Deleted:", deleted.strip())

    except FileNotFoundError:
        print("No notes yet.")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "add":
        add_note(" ".join(sys.argv[2:]))

    elif len(sys.argv) == 2 and sys.argv[1] == "list":
        list_notes()

    elif len(sys.argv) == 3 and sys.argv[1] == "delete":
        try:
            delete_note(int(sys.argv[2]))
        except ValueError:
            print("Please enter a valid note number.")

    else:
        print("Usage: python3 notes.py add <text> | list | delete <number>")