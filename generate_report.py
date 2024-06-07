import requests

def fetch_top_models():
    url = "https://huggingface.co/api/models?sort=downloads&direction=-1&limit=10"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def generate_report(models):
    report = "Top 10 Hugging Face Models by Downloads:\n\n"
    for i, model in enumerate(models, 1):
        report += f"{i}. {model['modelId']} - {model['downloads']} downloads\n"
    return report

def main():
    models = fetch_top_models()
    report = generate_report(models)
    with open("/reports/top_models_report.txt", "w") as f:
        f.write(report)
    print("Report generated and saved to /reports/top_models_report.txt")

if __name__ == "__main__":
    main()

