from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import MeetingPreparationTasks
from agents import MeetingPreparationAgents

tasks = MeetingPreparationTasks()
agents = MeetingPreparationAgents()

print("## Bem-vindo à Equipe de Preparação de Reuniões")
print('-------------------------------')
participants = input("Quais são os e-mails dos participantes (além de você) na reunião?\n")
context = input("Qual é o contexto da reunião?\n")
objective = input("Qual é o seu objetivo para esta reunião?\n")

# Criar Agentes
researcher_agent = agents.research_agent()
industry_analyst_agent = agents.industry_analysis_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

# Criar Tarefas
research = tasks.research_task(researcher_agent, participants, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, context)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

meeting_strategy.context = [research, industry_analysis]
summary_and_briefing.context = [research, industry_analysis, meeting_strategy]

# Criar Equipe responsável por Copiar
crew = Crew(
    agents=[
        researcher_agent,
        industry_analyst_agent,
        meeting_strategy_agent,
        summary_and_briefing_agent
    ],
    tasks=[
        research,
        industry_analysis,
        meeting_strategy,
        summary_and_briefing
    ]
)

game = crew.kickoff()

# Imprimir resultados
print("\n\n################################################")
print("## Aqui está o resultado")
print("################################################\n")
print(game)
