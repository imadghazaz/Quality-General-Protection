#!/usr/bin/env python3
import glob
import re

html_files = glob.glob('*.html')

success_count = 0
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace logo2.png with logo-QGP.png in the responsive header
        # This targets the mobile menu logo specifically
        content = re.sub(
            r'(<div class="logo"><a href="index\.html" title="Logo" itemprop="url"><img src="assets/images/)logo2\.png(" alt=")logo2\.png',
            r'\1logo-QGP.png\2QGP Logo',
            content
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {html_file}")
        success_count += 1
    except Exception as e:
        print(f"✗ Error updating {html_file}: {str(e)}")

print(f"\n✓ Successfully updated {success_count}/{len(html_files)} files")
