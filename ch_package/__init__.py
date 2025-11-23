"""ch_package package exports.

Use relative imports so `ch_package` works when the repository is imported
as a package or installed as a distribution. Absolute imports like
`from func import ...` fail when `ch_package` isn't on sys.path.
"""

from .func import add, sub, mul, div

__all__ = ["add", "sub", "mul", "div"]
