import yaml
from pystache import render
import sys
from pathlib import Path


def load_resume_data(yaml_file="resume.yaml"):
    """Load resume data from YAML file with error handling."""
    try:
        yaml_path = Path(yaml_file)
        if not yaml_path.exists():
            print(f"Error: YAML file '{yaml_file}' not found", file=sys.stderr)
            sys.exit(1)

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        if data is None:
            print(f"Error: YAML file '{yaml_file}' is empty or invalid", file=sys.stderr)
            sys.exit(1)

        return data

    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error loading YAML: {e}", file=sys.stderr)
        sys.exit(1)


# Load all data from YAML
resume_data = load_resume_data()

# Extract data - direct mapping from YAML
Name = resume_data['Name']
PageSummary = resume_data['PageSummary']
NPubs = resume_data['NPubs']
HIndex = resume_data['HIndex']
HomeURL = resume_data['HomeURL']
ScholarURL = resume_data['ScholarURL']
LinkedInURL = resume_data['LinkedInURL']
GithubURL = resume_data['GithubURL']
TwitterURL = resume_data['TwitterURL']
Jobs = resume_data['Jobs']
Schools = resume_data['Schools']
QuantumPapers = resume_data['QuantumPapers']
TheoryPapers = resume_data['TheoryPapers']
MaterialsPapers = resume_data['MaterialsPapers']

# Computed value (remains in Python)
PageTitle = Name + " Resume"

# Template configuration: (Input Template, Output File)
templates = [
    ("template.timeline.html", "rpmuller.html"),       # New main design
    ("template.html", "rpmuller.classic.html"),        # Previous design preserved
    ("template.sidebar.html", "rpmuller.sidebar.html"),
    ("template.right.sidebar.html", "rpmuller.right.sidebar.html"),
    ("template.concise.html", "rpmuller.concise.html"), # Demo
    ("template.dark.html", "rpmuller.dark.html"),       # Demo
    ("template.md", "rpmuller.md")
]

for template_file, output_file in templates:
    with open(template_file) as f:
        content = render(f.read(), locals())
    with open(output_file, "w") as f:
        f.write(content)
    print(f"Generated {output_file} from {template_file}")
