import json
import uuid

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

        entry = {
            "id": str(uuid.uuid4())[:8],
            "name": activity_obj.name, 
            "category": activity_obj.category
        }
        
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
        print(f"\n--- Full History for {self.student_name} ---")
        if not self.activities_data:
            print("No records found in file.")
        else:
            for item in self.activities_data:
                act_id = item.get("id", "N/A")
                
                if item["category"] == "Study":
                    print(f"ID: {act_id} | [Study] {item['name']} (Deadline: {item['deadline']})")
                elif item["category"] == "Sport":
                    print(f"ID: {act_id} | [Sport] {item['name']} ({item['duration']} min, {item['calories']} kcal)")

def main():
    tracker = StudentTracker("Nurali")
    
    while True:
        print("\n=== Student Activity Tracker ===")
        print("1. View Activity History")
        print("2. Add Study Task")
        print("3. Add Sports Exercise")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            tracker.display_history()
            
        elif choice == "2":
            name = input("Enter study task name: ").strip()
            deadline = input("Enter deadline (e.g., Monday, 23:59): ").strip()
            if name and deadline:
                task = StudyTask(name, deadline)
                tracker.add_activity(task)
            else:
                print("[Error]: Fields cannot be empty.")
                
        elif choice == "3":
            name = input("Enter exercise name: ").strip()
            try:
                duration = int(input("Enter duration (minutes): "))
                calories = int(input("Enter calories burned: "))
                if name:
                    run = Exercise(name, duration, calories)
                    tracker.add_activity(run)
                else:
                    print("[Error]: Name cannot be empty.")
            except ValueError:
                print("[Error]: Duration and Calories must be numbers! Action cancelled.")
                
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("[Error]: Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()