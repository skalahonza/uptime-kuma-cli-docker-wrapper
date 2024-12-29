# Uptime Kuma CLI Docker Wrapper

This repository provides a Dockerized CLI tool for managing Uptime Kuma monitors. The CLI tool is built using Python and the `click` library, and it interacts with the Uptime Kuma API to add and manage monitors.

## Setup

### Environment Variables

To configure the CLI tool, you need to set up the following environment variables in a `.env` file:

- `KUMA__URL`: The URL of your Uptime Kuma instance.
- `KUMA__USERNAME`: Your Uptime Kuma username.
- `KUMA__PASSWORD`: Your Uptime Kuma password.

You can use the provided `.env.template` file as a starting point. Copy the template to a new file named `.env` and fill in the required values.

### Building and Running the Docker Container

To build and run the Docker container using `compose.yml`, follow these steps:

1. Build the Docker image:
   ```sh
   docker-compose build
   ```

2. Run the Docker container:
   ```sh
   docker-compose up
   ```

This will start the CLI tool inside a Docker container, using the environment variables specified in the `.env` file.

## Usage

### Adding a Monitor

The CLI tool provides a command to add a monitor to your Uptime Kuma instance. The `add_monitor` command takes a single argument, `name`, which specifies the name of the monitor to be added.

To add a monitor, run the following command inside the Docker container:

```sh
docker-compose run uptime-kuma-cli add_monitor <name>
```

Replace `<name>` with the desired name of the monitor. The CLI tool will connect to your Uptime Kuma instance, check if a monitor with the specified name already exists, and add a new monitor if it does not.
