📌 Resume Cleaner & Validator (Python)
📖 Project Overview
This project is a rule-based Resume Cleaner and Validator built using core Python concepts.
It reads a resume in .txt format and validates important information such as:
1. Email address
2. Phone number
3. Skills section
4. Presence of important sections (Education, Projects, Skills)
5. The system uses Regular Expressions (Regex) and Object-Oriented Programming (OOP) to extract and validate structured information from unstructured resume text.

🎯Objective
The goal of this project is to automate basic resume validation without using external libraries or machine learning.
It demonstrates how Python fundamentals can be applied to solve real-world problems like resume screening.

⚙️ Technologies Used
-> Python (Core)
-> OOPS
-> Regex (re module)
-> Exception Handling
-> map() and filter()
-> File Handling

🧠 Features
-> Extracts email using regex
-> Extracts 10-digit phone numbers
-> Parses and cleans skill list
-> Removes duplicate skills
-> Detects missing sections
-> Generates structured validation report

📂 Project Structure
ResumeValidatorProject/
│
├── main.py
├── validator.py
├── utils.py
├── resume.txt
└── report.txt

▶️ How to Run
(1) Place your resume file (resume.txt) in the project folder.
(2) Run:
       python main.py
(3) Check report.txt for validation results.

🔮 Future Improvements
(1) PDF resume parsing
(2) Skill matching with job descriptions
(3) Resume scoring system
(4) GUI version
(5) Keyword density analysis
