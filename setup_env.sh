#!/bin/zsh

emulate -LR zsh
profile=${1:-gallerias3user}
echo "Using ${profile} credentials..."
echo "AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id --profile ${profile})" >> .env
echo "AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key --profile ${profile})" >> .env
env | grep AWS_ | sort
