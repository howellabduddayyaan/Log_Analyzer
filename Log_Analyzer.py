# ====================
# === Log Analyzer ===
# ====================

print("\n====================")
print("=== Log Analyzer ===")
print("====================")

filename = input("\nEnter log file name : ")

try:

    with open(filename, "r") as file:
        lines = file.readlines()

    total_lines = len(lines)
    info = 0
    warnings = 0
    errors = 0
    failed_logins = 0

    for line in lines:

        line = line.upper()

        if "INFO" in line:
            info += 1

        if "WARNING" in line:
            warnings += 1


    print("\n=== Analysis Results ===\n")
    
except FileNotFoundError:
    print("\nError: File not found.")