
# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import os

from anaconda_rust.plugin.handlers_rust.rust_lint_handler import RustLintHandler  # noqa


class TestLint(object):
    """AnacondaRUST linter tests suite
    """

    def setUp(self):
        self.settings = {'use_rustc_lint': True}

    def test_rustc_lint(self):
        fixture = os.path.join('fixtures', 'lint.rs')
        handler = RustLintHandler('lint', None, 0, 0, self._check_rustc)
        handler.lint(self.settings, '', fixture)

    def _check_rustc(self, result):
        assert result['success'] is True
        assert len(result['errors']) == 1
        assert result['errors'][0]['level'] == 'E'
        try:
            assert result['errors'][0]['message'] == '[E] rustc (error): expected one of `.`, `;`, or an operator, found `}`'  # noqa
        except:
            assert result['errors'][0]['message'] == '[E] rustc (error): expected one of `.`, `;`, `?`, or an operator, found `}`'  # noqa
        assert result['errors'][0]['underline_range'] is True
        assert result['errors'][0]['lineno'] == 3
        assert result['errors'][0]['offset'] == 1
        assert result['uid'] == 0
        assert result['vid'] == 0
