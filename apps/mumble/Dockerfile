FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

# Installer les dépendances nécessaires et compiler Mumble 
RUN apt-get update &&  apt-get install mumble-server -y

# Exposer le port par défaut de Murmur
EXPOSE 64738

# Commande pour démarrer Murmur
CMD ["murmurd", "-fg", "-v"]
