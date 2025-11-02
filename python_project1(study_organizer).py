import argparse             # For command-line argument parsing
import os                   # For file operations
import json                 # For JSON file(study_schedule.json) handling

                            # OS(founder) module is used to check if the schedule file exists

                            # JSON is used to save and load the study schedule

def prioritize_subjects(subjects_list):
    """Reorders subjects for the schedule."""
    return [
        subjects_list[0],
        subjects_list[4],
        subjects_list[2],
        subjects_list[1],
        subjects_list[3]
    ]

SCHEDULE_FILE = 'study_schedule.json'

def save_schedule(data):
    """Saves the generated schedule to a JSON file."""
    try:
        with open(SCHEDULE_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\n✅ Schedule successfully saved!")
    except Exception as e:
        print(f"❌ Error saving schedule: {e}")

def load_schedule():
    """Loads the schedule from a JSON file."""
    if os.path.exists(SCHEDULE_FILE):
        try:
            with open(SCHEDULE_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Error loading schedule: {e}")
    return None

print("\n\n\n\n\n                                       Welcome to the Study Organizer Program!\n")

import datetime                 # For date and time handling
from datetime import timedelta  # For time duration calculations
current_date = datetime.datetime.now()
print(f"Today's date: {current_date.strftime('%d/%m/%Y')}\n")


parser = argparse.ArgumentParser(description='A program to organize your study schedule.')
parser.add_argument('-d', '--day', type=str, help='Show schedule for a specific day (e.g., Monday).')
args = parser.parse_args()      # Parse command-line arguments
requested_day = args.day        # Get the requested day if provided

print("Task management: Organizing your study subjects and goals.\n")
subjects_list = ["Math", "Turkish Languge", "History", "Art", "Physics"]
#                   0            1               2        3       4
# From the most diffecult to the most simple ones: Math, Physics, History, Turkish Language, Art
new_subject_list = prioritize_subjects(subjects_list)
                                # Reorder the subjects based on priority(the saved order previously mentioned)
print("Subjects list order:")
print(subjects_list)
print('\n')
print("New subjects list order:")
print(new_subject_list)

# First step is done, now moving to the second step

print("\n              <------------------------------------------------------------------------------------>\n")
print("Focus & Time Management Tips:\n")
study_times = {
    "Morning shift(6:00am-8:00am)": "High focus, best for difficult subjects like Math and Physics.",
    "Afternoon shift(3:30pm-5:30pm)": "Moderate focus, suitable for subjects like History and Turkish Language.",
    "Evening shift(7:00pm-8:00pm)": "Lower focus, ideal for lighter subjects like Art."
}

print("Optimal Study Times:\n")
for time, tip in study_times.items():
                                # for each time slot, print the corresponding tip
    print(f"- {time}: {tip}\n")

# Second step is done, now moving to the third step

print("                <------------------------------------------------------------------------------------>\n")
print("Creating Study Schedule:")
study_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
study_log_per_day = 10
full_schedule = {}

for day in study_days:
    if requested_day and day.lower() != requested_day.lower():
                                # If a specific day is requested and it doesn't match the current day, skip it
        continue 
    
    daily_logs = []
    print(f"\n--------------------------\n\n{day}'s Study Log:")
    for log in range(1, study_log_per_day + 1):
        subject_index = (log - 1) % len(new_subject_list)
        subject = new_subject_list[subject_index]
                                # subject_index cycles through the new_subject_list
        log_message = f"Log {log}: {subject} - 25 min and 5 min break,"
        print(f"  {log_message}")
        daily_logs.append({"log": log, "subject": subject, "duration": "25 min study, 5 min break"})
    
    full_schedule[day] = daily_logs
save_schedule(full_schedule)

# Third step is done, now moving to the fourth step

print("\n              <------------------------------------------------------------------------------------>\n")

print("Recommended AI tools for each subject:\n")
ai_for_study = {
    "Math": "GeoGebra",
    "Physics": "Gauth",
    "Turkish Languge": "Talkpal",
    "History": "Historact AI",
    "Art": "Prisma"
}
valid_subjects = set(subjects_list)
                                # Ensure the subject is valid before printing

for subject, tool in ai_for_study.items():
                                # Print the recommended AI tool for each subject
    print(f"For {subject}, recommended AI tool: {tool}")

# Fourth step is done, now moving to the fifth step

print("\n              <------------------------------------------------------------------------------------>\n")

one_week_later = current_date + timedelta(weeks=1)
print(f"Target Date for Goal Completion: {one_week_later.strftime('%d/%m/%Y')}\n")

print("--------------------------\n")

print("Weekly Study Goals:\n")
for subject in new_subject_list:
                                # For each subject, calculate and print the weekly study goal
    if subject == "Art":
        weekly_goal = 10 * 25
    elif subject == "History":
        weekly_goal = 10 * 25
    elif subject == "Turkish Languge":
        weekly_goal = 10 * 25
    elif subject == "Physics":
        weekly_goal = 10 * 25
    elif subject == "Math":
        weekly_goal = 10 * 25
    else:
        weekly_goal = 0

    hours = weekly_goal // 60
    minutes = weekly_goal % 60
                                # Print the study goal in hours and minutes

    print(f"Study goal for {subject}: {hours} hours and {minutes} minutes.")

# Fifth step is done, now moving to the final message

print("\n              <------------------------------------------------------------------------------------>\n")

print("All tasks completed! Good luck with your studies!\n")

print("                                      Have a productive and successful study session!\n\n\n\n\n")

