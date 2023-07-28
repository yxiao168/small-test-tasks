# small test tasks

## email request
```text

    - Write a Docker file for nodeJS application ( https://github.com/heroku/node-js-getting-started ). Make sure to use all the Best Practices for Docker, it will be evaluated.
    - Prepare a docker-compose with Loki, Grafana, Promtail and nodeJS application ( https://github.com/heroku/node-js-getting-started ). Setup log collection from nodeJS application.
    - Write a simple script (in any language) that will print the numbers from 0 to 100 and convert every tenth to a wordy version.

```

## small test tasks

###  1. [Write a Docker file for nodeJS application ( https://github.com/heroku/node-js-getting-started ). Make sure to use all the Best Practices for Docker, it will be evaluated](01/node-js-getting-started/README.md)


###  2. [Prepare a docker-compose with Loki, Grafana, Promtail and nodeJS application ( https://github.com/heroku/node-js-getting-started ). Setup log collection from nodeJS application.](02/02.md)


### 3. [Write a simple script (in any language) that will print the numbers from 0 to 100 and convert every tenth to a wordy version.](03/03.md)


## Pack and unpack the archive

### Pack and unpack the archive
```shell
$ tar -czvf /tmp/ARIVAL.tar.gz ARIVAL
$ 
```


### Unpack and unpack the archive
```shell
$ pwd
/home/yxiao/Installs
$ ls
$ tar xvfz /tmp/ARIVAL.tar.gz 
$ tree
.
└── ARIVAL
    ├── 01
    │   ├── 01.md
    │   └── node-js-getting-started
    │       ├── app.json
    │       ├── Dockerfile
    │       ├── index.js
    │       ├── package.json
    │       ├── Procfile
    │       ├── public
    │       │   ├── lang-logo.png
    │       │   ├── node.svg
    │       │   └── stylesheets
    │       │       └── main.css
    │       ├── README.md
    │       ├── test.js
    │       └── views
    │           ├── pages
    │           │   ├── db.ejs
    │           │   └── index.ejs
    │           └── partials
    │               ├── header.ejs
    │               └── nav.ejs
    ├── 02
    │   ├── 02.log
    │   ├── 02.md
    │   ├── docker-compose.yml
    │   ├── grafana-data
    │   ├── grafana_web.gif
    │   ├── loki-config
    │   │   └── local-config.yaml
    │   ├── node-js-getting-started
    │   │   ├── app.json
    │   │   ├── Dockerfile
    │   │   ├── index.js
    │   │   ├── package.json
    │   │   ├── Procfile
    │   │   ├── public
    │   │   │   ├── lang-logo.png
    │   │   │   ├── node.svg
    │   │   │   └── stylesheets
    │   │   │       └── main.css
    │   │   ├── README.md
    │   │   ├── test.js
    │   │   └── views
    │   │       ├── pages
    │   │       │   ├── db.ejs
    │   │       │   └── index.ejs
    │   │       └── partials
    │   │           ├── header.ejs
    │   │           └── nav.ejs
    │   ├── node-js-getting-started_web.gif
    │   └── promtail-config
    │       └── config.yml
    ├── 03
    │   ├── 03.md
    │   ├── requirements.txt
    │   └── wordy1in10.py
    └── README.md

19 directories, 40 files

```



