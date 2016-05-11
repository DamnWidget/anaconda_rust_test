
# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import os

from anaconda_rust.plugin.handlers_rust.commands.rustfmt import RustFMT
from anaconda_rust.plugin.handlers_rust.rust_fmt_handler import RustFMTHandler

from utils import copyfile
from config import rust_paths


class TestRustFmt(object):
    """AnacondaRUST rustfmt tests suite
    """

    def setUp(self):
        self.settings = {'rustfmt_binary_path': rust_paths['rustfmt']}

    def test_rustfmt_command(self):
        fixture = os.path.join('fixtures', 'main.rs')
        RustFMT(self._check_rustfmt, 0, 0, copyfile(fixture), self.settings)

    def test_rustfmt_fail_no_file(self):
        RustFMT(self._check_fail_no_file, 0, 0, 'no.rs', self.settings)

    def test_rustfmt_handler(self):
        fixture = os.path.join('fixtures', 'main.rs')
        data = {'filename': copyfile(fixture), 'settings': self.settings}
        handler = RustFMTHandler("format", data, 0, 0, self._check_rustfmt)
        handler.run()

    def _check_rustfmt(self, result):
        assert os.path.exists('fixtures/_main.rs') is False
        assert result['success'] is True
        assert result['output'] == 'use std::str::FromStr;\n\nfn main() {\n    println!("Hello Test World!");\n}'  # noqa
        assert result['uid'] == 0
        assert result['vid'] == 0

    def _check_fail_no_file(self, result):
        assert result['success'] is False
