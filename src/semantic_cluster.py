from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

def semantic_cluster_classes(class_names, n_clusters=30):
    """
    Clusters class names based on semantic similarity using sentence embeddings.
    Returns a dictionary: {cluster_label: [class_names]}
    """
    # Load a pre-trained sentence transformer model
    model = SentenceTransformer(r"C:\tr-dna-reuters-news-alert-balancing-dataset\models\all-MiniLM-L6-v2")
    # Generate embeddings for each class name
    embeddings = model.encode(class_names)
    # Cluster the embeddings
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    # Group class names by cluster
    clusters = {}
    for class_name, label in zip(class_names, labels):
        clusters.setdefault(label, []).append(class_name)
    return clusters