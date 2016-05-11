from __future__ import absolute_import

# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import sys
import pkg_resources

if sys.version_info < (3, 4):
    raise RuntimeError('This can be test with python >= 3.4 only')

sys.path.append('anaconda_plugin/anaconda_server')
sys.path.append('anaconda_plugin/anaconda_lib')
pkg_resources.declare_namespace(__name__)
