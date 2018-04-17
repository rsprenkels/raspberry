#!/bin/bash

find . -name "*.py" | entr -c python testSplitJoiner.py
