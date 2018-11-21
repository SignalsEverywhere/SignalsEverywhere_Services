if [ ! "$(docker ps -q -f name=grant_bot)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=grant_bot)" ]; then
    # run your container
    docker restart grant_bot
    fi
fi
