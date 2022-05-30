#!/bin/bash
# Bash script that displays the size of the body of the response of URL request
curl -so /dev/null $1 -w '%{size_download}'
