import os
import requests
import time

def fetch_top_models():
    url = "https://huggingface.co/api/models?sort=downloads&direction=-1&limit=10"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def generate_report(models):
    # Generate a string for each model
    model_items = []
    for i, model in enumerate(models, 1):
        model_items.append(f"{i}. {model['modelId']} - {model['downloads']} downloads")

    # Combine the model items into a single string
    model_items_str = "\n".join(model_items)

    # Append the model items to the file
    report_file_path = "/reports/top_models_report.txt"
    with open(report_file_path, "a") as f:
        f.write(model_items_str)
        f.write("\n\n")  # Add an extra line to separate the reports

    print(f"Report generated and appended to {report_file_path}")

def main():
    while True:
        models = fetch_top_models()
        generate_report(models)
        time.sleep(3600)  # Sleep for 3600 seconds (1 hour)

if __name__ == "__main__":
    main()
