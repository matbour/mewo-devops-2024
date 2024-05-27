FROM ubuntu:latest

# Install the necessary dependencies and Mumble
RUN apt-get update && apt-get install -y \
  software-properties-common \
  wget \
  xz-utils \
  wayland-xcomposite-glx\
  mumble

# Expose the default port of Mumble (note that this is unnecessary for the Mumble client)
EXPOSE 64738

# Command to start Mumble
CMD ["mumble"]
