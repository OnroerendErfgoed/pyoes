"""
Cache busting: a short hash of a static file's contents, added to its url as
``?v=<hash>`` so browsers fetch a new version as soon as the file changes.
"""

import hashlib
import os
import stat
from functools import lru_cache

PARAM = "v"


def file_hash(path):
    """
    Return a short hash of the contents of ``path``, or ``None`` if it is not
    an existing file. The result is cached until the file's mtime or size
    changes, so edits during development are picked up.
    """
    try:
        st = os.stat(path)
    except OSError:
        return None
    if not stat.S_ISREG(st.st_mode):
        return None
    return _hash(path, st.st_mtime_ns, st.st_size)


@lru_cache(maxsize=1024)
def _hash(path, mtime_ns, size):
    with open(path, "rb") as f:
        return hashlib.md5(f.read(), usedforsecurity=False).hexdigest()[:10]
