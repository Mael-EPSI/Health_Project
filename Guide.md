# AI Health Assistant - API REST avec Django & IA

## Description du projet
L'**AI Health Assistant** est une API REST développée avec **Django Rest Framework (DRF)**, intégrant une **intelligence artificielle** pour fournir des analyses et recommandations médicales.

### Fonctionnalités principales :
- **Analyse des symptômes** pour identifier d'éventuelles maladies.
- **Recommandation de médicaments** en fonction des symptômes.
- **Recherche d'hôpitaux les plus proches** en fonction de la localisation de l'utilisateur.
- **Conseils de santé généraux**.
- **Analyse de la durée du sommeil**.

---

## Installation et configuration

### Prérequis
- Python 3.8+
- Django & Django REST Framework
- Virtualenv (recommandé)

### Étapes d'installation
Toutes les commandes ici sont écrites pour un Windows !
1. Cloner le projet :
   ```sh
   git clone https://github.com/Mael-EPSI/Health_Project.git
   cd api
   ```
2. Créer et activer un environnement virtuel :
   ```sh
   python -m venv env
   source env/bin/activate  
   ```
3. Appliquer les migrations :
   ```sh
   python manage.py migrate
   ```
4. Lancer le serveur :
   ```sh
   python manage.py runserver
   ```

L'API sera accessible à l'adresse : `http://127.0.0.1:8000/`

---

## Documentation des routes

### 1️⃣ Analyse des symptômes
**Route :** `POST api/analyze_health`

📌 **Description** : Permet d'analyser les symptômes fournis par l'utilisateur et de proposer des maladies probables.

📥 **Exemple de requête :**
```json
{
  "symptoms": "fièvre, toux, fatigue"
}
```
📤 **Réponse attendue :**
```json
{
  "message": "Exemple de réponse : Il est probable que vous souffriez d'une infection des voies respiratoires supérieures, telle qu'un rhume ou une grippe. La fièvre indique que votre corps lutte contre une infection, la toux est un symptôme courant des infections respiratoires, et la fatigue est souvent présente en cas de maladies virales. Il est recommandé de prendre un repos suffisant, de bien s'hydrater et de consulter un médecin si les symptômes persistent ou s'aggravent."
}
```

---

### 2️⃣ Recommandation de médicaments
**Route :** `POST api/recommend_medications`

📌 **Description** : Fournit une liste de médicaments potentiels en fonction des symptômes renseignés.

📥 **Exemple de requête :**
```json
{
  "symptoms": "maux de tête, fièvre"
}
```
📤 **Réponse attendue :**
```json
{
  "message": "Exemple de réponse : En tant qu'assistant virtuel, je ne suis pas un professionnel de la santé et je ne suis pas autorisé à prescrire des médicaments. Cependant, je recommande de consulter un médecin ou un pharmacien pour obtenir des conseils sur les médicaments appropriés pour traiter vos symptômes de maux de tête et de fièvre. En général, des médicaments tels que le paracétamol ou l'ibuprofène peuvent aider à soulager ces symptômes. Il est important de suivre les instructions du professionnel de la santé et de ne pas dépasser la dose recommandée."
}
```

---

### 3️⃣ Trouver l'hôpital le plus proche
**Route :** `POST api/find_nearest_hospital`

📌 **Description** : Recherche l'hôpital le plus proche en fonction de la localisation fournie.

📥 **Exemple de requête :**
```json
{
  "location": "Paris, France"
}
```
📤 **Réponse attendue :**
```json
{
  "message": "Exemple de réponse : L'hôpital le plus proche de Paris, France est l'Hôpital Cochin, situé à 27 Rue du Faubourg Saint-Jacques, 75014 Paris."
}
```

---

### 4️⃣ Obtenir un conseil santé
**Route :** `GET api/tips`

📌 **Description** : Affiche un conseil de santé basé sur une thématique donnée.

📥 **Exemple de requête :**
```json
{
  "tips": "heureux"
}
```
📤 **Réponse attendue :**
```json
{
  "message": "Exemple de réponse : 1. Pratiquer la gratitude chaque jour en se concentrant sur les aspects positifs de sa vie. 2. Cultiver des relations sociales saines et proches avec ses proches. 3. Faire de l'exercice régulièrement pour libérer des endorphines et améliorer son humeur. 4. Prendre du temps pour soi et privilégier les activités qui procurent du bonheur et de l'épanouissement."
}
```

---

### 5️⃣ Analyse du sommeil
**Route :** `POST api/analyze_sleep`

📌 **Description** : Permet d'analyser la durée du sommeil et de fournir une recommandation.

📥 **Exemple de requête :**
```json
{
  "duree": "7 heures"
}
```
📤 **Réponse attendue :**
```json
{
  "message": "Exemple de réponse : En général, il est recommandé de dormir entre 7 et 9 heures par nuit pour la plupart des adultes afin d'obtenir un sommeil de bonne qualité. Donc dormir 7 heures peut être considéré comme un bon sommeil pour certaines personnes, mais cela peut varier en fonction des besoins individuels en sommeil. Il est important de se sentir reposé et revigoré au réveil pour savoir si on a eu un bon sommeil."
}
```

---

🚀 **Bon développement !**

