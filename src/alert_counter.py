from collections import defaultdict


def count_alerts_by_class(alerts):
    """
    Counts how many alerts belong to each class.
    Returns a dictionary: {class_name: count}
    """
    class_counts = defaultdict(int)
    for alert in alerts:
        codes = alert['codes'].split()
        for code in codes:
            class_counts[code] += 1
    return dict(class_counts)