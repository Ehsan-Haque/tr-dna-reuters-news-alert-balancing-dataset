from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def semantic_cluster_classes(class_names, class_counts, n_clusters=10, plot_graph=False):
    """
    Clusters class names based on semantic similarity using sentence embeddings.
    Returns a dictionary: {cluster_label: [class_names]}
    """
    # Load a pre-trained sentence transformer model
    model = SentenceTransformer(r"C:\tr-dna-reuters-news-alert-balancing-dataset\models\all-MiniLM-L6-v2")
    # Generate embeddings for each class name
    embeddings = model.encode(class_names)

    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=30)
    labels = kmeans.fit_predict(embeddings)

    # Group classes by cluster
    clusters = []
    for cluster_id in range(n_clusters):
        cluster_classes = [class_names[i] for i in range(len(class_names)) if labels[i] == cluster_id]
        cluster_count = sum(class_counts.get(cls, 0) for cls in cluster_classes)
        clusters.append({'classes': cluster_classes, 'count': cluster_count})

    # Sort clusters by number of alerts
    clusters.sort(key=lambda x: x['count'])

    if plot_graph:
        cluster_labels = [f"Cluster {i+1}" for i in range(n_clusters)]
        alert_counts = [c['count'] for c in clusters]
        plt.figure(figsize=(10, 6))
        plt.bar(cluster_labels, alert_counts, color='orange')
        plt.xlabel('Cluster')
        plt.ylabel('Number of Alerts')
        plt.title('Semantic Cluster vs Number of Alerts')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    return clusters