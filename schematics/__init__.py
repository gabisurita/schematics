# -*- coding: utf-8 -*-

__version__ = '2.0.0.b1'

# TODO: remove deprecated API
from . import deprecated
deprecated.patch_all()

from . import types
from .models import Model, ModelMeta

types.compound.Model = Model
types.compound.ModelMeta = ModelMeta

__all__ = ['Model']
