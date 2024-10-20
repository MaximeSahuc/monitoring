
# Server monitoring solution

This Docker project is a simple monitoring infrastructure containing:
- an Apache2 web server with status APIs : Apache2 status page and system usage data
- a MariaDB database
- a Grafana instance
- a monitoring agent to query the web server status pages and insert data in the database


## Demo

![Grafana dashboard preview](./doc/images/grafana-dashboard-web-server.png)


## Installation

Install the project using docker compose.

```bash
  cd docker
  docker compose up --build
```


## Usage

Connect to Grafana web interface at this url: http://172.16.69.40:3000


## Authors

<table>
    <tr>
        <th>
            <div>
                <a href="https://github.com/MaximeSahuc"><img src="https://avatars.githubusercontent.com/u/84405949?s=256" width="48" /></a>
                <br>
                <a href="https://github.com/MaximeSahuc">@MaximeSahuc</a>
            </div>
        </th>
        <th>
            <div>
                 <a href="https://github.com/marccambon"><img src="https://avatars.githubusercontent.com/u/160885185?s=256" width="48" /></a>
                 <br>
                 <a href="https://github.com/marccambon">@marccambon</a>
            </div>
        </th>
    </tr>
</table>
