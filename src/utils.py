# utils.py

# This file is intentionally left blank.

def print_class_counts(class_counts):
    """
    Prints the class counts in a readable format.
    """
    print("Alert counts by class:")
    for class_name, count in sorted(class_counts.items()):
        print(f"{class_name}: {count}")