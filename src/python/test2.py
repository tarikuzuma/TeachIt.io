file_path = "test.html"

with open(file_path, 'r', encoding='utf-8') as file:
    html_source = file.read()
    print(html_source)