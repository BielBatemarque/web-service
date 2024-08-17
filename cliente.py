import requests

def main():
    response_text = requests.get('http://localhost:5000/olamundo')
    print(response_text.text)

    response_xml = requests.get('http://localhost:5000/olamundo/xml')
    print(response_xml.text)

    response_json = requests.get('http://localhost:5000/olamundo/json')
    print(response_json.json())

    response_contato = requests.get('http://localhost:5000/contato/json')
    print(response_contato.json())

if __name__ == '__main__':
    main()