# main.py

from csv_reader import read_alerts_from_csv
from alert_counter import count_alerts_by_class
from utils import print_class_counts
from semantic_cluster import semantic_cluster_classes
from hierarchical_cluster import (
    hierarchical_cluster_cooccurrence,
    print_clusters
)
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_cluster_alerts(cluster_dict, class_counts, title):
    """
    Plots a bar chart: cluster number vs number of alerts in that cluster.
    """
    cluster_labels = []
    alert_counts = []
    for idx, (cluster, code_list) in enumerate(sorted(cluster_dict.items()), 1):
        num_alerts = sum(class_counts.get(code, 0) for code in code_list)
        cluster_labels.append(f"Cluster {idx}")
        alert_counts.append(num_alerts)
    plt.figure(figsize=(10, 6))
    plt.bar(cluster_labels, alert_counts, color='skyblue')
    plt.xlabel('Cluster')
    plt.ylabel('Number of Alerts')
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    # Path to your CSV file
    filepath = r"C:\tr-dna-reuters-news-alert-balancing-dataset\topics_clean.csv"
    alerts = read_alerts_from_csv(filepath)
    class_counts = count_alerts_by_class(alerts)
    print_class_counts(class_counts)
    print(f"Number of unique classes/codes: {len(class_counts)}")

    # --- Semantic Clustering ---
    print("\nSemantic Clustering of Codes:")
    n_clusters = 30  # Set number of clusters to 30
    semantic_clusters = semantic_cluster_classes(
        list(class_counts.keys()), class_counts, n_clusters, plot_graph=False
    )

    # Prepare cluster dict for plotting
    semantic_cluster_dict = {}
    for idx, cluster in enumerate(semantic_clusters):
        semantic_cluster_dict[idx + 1] = cluster['classes']

    plot_cluster_alerts(semantic_cluster_dict, class_counts, "Semantic Cluster vs Number of Alerts")

    # --- Hierarchical Clustering (Co-occurrence) ---
    print("\nHierarchical Clustering of Codes (Co-occurrence Analysis):")
    codes, clusters = hierarchical_cluster_cooccurrence(
        alerts, plot_dendrogram=False, max_d=0.7
    )

    # Prepare cluster dict for reporting (no graph)
    hierarchical_cluster_dict = defaultdict(list)
    for code, cluster in zip(codes, clusters):
        hierarchical_cluster_dict[cluster].append(code)

    print(f"Number of clusters in hierarchical cluster algorithm: {len(hierarchical_cluster_dict)}\n")
    print_clusters(codes, clusters, class_counts)

if __name__ == "__main__":
    main()