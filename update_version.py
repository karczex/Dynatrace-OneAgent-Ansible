#!/usr/bin/env python3
import argparse
import yaml

def update_version_in_yaml(file_path, version_field_name , version):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    yaml_data[version_field_name] = version
    print(yaml_data[version_field_name])

    with open(file_path, 'w') as file:
        yaml.safe_dump(yaml_data, file)

def update_galaxy_yaml(version):
    update_version_in_yaml("galaxy.yml", "version" ,version)

def update_main_yaml(version):
    update_version_in_yaml("roles/oneagent/vars/main.yml", "oneagent_script_version",  version)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='update_version',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('new_version')
    args = parser.parse_args()
    print(args.new_version)
    update_galaxy_yaml(args.new_version)
    update_main_yaml(args.new_version)

