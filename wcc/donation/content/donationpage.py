from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from wcc.donation import MessageFactory as _
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from zope.interface import Interface

class IDonationCategory(Interface):
    
    value = schema.TextLine(title=_(u'Form Value'))
    label = schema.TextLine(title=_(u'Title/Label'))


# Interface class; used to define content-type schema.

DONATION_DEFAULT=[
        {"value": "MostNeeded", "label": "Where it's most needed"},
        {"value": "Assembly", "label": "WCC 10th Assembly"},
        {"value": "EcumenicalWaterNetwork", "label": "Ecumenical Water Network"},
        {"value": "EAPPI", "label": "Accompaniers in Palestine and Israel (EAPPI)"},
        {"value": "Study", "label": "Ecumenical study and research - Bossey"},
        {"value": "Church", "label": "Church relationships and Christian witness"},
        {"value": "Interreligious", "label": "Inter-religious dialogue"},
        {"value": "Peace", "label": "Peace and reconciliation"},
        {"value": "Development", "label": "Development and justice"},
        {"value": "HIV", "label": "HIV/AIDS initiative in Africa"},
]

class IDonationPage(form.Schema, IImageScaleTraversable):
    """
    Donation page
    """

    form.widget(header_text="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    header_text = schema.Text(title=_(u'Header text'), 
        description=_(u'This text will appear above the donation form'),
        required=False
    )

    form.widget(footer_text="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    footer_text = schema.Text(title=_(u'Footer text'), 
        description=_(u'This text will appear beneath the donation form'),
        required=False
    )

    form.widget(categories=DataGridFieldFactory)
    categories = schema.List(title=_(u'Donation Categories'),
            description=_(u'One category per line'),
            value_type=DictRow(schema=IDonationCategory),
            default=DONATION_DEFAULT)
