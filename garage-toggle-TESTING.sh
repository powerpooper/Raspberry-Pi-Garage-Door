#!/bin/bash

# Variables
relaypin="22"
toggle=$(pigs w $relaypin 0 mils 100 w $relaypin 1 mils 100 w $relaypin 0 mils 100 w $relaypin 1)

# Commands
$toggle
