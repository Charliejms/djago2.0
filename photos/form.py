# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):
    """
    Formulario para el modelo Photo
    """
    class Meta:
        model = Photo
        fields = [
            'name',
            'url',
            'description',
            'license',
            'visibility',
        ]

    def clean(self):
        """
        Valida si en la descripcion se han puesto palabra no permitidas
        :return: Diccionario con los atributos si OK
        """
        cleaned_data = super(PhotoForm, self).clean()
        description = cleaned_data.get('description', '')

        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError('La palabra {0} no esta permitida'.format(badword))
        # Si todo va Ok devuelbo los datos limpios / normalizados
        return cleaned_data
