from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from wcc.donation.content.donationpage import IDonationPage
# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.donation to 1002',
                description=u'Upgrade wcc.donation to 1002',
                source='1', destination='1002',
                sortkey=1, profile='wcc.donation:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.donation.upgrades:to1002')
    catalog = getToolByName(context, 'portal_catalog')

    for brain in catalog(object_provides=IDonationPage.__identifier__):
        obj = brain.getObject()
        obj.reindexObject()
