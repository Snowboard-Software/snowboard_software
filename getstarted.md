# Get Started

_Get support and advice at_ [_hi@sled.so_](mailto:hi@sled.so)

There are two ways to deploy Sled. We manage it for you in the [cloud](getstarted.md#cloud), or you [host it yourself](getstarted.md#self-hosted).

## Cloud

1. [Register here](https://register.s8.software) with your work-email
2. Verify your E-Mail. Now we start your cloud instance.
3. [Prepare a technical user in Snowflake](snowflake\_connection.md)
   * Write us to get support! Setting permissions can be tricky. Just using `ACCOUNTADMIN` is fast, but not a good practice.
4. Login to your instance and connect your Snowflake Account.
5. You did it! Great job. Tell your colleagues about it and explore!

## Self-Hosted

1. Install [`docker`](https://docs.docker.com/engine/install/) and [`docker-compose`](https://docs.docker.com/compose/install/) on a machine with 4 cores and 16GB RAM
2. Create a directory called `snowboard`
3. Download the Docker Compose configuration file: [`docker-compose.yml`](https://raw.githubusercontent.com/zurferr/snowboard\_software/main/docs/docker-compose.yml)
4. Start the deployment with `docker-compose up -d`
5. Sled is now ready on [http://localhost/onboarding/login](http://localhost/onboarding/login) or your server address
   * [Register here](https://register.s8.software) with your work-email. This will create your license. Now you can login on your self-hosted instance.&#x20;
6. Follow the on-boarding wizard and add your Snowflake account.
7. You did it! Great job. Tell your colleagues about it and explore!
