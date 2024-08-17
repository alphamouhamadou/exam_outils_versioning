import requests
from requests.auth import HTTPBasicAuth
import os

# Remplacez ces variables par vos informations personnelles
GITHUB_USERNAME = 'alphamouhamadou'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = 'exam_outils_versioning'
DESCRIPTION = 'Ceci est un dépôt créé par l\'API Rest de Github.'

# URL de base pour l'API Github
BASE_URL = 'https://api.github.com'

# Fonction pour créer un dépôt
def create_github_repo(repo_name, description):
    url = f'{BASE_URL}/user/repos'
    payload = {
        'name': repo_name,
        'description': description,
        'private': False  
    }
    response = requests.post(url, json=payload, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
    
    if response.status_code == 201:
        print(f'Dépôt {repo_name} créé avec succès.')
        return response.json()
    else:
        print(f'Échec de la création du dépôt: {response.status_code}')
        print(response.json())
        return None

# Fonction pour créer un issue
def create_github_issue(repo_name, title, body):
    url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}/issues'
    payload = {
        'title': title,
        'body': body
    }
    response = requests.post(url, json=payload, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
    
    if response.status_code == 201:
        print(f'Issue "{title}" créé avec succès.')
        return response.json()
    else:
        print(f'Échec de la création de l\'issue: {response.status_code}')
        print(response.json())
        return None

# Créer le dépôt
repo = create_github_repo(REPO_NAME, DESCRIPTION)

# Si le dépôt a été créé avec succès, créer deux issues
if repo:
    create_github_issue(REPO_NAME, 'Issue 1', 'Description de la première issue.')
    create_github_issue(REPO_NAME, 'Issue 2', 'Description de la deuxième issue.')
