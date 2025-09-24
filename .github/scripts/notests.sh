#!/bin/bash

FORBIDDEN_DIR="docs/unified-test-documentation"

# Get the list of files added in the current commit
added_files=$(git diff --name-only --diff-filter=A origin/master)

# Check if any added file is within the forbidden directory
if [[ -n "$added_files" ]]; then
  for file in $added_files; do
    if [[ "$file" == "$FORBIDDEN_DIR/"* ]]; then
      echo "Error: Files cannot be added to $FORBIDDEN_DIR"
      echo "Submit tests to the OSFV repo instead"
      exit 1
    fi
  done
fi

exit 0
