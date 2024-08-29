# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2024 CERN.
#
# weko-communities is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module of weko-communities."""

from __future__ import absolute_import, print_function

from flask_babelex import gettext as _
from werkzeug.exceptions import NotFound

from . import config
# from .views import handle_not_found


class wekoCommunities(object):
    """weko-communities extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)

        try:  # Check if handler already exists
            current_handler = app.error_handler_spec[None][404][NotFound]
        except (KeyError, TypeError):
            current_handler = None

        app.extensions['weko-communities'] = self

        # For widget pages
        # app.register_error_handler(404, lambda error:
        #                            handle_not_found(
        #                                error, current_handler=current_handler))

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if 'BASE_TEMPLATE' in app.config:
            app.config.setdefault(
                'WEKO_COMMUNITIES_BASE_TEMPLATE',
                app.config['BASE_TEMPLATE'],
            )
        for k in dir(config):
            if k.startswith('WEKO_GRIDLAYOUT_'):
                app.config.setdefault(k, getattr(config, k))
