# Daily Log

A simple command-line tool for tracking daily logs.

## Commands

Add a log:
py main.py add "study discrete math"

List logs:
py main.py list

Show current streak:
py main.py streak

## Error Handling

The program handles common input and data-loading errors:

- Empty logs, including whitespace-only input, are rejected.
- If `data.json` does not exist, the program starts with an empty log list.
- If `data.json` contains invalid JSON, the program reports the error and stops the current operation instead of treating the file as empty. This prevents existing data from being accidentally overwritten.