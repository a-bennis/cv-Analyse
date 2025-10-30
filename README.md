# 🧠 CV ↔ Offre RH — Système de Matching Automatique par IA (Grok xAI)

Ce projet est une application **Streamlit** qui permet d’analyser automatiquement la compatibilité entre un **CV de candidat** et une **fiche de poste** grâce à l’intelligence artificielle.  
Elle exploite le modèle **Grok 4 (xAI)** via la librairie **Agno**, combinant **NLP avancé**, **analyse sémantique** et **raisonnement intelligent** pour produire un **rapport RH complet, clair et objectif**.

---

## 🎯 Objectif du projet

Les processus de recrutement reposent souvent sur une lecture manuelle et chronophage des CV.  
Ce projet vise à **automatiser cette étape clé** en évaluant la compatibilité entre un profil et une offre d’emploi selon plusieurs axes :

- **Analyse sémantique des compétences et expériences**
- **Identification des correspondances techniques et comportementales**
- **Calcul d’un score de compatibilité (%)**
- **Génération d’un verdict clair et explicatif**

Grâce à l’IA, le système agit comme un **assistant RH intelligent**, capable d’interpréter le contenu des documents PDF, d’en extraire les informations clés et de déterminer si le profil correspond réellement à l’offre.

---

## ⚙️ Fonctionnement du système

1. **Téléversement des fichiers**
   - L’utilisateur importe un **CV PDF** et une **fiche de poste PDF**.

2. **Extraction du texte**
   - Le module d’extraction lit le contenu des deux fichiers à l’aide de **PyMuPDF (fitz)**.

3. **Analyse NLP**
   - Le modèle **Grok (xAI)** traite le texte et extrait :
     - Compétences techniques et soft skills
     - Expériences et projets significatifs
     - Formations et certifications

4. **Matching IA**
   - Une comparaison sémantique est effectuée pour déterminer :
     - Les **points communs**
     - Les **écarts de compétences**
     - Le **score global de correspondance**

5. **Rapport RH**
   - L’application affiche un **rapport lisible** contenant :
     - ✅ Le **score de compatibilité (%)**
     - 💬 Un **verdict clair**
     - 📈 Les **forces et faiblesses** du candidat

---

## 🧠 Exemple de résultat

> ### 📊 Rapport de compatibilité RH  
> **Score global : 88 / 100**  
>  
> **Compétences clés alignées :** Python, Power BI, Analyse de données, Machine Learning  
> **Points à améliorer :** Cloud computing, gestion de bases de données massives  
>  
> **Verdict :** Candidat **hautement compatible** avec le poste. Excellent potentiel d’évolution dans une équipe data.

---

## 🖼️ Aperçu de l’application

![Interface Streamlit](./image.png)

---

## 🛠️ Installation et exécution

### 1. Cloner le dépôt
```bash
git clone https://github.com/a-bennis/cv-analyse.git
cd cv-analyse

---

## 🧩 Technologies utilisées

| **Technologie** | **Description** |
|------------------|-----------------|
| 🐍 **Python 3.11+** | Langage principal |
| 🎨 **Streamlit** | Interface utilisateur web |
| 📄 **PyMuPDF (fitz)** | Extraction de texte PDF |
| 🤖 **Agno** | Orchestration des agents IA |
| 🧠 **xAI (Grok)** | Modèle d’analyse sémantique |
| ⚙️ **dotenv** | Gestion des variables d’environnement |

---

## 💼 Cas d’utilisation

- **Recruteurs** : évaluation rapide et automatisée des candidatures  
- **Entreprises** : tri des CV à grande échelle avec critères objectifs  
- **Candidats** : auto-évaluation avant de postuler à une offre  
- **Écoles / universités** : orientation professionnelle et accompagnement RH  

---

## 👨‍💻 Auteur

**Bennis Abdelhak**  
🎓 Étudiant en Ingénierie Informatique et Réseaux *(Option MIAGE)*  
💡 Passionné par l’IA, le NLP et l’automatisation RH  
📍 Casablanca, Maroc  
📧 [Bennis_Abdelhak@emsi-edu.ma](mailto:Bennis_Abdelhak@emsi-edu.ma)  
🌐 [GitHub - a-bennis](https://github.com/a-bennis)

---

## 📄 Licence

Projet distribué sous la licence **MIT**.  
Vous êtes libre de l’utiliser, le modifier et le distribuer avec mention de l’auteur original.

---

<p align="center">
  <b>© 2025 — CV ↔ Offre RH | Propulsé par Grok (xAI) & Agno</b>
</p>
