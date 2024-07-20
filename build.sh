#!/bin/bash

if [ -z "$1" ]; then
  echo "Registry failed"
  exit 1
fi

if [ $1 == 'dockerhub' ]
then
  REGISTRY="vourteen14"
elif [[ $1 == 'custom' ]]
then
  REGISTRY="registry.karuhun.online"
else
  echo "Registry failed"
fi

sudo docker buildx build --platform linux/arm64 --push -t $REGISTRY/devops-backend:$2 .
