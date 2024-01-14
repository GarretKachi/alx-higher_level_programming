#!/bin/bash
# Script that takes in a URL, sends a request to URL, and displays size of  body of response
curl -sX GET $1 -L
