#!/usr/bin/env python3
import re
import os
import glob

# New simplified navbar
NEW_NAVBAR = '''        <header class="stick">
            <div class="tb-br">
                <div class="container">
                    <div class="scl1 float-left">
                        <a href="#" title="Facebook" itemprop="url" target="_blank"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" title="LinkedIn" itemprop="url" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#" title="Instagram" itemprop="url" target="_blank"><i class="fab fa-instagram"></i></a>
                    </div>
                    <ul class="tp-lst float-right">
                        <li><i class="fas fa-envelope theme-clr"></i><a href="mailto:contact@qgp.ma" title="" itemprop="url">contact@qgp.ma</a></li>
                        <li><i class="flaticon-telephone theme-clr"></i>0669 53 85 33</li>
                    </ul>
                </div>
            </div>
            <div class="lg-mnu-sec sticky">
                <div class="container">
                    <div class="logo" style="width: 250px;"><a href="index.html" title="Logo" itemprop="url"><img src="assets/images/logo-QGP.png" alt="QGP Logo" itemprop="image"></a></div>
                    <nav>
                        <div>
                            <ul>
                                <li><a href="index.html" title="" itemprop="url">Accueil</a></li>
                                <li><a href="about.html" title="" itemprop="url">À Propos</a></li>
                                <li><a href="service.html" title="" itemprop="url">Services</a></li>
                                <li><a href="campaign.html" title="" itemprop="url">Nos Projets</a></li>
                                <li><a href="blog.html" title="" itemprop="url">Blog</a></li>
                                <li><a href="operation-videos.html" title="" itemprop="url">Vidéos</a></li>
                                <li><a href="contact.html" title="" itemprop="url">Contact</a></li>
                            </ul>
                        </div>
                    </nav>
                </div>
            </div>
        </header>'''

# New simplified footer
NEW_FOOTER = '''        <footer>
            <div class="gap drk-bg">
                <div class="container">
                    <div class="ftr-dta remove-ext5">
                        <div class="row">
                            <div class="col-md-4 col-sm-12 col-lg-4">
                                <div class="wdgt-bx">
                                    <h5 itemprop="headline">QGP - Quality General Protection</h5>
                                    <p itemprop="description" style="color: #ccc; line-height: 1.8;">
                                        Spécialiste en protection incendie à Tanger. Nous offrons des solutions complètes pour la sécurité de vos locaux : installation, maintenance et formation.
                                    </p>
                                    <div class="scl1" style="margin-top: 20px;">
                                        <a href="#" title="Facebook" itemprop="url" target="_blank"><i class="fab fa-facebook-f"></i></a>
                                        <a href="#" title="LinkedIn" itemprop="url" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                                        <a href="#" title="Instagram" itemprop="url" target="_blank"><i class="fab fa-instagram"></i></a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-12 col-lg-3">
                                <div class="wdgt-bx">
                                    <h5 itemprop="headline">Nos Services</h5>
                                    <ul>
                                        <li><a href="extincteurs.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Extincteurs</a></li>
                                        <li><a href="detection-incendie.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Détection Incendie</a></li>
                                        <li><a href="desenfumage.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Désenfumage</a></li>
                                        <li><a href="robinets-incendie-armes.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>RIA</a></li>
                                        <li><a href="portes-coupe-feu.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Portes Coupe-Feu</a></li>
                                        <li><a href="service.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Tous les services</a></li>
                                    </ul>
                                </div>
                            </div>
                            <div class="col-md-2 col-sm-12 col-lg-2">
                                <div class="wdgt-bx">
                                    <h5 itemprop="headline">Liens Rapides</h5>
                                    <ul>
                                        <li><a href="about.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>À Propos</a></li>
                                        <li><a href="campaign.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Nos Projets</a></li>
                                        <li><a href="blog.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Blog</a></li>
                                        <li><a href="operation-videos.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Vidéos</a></li>
                                        <li><a href="contact.html" title="" itemprop="url"><i class="fas fa-angle-double-right"></i>Contact</a></li>
                                    </ul>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-12 col-lg-3">
                                <div class="wdgt-bx">
                                    <h5 itemprop="headline">Contactez-nous</h5>
                                    <ul class="cntct-inf">
                                        <li>
                                            <i class="fas fa-map-marker-alt theme-clr"></i>
                                            <span style="color: #ccc;">Tanger, Maroc</span>
                                        </li>
                                        <li>
                                            <i class="fas fa-phone-alt theme-clr"></i>
                                            <span style="color: #ccc;">0669 53 85 33</span>
                                        </li>
                                        <li>
                                            <i class="fas fa-envelope theme-clr"></i>
                                            <a href="mailto:contact@qgp.ma" style="color: #ccc;">contact@qgp.ma</a>
                                        </li>
                                        <li>
                                            <i class="fas fa-clock theme-clr"></i>
                                            <span style="color: #ccc;">Disponible 24h/24 - 7j/7</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="btm-br">
                <div class="container">
                    <div class="row">
                        <div class="col-md-12 col-sm-12 col-lg-12">
                            <p class="mb-0" style="text-align: center;">&copy; 2024 QGP - Quality General Protection. Tous droits réservés.</p>
                        </div>
                    </div>
                </div>
            </div>
        </footer>'''

def update_html_file(filepath):
    """Update navbar and footer in an HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace header (from <header to </header>)
        header_pattern = r'<header class="stick">.*?</header>'
        content = re.sub(header_pattern, NEW_NAVBAR, content, flags=re.DOTALL)
        
        # Replace footer (from <footer> to </footer>)
        footer_pattern = r'<footer>.*?</footer>'
        content = re.sub(footer_pattern, NEW_FOOTER, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print(f"✗ Error updating {os.path.basename(filepath)}: {str(e)}")
        return False

# Get all HTML files
html_files = glob.glob('*.html')
print(f"Found {len(html_files)} HTML files\n")

success_count = 0
for html_file in html_files:
    if update_html_file(html_file):
        success_count += 1

print(f"\n✓ Successfully updated {success_count}/{len(html_files)} files")
