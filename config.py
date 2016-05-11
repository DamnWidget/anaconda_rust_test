
# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import os

# set this to False if you don't have or you don't want to use
# your environ RUST_SRC_PATH variable but add a custom path
USE_ENVIRON_RUST_PATH = True

rust_paths = {
    'src': '',  # this should be set if USE_ENVIRON_RUST_PATH is False
    'rustc': 'rustc',
    'racer': 'racer',
    'rustfmt': 'rustfmt'
}

if USE_ENVIRON_RUST_PATH is True:
    rust_paths['src'] = os.environ.get('RUST_SRC_PATH', rust_paths['src'])
