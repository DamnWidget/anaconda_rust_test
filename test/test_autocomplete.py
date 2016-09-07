
# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import os

from anaconda_rust.plugin.handlers_rust.rust_racer_handler import RacerHandler
from anaconda_rust.plugin.handlers_rust.commands.autocomplete import AutoComplete  # noqa

from config import rust_paths


class TestAutoComplete(object):
    """AnacondaRUST auto completion tests suite
    """

    def setUp(self):
        with open('fixtures/completion.rs') as f:
            source = f.read()
        self.settings = {
            'source': source,
            'rust_src_path': rust_paths['src'],
            'racer_binary_path': rust_paths['racer'],
            'row': 0,
            'col': 14
        }

    def test_autocomplete(self):
        fixture = os.path.join('fixtures', 'completion.rs')
        AutoComplete(self._check_completion, 0, 0, fixture, self.settings)  # noqa

    def test_autocompete_fail_no_file(self):
        AutoComplete(self._check_fail_no_file, 0, 0, 'no.rs', self.settings)

    def test_autocomplete_handler(self):
        fixture = os.path.join('fixtures', 'completion.rs')
        data = {'filename': fixture, 'settings': self.settings}
        handler = RacerHandler('autocomplete', data, 0, 0, self._check_completion)  # noqa
        handler.run()

    def _check_completion(self, result):
        assert result['success'] is True
        assert 'FromStr' in result['completions'][0][0]
        assert 't pub trait FromStr: Sized' in result['completions'][0][0]
        assert result['completions'][0][1] == 'FromStr'
        assert 'Utf8Error' in result['completions'][1][0]
        assert 's pub struct Utf8Error' in result['completions'][1][0]
        assert result['completions'][1][1] == 'Utf8Error'

    def _check_fail_no_file(self, result):
        assert result['success'] is False
