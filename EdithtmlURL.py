import os
import re

# Your transformation string
TRANSFORMATION = 'e_brightness:30,e_contrast:20'

# Regex: matches Cloudinary URLs and injects the transformation after '/upload/'
pattern = re.compile(r'(https://res\.cloudinary\.com/[^/]+/image/upload/)([^"\s]*)')

def inject_transformations(content):
    def replacer(match):
        base = match.group(1)
        rest = match.group(2)

        # If the transformation is already in the URL, skip it
        if TRANSFORMATION in rest:
            return match.group(0)

        # Add transformation right after /upload/
        return base + TRANSFORMATION + '/' + rest

    return pattern.sub(replacer, content)

def update_html_files():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            updated = inject_transformations(content)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(updated)

            print(f'Updated: {filename}')

if __name__ == '__main__':
    update_html_files()
