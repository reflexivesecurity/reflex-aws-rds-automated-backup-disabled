""" Module for RDSAutomatedBackupDisabled """

import json
import os

import boto3
from reflex_core import AWSRule, subscription_confirmation


class RDSAutomatedBackupDisabled(AWSRule):
    """ Rule to detect the disabling of automated backups."""

    client = boto3.client("rds")

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.instance_id = event["detail"]["requestParameters"]["dBInstanceIdentifier"]
        self.backup_retention_period = event["detail"]["requestParameters"][
            "backupRetentionPeriod"
        ]
        self.default_backup_retention = os.environ.get("DEFAULT_BACKUP_RETENTION")

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        return self.backup_retention_period != 0

    def remediate(self):
        """ Fix the non-compliant resource """
        self.set_backup_retention_period()

    def set_backup_retention_period(self):
        """Function to reset a backup retention period to default time"""
        self.client.modify_db_instance(
            DBInstanceIdentifier=self.instance_id,
            BackupRetentionPeriod=int(self.default_backup_retention)
        )

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        message = (
            f"The RDS instance {self.instance_id} has had automated backups disabled."
        )
        if self.should_remediate():
            message += f"Automated backups were re-enabled with a period of {self.default_backup_retention} days."

        return message


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return
    rule = RDSAutomatedBackupDisabled(event_payload)
    rule.run_compliance_rule()
