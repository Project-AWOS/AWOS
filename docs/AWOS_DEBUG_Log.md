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


