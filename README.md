# Server monitoring


## TODO list
- [ ] Web server container
    - [x] Apache2 status page, on port 8080 /server-status
    - [ ] Status page for server ressources, on port 81
- [ ] Monitoring agent container
    - [x] Script to get data from web server status pages
    - [ ] Script to insert data in database
    - [ ] Merge scripts in a Dockerfile
    - [ ] Run the container and test
- [ ] Mariadb container
    - [ ] Create databases
    - [ ] Create tables
    - [ ] Tests
- [ ] Grafana container
    - [x] Custom config file
    - [ ] Link to database
    - [ ] Create Graphs
    - [ ] Save config to use in docker compose

## Infrastructure diagram
![Infrastructure diagram](./doc/infrastructure_diagram.png)