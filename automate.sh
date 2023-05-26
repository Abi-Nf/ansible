#!/bin/sh

ansible-playbook index.yaml -e "test.config=$@" --ask-become-pass

echo Configuration done !