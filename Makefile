#!/bin/bash

all:
	python text.py

push:
	@githome
	@git status
	@git add .
	@git commit -m "Makefile auto commit"
	@git status
	@git push