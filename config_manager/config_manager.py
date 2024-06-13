import os
import json
import yaml
import shutil

class ConfigManager:
    def __init__(self, file_path ):
        self.file_path = file_path 
        self.data = None
        self.load_config()

    def load_config(self):
        with open(self.file_path, 'r') as file:
            if self.file_path.endswith('.json'):
                self.data = json.load(file)
            elif self.file_path.endswith('.yaml') or self.file_path.endswith('.yml'):
                self.data = yaml.safe_load(file)
            else:
                raise ValueError('Unsupported file format. Only JSON and YAML are supported.')

    def save_config(self):
        with open(self.file_path, 'w') as file:
            if self.file_path.endswith('.json'):
                json.dump(self.data, file, indent=4)
            elif self.file_path.endswith('.yaml') or self.file_path.endswith('.yml'):
                yaml.dump(self.data, file, default_flow_style=False)
            else:
                raise ValueError('Unsupported file format. Only JSON and YAML are supported.')

    def backup_config(self):
        backup_file_path = f"{self.file_path}.bak".replace("configs","configs\\backups")
        shutil.copy(self.file_path, backup_file_path)

    def validate_config(self):
        # Implement your validation logic here
        # Example: Check if certain keys exist in the configuration
        required_keys = ['db_host', 'db_user', 'db_password']
        for key in required_keys:
            if key not in str(self.data):
                raise ValueError(f"Missing required configuration key: {key}")

    def update_config(self, key, value):

        '''Supports Nested config update'''

        keys = key.split('.')
        d = self.data
        for k in keys[:-1]:
            if k not in d:
                d[k] = {}
            d = d[k]
        d[keys[-1]] = value
        self.save_config()


class DevConfig(ConfigManager):
    def __init__(self, file_path):
        super().__init__(file_path)
        # Add dev-specific initialization here

class StagingConfig(ConfigManager):
    def __init__(self, file_path):
        super().__init__(file_path)
        # Add staging-specific initialization here

class ProdConfig(ConfigManager):
    def __init__(self, file_path):
        super().__init__(file_path)
        # Add production-specific initialization here

# Example usage
def main():
    dev_config_path = 'configs\\dev_config.yaml'  # Can be .json or .yaml/.yml

    dev_config = DevConfig(dev_config_path)  # dev config update
    dev_config.backup_config()
    dev_config.validate_config()

    # Update the config with a new key-value pair
    dev_config.update_config('database.db_user', 'Admin')
    dev_config.update_config('apikey', 'ksdjfkljasklfdjlkasjfkld')

    staging_config_path = 'configs\\staging_config.yaml'  # Can be .json or .yaml/.yml
    staging_config = DevConfig(staging_config_path)  # Or use StagingConfig or ProdConfig
    staging_config.backup_config()
    staging_config.validate_config()

    # Update the config with a new key-value pair
    staging_config.update_config('database.db_host', 'staging-rds.mydomain.com')
    staging_config.update_config('apikey', 'ksdjfkljasklfdjlkasjfkld')

    prod_config_path = 'configs\\prod_config.json'  # Can be .json or .yaml/.yml
    prod_config = DevConfig(prod_config_path)  # ProdConfig
    prod_config.backup_config()
    prod_config.validate_config()

    # Update the config with a new key-value pair
    prod_config.update_config('database.db_host', 'prod-rds.mydomain.com')
    prod_config.update_config('apikey', 'ksdjfkljasklfdjlkasjfkld')

if __name__ == '__main__':
    main()
