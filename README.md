# PostgreSQL Database Catalog Item on SURF Research Cloud

## Introduction
The PostgreSQL Database Catalog Item on SURF Research Cloud provides a PostgreSQL database that runs in a docker container on a linux (ubuntu 22.04) VM. It is made up of several components and runs automatically on port 5432. To configure the database, it uses several variables that are passed by a user when the workspace (a VM) is created. First, the postgres-env component collects these variables and prepares the workspace for the docker container. Then the postgres-docker component runs a container from the docker-compose file. 

This repo is not meant to run locally. Its only purpose is to provide the necessary code to set up the database on the SURF Research Cloud.

## Components
On SURF, every catalog item consists of multiple components. There are several components that are standard to (a specific type of) SURF catalog items, see *step 1* of this [documentation page](https://servicedesk.surf.nl/wiki/display/WIKI/Create+a+catalog+item). Below the current section, you can find the detailed description of the custom components that are used for this catalog item. The information is also available on SURF in the description of the catalog item.

The PostgreSQL Database Catalog Item consists of the following components:
- **SRC-OS**: standard SURF component
- **SRC-CO**: standard SURF component
- **SRC-External plugin**: standard SURF component that must be put before an external component. In our case, the postgres-env component.
- **Postgres-env**: sets relevant environmental variables (user name, password, database name), checks for attached storage, sets POSTGRES_DATA (path to the postgres folder) to the attached volume or /data/postgres
- **SRC-External Docker Compose**: standard SURF component that must be put before a docker-compose component. It makes sure that the docker-compose file in the next component will be run
- **Postgres-docker**: A docker-compose file that defines the configuration (bind mount, network, ports) of the container that runs the postgres database. 

### Postgres-env
This component is needed to prepare for the Postgres DB component. Based on the provided variables, it sets the following environmental variables: POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER. 

It also searches for attached storage. If no attached storage is found, the environmental variable POSTGRES_DATA is set to data/postgres. POSTGRES_DATA contains the path to the folder with the Postgres database files. If attached storage is found, it sets POSTGRES_DATA to a postgres folder in the root of the attached storage. Note that in the case of multiple attached storages, it just picks one. Attached storage allows you to persist the data and attach a (more powerfull) workspace to it. In both cases, it makes sure that POSTGRES_DATA exists.

### Postgres-docker
The database runs in a docker container and uses several environmental variables (that are set in postgres-env) for its configuration.

## Problems Encountered
I encountered some problems when I tried to create the catalog item, the list below describes them. Most of the content is also in the SURF [documentation](https://servicedesk.surf.nl/wiki/display/WIKI/SURF+Research+Cloud). This section is not intended to serve as a complete guide to SURF; the sole purpose is to help you avoid these pitfalls.

- At the moment of writing, SURF doesn't make a backup of their VMs and storage nor is there any option to do so. SURF anticipates creating these in the future, but this is still uncertain.
- I couldn't access all catalog items at first nor could I create them. This is due to the different groups you can be a member of in SURF, you must be member of the src_co_developer group to create amd access all catalog items. Documentation [here](https://servicedesk.surf.nl/wiki/display/WIKI/Special+CO-groups)
- To make any external/docker components work, you should put special components in front of them. I discussed this in the components part above.
- Once you have made changes to a component, the changes are only included in the development version. You can promote the development version to the pilot version, and then to the live version. The catalog items use the live version by default.