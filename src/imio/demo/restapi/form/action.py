# -*- coding: utf-8 -*-

from imio.restapi.form.action import RESTAction
from zope.component import adapter
from zope.publisher.interfaces.browser import IBrowserRequest
from Products.ATContentTypes.interfaces.document import IATDocument


@adapter(IATDocument, IBrowserRequest)
class DocumentAction(RESTAction):
    title = u"Add Document"
    application_id = u"IADELIB"
    schema_name = u"Document"
    view_name = u"document-form"
