# Log #001

# Issue
The `awos-core` directory was not appearing in Git.
Only README.md was being tracked.

# Cause
The `.gitignore` inside `awos-core` contained:
*
which caused Git to ignore every file in that directory.

# Solution
Removed the `*` line from
`awos-core/.gitignore`.
Verified using:
git status

# Result
The backend files were detected and committed successfully.


# problem
Wrong Python Environment

Issue

Conda Python being used.

# solution

Activated

.venv

# Verified

echo $VIRTUAL_ENV

# problem
LangGraph Integration

Risk

Breaking execution service.

# Solution

Wrapped existing pipeline.

No functionality changed.