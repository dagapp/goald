# goald
Online service for collecting money

Do not forget to check our [plan](plan.md)

## How to deploy
Requirements: docker

To deploy run

```bash
$> docker-compose up -d
```

**Note:** a new sqlite database will be created inside a docker container. If you already have a db file and want it
inside a docker container, then adjust .env file (DB_TARGET shoulde be /goald/\<db file\>) and run before deployment

```bash
$> docker-compose build
```
