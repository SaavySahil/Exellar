import re

def patch_logo_strip():
    with open('Home.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update .client-logos-strip properties
    pattern = r'\.client-logos-strip\s*\{([^}]+)\}'
    def repl(m):
        inner = m.group(1)
        # Remove existing borders
        inner = re.sub(r'border-top:[^;]+;', '', inner)
        inner = re.sub(r'border-bottom:[^;]+;', '', inner)
        return '.client-logos-strip { position: relative; ' + inner.strip() + ' }'
    
    content = re.sub(pattern, repl, content)
    
    # 2. Add pseudo-elements for full-width lines
    pseudo_css = """
        .client-logos-strip::before, .client-logos-strip::after { content: ''; position: absolute; left: 50%; transform: translateX(-50%); width: 100vw; height: 1px; background: rgba(0,0,0,0.08); z-index: 1; }
        .client-logos-strip::before { top: 0; }
        .client-logos-strip::after { bottom: 0; }
    """
    
    if '.client-logos-strip::before' not in content:
        content = content.replace('</style>', pseudo_css + '\n    </style>')
    
    with open('Home.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    patch_logo_strip()
