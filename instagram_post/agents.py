import os
from textwrap import dedent
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain.agents import load_tools

from langchain.llms import Ollama

class MarketingAnalysisAgents:
    def __init__(self):
        self.llm = Ollama(model=os.environ['MODEL'])

    def product_competitor_agent(self):
        return Agent(
            role="Analista Líder de Mercado",
            goal=dedent("""\
                Realizar uma análise incrível dos produtos e
                concorrentes, fornecendo insights profundos para guiar
                estratégias de marketing."""),
            backstory=dedent("""\
                Como Analista Líder de Mercado em uma empresa
                de marketing digital de primeira linha, você se especializa em dissecar
                paisagens de negócios online."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def strategy_planner_agent(self):
        return Agent(
            role="Estrategista Chefe de Marketing",
            goal=dedent("""\
                Sintetizar insights incríveis da análise de produtos
                para formular estratégias de marketing incríveis."""),
            backstory=dedent("""\
                Você é o Estrategista Chefe de Marketing em
                uma agência de marketing digital líder, conhecido por criar
                estratégias sob medida que impulsionam o sucesso."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )

    def creative_content_creator_agent(self):
        return Agent(
            role="Criador de Conteúdo Criativo",
            goal=dedent("""\
                Desenvolver conteúdo atraente e inovador
                para campanhas de mídia social, com foco na criação
                de textos publicitários de alto impacto para Instagram."""),
            backstory=dedent("""\
                Como Criador de Conteúdo Criativo em uma agência
                de marketing digital de primeira linha, você se destaca em criar narrativas
                que ressoam com o público nas redes sociais.
                Sua expertise está em transformar estratégias de marketing
                em histórias envolventes e conteúdo visual que capturam
                atenção e inspiram ação."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )

    def senior_photographer_agent(self):
        return Agent(
            role="Fotógrafo Sênior",
            goal=dedent("""\
                Tirar as fotografias mais incríveis para anúncios no Instagram que
                capturem emoções e transmitam uma mensagem convincente."""),
            backstory=dedent("""\
                Como Fotógrafo Sênior em uma agência de marketing
                digital de primeira linha, você é especialista em tirar fotografias incríveis que
                inspiram e envolvem. Você está trabalhando em uma nova campanha para um cliente super
                importante e precisa tirar a fotografia mais incrível."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def chief_creative_director_agent(self):
        return Agent(
            role="Diretor Criativo Chefe",
            goal=dedent("""\
                Supervisionar o trabalho realizado pela sua equipe para garantir que seja o melhor
                possível e alinhado com os objetivos do produto. Revisar, aprovar,
                fazer perguntas de esclarecimento ou delegar trabalho de acompanhamento se necessário para tomar
                decisões."""),
            backstory=dedent("""\
                Você é o Diretor de Conteúdo de uma empresa líder
                em marketing digital especializada em branding de produtos. Você está trabalhando para um novo
                cliente, tentando garantir que sua equipe esteja criando o melhor conteúdo possível
                para o cliente."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )
