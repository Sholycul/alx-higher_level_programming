#!/bin/bash
# This script sends a GET request to the URL provided with a custom header and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
