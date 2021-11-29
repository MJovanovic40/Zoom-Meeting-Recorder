import pickle
import os

SUBJECTS_FILE = "subjects.pickle"


class Subjects:
    def __init__(self):
        self.subjects = []

        exists = self.read()
        if not exists:
            with open(SUBJECTS_FILE, "wb") as f:
                pickle.dump(self.subjects, f)

    def read(self):
        if os.path.isfile(SUBJECTS_FILE):
            with open(SUBJECTS_FILE, "rb") as f:
                self.subjects = pickle.load(f)
            return True
        return False

    def save(self):
        with open(SUBJECTS_FILE, "wb") as f:
            pickle.dump(self.subjects, f)

    def add(self, subject):
        self.subjects.append(subject)
        self.save()

    def remove(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            self.save()


class Subject:
    def __init__(self, name, link, duration, start_time, day, type):
        self.name = name
        self.link = link
        self.duration = duration
        self.start_time = start_time
        self.day = day
        self.type = type
        self.make_subject_directory()

    def make_subject_directory(self):
        root_dir = os.path.join(os.curdir, "videos")
        directory = os.path.join(root_dir, self.name)
        os.mkdir(directory)