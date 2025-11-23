"""Entry script that demonstrates use of `ch_package`.

When executed directly (python practises/pac.py), Python's import path only
includes the `practises` directory, so a top-level package like `ch_package`
may not be found. To make this script runnable both as a module
(python -m practises.pac) and as a standalone script, we add the repository
root to sys.path if necessary.
"""

try:
    from ch_package import add, sub
except ModuleNotFoundError:
    # Add parent directory to sys.path (this file lives inside /practises)
    import os
    import sys

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    from ch_package import add, sub


if __name__ == "__main__":
    res = add()
    sub(10, 5)
