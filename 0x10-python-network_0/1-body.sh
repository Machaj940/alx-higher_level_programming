#!/bin/bash
# Script that sends a GET request and displays the 200 status code response
curl -so /dev/null -I -w '%{http_code}' $1
