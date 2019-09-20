import sys
import os
from scripts.strip_metadata import main
from unittest.mock import patch


def test_consistency():
    cur_dir = os.path.dirname(__file__)
    metadata_file = os.path.abspath(os.path.join(
        cur_dir, "..", "..", "..", "wm_metadata.yml"))
    wm_file = os.path.abspath(os.path.join(
        cur_dir, "..", "..", "..", "wm.yml"))
    sys_argv = ['strip_metadata.py', metadata_file,  'temp_wm.yml']
    with patch.object(sys, 'argv', sys_argv):
        main()
    with open(wm_file, 'r') as real_wm, open('temp_wm.yml', 'r') as test_wm:
        for line1, line2 in zip(real_wm, test_wm):
            assert line1 == line2, (
                'Stripping metadata.yml produces: %s, '
                'but wm.yml contains: %s' % (line1, line2))
