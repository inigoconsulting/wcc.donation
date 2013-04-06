from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.donation import MessageFactory as _

class IWCCDonationLinkPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    url = schema.TextLine(
        title=_(u'URL'),
        required=True
    )

class Assignment(base.Assignment):
    implements(IWCCDonationLinkPortlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('WCC Donation Link Portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/wccdonationlinkportlet.pt')

    @property
    def available(self):
        return True

class AddForm(base.AddForm):
    form_fields = form.Fields(IWCCDonationLinkPortlet)
    label = _(u"Add WCC Donation Link Portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IWCCDonationLinkPortlet)
    label = _(u"Edit WCC Donation Link Portlet")
    description = _(u"")
