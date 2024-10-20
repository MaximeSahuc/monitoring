
# SAE Project collecte de logs

Le but de ce projet est de superviser un système en collectant des métriques pour ensuite les afficher sur une interface intuitive.


## Infrastructure

Nous avons choisis pour ce projet, de **superviser un serveur web Apache2**.

Nous nous sommes également imposés quelques containtes pour rendre le projet plus intéressant :
- L'infrastructure devra être entièrement configuré via des **fichiers de configuration**, pas besoin d'actions manuelles.
- L'**agent de monitoring** devra être **développé par nos soins**.

Notre projet contient 4 containers Docker :
- un serveur web
- un agent de supervision
- une base de donnée MariaDB
- une instance Grafana


- **Serveur web :** Ce container est basé sur une image Ubuntu, et contient un **serveur web** apache2 ainsi qu'une **API Flask** exposant des données sur les ressources systèmes utilisés.

- **Agent de supervision :** L'agent de supervision est un **programme Python**. Son rôle est de **collecter des métriques** sur le serveur web, via la page de status apache2 (connections, temps de latence) ainsi que l'API Flash (CPU, mémoire, réseau, dique) pour ensuite les **insérer dans la base de donnée** SQL.

- **MariaDB :** La base de donnée contient deux tables, une pour les **métriques récoltés** sur apache2 et une seconde table pour les métriques systèmes.

- **Grafana :** L'interface web Grafana nous permet de visualiser sur différents tableaux de bords les données collectés.


## Tableau de bord serveur web

![Grafana dashboard preview](./doc/images/grafana-dashboard-web-server.png)


## Documentation

- [Infrastructure diagram](./doc/infrastructure-diagram.md)
- [Infrastructure choices](./doc/infrastructure-choices.md)


## Installation

Install the project using docker compose.

```bash
  git clone x
  cd x/docker
  docker compose up --build
```


## Usage

Connect to Grafana web interface at this url: http://172.16.69.40:3000


## Auteurs

- Maxime Sahuc
- Marc Cambon