#! /bin/sh
# exit this script if any commmand fails
set -e

echo "Get Unity version for $UNITY_VERSION"
url=$(python unitydownloadurl.py $UNITY_VERSION)
realVersion=${url/*Unity-/}
realVersion=${realVersion/.pkg*/}
echo "Got Unity version:$realVersion"
echo "Got Unity url:$url"

echo "Downloading from $url: "
curl -o Unity.pkg "$url"

echo 'Installing Unity.pkg'
sudo installer -dumplog -package Unity.pkg -target /
