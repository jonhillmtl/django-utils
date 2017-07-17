import os

def get_settings_module():
    for root, dir, files in os.walk(os.getcwd()):
        if "settings.py" in files:
            return "{}.settings".format(root.rsplit("/")[-1])
    return None