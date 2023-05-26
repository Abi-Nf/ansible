#!/bin/sh

ansible-playbook config.yml -e "test.config=$@" --ask-become-pass