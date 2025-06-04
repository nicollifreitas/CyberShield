import dash
from layout import get_layout
from callbacks import register_callbacks

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Expõe o servidor Flask embutido para o Gunicorn
server = app.server

app.layout = get_layout()

register_callbacks(app)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port, debug=True)