#!/usr/bin/env bash
# Added --user 1001 because it needs to be root

# TODO Remove README_DOCKER.md from main folder once this works

CMD=$@

#Setting default command
if [ "$CMD" == "" ]; then
    CMD="python3 -m FreeTAKServer.controllers.services.FTS"
    CMD="$CMD -DataPackageIP 0.0.0.0"
    CMD="$CMD -AutoStart True"
fi

echo "Getting Public IP..."
PUBLIC_IP="$(curl ifconfig.me)"
echo "Public IP Found: $PUBLIC_IP"

USER="1001"
echo ""
echo "Running \`$CMD\` in Docker Container"
echo ""
docker run -it \
    --user $USER \
    -e FTS_DP_ADDRESS=$PUBLIC_IP \
    --mount src=ftsdata,target=/opt/FTSData \
	-p 8080:8080 -p 8087:8087 -p 8443:8443 \
	-p 9000:9000 -p 19023:19023 \
	fts:local \
	$CMD

#docker run -it \
#    --user 1001 \
#	-e FTS_DP_ADDRESS="$(curl ifconfig.me)" \
#	--mount src=ftsdata,target=/opt/FTSData \
#	-p 8080:8080 -p 8087:8087 -p 8443:8443 \
#	-p 9000:9000 -p 19023:19023 \
#	fts:local