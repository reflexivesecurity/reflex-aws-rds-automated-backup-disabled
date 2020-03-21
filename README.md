# reflex-aws-rds-automated-backup-disabled
Rule to detect the disabling of automated backups.

## Usage
To use this rule either add it to your `reflex.yaml` configuration file:  
```
rules:
  - reflex-aws-rds-automated-backup-disabled:
      version: latest
```

or add it directly to your Terraform:  
```
...

module "reflex-aws-rds-automated-backup-disabled" {
  source           = "github.com/cloudmitigator/reflex-aws-rds-automated-backup-disabled"
}

...
```

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-rds-automated-backup-disabled/blob/master/LICENSE) 
