#!/bin/bash
until ./bot.py; do
	echo "Crashed with exit code $?. Restarting...">&2
	sleep 1
done
