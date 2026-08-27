import os
import re

workspace = 'e:/github-portfolio'
secret_patterns = [
    r'(?i)api[_-]?key\s*[:=]\s*[\'"][a-zA-Z0-9_\-]{16,}[\'"]',
    r'(?i)secret\s*[:=]\s*[\'"][a-zA-Z0-9_\-]{16,}[\'"]',
    r'(?i)password\s*[:=]\s*[\'"][^\'"]+[\'"]',
    r'ghp_[a-zA-Z0-9]{36}',
    r'sk-[a-zA-Z0-9]{32,}',
    r'gsk_[a-zA-Z0-9]{32,}'
]

print("=== SECURITY SCAN STARTED ===")
secrets_found = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith('.env'):
            secrets_found.append((os.path.join(root, f), "ENV file detected"))
        filepath = os.path.join(root, f)
        if f.endswith(('.md', '.json', '.py', '.txt', '.svg')):
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                for idx, line in enumerate(fp, 1):
                    for pat in secret_patterns:
                        if re.search(pat, line):
                            secrets_found.append((filepath, f"Line {idx}: pattern match {pat}"))

if secrets_found:
    print("SECURITY ISSUES FOUND:")
    for item in secrets_found:
        print(item)
else:
    print("SECURITY CHECK RESULT: ZERO SECRETS FOUND. CLEAN FOR GIT COMMIT.")

print("\n=== WORKSPACE FILE TREE ===")
for root, dirs, files in os.walk(workspace):
    level = root.replace(workspace, '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")
