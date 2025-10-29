#!/usr/bin/env python3
import glob
import re

html_files = glob.glob('*.html')

success_count = 0
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the mobile contact info in rspn-cnt section
        old_pattern = r'<div class="rspn-cnt">\s*<span><i class="fas fa-envelope theme-clr"></i><a href="#" title="" itemprop="url">info@example\.com</a></span>\s*<span><i class="flaticon-telephone theme-clr"></i>\+\(00\) 123-345-11</span>\s*</div>'
        
        new_contact = '''<div class="rspn-cnt">
                    <span><i class="fas fa-envelope theme-clr"></i><a href="mailto:contact@qgp.ma" title="" itemprop="url">contact@qgp.ma</a></span>
                    <span><i class="flaticon-telephone theme-clr"></i>0669 53 85 33</span>
                </div>'''
        
        content = re.sub(old_pattern, new_contact, content, flags=re.DOTALL)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {html_file}")
        success_count += 1
    except Exception as e:
        print(f"✗ Error updating {html_file}: {str(e)}")

print(f"\n✓ Successfully updated {success_count}/{len(html_files)} files")
