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

        if "ERROR" in line:
            errors += 1

        if "FAILED LOGIN" in line:
            failed_logins += 1

    print("\n=== Analysis Results ===\n")
    
    print(f"Total Log Entries : {total_lines}")
    print(f"Information       : {info}")
    print(f"Warnings          : {warnings}")
    print(f"Errors            : {errors}")
    print(f"Failed Logins     : {failed_logins}")
    
except FileNotFoundError:
    print("\nError: File not found.")