from django_xworkflows import models as xwf_models
from django.utils.translation import ugettext_lazy as _


class SalesOrderWorkflow(xwf_models.Workflow):
    '''
    States of a sales order based transaction
    '''
    states = (
        ('init', _(u'Sales order initialized')),
        ('commitment', _(u'Sales order commitment reciprocity established')),
        ('event', _(u'Sales exchange duality achieved')),
    )

    transitions = (
        ('customer_committed', ('init'), 'commitment'),
        ('payment_recieved', 'commitment', 'event'),
        # XXX add order / fulfilment
    )

    initial_state = 'init'
