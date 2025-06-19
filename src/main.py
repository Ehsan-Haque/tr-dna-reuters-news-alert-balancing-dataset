# main.py

from csv_reader import read_alerts_from_csv
from alert_counter import count_alerts_by_class
from utils import print_class_counts
from semantic_cluster import semantic_cluster_classes
import matplotlib.pyplot as plt

def main():
    # Hardcoded CSV file path
    filepath = r"C:\tr-dna-reuters-news-alert-balancing-dataset\topics_clean.csv"
    alerts = read_alerts_from_csv(filepath)
    class_counts = count_alerts_by_class(alerts)
    print_class_counts(class_counts)
    print(f"\nTotal number of classes: {len(class_counts)}")

    # Semantic clustering
    n_clusters = 20  # You can adjust this number
    clusters = semantic_cluster_classes(list(class_counts.keys()), n_clusters=n_clusters)

    # Prepare cluster info with alert counts
    cluster_info = []
    for label, class_list in clusters.items():
        total_alerts = sum(class_counts.get(class_name, 0) for class_name in class_list)
        cluster_info.append((label, class_list, total_alerts))

    # Sort clusters by total_alerts (ascending)
    cluster_info.sort(key=lambda x: x[2])

    print(f"\nSemantic Clusters (sorted by alert count, showing up to 5 classes per cluster):")
    for label, class_list, total_alerts in cluster_info:
        print(
            f"Cluster {label} ({len(class_list)} classes, {total_alerts} alerts): "
            f"{', '.join(class_list[:5])}{'...' if len(class_list) > 5 else ''}"
        )

    # After you have clusters and their alert counts, e.g.:
    # clusters = [(cluster_id, [class1, class2, ...], total_alerts), ...]
    # Let's assume you have a list of tuples: (cluster_id, class_names, total_alerts)

    # Example: clusters = [(3, ['JP', 'NEWS1'], 2), (7, ['QUAK', 'DIS'], 2), ...]

    # Sort clusters by total_alerts (ascending)
    clusters_sorted = sorted(cluster_info, key=lambda x: x[2])

    # Prepare data for plotting
    cluster_labels = [f"Cluster {c[0]}" for c in clusters_sorted]
    alert_counts = [c[2] for c in clusters_sorted]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(cluster_labels, alert_counts, color='skyblue')
    plt.xlabel('Cluster')
    plt.ylabel('Number of Alerts')
    plt.title('Number of Alerts per Cluster (Lowest to Highest)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()