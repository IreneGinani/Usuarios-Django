# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Usuario(models.Model):
    nome = models.TextField()
    idade = models.IntegerField()
    sexo = models.TextField()

    def __str__(self):
        return self.nome

