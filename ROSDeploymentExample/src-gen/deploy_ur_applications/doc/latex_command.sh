#!/bin/sh
IMAGE=ghcr.io/ipa-rwu/latex_builder:latest
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD/build/latex":/data "$IMAGE" "$@"

