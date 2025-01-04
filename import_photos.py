import os
from datetime import datetime

# Directory containing the JPEG files
directory = '/Users/cngan/Documents/mikecngan.github.io/sarasota_2024/'

# Get list of JPEG files sorted by date modified
jpeg_files = sorted(
    (f for f in os.listdir(directory) if f.lower().endswith('.jpeg')),
    key=lambda f: os.path.getmtime(os.path.join(directory, f))
)

# Generate HTML snippets
html_snippets = []
for jpeg in jpeg_files:
    snippet = f'''
    <div>
        <p>Sample Text</p>
        <img src="{jpeg}" alt="Alpine Visitor Center" style="width:100%">
    </div>'''
    html_snippets.append(snippet)

# Join all snippets into a single string
html_output = '\n'.join(html_snippets)

# Print or save the output
print(html_output)