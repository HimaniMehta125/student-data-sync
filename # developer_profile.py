# developer_profile.py

class Developer:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def bio(self):
        return "📚 Continuously learning and exploring new technologies."

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(self.bio())


if __name__ == "__main__":
    dev = Developer("Himani", "Python Developer")
    dev.display_profile()