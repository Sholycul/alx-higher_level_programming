#!/bin/bash
# This script displays all HTTP methods the server will accept for the given URL
curl -s -I -X OPTIONS "$1" | grep "Allow:" | sed 's/Allow: //'
