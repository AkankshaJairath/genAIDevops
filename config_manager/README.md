As a DevOps engineer, you are tasked with (e.g., development, staging, production) in a consistent and automated manner. Each configuration file contains various settings such as database credentials, API keys, and other environment-specific parameters. Your task is to: 
1.Create a base class ConfigManager that handles reading from and writing to configuration files. 
2.Create derived classes for each environment (DevConfig, StagingConfig, ProdConfig) that inherit from the ConfigManager and include specific methods or attributes for those environments. 
3.Implement a method to backup existing configuration files before making any changes.
4.Implement a method to validate the configuration file content. 
5.Ensure the script can handle both JSON and YAML configuration files.
