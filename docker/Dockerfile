# Docker Image for Running FreeTakServer (FTS)

FROM python:3.8

# Getting Update to OS
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3.8 python3-pip python3.8-dev

# Upgrade Pip
RUN pip install --upgrade pip

# Set Location for FTS Data Artifacts
ENV FTS_DATA_PATH="/opt/FTSData/"
ENV FTS_REPO_LOCATION="/fts-repo/"

# Setup User/Group with Correct Permissions
RUN groupadd -r freetak && useradd -m -r -g freetak freetak
RUN mkdir $FTS_DATA_PATH ; chown -R freetak:freetak $FTS_DATA_PATH
RUN mkdir $FTS_REPO_LOCATION ; chown -R freetak:freetak $FTS_REPO_LOCATION
USER freetak

# Install FTS Server
WORKDIR $FTS_REPO_LOCATION

# Install Deps early as they won't change often
COPY requirements.txt $FTS_REPO_LOCATION
RUN pip install -r requirements.txt

COPY setup.py README.md $FTS_REPO_LOCATION
COPY ./FreeTAKServer $FTS_REPO_LOCATION/FreeTAKServer
RUN pip install -e .

RUN python -c "import yaml"
#WORKDIR /FreeTAKServer
#
##TODO Fix this so it doesn't pull in entire tree
##COPY . /FreeTAKServer/.
#COPY --chown=freetak:freetak ./FreeTAKServer /FreeTAKServer
#
##TODO Figure out why this is re-installing packages from install above
#RUN pip3 install -e /FreeTAKServer
#
## DataPackagePort
#EXPOSE 8080
## CoTPort
#EXPOSE 8087
## SSLCoTPort
#EXPOSE 8089
## SSLDataPackagePort
#EXPOSE 8443
## FederationPort
#EXPOSE 9000
## APIPort
#EXPOSE 19023
#
##ENTRYPOINT [ "python", "TAKfreeServer/run.py", "-p", "8087" ]
#ENTRYPOINT [ "python3", "-m", "FreeTAKServer.controllers.services.FTS", "-DataPackageIP", "0.0.0.0", "-AutoStart", "True"]