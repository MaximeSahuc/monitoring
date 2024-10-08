# Grafana doc


- ### mkdir: can't create directory '/var/lib/grafana/plugins': Permission denied
> Get grafana data folder ownership : `sudo chown -R $USER ./data/grafana`

- ### Grafana dont detect custom config file
> Add the custom config file path to this env var : `GF_PATHS_CONFIG=/etc/grafana/custom.ini`