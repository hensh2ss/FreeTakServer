# Docker Quickstart

:warning: **THIS IS NOT WELL SUPPORTED BY THE FTS TEAM RIGHT NOW, YOU ARE IN UNCHARTED TERRITORY** :warning:

I'd like to set this repo up to use github actions to push to pip and docker hub at the same time. Until that happens, here's how you can build and use this repo to build a docker image and run a container from it. It assumes you've already cloned it where you plan to use it. It _also_ means you'll be running whatever's in development, _not_ what's been released / in Pypi. 

:warning: **That means you might be running unreleased code with this method**

## Persistence
By default, docker will save pretty much nothing between runs of this container. So before we run this, we _really_ want somewhere for FreeTAKServer to store data. This container expects you to mount that volume at `/opt/FTSData/` inside the container. Let's put this in your home directory, for now. 

```shell
# This should work for all dockers, linux, windows, etc
docker volume create ftsdata 
```

:warning: FTS will store its database, data packages, ExCheck lists, and importantly, your _certificates_ in this volume. Keep all of these safe. 

## Creating a docker image from this repo.
`bash docker/build.sh`

## Run the container
OK, there's a lot to put in this command line, because there's lots of options we want to pass.

Let's run this interactively to start, so we can control the server. This assumes you want to use your public IP for the relevant IP Address configurations.
`bash docker/run.sh`