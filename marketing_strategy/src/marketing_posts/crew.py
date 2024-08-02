from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Descomente a linha abaixo para usar um exemplo de ferramenta personalizada
# from marketing_posts.tools.custom_tool import MyCustomTool

# Consulte nossa documentação de ferramentas para mais informações sobre como usá-las
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field

class MarketStrategy(BaseModel):
    """Modelo de estratégia de mercado"""
    name: str = Field(..., description="Nome da estratégia de mercado")
    tatics: List[str] = Field(..., description="Lista de táticas a serem usadas na estratégia de mercado")
    channels: List[str] = Field(..., description="Lista de canais a serem usados na estratégia de mercado")
    KPIs: List[str] = Field(..., description="Lista de KPIs a serem usados na estratégia de mercado")

class CampaignIdea(BaseModel):
    """Modelo de ideia de campanha"""
    name: str = Field(..., description="Nome da ideia de campanha")
    description: str = Field(..., description="Descrição da ideia de campanha")
    audience: str = Field(..., description="Público-alvo da ideia de campanha")
    channel: str = Field(..., description="Canal da ideia de campanha")

class Copy(BaseModel):
    """Modelo de cópia"""
    title: str = Field(..., description="Título da cópia")
    body: str = Field(..., description="Corpo da cópia")

@CrewBase
class MarketingPostsCrew():
    """Equipe MarketingPosts"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def lead_market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_market_analyst'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            memory=False,
        )

    @agent
    def chief_marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_marketing_strategist'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            memory=False,
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_content_creator'],
            verbose=True,
            memory=False,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.lead_market_analyst()
        )

    @task
    def project_understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_understanding_task'],
            agent=self.chief_marketing_strategist()
        )

    @task
    def marketing_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_strategy_task'],
            agent=self.chief_marketing_strategist(),
            output_json=MarketStrategy
        )

    @task
    def campaign_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['campaign_idea_task'],
            agent=self.creative_content_creator(),
            output_json=CampaignIdea
        )

    @task
    def copy_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['copy_creation_task'],
            agent=self.creative_content_creator(),
            context=[self.marketing_strategy_task(), self.campaign_idea_task()],
            output_json=Copy
        )

    @crew
    def crew(self) -> Crew:
        """Cria a equipe MarketingPosts"""
        return Crew(
            agents=self.agents, # Criado automaticamente pelo decorador @agent
            tasks=self.tasks, # Criado automaticamente pelo decorador @task
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # Caso queira usar isso em vez de https://docs.crewai.com/how-to/Hierarchical/
        )
