#!/usr/bin/env python3
import re
import glob

# Define page titles in French
page_titles = {
    'about.html': ('À Propos', 'À Propos'),
    'campaign.html': ('Nos Projets', 'Nos Projets'),
    'blog.html': ('Actualités & Formations', 'Blog'),
    'contact.html': ('Contactez-nous', 'Contact'),
    'operation-videos.html': ('Vidéos Opérationnelles', 'Vidéos'),
    'extincteurs.html': ('Extincteurs', 'Services'),
    'detection-incendie.html': ('Détection Incendie', 'Services'),
    'desenfumage.html': ('Désenfumage', 'Services'),
    'robinets-incendie-armes.html': ('Robinets d\'Incendie Armés', 'Services'),
    'portes-coupe-feu.html': ('Portes Coupe-Feu', 'Services'),
    'signaletique-evacuation.html': ('Signalétique d\'Évacuation', 'Services'),
    'extinction-automatique.html': ('Extinction Automatique', 'Services'),
    'stations-pompage.html': ('Stations de Pompage', 'Services'),
}

def update_page_header(filepath, title, breadcrumb_parent):
    """Update page header to use hero image and French title"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the page header section - match from section tag to /section tag
        # Replace the background image and title
        header_pattern = r'<section>\s*<div class="gap black-layer opc8 overlap144">.*?</section>'
        
        new_header = f'''<section>
            <div class="gap black-layer opc8 overlap144">
                <div class="fixed-bg2" style="background-image: url(assets/images/hero-slide1.jpg);"></div>
                <div class="container">
                    <div class="pg-tp-wrp">
                        <h1 itemprop="headline">{title}</h1>
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><a href="index.html" title="" itemprop="url">Accueil</a></li>'''
        
        # Add parent breadcrumb if it's a service page
        if breadcrumb_parent == 'Services':
            new_header += '''
                            <li class="breadcrumb-item"><a href="service.html" title="" itemprop="url">Services</a></li>'''
        
        new_header += f'''
                            <li class="breadcrumb-item active">{title}</li>
                        </ol>
                    </div>
                </div>
            </div>
        </section>'''
        
        # Replace the header
        content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"✗ Error updating {filepath}: {str(e)}")
        return False

# Update all pages
success_count = 0
for filename, (title, parent) in page_titles.items():
    if update_page_header(filename, title, parent):
        print(f"✓ Updated: {filename}")
        success_count += 1

print(f"\n✓ Successfully updated {success_count}/{len(page_titles)} page headers")
