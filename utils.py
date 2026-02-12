def generate_report(validator):
    with open("report.txt", "w") as file:
        file.write("RESUME VALIDATION REPORT\n\n")
        file.write(f"Email: {validator.email}\n")
        file.write(f"Phone: {validator.phone}\n")
        file.write("Skills:\n")
        for skill in validator.skills:
            file.write(f"- {skill}\n")
