# 🧠 CV ↔ Offre RH — Matching Automatique avec IA (Grok)

Ce projet est une application **Streamlit** qui permet d’analyser automatiquement la compatibilité entre un **CV de candidat** et une **fiche de poste**.  
L’objectif est d’aider les **équipes RH et les recruteurs** à évaluer rapidement l’adéquation d’un profil grâce à une **analyse sémantique IA** et un **score de compatibilité intelligent**.

Le système s’appuie sur le modèle **Grok (xAI)** via la librairie **Agno**, offrant une compréhension contextuelle du langage pour extraire les points forts, les manques et générer un **rapport RH clair et lisible** en français.

---

## 🚀 Fonctionnalités principales

✅ **Analyse complète du CV et de la fiche de poste** (PDF)  
✅ **Extraction automatique du texte** avec PyMuPDF  
✅ **Comparaison sémantique intelligente** des compétences et expériences  
✅ **Score de compatibilité RH (%)** calculé automatiquement  
✅ **Verdict clair et structuré** pour aider la décision de recrutement  
✅ **Interface utilisateur moderne et intuitive** via Streamlit  
✅ **Intégration IA Grok (xAI)** via la librairie Agno

---

## 🧩 Objectif du projet

L’application vise à :
- **Automatiser la présélection** des candidats sur la base de critères objectifs.  
- **Réduire le temps de traitement** des candidatures répétitives.  
- **Aider les recruteurs** à se concentrer sur les profils réellement pertinents.  
- **Améliorer la transparence** et la cohérence des décisions RH.  

Grâce à une architecture simple, tout le traitement — de l’extraction PDF jusqu’au rapport RH final — est effectué dans un **seul script (`app.py`)**, rendant le projet facile à déployer et à maintenir.

---

## 🖼️ Aperçu de l’application

![Interface Streamlit](./image.png)

---

## 🧠 Exemple de résultat

> ### 📊 Rapport de compatibilité RH  
> **Score global : 85 / 100**  
>  
> **Compétences clés alignées :** Python, Power BI, SQL, Analyse de données  
> **Points à améliorer :** Connaissances Cloud, expérience en DataOps  
>  
> **Verdict :** Candidat **hautement compatible** avec le poste. Excellent potentiel d’intégration.

---

## 🛠️ Installation et exécution

### 1. Cloner le dépôt
```bash
git clone https://github.com/a-bennis/cv-analyse.git
cd cv-analyse
