#!/usr/bin/env python
import sys
from marketing_posts.crew import MarketingPostsCrew

def run():
    # Substitua pelos seus inputs, eles irão automaticamente interpolar qualquer informação de tarefas e agentes
    inputs = {
        'customer_domain': 'crewai.com',
        'project_description': """
A CrewAI, um provedor líder de sistemas multiagentes, tem como objetivo revolucionar a automação de marketing para seus clientes empresariais. Este projeto envolve o desenvolvimento de uma estratégia de marketing inovadora para mostrar as soluções avançadas da CrewAI impulsionadas por IA, enfatizando facilidade de uso, escalabilidade e capacidades de integração. A campanha terá como alvo tomadores de decisão com afinidade por tecnologia em empresas de médio a grande porte, destacando histórias de sucesso e o potencial transformador da plataforma da CrewAI.

Domínio do Cliente: Soluções de IA e Automação
Visão Geral do Projeto: Criar uma campanha de marketing abrangente para aumentar a conscientização e a adoção dos serviços da CrewAI entre clientes empresariais.
"""
    }
    MarketingPostsCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Treinar a equipe por um determinado número de iterações.
    """
    inputs = {
        'customer_domain': 'crewai.com',
        'project_description': """
A CrewAI, um provedor líder de sistemas multiagentes, tem como objetivo revolucionar a automação de marketing para seus clientes empresariais. Este projeto envolve o desenvolvimento de uma estratégia de marketing inovadora para mostrar as soluções avançadas da CrewAI impulsionadas por IA, enfatizando facilidade de uso, escalabilidade e capacidades de integração. A campanha terá como alvo tomadores de decisão com afinidade por tecnologia em empresas de médio a grande porte, destacando histórias de sucesso e o potencial transformador da plataforma da CrewAI.

Domínio do Cliente: Soluções de IA e Automação
Visão Geral do Projeto: Criar uma campanha de marketing abrangente para aumentar a conscientização e a adoção dos serviços da CrewAI entre clientes empresariais.
"""
    }
    try:
        MarketingPostsCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao treinar a equipe: {e}")
