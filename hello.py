import os

Student = os.getenv("WHO_TO_GREET", "World")

print(f"Hello GitHub Actions {Student}!")
print("This program is running inside GitHub Actions.")