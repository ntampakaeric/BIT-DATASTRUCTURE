import array

# -------------------------------
# INTEGERS: Inspection scores
# -------------------------------
inspection_scores = [85, 90, 78, 92, 88, 70, 95]
total_score = sum(inspection_scores)
average_score = total_score / len(inspection_scores)
min_score = min(inspection_scores)
max_score = max(inspection_scores)

# -------------------------------
# STRINGS: Formatted Report
# -------------------------------
report = (
    f"SAFETY INSPECTION SUMMARY REPORT\n"
    f"---------------------------------\n"
    f"Total Score: {total_score}\n"
    f"Average Score: {average_score:.2f}\n"
    f"Minimum Score: {min_score}\n"
    f"Maximum Score: {max_score}\n"
)
print(report)

# -------------------------------
# BOOLEANS: Threshold check
# -------------------------------
threshold = 80
meets_standard = average_score > threshold and max_score > 90

if meets_standard:
    print("Inspection Status: Above Standard\n")
else:
    print("Inspection Status: Below Standard\n")

# -------------------------------
# LISTS: Safety checklist items
# -------------------------------
checklist_items = ["Fire Extinguisher", "Emergency Exit", "First Aid Kit", "Smoke Detector", "Sprinkler System"]

# Add a new item
checklist_items.append("Safety Signage")

# Remove item if it matches a specific condition
if "First Aid Kit" in checklist_items:
    checklist_items.remove("First Aid Kit")

# Display before and after sorting
print("Checklist Items (Before Sorting):", checklist_items)
checklist_items.sort()
print("Checklist Items (After Sorting):", checklist_items)
print()

# -------------------------------
# ARRAYS: Fixed-size numeric subset
# -------------------------------
# Using first four inspection scores
subset_scores = array.array('i', inspection_scores[:4])
array_sum = sum(subset_scores)
list_sum = sum(inspection_scores[:4])

print("Numeric Subset (Array):", list(subset_scores))
print("Sum using array module:", array_sum)
print("Sum using list slice:  ", list_sum)

if array_sum == list_sum:
    print("Result: Array sum matches list sum.\n")
else:
    print("Result: Array sum does not match list sum.\n")

# -------------------------------
# DICTIONARIES: Record entries
# -------------------------------
inspection_records = [
    {"id": 1, "name": "Fire Extinguisher", "value": 85},
    {"id": 2, "name": "Emergency Exit", "value": 90},
    {"id": 3, "name": "First Aid Kit", "value": 78},
    {"id": 4, "name": "Smoke Detector", "value": 92}
]

# Update value for a specific record
for record in inspection_records:
    if record["id"] == 2:
        record["value"] = 95  # New updated score

# Delete a record with a specific ID
inspection_records = [record for record in inspection_records if record["id"] != 3]

# Compute total value across all remaining records
total_record_value = sum(record["value"] for record in inspection_records)

print("Updated Inspection Records:")
for record in inspection_records:
    print(f"ID: {record['id']}, Item: {record['name']}, Score: {record['value']}")

print(f"\nTotal Value of All Records: {total_record_value}")

