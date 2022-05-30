#!/bin/bash
# Bash script that displays all HTTP methods the server will accept
curl -i -L -X OPTIONS $1
