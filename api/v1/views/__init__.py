#!/usr/bin/python3
"""blueprint"""
from flask import Blueprint

app_views = Blueprint("base", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
