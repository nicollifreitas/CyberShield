from dash import html, dcc
import dash_bootstrap_components as dbc
from cards import (
    card_tipos_ataque,
    card_ataques_ano,
    card_severidade,
    card_vulnerabilidades,
    card_perda_financeira,
    card_gravidade_pais,
    card_conclusoes,
)

def get_layout():
    return dbc.Container([
        # Header
        html.Div([
            html.H1("Análise de Ameaças Cibernéticas (2015–2024)"),
            html.P(
                "Dashboard interativo com visualizações e insights detalhados sobre tipos de ataque, severidade e impactos geográficos"),
        ], className="header-container"),

        # Tabs com os cards

        dcc.Tabs(
            id='tabs',
            value='tab-1',
            className="custom-tabs",
            children=[
                dcc.Tab(label="Tipos de Ataque", value='tab-1',
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        children=[card_tipos_ataque]),
                dcc.Tab(label="Ataques por Ano", value='tab-2',
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        children=[card_ataques_ano]),
                dcc.Tab(label="Severidade e Criticidade", value='tab-3',
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        children=[card_severidade]),
                dcc.Tab(label="Vulnerabilidades", value='tab-4',
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        children=[card_vulnerabilidades]),
                dcc.Tab(label="Perda Financeira", value='tab-5',
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        children=[card_perda_financeira]),
                dcc.Tab(label="Gravidade por País", value='tab-6',
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        children=[card_gravidade_pais]),
                dcc.Tab(label="Conclusões", value='tab-7',
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        children=[card_conclusoes]),
            ]),

        html.Br(),
        html.Footer("© 2025 Nicolli Carvalho Freitas",
                    className="footer")
    ], fluid=True)
