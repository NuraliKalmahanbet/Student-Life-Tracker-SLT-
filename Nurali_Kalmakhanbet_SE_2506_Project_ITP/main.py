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
    def __init__(self, student_name):
        self.student_name = student_name
        self.activities = []
        self.stats = {"total_study_time": 0, "total_calories": 0}

    def add_activity(self, activity_obj):
        self.activities.append(activity_obj)
        if isinstance(activity_obj, Exercise):
            self.stats["total_calories"] += activity_obj.calories_burned
        print(f"Added to tracker: {activity_obj.name}")

    def display_all(self):
        print(f"\n--- Progress Report for {self.student_name} ---")
        for activity in self.activities:
            print(activity.get_info())
        print(f"\nSummary Stats: {self.stats}")

if __name__ == "__main__":
    tracker = StudentTracker("Nurali")
    
    task1 = StudyTask("Python Project", "Friday")
    task2 = Exercise("Morning Run", 30, 250)
    task3 = Exercise("Pull-ups", 15, 100)
    
    tracker.add_activity(task1)
    tracker.add_activity(task2)
    tracker.add_activity(task3)
    
    tracker.display_all()