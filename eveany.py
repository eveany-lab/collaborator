import argparse
import os
import datetime

def generate_files(project_name, organization, year):
    # Template for LICENSE-EICL.md
    license_template = f"""Copyright © {year} {organization}\n\nThis project is licensed under the Ethical Internet Computing License (EICL)."""
    license_path = os.path.join(os.getcwd(), 'LICENSE-EICL.md')
    with open(license_path, 'w') as license_file:
        license_file.write(license_template)

    # Template for copyright attribution file
    attribution_template = f"""Project Name: {project_name}\nOrganization: {organization}\nYear: {year}"""
    attribution_path = os.path.join(os.getcwd(), 'COPYRIGHT_ATTRIBUTION.md')
    with open(attribution_path, 'w') as attribution_file:
        attribution_file.write(attribution_template)
    
    print(f'Generated files: {license_path} and {attribution_path}')


def main():
    parser = argparse.ArgumentParser(description='Eveany CLI tool')
    parser.add_argument('command', choices=['add'], help='Command to run')
    parser.add_argument('attrib', help='Sub-command to add attribution')
    args = parser.parse_args()

    if args.command == 'add' and args.attrib == 'attrib':
        # Auto-detecting or prompting for project details
        project_name = input('Enter project name: ') or 'Default Project'
        organization = input('Enter organization name: ') or 'Default Organization'
        year = input('Enter year of authorship: ') or str(datetime.datetime.now().year)
        generate_files(project_name, organization, year)

if __name__ == '__main__':
    main()