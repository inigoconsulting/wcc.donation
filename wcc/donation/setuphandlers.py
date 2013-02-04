from collective.grok import gs
from wcc.donation import MessageFactory as _

@gs.importstep(
    name=u'wcc.donation', 
    title=_('wcc.donation import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.donation.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
