# Application Report Generator

users = [
    {"name": "Mona", "active": True},
    {"name": "Karthi", "active": True},
    {"name": "Sowmiya", "active": False},
    {"name": "Lithish", "active": True},
    {"name": "Priya", "active": False},
    {"name": "Rahul", "active": True}
]

# Calculate total users
total_users = len(users)

# Count active users
active_users = 0

for user in users:
    if user["active"]:
        active_users += 1

# Calculate inactive users
inactive_users = total_users - active_users

# Calculate active percentage
active_percentage = (active_users / total_users) * 100

# Generate report
with open("report.txt", "w") as file:
    file.write("APPLICATION USER REPORT\n")
    file.write("=======================\n")
    file.write(f"Total Users      : {total_users}\n")
    file.write(f"Active Users     : {active_users}\n")
    file.write(f"Inactive Users   : {inactive_users}\n")
    file.write(f"Active Percentage: {active_percentage:.2f}%\n")

print("Application report generated successfully.")
