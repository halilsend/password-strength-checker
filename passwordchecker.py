password = input("Enter a password: ")


problems = []

if len(password) < 8:
    problems.append("at least 8 characters")

if not any(c.islower() for c in password):
    problems.append("a lowercase letter")

if not any(c.isdigit() for c in password):
    problems.append("a digit")    


if not any(c.isupper() for c in password):
    problems.append("an uppercase letter")

if problems:
    print("weak password. it needs: " + ", ".join(problems))
else: 
    print("password is valid")      
    