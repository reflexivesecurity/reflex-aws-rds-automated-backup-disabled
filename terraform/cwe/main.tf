module "cwe" {
  source      = "git::https://github.com/reflexivesecurity/reflex-engine.git//modules/cwe?ref=v2.1.0"
  name        = "RdsAutomatedBackupDisabled"
  description = "Rule to detect the disabling of automated backups."

  event_pattern = <<PATTERN
{
  "source": [
    "aws.rds"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "rds.amazonaws.com"
    ],
    "eventName": [
      "ModifyDBInstance"
    ]
  }
}
PATTERN

}
