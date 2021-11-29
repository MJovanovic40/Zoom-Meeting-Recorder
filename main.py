from subject import Subjects, Subject
import scheduler

def add_subject():
    name = input("Name: ")
    link = input("Link: ")
    duration = input("Duration: ")
    start_time = input("Starts at (HH:MM): ")
    day = input("Day: ")
    type = input("Type: ")

    return Subject(name, link, duration, start_time, day, type)

def menu():
    print("1. Dodaj predmet")
    print("2. Ukloni predmet")
    print("3. Pokreni snimanje")
    print("4. Exit")

def main():
    subjects = Subjects()

    while True:
        menu()
        choice = int(input("-> "))

        if choice == 1:
            subject = add_subject()
            subjects.add(subject)
        elif choice == 2:
            pass
        elif choice == 3:
            scheduler.initialize_shedule(subjects.subjects)
        elif choice == 4:
            exit()


if __name__ == "__main__":
    main()
