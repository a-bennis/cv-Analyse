from agno.agent import Agent
from agno.models.xai import xAI
import os
from dotenv import load_dotenv
from textwrap import dedent
from utils.text_cleaner import readable_output

load_dotenv()
model = xAI(id="grok-4-fast-reasoning", api_key=os.getenv("XAI_API_KEY"))

def analyze_profiles(extracted_data):
    """
    🧠 Agent NLP — Analyse les CV et fiches de poste (compétences, expériences, formations).
    """
    analyzed_profiles = []

    for doc in extracted_data:
        nlp_agent = Agent(
            name="Agent NLP Analyste",
            role="Extraction des compétences, expériences et formations.",
            model=model,
            instructions=dedent("""
                🎯 Objectif :
                Identifier et structurer les éléments RH essentiels à partir d’un texte.

                🧩 Étapes :
                - Identifier les compétences techniques et comportementales.
                - Extraire les expériences clés (poste, durée, entreprise).
                - Identifier les formations (diplôme, année, établissement).
                - Sortie :
                  ### Type de document
                  ### Compétences techniques
                  ### Compétences comportementales
                  ### Expériences
                  ### Formations
            """),
        )

        analysis = nlp_agent.run(doc["content"])
        analyzed_profiles.append({
            "filename": doc["filename"],
            "analysis": readable_output(analysis)
        })

    return analyzed_profiles
