# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2024 CERN.
#
# weko-communities is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module of weko-communities."""

from __future__ import absolute_import, print_function

from .ext import wekoCommunities
from .version import __version__

__all__ = ('__version__', 'wekoCommunities')