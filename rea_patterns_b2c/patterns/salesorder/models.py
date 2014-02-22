from django.db import models
from django_xworkflows import models as xwf_models

from rea.models import Contract, ContractInstance, ClauseRuleAspect

from .workflows import SalesOrderWorkflow


class SalesOrder(Contract):
    '''
    Sales Order Pattern Contract

    '''
    pass


class SalesOrderInstance(ContractInstance):
    '''
    An Instance of the SalesOrder and corresponding Offer
    and economic Event.
    '''
    # receiving_agent
    # providing_agent

    # schematically equivalent to the StateField below as a temp fix
    # for a seeming incompatibility with Django 1.7                                                                                
    state = models.CharField(max_length='512')

    # is this field django 1.7 compatible?
    # how can I know? 
    # state = xwf_models.StateField(SalesOrderWorkflow, max_length='512')

# 
# Sales Order Clause Rules
# 
