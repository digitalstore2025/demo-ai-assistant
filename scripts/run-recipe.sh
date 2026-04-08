#!/bin/bash

set -e

echo "Running Goose recipe..."
goose run recipes/test-stabilization.yaml
