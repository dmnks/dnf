# Copyright (C) 2016 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

import os
import sys
import unittest

# Import the yum binary via the symlink since the binary doesn't have the .py
# extension.  Also ensure that, if the symlink breaks, the import won't
# fallback to a cached version.
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(__file__))
from . import yum


def translates(before, after):
    args = yum.filter_args(before.split(' '))
    return ' '.join(args) == after


class YumCompatTest(unittest.TestCase):
    def test_deprecate(self):
        assert translates('--disablerepo=* update foo bar -q',
                          '--disablerepo=* upgrade foo bar -q')
