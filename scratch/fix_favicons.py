import os

def fix_favicons():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                new_content = content.replace(
                    '<link rel="icon" type="image/svg+xml" href="images/favicon.svg">',
                    '<link rel="icon" type="image/png" href="images/exellar-logo.png">'
                ).replace(
                    '<link rel="icon" type="image/svg+xml" href="/favicon.svg" />',
                    '<link rel="icon" type="image/png" href="/exellar-logo.png" />'
                )
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {path}")

if __name__ == "__main__":
    fix_favicons()
