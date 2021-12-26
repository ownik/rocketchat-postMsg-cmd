import pytest

import sys
sys.path.append('src')

import utils

@pytest.mark.parametrize("str, expected", [
    ('Hello world!', 'Hello world!'),
    ('Hello\\nworld!', 'Hello\nworld!'),
    ('Hello\\\\n\\nworld!', 'Hello\\n\nworld!'),
    ('Hello world!\\n', 'Hello world!\n'),
    ('\\\\\\nHello world!\\\\\\n', '\\\nHello world!\\\n'),
])
def test_escape_string(str, expected):
    assert utils.parse_escaped_str(str) == expected