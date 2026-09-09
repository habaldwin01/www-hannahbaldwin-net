#!/bin/bash

podman build -t habaldwin01/www-hannahbaldwin-net:latest -t habaldwin01/www-hannahbaldwin-net:$(git describe --tags) .
