#!/bin/bash
# Bash script that sends a DELETE request to the URL and displays response body
curl -X "DELETE" $1 && curl -s -w "%{http_code}\n" -o /dev/null $1
