#!/usr/bin/env python

import re

__version__ = '0.0.3'
version = __version__
version_info = tuple(re.split(r'[-\.]', __version__))

del re
