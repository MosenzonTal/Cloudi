import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

def calculate(resource_id, activatedPolicy, user, region):
    validator = Violation.objects.get(connectedPolicy=activatedPolicy, resource_id=resource_id)

    if validator:
        validator.isChecked = True
        validator.isFixed = False
        recipient = validator.get_recipient(user, region)
        if activatedPolicy.actionItem.lower() == "notify":
            validator.notify(recipient)
        if activatedPolicy.actionItem.lower() == "delete":
            validator.delete_me(user, region)

        validator.save()
    else:
        create_violation(resource_id, activatedPolicy, user, region)


def create_violation(resource_id, activatedPolicy, user, region):
    new_violation = Violation.objects.create(connectedPolicy=activatedPolicy, resource_id=resource_id,
                             date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True, isFixed=False)

    recipient = new_violation.get_recipient(user, region)
    if activatedPolicy.actionItem.lower() == "notify":
        new_violation.notify(recipient)
    if activatedPolicy.actionItem.lower() == "delete":
        new_violation.delete_me(user, region)

def validator(resource_id, activatedPolicy, user, region):
    try:
        try:
            try:
                calculate(resource_id, activatedPolicy, user, region)
            except ObjectDoesNotExist:
                create_violation(resource_id, activatedPolicy, user, region)

        except KeyError:
            try:
                calculate(resource_id, activatedPolicy, user, region)
            except ObjectDoesNotExist:
                create_violation(resource_id, activatedPolicy, user, region)
    except:
        return sys.exc_info()
