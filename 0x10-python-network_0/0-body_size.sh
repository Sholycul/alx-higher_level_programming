#!/bin/bash
# Takes a URL and send a request to it
curl -s "$1" | wc -c
