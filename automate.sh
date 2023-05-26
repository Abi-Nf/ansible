#!/bin/sh

ansible-playbook index.yml -e "test.config=$@" --ask-become-pass

echo Configuration done !