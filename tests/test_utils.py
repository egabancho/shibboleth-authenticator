# -*- coding: utf-8 -*-
#
# This file is part of the shibboleth-authenticator module for Invenio.
# Copyright (C) 2017  Helmholtz-Zentrum Dresden-Rossendorf
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Test utils."""

from __future__ import absolute_import, print_function

import pytest

from shibboleth_authenticator.utils import get_account_info


def _attributes():
    return dict(
        email_mapping='test@hzdr.de',
        id_mapping='123456',
        full_name_mapping='Test Tester',
    )


def _correct_result():
    return dict(
        user=dict(
            email='test@hzdr.de',
            profile=dict(
                full_name='Test Tester',
                username='123456',
            ),
        ),
        external_id='123456',
        external_method='hzdr',
    )


def test_accountinfo(models_fixture):
    """Test get_account_info."""
    # Test valid result.
    res = get_account_info(_attributes(), 'hzdr')
    assert res == _correct_result()

    # Test invalid remote app.
    with pytest.raises(KeyError):
        res = get_account_info(_attributes(), 'invalid')
