from dash import dcc, html
import dash_bootstrap_components as dbc

# Card - Tipos de Ataque
card_tipos_ataque = dbc.Card(
    dbc.CardBody([
        dcc.Graph(id='visao-geral-graph'),
        html.P(
            "As médias das variáveis numéricas são relativamente próximas entre os diferentes tipos de ataque, "
            "com variações geralmente inferiores a 7%. Isso indica que o tipo de ataque não é um fator determinante "
            "para variações significativas nessas métricas.",
            className="card-text"
        ),
    ]),
    className="custom-card"
)

# Card - Ataques por Ano
card_ataques_ano = dbc.Card(
    dbc.CardBody([
        dcc.Graph(id='ataques-por-ano-graph'),
        html.Ul([
            html.Li("O número total de ataques variou ao longo dos anos, com picos em 2017, 2018, 2020 e 2022."),
            html.Li("O ano com menos ataques foi 2019, evidenciando uma queda significativa nesse período."),
            html.Li("Após 2019, observa-se uma recuperação no número de ataques até estabilizar entre 299 e 318 nos anos seguintes."),
            html.Li("A diversidade de tipos de ataques continua alta, exigindo estratégias de defesa cibernética amplas e específicas."),
        ])
    ]),
    className="custom-card"
)

# Card - Severidade
card_severidade = dbc.Card(
    dbc.CardBody([
        html.P(
            "Score normalizado (0 a 1) compara a severidade dos tipos de ataques nas métricas: "
            "Impacto Financeiro, Usuários Afetados e Tempo de Resolução. "
            "A partir disso, é possível saber quais tipos de ataque são, em média, mais severos.",
            className="alert-danger"
        ),
        dcc.Graph(id='severidade-graph'),
        html.P(
            "Os ataques do tipo Man-in-the-Middle se destacam como os mais severos no geral, apresentando altos "
            "impactos em todas as métricas. DDoS é o que gera maior prejuízo financeiro, enquanto Malware e SQL "
            "Injection exigem maior tempo de resolução. Já o Phishing apresenta os menores níveis de severidade, "
            "sendo relativamente fácil de conter e com impactos mais baixos.",
            className="alert-danger"
        ),
        dcc.Graph(id='criticidade-graph'),
        html.P(
            "O gráfico apresenta a criticidade ponderada por tipo de ataque cibernético, calculada com base em três métricas normalizadas: "
            "impacto financeiro (50%), usuários afetados (30%) e tempo de resolução (20%). Esse método de ponderação permite considerar a importância relativa de cada fator, oferecendo uma avaliação mais equilibrada da gravidade de cada tipo de ameaça.\n\n"
            "A análise mostra que ataques do tipo Man-in-the-Middle de fato possuem a maior criticidade. Em seguida, vêm os ataques DDoS e SQL Injection, que também apresentam criticidade significativa, embora por razões diferentes. Já ataques como Phishing e Ransomware aparecem com menor criticidade na análise ponderada, indicando menor impacto geral.",
            className="alert-danger"
        ),
    ]),
    className="custom-card"
)

# Card - Vulnerabilidades
card_vulnerabilidades = dbc.Card(
    dbc.CardBody([
        dcc.Graph(id='vulnerabilidades-graph'),
        html.P([
            "O gráfico acima revela que alguns pares específicos ocorrem com maior frequência:",
            html.Br(), html.Br(),
            "• Phishing ↔ Zero-day: combinação mais recorrente no conjunto de dados.",
            html.Br(),
            "• DDoS ↔ Weak Passwords: também se destaca entre as associações mais comuns.",
            html.Br(), html.Br(),
            "No entanto, mesmo com a presença de algumas combinações frequentes, a maioria dos tipos de ataque e vulnerabilidades aparece cruzada com diversas outras categorias. ",
        "Isso dilui a força estatística geral das associações, como evidenciado pelos valores baixos do V de Cramér apresentados no arquivo notebook 'eda_and_statistical_tests'.",
            html.Br(), html.Br(),
            "Ou seja, embora existam pares frequentes, não há uma dependência estatística global forte entre as variáveis categóricas analisadas. ",
            "Isso pode indicar que:",
            html.Br(), html.Br(),
            "🔁 Um mesmo tipo de ataque pode explorar diferentes vulnerabilidades.",
            html.Br(),
            "🔁 Uma mesma vulnerabilidade pode ser explorada por diversos tipos de ataque.",
        ], className="card-text")
    ]),
    className="custom-card"
)

# Card - Perda Financeira
card_perda_financeira = dbc.Card(
    dbc.CardBody([
        dcc.Graph(id='perda-financeira-graph'),
        html.P(
            "A análise das perdas por país mostra que, embora os valores sejam próximos, a Alemanha lidera em perda média, indicando menos incidentes, porém com grande impacto individual, sugerindo vulnerabilidades críticas. "
            "O Reino Unido apresenta perda total e média ligeiramente maiores, refletindo maior volume de incidentes moderados, demandando foco na escala de resposta. "
            "Brasil, Austrália e EUA exibem perdas consistentes, levemente acima da média, destacando a necessidade contínua de prevenção e resposta. "
            "Índia e China têm perdas um pouco menores, o que pode indicar incidentes menos severos, subnotificação ou menor exposição. "
            "Em resumo, países com maior perda média devem focar na identificação de vulnerabilidades críticas, enquanto aqueles com valores equilibrados precisam manter estratégias robustas de resposta e mitigação.",
            className="card-text"
        ),
    ]),
    className="custom-card"
)

# Card - Gravidade por País
card_gravidade_pais = dbc.Card(
    dbc.CardBody([
        html.P(
            "Score normalizado (0 a 1) compara a severidade média por país nas métricas: "
            "Impacto Financeiro, Usuários Afetados e Tempo de Resolução.",
            className="alert-danger"
        ),
        dcc.Graph(id='gravidade-pais-graph'),
        html.P(
            "O Brasil se destaca como o país com maior gravidade média em tempo de resolução e usuários afetados, indicando ataques mais severos. "
            "A Alemanha apresenta altos custos por ataque, enquanto a China sofre com longos tempos de resolução. "
            "Já a Índia possui os menores valores em todas as frentes, sugerindo baixa severidade ou subnotificação. "
            "O heatmap facilita a identificação de padrões e perfis de impacto, sendo eficaz para análises comparativas rápidas entre países.",
            className="card-text"
        ),
    ]),
    className="custom-card"
)

# Card - Análise Geográfica
card_analise_geografica = dbc.Card(
    dbc.CardBody([
        html.H4("Análise Geográfica", className="card-title"),
        html.P(
            "A análise geográfica revela que países economicamente mais desenvolvidos tendem a registrar maior número de incidentes, "
            "possivelmente devido a maior exposição digital e melhor capacidade de monitoramento. "
            "Entretanto, o Brasil aparece como destaque em severidade, indicando vulnerabilidades específicas que demandam atenção. "
            "Esse panorama reforça a importância de estratégias de defesa cibernética adaptadas a contextos locais.",
            className="card-text"
        ),
    ]),
    className="custom-card"
)

# Card - Conclusões
card_conclusoes = dbc.Card(
    dbc.CardBody([
        html.H2('📝 Conclusões', className='h2-title'),

        html.P(
            "O projeto de análise das ameaças cibernéticas entre 2015 e 2024 forneceu uma visão abrangente sobre o comportamento, impacto e padrões dos ataques digitais ao longo do tempo.",
            className='card-text'
        ),

        html.H3('📊 Principais Resultados e Insights', className='h3-title'),

        html.H4('Frequência e Severidade dos Ataques:', className='h4-title'),
        html.P([
            "A análise mostrou que ataques do tipo ",
            html.B('Man-in-the-Middle'),
            " apresentam a maior criticidade geral, considerando impacto financeiro, número de usuários afetados e tempo de resolução. Ataques ",
            html.B('DDoS'),
            " geram o maior prejuízo financeiro médio, enquanto ",
            html.B('Malware'),
            " e ",
            html.B('SQL Injection'),
            " demandam mais tempo para resolução. Já ataques ",
            html.B('Phishing'),
            " tendem a ser os menos severos. Essa diferenciação ajuda a priorizar esforços e alocar recursos na mitigação das ameaças mais impactantes."
        ], className='card-text'),

        html.H4('Padrões Temporais:', className='h4-title'),
        html.P(
            "Observou-se que o número total de ataques variou significativamente ao longo dos anos, com picos notáveis em 2017, 2018, 2020 e 2022, e uma queda acentuada em 2019. Essa oscilação sugere a influência de fatores externos, como evolução tecnológica, legislação, ou campanhas de segurança, que podem afetar o volume de incidentes.",
            className='card-text'
        ),

        html.H4('Associação entre Ataques e Vulnerabilidades:', className='h4-title'),
        html.P([
            "O cruzamento entre tipos de ataque e vulnerabilidades revelou algumas combinações frequentes, como ",
            html.B('Phishing ↔ Zero-day'),
            " e ",
            html.B('DDoS ↔ Senhas Fracas'),
            ". No entanto, a ausência de uma associação estatística forte indica que ataques exploram múltiplas vulnerabilidades e que vulnerabilidades são alvo de diferentes tipos de ataques, refletindo a complexidade e diversidade do cenário."
        ], className='card-text'),

        html.H4('Análise Geográfica:', className='h4-title'),
        html.P([
            "Países como ",
            html.B('Alemanha'),
            " e ",
            html.B('Reino Unido'),
            " apresentam altos valores de perda financeira média e total, com a Alemanha tendo menos incidentes porém mais impactantes, enquanto o Reino Unido tem maior volume com impacto moderado. ",
            html.B('Brasil'),
            " se destaca com maior severidade média em quase todas as métricas, evidenciando necessidade de fortalecimento em segurança cibernética. Já a ",
            html.B('Índia'),
            " mostrou as menores perdas, o que pode refletir menor exposição, subnotificação ou diferentes estratégias de mitigação."
        ], className='card-text'),

        html.H4('Avaliação da Correlação e Associação:', className='h4-title'),
        html.P(
            "Os testes estatísticos indicam que não há correlação significativa entre variáveis categóricas, e as variáveis numéricas relacionadas ao impacto financeiro, usuários afetados e tempo de resolução apresentam baixa correlação entre si. Isso sugere que o impacto dos ataques depende de fatores não capturados pela base de dados, como características específicas das vítimas, resposta organizacional ou outros elementos contextuais.",
            className='card-text'
        ),

        html.H4('Limitações para Modelagem Preditiva:', className='h4-title'),
        html.P(
            "Devido à alta variabilidade, falta de associações estatísticas relevantes e ausência de variáveis críticas, os modelos preditivos desenvolvidos apresentaram desempenho insatisfatório, com altos erros e baixa acurácia na classificação de níveis de impacto. Isso reforça que a base é mais adequada para análises exploratórias e descritivas do que para previsão quantitativa.",
            className='card-text'
        ),

        html.H3('✅ Considerações Finais', className='h3-title'),
        html.P(
            "Este estudo forneceu um diagnóstico valioso para entender o cenário das ameaças cibernéticas, destacando quais tipos de ataque são mais severos, quando ocorrem picos, quais países são mais afetados e como as vulnerabilidades se relacionam com os incidentes. A análise reforça a complexidade e heterogeneidade das ameaças digitais, indicando que estratégias de defesa precisam ser multifacetadas e continuamente atualizadas.",
            className='card-text'
        ),
        html.P(
            "Assim, as informações geradas podem apoiar empresas e governos a priorizar investimentos em segurança, otimizar políticas de resposta e fortalecer a resiliência frente ao crescente desafio das ameaças cibernéticas.",
            className='paragraph-italic'
        ),
    ]),
    className="custom-card"
)
