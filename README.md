# tr-dna-reuters-news-alert-balancing-dataset

This project processes a CSV file of news alerts, each with associated codes (classes), and provides two clustering methods for analyzing the codes:

## Features

- **Semantic Clustering:**  
  Groups codes based on their semantic meaning using sentence embeddings and KMeans clustering. You can control the number of clusters (default: 30).

- **Hierarchical Clustering (Co-occurrence Analysis):**  
  Groups codes that frequently appear together in the same alert using hierarchical clustering. The number of clusters can be adjusted by changing the `max_d` parameter.

- **Visualization:**  
  Plots a bar chart showing the number of alerts in each semantic cluster.

- **Flexible Input:**  
  Reads a CSV file with columns: `serial`, `alert`, `codes`. The `codes` column should contain space-separated codes (e.g., `ASIA MIDDLEEAST IRAN ISRAEL WAR GASPRICE`).

## How It Works

1. **Read Data:**  
   Loads alerts and splits the codes column by spaces.

2. **Count Alerts:**  
   Counts how many alerts belong to each code.

3. **Semantic Clustering:**  
   - Uses sentence embeddings to represent codes.
   - Applies KMeans to group codes by meaning.

4. **Hierarchical Clustering:**  
   - Builds a co-occurrence matrix of codes.
   - Uses hierarchical clustering to group codes that often appear together.

5. **Visualization:**  
   - Plots the number of alerts per semantic cluster.

## Usage

1. Place your CSV file (e.g., `topics_clean.csv`) in the project directory.
2. Update the file path in `main.py` if needed.
3. Run the main script:
   ```
   python src/main.py
   ```
4. Adjust the number of semantic clusters (`n_clusters`) or hierarchical cluster threshold (`max_d`) in `main.py` as needed.

## Example CSV Format

| serial | alert                | codes                               |
|--------|----------------------|-------------------------------------|
| 1      | Iran vs Israel war   | ASIA MIDDLEEAST IRAN ISRAEL WAR     |
| 2      | Gas price up         | GASPRICE STOCKPRICE                 |

## Requirements

- Python 3.8+
- `scikit-learn`
- `sentence-transformers`
- `matplotlib`
- `scipy`
- (See `requirements.txt`)

## Notes

- The project does **not** reconstruct the true parent-child hierarchy of codes; it groups codes by co-occurrence or semantic similarity.
- The number of clusters for each method is user-configurable.

## License

MIT License

---

Let me know if you want to add usage examples, architecture diagrams, or