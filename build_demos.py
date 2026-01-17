from pystache import render
import os
import rpmuller  # Import the module to access data directly

# We need to access the data variables from rpmuller.py
# Since they are global variables in that module, we can access them like rpmuller.Name, etc.
# Ideally we would construct a dictionary of the context.
context = {
    "Name": rpmuller.Name,
    "PageTitle": rpmuller.PageTitle,
    "PageSummary": rpmuller.PageSummary,
    "NPubs": rpmuller.NPubs,
    "HIndex": rpmuller.HIndex,
    "HomeURL": rpmuller.HomeURL,
    "ScholarURL": rpmuller.ScholarURL,
    "LinkedInURL": rpmuller.LinkedInURL,
    "GithubURL": rpmuller.GithubURL,
    "TwitterURL": rpmuller.TwitterURL,
    "Jobs": rpmuller.Jobs,
    "Schools": rpmuller.Schools,
    "QuantumPapers": rpmuller.QuantumPapers,
    "TheoryPapers": rpmuller.TheoryPapers,
    "MaterialsPapers": rpmuller.MaterialsPapers,
}

templates = [
    "template.concise.html",
    "template.timeline.html",
    "template.dark.html"
]

for template in templates:
    if not os.path.exists(template):
        print(f"Skipping {template} (not found)")
        continue
        
    fname = template.replace("template", "rpmuller")
    print(f"Rendering {template} -> {fname}...")
    
    with open(template, 'r') as f:
        template_content = f.read()
        
    output_content = render(template_content, context)
    
    with open(fname, "w") as f:
        f.write(output_content)
        
print("Done!")
