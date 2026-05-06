import os
import re

base_dir = "/home/adzibilal/adzibilal/ims/ims-docs/content/docs"

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".mdx"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
            
            # Using regex to find ```mermaid ... ``` blocks
            # We replace it with <Mermaid chart={` ... `} />
            
            new_content = re.sub(
                r'```mermaid\n(.*?)\n```',
                r'<Mermaid\n  chart={`\n\1\n`}\n/>',
                content,
                flags=re.DOTALL
            )
            
            if new_content != content:
                with open(file_path, "w") as f:
                    f.write(new_content)
                print(f"Updated {file_path}")

print("Mermaid replacement done.")
