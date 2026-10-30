#!/bin/sh
# Run everything with one command:  bash run_all.sh
set -e
cd "$(dirname "$0")"
python3 pipeline.py
PYTHONPATH=. python3 -m unittest discover -s tests -v
echo "All done: pipeline ran and tests passed."
