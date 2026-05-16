import json

def log_activity(func):
    def wrapper(*args, **kwargs):
        print("\n" + "="*40)
        print("[LOG]: Starting activity registration...")
        result = func(*args, **kwargs)
        if result:
            print("[LOG]: Activity registration completed successfully.")
        else:
            print("[LOG]: Registration skipped (Duplicate detected).")
        print("="*40 + "\n")
        return result
    return wrapper

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

    @log_activity
    def add_activity(self, activity_obj):
        for existing_activity in self.activities_data:
            if existing_activity["name"].lower() == activity_obj.name.lower():
                print(f"[WARNING]: Activity '{activity_obj.name}' already exists! Skipped.")
                return False

        entry = {"name": activity_obj.name, "category": activity_obj.category}
        if isinstance(activity_obj, StudyTask):
            entry["deadline"] = activity_obj.deadline
        elif isinstance(activity_obj, Exercise):
            entry["duration"] = activity_obj.duration
            entry["calories"] = activity_obj.calories_burned
            
        self.activities_data.append(entry)
        self.save_to_file()
        print(f"Added and saved: {activity_obj.name}")
        return True

    def display_history(self):
        print(f"--- Full History for {self.student_name} ---")
        if not self.activities_data:
            print("No records found in file.")
        else:
            for item in self.activities_data:
                print(item)

if __name__ == "__main__":
    tracker = StudentTracker("Nurali")
    
    print("Reading existing data...")
    tracker.display_history()
    
    print("\nProcessing new entries...")
    task1 = StudyTask("Advanced Programming Lab", "Thursday")
    task2 = StudyTask("Advanced Programming Lab", "Thursday")
    
    tracker.add_activity(task1)
    tracker.add_activity(task2)
    
    tracker.display_history()