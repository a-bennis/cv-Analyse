import fitz  # PyMuPDF
from agno.agent import Agent
from agno.models.xai import xAI
import os
from dotenv import load_dotenv
from textwrap import dedent
from utils.text_cleaner import readable_output

load_dotenv()
model = xAI(id="grok-4-fast-reasoning", api_key=os.getenv("XAI_API_KEY"))

def extract_pdfs(uploaded_files):
    """
    🧠 Agent Extracteur — Lit le contenu des PDF et renvoie un texte propre et lisible.
    """
    extracted_data = []

    for uploaded_file in uploaded_files:
        pdf_path = f"temp_{uploaded_file.name}"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extraction brute
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"

        extractor = Agent(
            name="Agent Extracteur",
            role="Extraction et structuration du texte à partir de CV et fiches de poste.",
            model=model,
            instructions=dedent("""
                🎯 Objectif :
                Extraire le texte brut d’un CV ou d’une fiche de poste et le rendre lisible.

                🧩 Étapes :
                1. Identifier le type de document (CV ou Fiche de poste).
                2. Supprimer les artefacts inutiles.
                3. Structurer le texte :
                   - CV → Nom, poste, compétences, expériences, formations.
                   - Poste → Intitulé, missions, compétences, profil recherché.
                4. Sortie : texte clair, formaté en français.
            """),
        )

        structured_text = extractor.run(text)
        extracted_data.append({
            "filename": uploaded_file.name,
            "content": readable_output(structured_text)
        })

    return extracted_data
