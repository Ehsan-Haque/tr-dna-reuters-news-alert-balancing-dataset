# tr-dna-reuters-news-alert-balancing-dataset

This tool reads a CSV file with columns: `serial`, `alert`, `codes`.  
It counts how many alerts belong to each class (codes can be space-separated), and also groups similar classes into semantic clusters using sentence embeddings.

---

## Features

- **Counts alerts per class** (even if an alert belongs to multiple classes)
- **Semantic clustering**: Groups similar classes using AI-based embeddings
- **Shows number of classes and total alerts in each cluster**
- **Clusters are sorted by total alert count (lowest first)**

---

## Usage

1. Place your CSV file at:
   ```
   C:\tr-dna-reuters-news-alert-balancing-dataset\topics_clean.csv
   ```
   The CSV should have columns: `serial`, `alert`, `codes`.

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download the model files for `all-MiniLM-L6-v2` from Hugging Face and place them in:
   ```
   C:\tr-dna-reuters-news-alert-balancing-dataset\models\all-MiniLM-L6-v2
   ```
   (See instructions in this README or ask for help if needed.)

4. Run the program:
   ```
   python src/main.py
   ```

---

## Example CSV

| serial | alert         | codes                       |
|--------|--------------|-----------------------------|
| 1      | Alert text 1 | ASIA ASXPAC DIS EASIA GEN   |
| 2      | Alert text 2 | JP NEWS1 QUAK               |

---

## Example Output

```
Alert counts by class:
ASIA: 1
ASXPAC: 1
DIS: 1
EASIA: 1
GEN: 1
JP: 1
NEWS1: 1
QUAK: 1

Total number of classes: 8

Semantic Clusters (sorted by alert count, showing up to 5 classes per cluster):
Cluster 3 (2 classes, 2 alerts): JP, NEWS1
Cluster 7 (2 classes, 2 alerts): QUAK, DIS
Cluster 12 (2 classes, 2 alerts): ASIA, EASIA
Cluster 15 (2 classes, 2 alerts): ASXPAC, GEN
...
```

---

## Model Download Instructions

If you cannot download the model automatically, do this:

1. Install [Git LFS](https://git-lfs.com/).
2. Open Command Prompt and run:
   ```
   git lfs install
   git clone https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 C:\python-csv-alert-counter\models\all-MiniLM-L6-v2
   ```
3. Or, download all files from the [model page](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) and place them in the folder above.

---

## Requirements

- Python 3.13
- `sentence-transformers`
- `scikit-learn`

Install with:
```
pip install -r requirements.txt
```

---

## Customization

- Change the number of clusters by editing `n_clusters` in `src/main.py`.
- Change the CSV file path by editing `filepath` in `src/main.py`.

---

## Troubleshooting

- If you see SSL or certificate errors, try updating `certifi` or manually downloading the model as described above.
- If you see a warning about "No sentence-transformers model found", make sure all model files are present in the correct folder.

---

## Architecture Overview

```
+-------------------------+
|    topics_clean.csv     |
| (serial, alert, codes)  |
+-----------+-------------+
            |
            v
+-------------------------+
|   CSV Reader Module     |
| (src/csv_reader.py)     |
+-----------+-------------+
            |
            v
+-------------------------+
|  Alert Counter Module   |
| (src/alert_counter.py)  |
+-----------+-------------+
            |
            v
+-------------------------+
|  Semantic Clustering    |
| (src/semantic_cluster.py)|
|  - Loads MiniLM model   |
+-----------+-------------+
            |
            v
+-------------------------+
|      Output/Utils       |
| (src/utils.py, main.py) |
+-------------------------+
            |
            v
+-------------------------+
|   Console Output        |
+-------------------------+
```

**Flow:**
1. The CSV is read and parsed.
2. Alerts are counted per class.
3. Classes are embedded and clustered semantically.
4. Results are formatted and printed.

---