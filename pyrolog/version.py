
from collections import namedtuple

__all__ = ['__version__', '__version_info__']

VersionInfo = namedtuple('VersionInfo', ['major', 'minor', 'patch', 'release_level', 'commit'])

__version__ = (2, 1, 0)
__version_info__ = VersionInfo(*__version__, 'beta', '3af325d')
