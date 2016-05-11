
# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import os

from anaconda_rust.plugin.handlers_rust.commands.goto import Goto
from anaconda_rust.plugin.handlers_rust.rust_racer_handler import RacerHandler

from utils import copyfile
from config import rust_paths


class TestGoto(object):
    """AnacondaRUST goto tests suite
    """

    def setUp(self):
        self.settings = {
            'racer_binary_path': rust_paths['racer'],
            'rust_src_path': rust_paths['src'],
            'row': 0,
            'col': 21
        }

    def test_goto_command(self):
        fixture = os.path.join('fixtures', 'main.rs')
        Goto(self._check_goto, 0, 0, copyfile(fixture), self.settings)

    def test_goto_no_existing_file(self):
        Goto(self._check_fail_no_file, 0, 0, 'no.rs', self.settings)

    def test_goto_handler(self):
        fixture = os.path.join('fixtures', 'main.rs')
        data = {'filename': copyfile(fixture), 'settings': self.settings}
        handler = RacerHandler('goto', data, 0, 0, self._check_goto)
        handler.run()

    def _check_goto(self, result):
        assert os.path.exists('fixtures/_main.rs') is False
        assert result['success'] is True
        assert len(result['goto']) == 1
        assert len(result['goto'][0]) == 3
        assert 'mod.rs' in result['goto'][0][0]
        assert result['goto'][0][1] > 0 and result['goto'][0][2] > 0
        assert result['uid'] == 0
        assert result['vid'] == 0

    def _check_fail_no_file(self, result):
        assert result['success'] is False
