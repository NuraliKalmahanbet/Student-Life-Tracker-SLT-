import json

class Activity:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_info(self):
        return f"[{self.category}] {self.name}"

class StudyTask(Activity):
    def __init__(self, name, deadline):
        super().__init__(name, "Study")
        self.deadline = deadline

    def get_info(self):
        return f"[Study] {self.name} - Deadline: {self.deadline}"

class Exercise(Activity):
    def __init__(self, name, duration, calories_burned):
        super().__init__(name, "Sport")
        self.duration = duration
        self.calories_burned = calories_burned

    def get_info(self):
        return f"[Sport] {self.name} - {self.duration} min, {self.calories_burned} kcal"

class StudentTracker:
    def __init__(self, student_name, filename="data.json"):
        self.student_name = student_name
        self.filename = filename
        self.activities_data = self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.activities_data, file, indent=4)

    def add_activity(self, activity_obj):
        entry = {"name": activity_obj.name, "category": activity_obj.category}
        if isinstance(activity_obj, StudyTask):
            entry["deadline"] = activity_obj.deadline
        elif isinstance(activity_obj, Exercise):
            entry["duration"] = activity_obj.duration
            entry["calories"] = activity_obj.calories_burned
            
        self.activities_data.append(entry)
        self.save_to_file()
        print(f"Added and saved: {activity_obj.name}")

    def display_history(self):
        print(f"\n--- Full History for {self.student_name} ---")
        if not self.activities_data:
            print("No records found in file.")
        else:
            for item in self.activities_data:
                print(item)

if __name__ == "__main__":
    tracker = StudentTracker("Nurali")
    
    print("Reading existing data...")
    tracker.display_history()
    
    print("\nAdding new activities for today...")
    task = StudyTask("History Essay", "Wednesday")
    run = Exercise("Gym Session", 60, 450)
    
    tracker.add_activity(task)
    tracker.add_activity(run)
    
    tracker.display_history()