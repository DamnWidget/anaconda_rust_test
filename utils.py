
# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import os
import shutil


def copyfile(filepath):
    path = 'fixtures/_{0}'.format(os.path.basename(filepath))
    shutil.copyfile(filepath, path)
    return path
