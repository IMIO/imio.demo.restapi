# -*- coding: utf-8 -*-

from imio.restapi.form.form import BaseForm
from plone.z3cform.layout import FormWrapper


class DocumentForm(BaseForm):
    _request_schema = "Document"
    _application_id = "IADELIB"


class DocumentFormView(FormWrapper):
    form = DocumentForm
