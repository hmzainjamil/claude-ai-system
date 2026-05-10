# CLI-Based Actorization

For languages without an SDK (Go, Rust, Java, etc.), create a wrapper script that uses the Apify CLI.

## Create Wrapper Script

Create `start.sh` in project root:

```bash
#!/bin/bash
set -e

# Get input from Apify key-value store
INPUT=$(apify actor:get-input)

# Parse input values (adjust based on your input schema)
MY_PARAM=$(echo "$INPUT" | jq -r '.myParam // "default"')

# Run your application with the input
./your-application --param "$MY_PARAM"

# If your app wr