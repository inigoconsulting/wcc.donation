from five import grok
from plone.directives import dexterity, form
from wcc.donation.content.donationpage import IDonationPage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IDonationPage)
    grok.require('zope2.View')
    grok.template('donationpage_view')
    grok.name('view')
