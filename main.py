from validator import ResumeValidator
from utils import generate_report

if __name__ == "__main__":
    validator = ResumeValidator("resume.txt")

    validator.load_resume()
    validator.extract_email()
    validator.extract_phone()
    validator.extract_skills()

    generate_report(validator)

    print("Validation completed. Check report.txt")
