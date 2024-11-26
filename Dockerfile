# Use an official Rust image as the base
FROM rust:latest

# Set the working directory inside the container
WORKDIR /app

# Install dependencies required for building Rust projects
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install the CLI tool from the specified Git repository
RUN cargo install --git https://github.com/BigBoot/AutoKuma.git kuma-cli

# Create a symbolic link to make the tool easily executable
RUN ln -s /usr/local/cargo/bin/kuma-cli /usr/bin/kuma-cli

# Set the entry point to the CLI tool
ENTRYPOINT ["kuma"]

# Optionally specify a default command
CMD ["--help"]
