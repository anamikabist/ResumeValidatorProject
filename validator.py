import re

class ResumeValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""
        self.email = None
        self.phone = None
        self.skills = []

    def load_resume(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print("File not found.")

    def extract_email(self):
        pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        match = re.search(pattern, self.content)
        if match:
            self.email = match.group()

    def extract_phone(self):
        pattern = r"\b\d{10}\b"
        match = re.search(pattern, self.content)
        if match:
            self.phone = match.group()

    def extract_skills(self):
        skills_section = re.search(r"Skills:(.*?)(\n\n|\Z)", self.content, re.DOTALL)
        if skills_section:
            raw_skills = skills_section.group(1)
            skills_list = re.split(r",|\n", raw_skills)
            self.skills = list(set(
                map(lambda x: x.strip(),
                    filter(lambda x: x.strip() != "", skills_list))
            ))
