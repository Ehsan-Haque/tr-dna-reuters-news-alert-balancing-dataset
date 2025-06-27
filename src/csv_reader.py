import csv

def read_alerts_from_csv(filepath):
    """
    Reads alerts from a CSV file.
    Returns a list of dictionaries with keys: 'serial', 'alert', 'codes'
    """
    alerts = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            alerts.append({
                'serial': row.get('serial') or row.get('Serial') or row.get('Serial Number'),
                'alert': row['alert'],
                'codes': row['codes'].split()  # Split codes by blank space
            })
    return alerts