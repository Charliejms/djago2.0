# -*- coding: utf-8 -*-
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError


def badwords_detector(value):
    """
    Valida si en el 'value' se han puesto palabra no permitidas
    :return: Boolean
    """
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError('La palabra {0} no esta permitida'.format(badword))
    # Si todo va Ok devuelvi True
    return True
