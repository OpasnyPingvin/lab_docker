from flask import Flask
from models import ItemModel

app = Flask(__name__)

@app.route('/')
def index():
    model = ItemModel()
    items = model.get_all_items() 
    
    html = "<h1>Список из Базы Данных</h1><ul>"
    for item in items:
        name = item['name']
        if isinstance(name, str):
            try:
                name = name.encode('latin1').decode('utf-8')
            except Exception:
                pass
        html += f"<li>{name}</li>"
    html += "</ul>"
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
