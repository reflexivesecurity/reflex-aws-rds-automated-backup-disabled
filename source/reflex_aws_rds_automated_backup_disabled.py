""" Module for RDSAutomatedBackupDisabled """

import json
import os

import boto3
from reflex_core import AWSRule, subscription_confirmation


class RDSAutomatedBackupDisabled(AWSRule):
    """ Rule to detect the disabling of automated backups."""

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.instance_id = event["detail"]["requestParameters"]["dBInstanceIdentifier"]
        self.backup_retention_period = event["detail"]["requestParameters"]["backupRetentionPeriod"]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        return self.backup_retention_period != 0

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        return f"The RDS instance {self.instance_id} has had automated backups disabled."


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    if subscription_confirmation.is_subscription_confirmation(event):
        subscription_confirmation.confirm_subscription(event)
        return
    rule = RDSAutomatedBackupDisabled(json.loads(event["Records"][0]["body"]))
    rule.run_compliance_rule()
