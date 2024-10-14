#!/bin/bash

python3 /api/get_resources.py &
apache2ctl -D FOREGROUND