Get Started
===========
*Get support and advice at [hi@snowboard.software](mailto:hi@snowboard.software)*

There are two ways to deploy Snowboard.
We manage it for you in the [cloud](#cloud), or you [host it yourself](#self-hosted). 

## Cloud

1. [Register here](https://register.s8.software/) with your work-email
2. Verify your E-Mail. Now we start your cloud instance.
3. [Prepare a technical user in Snowflake](snowflake_connection.md)
    - Write us to get support! Setting permissions can be tricky. Just using `ACCOUNTADMIN` is not a good practice.
4. Login to your instance and connect your Snowflake Account.
5. You did it! Great job. Tell your colleagues about it and explore!

## Self-Hosted
***~ 30 min to go from 0 to data discovery***  <br>


1. Install [`docker`](https://docs.docker.com/engine/install/) and [`docker-compose`](https://docs.docker.com/compose/install/) on a machine with 4 cores and 16GB RAM
2. Create a directory called `snowboard`
3. Download the Docker Compose configuration file: [`docker-compose.yml`](https://raw.githubusercontent.com/zurferr/snowboard_software/main/docs/docker-compose.yml "Download file")
4. Start the deployment with `docker-compose up -d`
5. The Snowboard Data Catalog is now ready on [http://localhost/login](http://localhost/login) or your server address
    - Login in with `admin@s8.software` and `snowboard`
6. [Prepare a technical user in Snowflake](snowflake_connection.md)
7. Follow the on-boarding wizard and add your Snowflake account.
8. Configure SSL Certificate _( optional / recommended )_
9. You did it! Great job. Tell your colleagues about it and explore!


## Overview

The Snowboard Data Catalog connects directly with your cloud data warehouse.
It needs access to the system database and tables of the warehouse (e.g. in `SNOWFLAKE.ACCOUNT_USAGE`).

Snowboard then provides the ability to quickly and automatically: 
- profile data
- view access rights and ownership
- document information objects 
- understand relationships between tables
- search everything

![System Architecture](_static/overview.png)