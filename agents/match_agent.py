from agno.agent import Agent
from agno.models.xai import xAI
import os
from dotenv import load_dotenv
from textwrap import dedent
from utils.text_cleaner import readable_output

load_dotenv()
model = xAI(id="grok-4-fast-reasoning", api_key=os.getenv("XAI_API_KEY"))

def compare_profiles(analyzed_profiles):
    """
    ⚖️ Compare 1 CV et 1 fiche de poste, et retourne un score clair + verdict court.
    """
    matcher = Agent(
        name="Agent RH Matching",
        role="Comparer un CV et une fiche de poste et donner un verdict court et clair.",
        model=model,
        instructions=dedent("""
            🎯 Objectif :
            Comparer le CV du candidat avec la fiche de poste fournie.

            🧩 Étapes :
            - Analyse les compétences, expériences et formations.
            - Évalue la correspondance globale.
            - Donne une réponse concise (2-3 phrases max) avec un score de compatibilité.

            🧾 Format attendu :
            Score global : XX / 100
            Verdict : [phrase courte sur la compatibilité du profil]
        """),
    )

    combined_text = f"""
    --- CV ---
    {analyzed_profiles[0]['analysis']}

    --- Fiche de poste ---
    {analyzed_profiles[1]['analysis']}
    """

    response = matcher.run(combined_text)
    return readable_output(response)
