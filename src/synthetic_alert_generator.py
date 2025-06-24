import os
import requests

# Set your Azure OpenAI endpoint and API key
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g., "https://<resource-name>.openai.azure.com/openai/deployments/<deployment-name>/chat/completions?api-version=2024-02-15-preview"
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")    # Set this in your environment variables

def generate_synthetic_alerts(cluster_name, codes, seed_alerts, num_alerts=5):
    """
    Generate synthetic alerts using Azure OpenAI LLM.

    Args:
        cluster_name (str): Name or ID of the cluster.
        codes (list): List of class codes in the cluster.
        seed_alerts (list): List of existing alerts in the cluster.
        num_alerts (int): Number of synthetic alerts to generate.

    Returns:
        str: The generated synthetic alerts as a string.
    """
    prompt = (
        f"Cluster: {cluster_name}\n"
        f"Codes: {', '.join(codes)}\n"
        f"Existing alerts:\n"
        + "\n".join(f"- {alert}" for alert in seed_alerts)
        + f"\n\nGenerate {num_alerts} new, grammatically correct alerts that are semantically similar to the above."
    )

    headers = {
        "api-key": AZURE_OPENAI_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates news alerts."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 512,
        "temperature": 0.8,
        "n": 1
    }

    response = requests.post(AZURE_OPENAI_ENDPOINT, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    return result["choices"][0]["message"]["content"]

# Example usage (uncomment to test):
# synthetic_alerts = generate_synthetic_alerts("Cluster 1", ["CODE1", "CODE2"], ["Alert 1", "Alert 2"])
# print(synthetic_alerts)