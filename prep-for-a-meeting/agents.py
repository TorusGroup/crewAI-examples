from textwrap import dedent
from crewai import Agent
from tools.ExaSearchTool import ExaSearchTool

class MeetingPreparationAgents():
    def research_agent(self):
        return Agent(
            role='Especialista em Pesquisa',
            goal='Realizar uma pesquisa completa sobre as pessoas e empresas envolvidas na reunião',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                Como Especialista em Pesquisa, sua missão é descobrir informações detalhadas
                sobre os indivíduos e entidades participantes da reunião. Seus insights
                fornecerão a base para a preparação estratégica da reunião."""),
            verbose=True,
            model="gpt-4o-mini"  # Adicionando a especificação do modelo
        )

    def industry_analysis_agent(self):
        return Agent(
            role='Analista de Indústria',
            goal='Analisar as tendências atuais do setor, desafios e oportunidades',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                Como Analista de Indústria, sua análise identificará as principais tendências,
                desafios enfrentados pelo setor e potenciais oportunidades que
                podem ser aproveitadas durante a reunião para vantagem estratégica."""),
            verbose=True,
            model="gpt-4o-mini"  # Adicionando a especificação do modelo
        )

    def meeting_strategy_agent(self):
        return Agent(
            role='Consultor de Estratégia de Reunião',
            goal='Desenvolver pontos de discussão, perguntas e ângulos estratégicos para a reunião',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                Como Consultor de Estratégia, sua experiência guiará o desenvolvimento de
                pontos de discussão, perguntas perspicazes e ângulos estratégicos
                para garantir que os objetivos da reunião sejam alcançados."""),
            verbose=True,
            model="gpt-4o-mini"  # Adicionando a especificação do modelo
        )

    def summary_and_briefing_agent(self):
        return Agent(
            role='Coordenador de Resumos',
            goal='Compilar todas as informações reunidas em um documento informativo e conciso',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                Como Coordenador de Resumos, seu papel é consolidar a pesquisa,
                análise e insights estratégicos."""),
            verbose=True,
            model="gpt-4o-mini"  # Adicionando a especificação do modelo
        )
