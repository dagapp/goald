import requests
import json
import sys

def validate_html(file_path):
    validation_url = "https://validator.w3.org/nu/?out=json"

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    response = requests.post(validation_url, data=html_content.encode("utf-8"), headers={"Content-Type": "text/html; charset=utf-8"})

    if response.status_code == 200:
        results = response.json()
        formatted_json = json.dumps(results, indent=2)
        print(formatted_json)
    else:
        print(f"Ошибка при запросе к W3C API: {response.status_code}")

if len(sys.argv) > 1:
    validate_html("templates/" + sys.argv[1])
else:
    print("Не указан html файл")