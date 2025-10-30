import streamlit as st
from agents.extract_agent import extract_pdfs
from agents.nlp_agent import analyze_profiles
from agents.match_agent import compare_profiles
from utils.text_cleaner import readable_output

st.set_page_config(page_title="CV ↔ Offre Matcher", page_icon="💼", layout="centered")

st.title("💼 Analyse CV ↔ Offre — Matching Automatique")
st.write("Analysez la compatibilité entre un **CV candidat** et une **fiche de poste** à l’aide de Grok (xAI).")

uploaded_files = st.file_uploader(
    "📂 Importez le CV et la fiche de poste (2 fichiers PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) == 2:
    st.info("🧾 Traitement des documents en cours...")

    # Étapes principales (extraction, analyse, comparaison)
    extracted_data = extract_pdfs(uploaded_files)
    analyzed_profiles = analyze_profiles(extracted_data)
    result = compare_profiles(analyzed_profiles)

    # ✅ Affichage final : uniquement le rapport RH
    st.subheader("📊 Rapport de compatibilité RH")
    st.success(readable_output(result))

elif uploaded_files and len(uploaded_files) != 2:
    st.warning("⚠️ Vous devez importer exactement **2 fichiers** : un CV et une fiche de poste.")
else:
    st.info("⬆️ Importez un CV et une fiche de poste pour lancer l’analyse.")
