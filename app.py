import dash
from layout import get_layout
from callbacks import register_callbacks

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = get_layout()

register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)
