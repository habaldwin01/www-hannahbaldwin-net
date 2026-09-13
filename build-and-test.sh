#!/bin/bash

podman build -t habaldwin01/www-hannahbaldwin-net:latest -t habaldwin01/www-hannahbaldwin-net:$(git describe --tags) .
podman run -it --rm -p 8080:8080 habaldwin01/www-hannahbaldwin-net:latest
