from django.db import models
from django_xworkflows import models as xwf_models

from rea.models import Contract
from rea.settings import REA_RECEIVING_AGENT_MODEL, REA_PROVIDING_AGENT_MODEL

from .workflows import SalesOrderWorkflow


class SalesOrder(Contract):
    '''
    Sales Order Pattern Contract

    '''

    # schematically equivalent to the StateField below as a temp fix
    # for a seeming incompatibility with Django 1.7                                                                                
    state = models.CharField(max_length='512')

    # is this field django 1.7 compatible?
    # how can I know? 
    # state = xwf_models.StateField(SalesOrderWorkflow, max_length='512')

    receiving_agent = models.ForeignKey(
        REA_RECEIVING_AGENT_MODEL,
        related_name='%(app_label)s_%(class)s_receiving_agent'
    )
    providing_agent = models.ForeignKey(
        REA_PROVIDING_AGENT_MODEL,
        related_name='%(app_label)s_%(class)s_providing_agent'
    )