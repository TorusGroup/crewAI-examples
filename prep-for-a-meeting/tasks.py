from textwrap import dedent
from crewai import Task

class MeetingPreparationTasks:
    def research_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""
                Realizar uma pesquisa completa sobre o tópico da reunião, incluindo
                antecedentes dos participantes, pontos de dados relevantes e desenvolvimentos recentes.

                Participantes: {participants}
                Contexto da Reunião: {context}
            """),
            expected_output=dedent("""
                Um relatório detalhado de pesquisa cobrindo todos os aspectos relevantes do tópico da reunião.
            """),
            async_execution=True,
            agent=agent
        )

    def industry_analysis_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""
                Analisar as tendências atuais do setor, desafios e oportunidades
                relevantes para o contexto da reunião. Considere relatórios de mercado, desenvolvimentos recentes
                e opiniões de especialistas para fornecer uma visão abrangente do cenário do setor.

                Participantes: {participants}
                Contexto da Reunião: {context}
            """),
            expected_output=dedent("""
                Uma análise perspicaz que identifica principais tendências, potenciais desafios e oportunidades estratégicas.
            """),
            async_execution=True,
            agent=agent
        )

    def meeting_strategy_task(self, agent, context, objective):
        return Task(
            description=dedent(f"""
                Desenvolver pontos de discussão estratégicos, perguntas e ângulos de discussão
                para a reunião com base na pesquisa e análise do setor conduzidas.

                Contexto da Reunião: {context}
                Objetivo da Reunião: {objective}
            """),
            expected_output=dedent("""
                Relatório completo com uma lista de pontos de discussão chave, perguntas estratégicas
                a serem feitas para ajudar a alcançar o objetivo da reunião.
            """),
            agent=agent
        )

    def summary_and_briefing_task(self, agent, context, objective):
        return Task(
            description=dedent(f"""
                Compilar todas as descobertas da pesquisa, análise do setor e pontos de discussão estratégicos
                em um documento informativo e conciso para a reunião. Assegurar que o resumo seja fácil de entender e
                forneça aos participantes da reunião todas as informações e estratégias necessárias.

                Contexto da Reunião: {context}
                Objetivo da Reunião: {objective}
            """),
            expected_output=dedent("""
                Um documento de resumo bem estruturado que inclui seções para biografias dos participantes, visão geral do setor,
                pontos de discussão e recomendações estratégicas.
            """),
            agent=agent
        )
