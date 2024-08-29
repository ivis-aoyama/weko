# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2024 CERN.
#
# weko-communities is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Command line interface creation kit."""
import click
from flask.cli import with_appcontext
from invenio_files_rest.errors import FilesException

# from .models import WidgetType
# from .utils import WidgetBucket


@click.group()
def widget_type():
    """Widget Type commands."""


# @widget_type.command('create')
# @click.argument('type_id')
# @click.argument('type_name')
# @with_appcontext
# def insert_widget_type_to_db(type_id, type_name):
#     """Ex: fd Free description."""
#     try:
#         WidgetType.create(data={"type_id": type_id, "type_name": type_name})
#         click.secho('insert widget type success')
#     except Exception as e:
#         click.secho(str(e))


@click.group()
def widget():
    """Management commands for widgets."""


# @widget.command('init')
# @with_appcontext
# def init():
#     """Initialize widget bucket."""
#     try:
#         WidgetBucket().initialize_widget_bucket()
#     except FilesException as e:
#         click.secho(e.errors, fg='red')
