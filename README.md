# PostgreSQL Database Catalog Item on SURF Research Cloud

## Introduction
The PostgreSQL Database Catalog Item on SURF Research Cloud provides a PostgreSQL database setup on the SURF Research Cloud. It is made up of several components and runs automatically on port 5432. To configure the database, it uses several variables that are passed by a user when the workspace (a VM) is created. First, the postgres-env component collects these variables and prepares the workspace for the docker container. Then the postgres-docker component runs a container from the docker-compose file.

## Components
Every catalog item cosists of multiple components. There are several componentents that are standard to (a specific type of) Surf catalog items, see *step 1* of this [documentation page](https://servicedesk.surf.nl/wiki/display/WIKI/Create+a+catalog+item). Below the current section you can find the detailed description of the custom components, it is also available on SURF in the description of the catalog item.

The PostgreSQL Database Catalog Item consists of the following components:
- **SRC-OS**: standard SURF component
- **SRC-CO**: standard SURF component
- **SRC-External plugin**: standard SURF component that must be put before an external component. In our case the postgres-env component.
- **Postgres-env**: sets environmental variables, checks for attached storage, sets POSTGRES_DATA (path to the postgres folder) to the attached volume or /data/postgres
- **SRC-External Docker Compose**: standard SURF component that must be put before a docker-compose component. It makes sure that the docker-compose file in the next component will be run
- **Postgres-docker**: A docker-compose file that defines the configuration (bind mount, network, ports) of the container that runs the postgres database. 

### Postgres-env
This component is needed for the preparation for the Postgres DB component. Based on the provided variables it sets the following environmental variables: POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER. It also searches for an attached storage. If there is an attached storage it sets the environmental variable POSTGRES_DATA to the postgres folder in the attached storage (path/to/attached/storage/postgres). Otherwise POSTGRES_DATA is set to data/postgres. In both cases, it makes sure that POSTGRES_DATA exists.

### Postgres-docker
The database runs in a docker container and uses several environmental variables (that are set in postgres-env) for its configuration.
