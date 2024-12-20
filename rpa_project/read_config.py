import json

def load_config(config_file="config.json"):
    """Load configuration parameters from the config file."""
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config
