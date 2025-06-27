from collections import Counter


def count_alerts_by_class(alerts):
    """
    Counts the number of alerts per class.
    Returns a dictionary: class_code -> count
    """
    class_counter = Counter()
    for alert in alerts:
        codes = alert['codes']  # codes is already a list
        for code in codes:
            class_counter[code] += 1
    return dict(class_counter)