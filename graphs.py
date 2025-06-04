import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

DARK_BG = '#272727'
DARK_CARD = '#272727'
DARK_TEXT = '#d1d1e9'
ACCENT_COLOR = '#0077b6'
SECONDARY_COLOR = '#6c757d'
DANGER_COLOR = '#ff4d6d'

# Função auxiliar para barras no subplot
def plot_bar(fig, x, y, text=None, title=None, row=1, col=1, showlegend=False):
    bar = go.Bar(
        x=x,
        y=y,
        text=text,
        marker_color=ACCENT_COLOR,
        textposition='inside',
        textfont_color='white',
        showlegend=showlegend
    )
    fig.add_trace(bar, row=row, col=col)
    if title:
        fig.layout.annotations[(row-1)*2 + (col-1)].text = title

# Atualizar layouts de todas as figuras para tema escuro
def update_fig_layout(fig, height=None):
    fig.update_layout(
        plot_bgcolor=DARK_CARD,
        paper_bgcolor=DARK_BG,
        font_color=DARK_TEXT,
        title_font_color=ACCENT_COLOR,
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
    )
    if height:
        fig.update_layout(height=height)
    return fig

# Função 1: Visão Geral dos tipos de ataque (subplots 2x2)
def create_visao_geral_fig(df):
    ataques_frequentes = df['Attack Type'].value_counts().reset_index()
    ataques_frequentes.columns = ['Attack Type', 'Count']

    ataques_usuarios_afetados = df.groupby('Attack Type')['Number of Affected Users'].mean().sort_values(ascending=False).reset_index()
    ataques_tempo_resp = df.groupby('Attack Type')['Incident Resolution Time (in Hours)'].mean().sort_values(ascending=False).reset_index()
    ataques_impacto_fin = df.groupby('Attack Type')['Financial Loss (in Million $)'].mean().sort_values(ascending=False).reset_index()

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[
            "Mais Frequentes",
            "Média - Usuários Afetados",
            "Média - Tempo de Resposta (horas)",
            "Média - Impacto Financeiro (milhões $)"
        ]
    )

    plot_bar(fig, ataques_frequentes['Attack Type'], ataques_frequentes['Count'], text=ataques_frequentes['Count'], row=1, col=1)
    plot_bar(fig, ataques_usuarios_afetados['Attack Type'], ataques_usuarios_afetados['Number of Affected Users'], text=ataques_usuarios_afetados['Number of Affected Users'].map('{:.1f}'.format), row=1, col=2)
    plot_bar(fig, ataques_tempo_resp['Attack Type'], ataques_tempo_resp['Incident Resolution Time (in Hours)'], text=ataques_tempo_resp['Incident Resolution Time (in Hours)'].round(2), row=2, col=1)
    plot_bar(fig, ataques_impacto_fin['Attack Type'], ataques_impacto_fin['Financial Loss (in Million $)'], text=ataques_impacto_fin['Financial Loss (in Million $)'].round(2), row=2, col=2)

    fig.update_layout(
        title_text="Visão Geral dos Tipos de Ataques",
        title_x=0.5,
        uniformtext_mode='hide',
        height=700,
        showlegend=False,
        margin=dict(t=80)
    )
    return update_fig_layout(fig)

# Função 2: Ataques por ano
def create_ataques_por_ano_fig(df):
    ataques_por_ano = df.groupby(['Year', 'Attack Type']).size().reset_index(name='Count')
    total_por_ano = ataques_por_ano.groupby('Year')['Count'].sum().reset_index()

    fig = px.bar(
        ataques_por_ano,
        x='Year',
        y='Count',
        text='Count',
        color='Attack Type',
        title='Número de ataques por tipo e por ano',
        labels={'Year': 'Ano', 'Count': 'Número de ataques', 'Attack Type': 'Tipo de ataque'},
    )

    fig.update_layout(
        title_x=0.5
    )

    for i, row in total_por_ano.iterrows():
        fig.add_annotation(
            x=row['Year'],
            y=row['Count'],
            text=str(row['Count']),
            showarrow=False,
            yshift=10,
            font=dict(color='white', size=12)
        )
    return update_fig_layout(fig)

# Função 3: Severidade dos ataques (barras normalizadas)
def create_severidade_fig(df):
    df_tipos_ataques = df.groupby('Attack Type').agg({
        'Financial Loss (in Million $)': 'mean',
        'Number of Affected Users': 'mean',
        'Incident Resolution Time (in Hours)': 'mean'
    }).reset_index()

    scaler = MinMaxScaler()
    valores_normalizados = scaler.fit_transform(df_tipos_ataques[['Financial Loss (in Million $)', 'Number of Affected Users', 'Incident Resolution Time (in Hours)']])
    df_normalizado = pd.DataFrame(valores_normalizados, columns=['Financial_Loss_Score', 'Users_Affected_Score', 'Resolution_Time_Score'])
    df_final = pd.concat([df_tipos_ataques[['Attack Type']], df_normalizado], axis=1)
    df_dinamizado = df_final.melt(id_vars='Attack Type', var_name='Metric', value_name='Score')

    fig = px.bar(
        df_dinamizado,
        x='Attack Type',
        y='Score',
        color='Metric',
        barmode='group',
        labels={'Score': 'Score normalizado', 'Attack Type': 'Tipo de ataque'},
        color_discrete_sequence=[ACCENT_COLOR, DANGER_COLOR, '#00f5d4']
    )

    fig.update_layout(
        title={
            'text': 'Comparativo de severidade por tipo de ataque<br><sup>Scores relativos (0-1), onde 1 = valor máximo observado em cada métrica</sup>',
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_tickangle=-45,
        yaxis_range=[0, 1],
    )
    return update_fig_layout(fig)

# Função 4: Criticidade ponderada (treemap)
def create_criticidade_ponderada_fig(df):
    df_tipos_ataques = df.groupby('Attack Type').agg({
        'Financial Loss (in Million $)': 'mean',
        'Number of Affected Users': 'mean',
        'Incident Resolution Time (in Hours)': 'mean'
    }).reset_index()

    scaler = MinMaxScaler()
    valores_normalizados = scaler.fit_transform(df_tipos_ataques[['Financial Loss (in Million $)', 'Number of Affected Users', 'Incident Resolution Time (in Hours)']])
    df_normalizado = pd.DataFrame(valores_normalizados, columns=['Financial_Loss_Score', 'Users_Affected_Score', 'Resolution_Time_Score'])
    df_final = pd.concat([df_tipos_ataques[['Attack Type']], df_normalizado], axis=1)

    df_final['Criticidade'] = (
        0.5 * df_final['Financial_Loss_Score'] +
        0.3 * df_final['Users_Affected_Score'] +
        0.2 * df_final['Resolution_Time_Score']
    )

    fig = px.treemap(
        df_final,
        path=['Attack Type'],
        values='Criticidade',
        color='Criticidade',
        color_continuous_scale='Teal',
        title='Criticidade por tipo de ataque (Ponderada)',
    )

    fig.update_layout(
        title_x=0.5,
        annotations=[dict(
            x=0.5, y=-0.15,
            text="<b>Criticidade:</b> 50% Impacto Financeiro + 30% Usuários Afetados + 20% Tempo de Resolução (valores normalizados)",
            showarrow=False,
            xref="paper", yref="paper",
            font=dict(size=10, color=DARK_TEXT)
        )]
    )

    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>Criticidade: %{value:.2f}<extra></extra>"
    )
    return update_fig_layout(fig)

# Função 5: Vulnerabilidades (heatmap)
def create_vulnerabilidades_fig(df):
    cross_tab = pd.crosstab(df['Attack Type'], df['Security Vulnerability Type'])
    fig = px.imshow(
        cross_tab,
        aspect="auto",
        title='Relação entre Ataques e Vulnerabilidades',
        color_continuous_scale='Blues'
    )
    fig.update_layout(title_x=0.5)
    return update_fig_layout(fig)

# Função 6: Perda financeira por país (scatter)
def create_perda_financeira_pais_fig(df):
    df_grouped = df.groupby('Country').agg({
        'Financial Loss (in Million $)': ['mean', 'sum']
    }).reset_index()
    df_grouped.columns = ['Country', 'Avg_Financial_Loss', 'Total_Financial_Loss']

    fig = px.scatter(
        df_grouped,
        x='Avg_Financial_Loss',
        y='Total_Financial_Loss',
        text='Country',
        size='Total_Financial_Loss',
        color='Avg_Financial_Loss',
        color_continuous_scale='Reds',
        labels={
            'Avg_Financial_Loss': 'Perda Financeira Média ($M)',
            'Total_Financial_Loss': 'Perda Financeira Total ($M)'
        },
        title='Perda Financeira Média vs Total por País'
    )
    fig.update_traces(
        textposition='top center',
        marker=dict(line=dict(width=1, color='DarkSlateGrey'))
    )
    fig.update_layout(title_x=0.5)
    return update_fig_layout(fig)

# Função 7: Gravidade dos ataques por país (heatmap)
def create_gravidade_pais_fig(df):
    df_paises = df.groupby('Country').agg({
        'Financial Loss (in Million $)': 'mean',
        'Number of Affected Users': 'mean',
        'Incident Resolution Time (in Hours)': 'mean'
    }).reset_index()

    scaler = MinMaxScaler()
    valores_normalizados = scaler.fit_transform(df_paises[['Financial Loss (in Million $)', 'Number of Affected Users', 'Incident Resolution Time (in Hours)']])
    df_normalizado = pd.DataFrame(valores_normalizados, columns=['Financial_Loss_Score', 'Users_Affected_Score', 'Resolution_Time_Score'])
    df_final = (pd.concat([df_paises[['Country']], df_normalizado], axis=1)).set_index('Country')

    fig = px.imshow(
        df_final,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale='deep',
        title="Gravidade dos ataques por país (scores normalizados)"
    )
    fig.update_layout(title_x=0.5)
    return update_fig_layout(fig)