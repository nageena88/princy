import pandas as pd
from datetime import datetime, timedelta

# Define the tasks with their frequencies
common_area_tasks = [
    {"Task": "Podium", "Frequency": "Every Two Days"},
    {
        "Task": "Clubhouse - Regular & Alt. Days (Washroom)",
        "Frequency": "Alternate Days",
    },
    {"Task": "Hall Booking - Before & After", "Frequency": "As Needed"},
    {"Task": "All Society Roads", "Frequency": "Daily"},
    {"Task": "Basement", "Frequency": "Every Two Days"},
]

wing_wise_tasks = [
    {"Task": "Lobby, Lift, Duct", "Frequency": "Daily"},
    {"Task": "Staircase, Refuge Area", "Frequency": "Weekly"},
    {"Task": "Wing Parking", "Frequency": "Every Two Days"},
]

# Combine all tasks
all_tasks = common_area_tasks + wing_wise_tasks

# Create a date range for the current month
start_date = datetime.today().replace(day=1)
end_date = start_date.replace(month=start_date.month % 12 + 1, day=1) - timedelta(
    days=1
)
date_range = pd.date_range(start=start_date, end=end_date)

# Prepare schedule
schedule = []

for task in all_tasks:
    for date in date_range:
        freq = task["Frequency"]
        add_task = False

        if freq == "Daily":
            add_task = True
        elif freq == "Every Two Days" and (date - start_date).days % 2 == 0:
            add_task = True
        elif freq == "Alternate Days" and (date - start_date).days % 2 == 0:
            add_task = True
        elif freq == "Weekly" and date.weekday() == 0:  # Monday
            add_task = True
        elif freq == "As Needed":
            continue  # Skip as it's based on hall bookings

        if add_task:
            schedule.append(
                {
                    "Date": date.strftime("%Y-%m-%d"),
                    "Task": task["Task"],
                    "Frequency": freq,
                }
            )

# Convert to DataFrame
schedule_df = pd.DataFrame(schedule)

# Save to Excel
schedule_df.to_excel("Housekeeping_Schedule.xlsx", index=False)

print("✅ Excel file 'Housekeeping_Schedule.xlsx' has been created successfully.")
