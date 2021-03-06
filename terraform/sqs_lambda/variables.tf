variable "sns_topic_arn" {
  description = "SNS topic arn of central or local sns topic"
  type        = string
}

variable "reflex_kms_key_id" {
  description = "KMS Key Id for common reflex usage."
  type        = string
}

variable "cloudwatch_event_rule_id" {
  description = "Easy name of CWE"
  type        = string
  default     = null
}

variable "cloudwatch_event_rule_arn" {
  description = "Full arn of CWE"
  type        = string
  default     = null
}

variable "mode" {
  description = "The mode that the Rule will operate in. Valid choices: DETECT | REMEDIATE"
  type        = string
  default     = "detect"
}

variable "default_backup_retention" {
  description = "Days of retention in case retention set to zero."
  type        = number
  default     = 1
}

variable "package_location" {
  description = "Path for the Lambda deployment package"
  type        = string
  default     = "../package_build/rds-automated-backup-disabled.zip"
}
