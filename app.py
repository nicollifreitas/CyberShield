import os
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
    is_render = os.environ.get("RENDER", False)

    app.run(
        host="0.0.0.0" if is_render else "127.0.0.1",
        port=port,
        debug=False
    )
