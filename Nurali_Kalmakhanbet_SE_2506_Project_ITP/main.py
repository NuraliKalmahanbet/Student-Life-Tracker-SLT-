class Activity:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_info(self):
        return f"[{self.category}] {self.name}"

class StudentTracker:
    def __init__(self, student_name):
        self.student_name = student_name
        self.activities = []

    def add_activity(self, name, category):
        new_activity = Activity(name, category)
        self.activities.append(new_activity)
        print(f"Added: {name}")

    def display_all(self):
        print(f"\nTracker for {self.student_name}:")
        for activity in self.activities:
            print(activity.get_info())

if __name__ == "__main__":
    tracker = StudentTracker("User")
    tracker.add_activity("Math Assignment", "Study")
    tracker.add_activity("Running", "Sport")
    tracker.display_all()