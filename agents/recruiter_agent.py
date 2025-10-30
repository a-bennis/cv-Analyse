import streamlit as st
from agno.agent import Agent
from agno.models.xai import xAI
import os
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()
model = xAI(id="grok-4-fast-reasoning", api_key=os.getenv("XAI_API_KEY"))

def recruiter_interface(report):
    st.subheader("📊 Rapport de compatibilité RH")
    st.markdown(report)

    question = st.text_input("💬 Posez une question sur le matching :")
    if question:
        recruiter = Agent(
            name="Agent Recruteur Virtuel",
            role="Répondre aux questions RH sur le matching entre CV et poste.",
            model=model,
            instructions=dedent("""
                🎯 Objectif :
                Répondre clairement aux questions de l’utilisateur sur les résultats du matching.
                - Se baser uniquement sur le rapport fourni.
                - Donner des réponses RH concises et en français.
                - Maximum 3 phrases.
            """),
        )
        answer = recruiter.run(f"Rapport : {report}\n\nQuestion : {question}")
        st.success(getattr(answer, "output_text", str(answer)))
