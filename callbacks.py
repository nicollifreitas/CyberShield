from dash.dependencies import Input, Output
from graphs import create_visao_geral_fig, create_ataques_por_ano_fig, create_severidade_fig, create_criticidade_ponderada_fig, create_vulnerabilidades_fig, create_perda_financeira_pais_fig, create_gravidade_pais_fig
import pandas as pd
import dash

df = pd.read_csv('data/Global_Cybersecurity_Threats_2015-2024.csv')

def register_callbacks(app):
    @app.callback(
        Output('visao-geral-graph', 'figure'),
        Input('tabs', 'value')
    )
    def update_visao_geral(tab):
        if tab == 'tab-1':
            return create_visao_geral_fig(df)
        return dash.no_update

    @app.callback(
        Output('ataques-por-ano-graph', 'figure'),
        Input('tabs', 'value')
    )
    def update_ataques_por_ano(tab):
        if tab == 'tab-2':
            return create_ataques_por_ano_fig(df)
        return dash.no_update

    @app.callback(
        Output('severidade-graph', 'figure'),
        Input('tabs', 'value')
    )
    def update_severidade(tab):
        if tab == 'tab-3':
            return create_severidade_fig(df)
        return dash.no_update

    @app.callback(
        Output('criticidade-graph', 'figure'),
        Input('tabs', 'value')
    )
    def update_criticidade(tab):
        if tab == 'tab-3':
            return create_criticidade_ponderada_fig(df)
        return dash.no_update

    @app.callback(
        Output('vulnerabilidades-graph', 'figure'),
        Input('tabs', 'value')
    )
    def update_vulnerabilidades(tab):
        if tab == 'tab-4':
            return create_vulnerabilidades_fig(df)
        return dash.no_update

    @app.callback(
        Output('perda-financeira-graph', 'figure'),
        Input('tabs', 'value')
    )
    def update_perda_financeira(tab):
        if tab == 'tab-5':
            return create_perda_financeira_pais_fig(df)
        return dash.no_update

    @app.callback(
        Output('gravidade-pais-graph', 'figure'),
        Input('tabs', 'value')
    )
    def update_gravidade_pais(tab):
        if tab == 'tab-6':
            return create_gravidade_pais_fig(df)
        return dash.no_update

