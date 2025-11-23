"""practises package initializer.

We attempt to import `ch_package` so callers can access helpers from
`practises` directly. If `ch_package` is not available because the repo
root isn't on sys.path (common when executing modules directly), we add a
fallback that inserts the repo root into sys.path.
"""

try:
	from ch_package import *
except ModuleNotFoundError:
	import os
	import sys

	repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
	if repo_root not in sys.path:
		sys.path.insert(0, repo_root)
	try:
		from ch_package import *
	except ModuleNotFoundError:
		# Fail silently so imports of `practises` will not always raise.
		# Consumers that need `ch_package` should run the package from the
		# repository root or install the package into the environment.
		pass
