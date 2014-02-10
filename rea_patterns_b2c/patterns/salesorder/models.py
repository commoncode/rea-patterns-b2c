from django.db import models
from django_xworkflows import models as xwf_models

from rea.models import Contract
from rea.settings import REA_RECEIVING_AGENT_MODEL, REA_PROVIDING_AGENT_MODEL

from .workflows import SalesOrderWorkflow


class SalesOrder(Contract):
    '''
    Sales Order Pattern Contract

    '''
    state = xwf_models.StateField(SalesOrderWorkflow)

    receiving_agent = models.ForeignKey(
        REA_RECEIVING_AGENT_MODEL
    )
    providing_agent = models.ForeignKey(
        REA_PROVIDING_AGENT_MODEL
    )