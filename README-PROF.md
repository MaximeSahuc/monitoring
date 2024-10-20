
# SAE Projet collecte de logs

Le but de ce projet est de superviser un système en collectant des métriques pour ensuite les afficher sur une interface intuitive.


## Infrastructure

Nous avons choisis pour ce projet, de **superviser un serveur web Apache2**.

Nous nous sommes également imposés quelques containtes pour rendre le projet plus intéressant :
- L'infrastructure devra être entièrement configuré via des **fichiers de configuration**, pas besoin d'actions manuelles.
- L'**agent de monitoring** devra être **développé par nos soins**.

Notre projet contient 4 containers Docker :
- **Serveur web :** Ce container est basé sur une image Ubuntu, et contient un **serveur web** apache2 ainsi qu'une **API Flask** exposant des données sur les ressources systèmes utilisés.

- **Agent de supervision :** L'agent de supervision est un **programme Python**. Son rôle est de **collecter des métriques** sur le serveur web, via la page de status apache2 (connections, temps de latence) ainsi que l'API Flash (CPU, mémoire, réseau, dique) pour ensuite les **insérer dans la base de donnée** SQL.

- **MariaDB :** La base de donnée contient deux tables, une pour les **métriques récoltés** sur apache2 et une seconde table pour les métriques systèmes.

- **Grafana :** L'interface web Grafana nous permet de visualiser sur différents tableaux de bords les données collectés. Nous avons deux tableau de bord, un pour les métriques apache2, et un second pour les métriques systèmes.

**Schéma d'infrastructure :**
![Schéma d'infrastrucure](./doc/images/infrastructure_diagram.png)


## Schreenshot : Tableau de bord serveur web

![Grafana dashboard preview](./doc/images/grafana-dashboard-web-server.png)


## Installation

Pour lancer le projet, se placer dans le dossier "docker" contenant le fichier `docker-compose.yml`, puis lancer le projet avec docker compose.

```bash
  cd docker
  docker compose up --build
```


## Utilisation

Avant de visualiser les donnés dans le Grafana, il est nécessaire d'effectuer quelques requêttes sur le serveur web pour faire varier les métriques remontés. L'URL du site web est : http://172.16.69.10/

L'intervale de collecte de métrique à été réduit à 5 secondes afin de pouvoir voir assez rapidement un résultat dans les graphiques.

Ensuite, il faut se connecter l'interface Grafana : http://172.16.69.40:3000
- Login : `admin`
- Password : `meg`

Dans le menu `Dashboards`, deux dashboards sont disponibles, un remontant les métriques relatives à apache2, et un second avec les métriques systèmes.


## Difficultés et solutions
- **Intégration de l'API au container httpd :** L'API Flask sur le serveur web est un processus Python indépendant d'apache2, nous avons remarqués qu'il n'était pas possible d'utiliser l'image docker `httpd` conjointement avec notre script Python, car le point d'entré du container était le processus apache2. Nous sommes donc passés sur une image Ubuntu, nous installons et configurons apache2 ainsi que nôtre API Flask via le Dockerfile du container.


## Auteurs

- Maxime Sahuc
- Marc Cambon