"""
Hierarchical clustering of codes using co-occurrence analysis.

This approach:
- Builds a co-occurrence matrix for codes (how often codes appear together in alerts)
- Computes a distance matrix (1 - normalized co-occurrence)
- Performs hierarchical clustering (agglomerative)
- Plots a dendrogram and returns cluster assignments
"""

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

def build_cooccurrence_matrix(alerts):
    """
    Build a co-occurrence matrix for codes.
    Returns:
        codes: list of unique codes
        matrix: numpy array (codes x codes) with co-occurrence counts
    """
    # Get all unique codes, stripping whitespace and skipping empty codes
    code_set = set()
    for alert in alerts:
        for c in alert['codes']:
            c = c.strip()
            if c:
                code_set.add(c)
    codes = sorted(list(code_set))
    code_idx = {code: i for i, code in enumerate(codes)}

    # Initialize matrix
    matrix = np.zeros((len(codes), len(codes)), dtype=int)

    # Fill matrix
    for alert in alerts:
        codes_in_alert = [c.strip() for c in alert['codes'] if c and c.strip() in code_idx]
        for i in range(len(codes_in_alert)):
            for j in range(i, len(codes_in_alert)):
                idx_i = code_idx[codes_in_alert[i]]
                idx_j = code_idx[codes_in_alert[j]]
                matrix[idx_i, idx_j] += 1
                if idx_i != idx_j:
                    matrix[idx_j, idx_i] += 1  # symmetric

    return codes, matrix

def hierarchical_cluster_cooccurrence(alerts, plot_dendrogram=True, max_d=0.7):
    """
    Perform hierarchical clustering on codes using co-occurrence analysis.
    Returns:
        codes: list of codes
        clusters: cluster labels for each code
    """
    codes, co_matrix = build_cooccurrence_matrix(alerts)
    # Normalize to get similarity (divide by max co-occurrence for each code)
    norm_matrix = co_matrix / np.maximum(co_matrix.max(axis=1, keepdims=True), 1)
    # Convert similarity to distance
    dist_matrix = 1 - norm_matrix
    # Condensed distance matrix for linkage
    condensed = dist_matrix[np.triu_indices(len(codes), k=1)]
    # Hierarchical clustering
    Z = linkage(condensed, method='average')
    # Plot dendrogram
    if plot_dendrogram:
        plt.figure(figsize=(10, 6))
        dendrogram(Z, labels=codes, leaf_rotation=90)
        plt.title("Code Hierarchy (Co-occurrence Dendrogram)")
        plt.tight_layout()
        plt.show()
    # Assign clusters (optional, based on max_d threshold)
    clusters = fcluster(Z, t=max_d, criterion='distance')
    return codes, clusters

def print_clusters(codes, clusters, class_counts=None):
    """
    Print codes grouped by cluster label.
    Output format:
    Cluster N (number of classes, number of alerts): class1, class2, ...
    """
    from collections import defaultdict

    cluster_dict = defaultdict(list)
    for code, cluster in zip(codes, clusters):
        cluster_dict[cluster].append(code)

    for idx, (cluster, code_list) in enumerate(sorted(cluster_dict.items()), 1):
        num_classes = len(code_list)
        num_alerts = 0
        if class_counts:
            num_alerts = sum(class_counts.get(code, 0) for code in code_list)
        print(f"Cluster {idx} ({num_classes} classes, {num_alerts} alerts): {', '.join(code_list)}")

# Example usage:
if __name__ == "__main__":
    codes = [
        "ASIA", "ASIA-PACIFIC", "ASIA-SOUTH-EAST-ASIA", "ASIA-MIDDLE-EAST",
        "ASIA-MIDDLE-EAST-IRAN", "ASIA-MIDDLE-EAST-ISRAEL", "EUROPE", "EUROPE-UK"
    ]
    tree = get_hierarchical_clusters(codes)
    print_hierarchy(tree)