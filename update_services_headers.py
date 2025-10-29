#!/usr/bin/env python3
import re

# Read the service.html file
with open('service.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the page header section
old_header_pattern = r'<section>\s*<div class="gap black-layer opc8 overlap144">.*?</section>'
new_header = '''<section>
            <div class="gap black-layer opc8 overlap144">
                <div class="fixed-bg2" style="background-image: url(assets/images/hero-slide1.jpg);"></div>
                <div class="container">
                    <div class="pg-tp-wrp">
                        <h1 itemprop="headline">Nos Services</h1>
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><a href="index.html" title="" itemprop="url">Accueil</a></li>
                            <li class="breadcrumb-item active">Nos Services</li>
                        </ol>
                    </div>
                </div>
            </div>
        </section>'''

content = re.sub(old_header_pattern, new_header, content, flags=re.DOTALL)

# Replace the entire services section with the one from index.html
old_services_pattern = r'<section>\s*<div class="gap gray-bg">.*?</section>'
new_services = '''<section>
            <div class="gap gray-bg">
                <div class="container">
                    <div class="sec-tl text-center">
                        <span>Des solutions complètes en protection incendie</span>
                        <h2 itemprop="headline">Nos <span class ="theme-clr">Services</span></h2>
                    </div>
                    <div class="srv-wrp remove-ext7">
                        <div class="row">
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Extincteurs.png" alt="Extincteurs" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="extincteurs.html" title="" itemprop="url">Extincteurs</a></h5>
                                        <p itemprop="description">Installation et maintenance d'extincteurs fixes et mobiles conformément aux normes de sécurité.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Robinets-Incendie-Armes.png" alt="Robinets d'Incendie Armés" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="robinets-incendie-armes.html" title="" itemprop="url">Robinets d'Incendie Armés</a></h5>
                                        <p itemprop="description">Installation et maintenance de RIA (Robinets d'Incendie Armés) pour une protection optimale.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Detection-Incendie.jpg" alt="Détection Incendie" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="detection-incendie.html" title="" itemprop="url">Détection Incendie</a></h5>
                                        <p itemprop="description">Systèmes de détection d'incendie et asservissements pour une sécurité maximale.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Stations-de-Pompage.png" alt="Stations de Pompage" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="stations-pompage.html" title="" itemprop="url">Stations de Pompage</a></h5>
                                        <p itemprop="description">Installation et maintenance de stations de pompage pour systèmes anti-incendie.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Portes-Coupe-Feu.png" alt="Portes Coupe-Feu" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="portes-coupe-feu.html" title="" itemprop="url">Portes Coupe-Feu</a></h5>
                                        <p itemprop="description">Installation et maintenance de portes coupe-feu et portes de secours.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Desenfumage.png" alt="Désenfumage" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="desenfumage.html" title="" itemprop="url">Désenfumage</a></h5>
                                        <p itemprop="description">Installation d'exutoires de désenfumage pour l'évacuation des fumées.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Signaletique-Evacuation.png" alt="Signalétique d'Évacuation" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="signaletique-evacuation.html" title="" itemprop="url">Signalétique d'Évacuation</a></h5>
                                        <p itemprop="description">Plans, traçage et plaques d'évacuation conformes aux normes.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-6 col-lg-3">
                                <div class="srv-bx">
                                    <div class="srv-icn"><img src="assets/images/Extinction-Automatique.png" alt="Extinction Automatique" style="width: 80px; height: 80px; object-fit: contain; border-radius: 50%; margin-bottom: 20px;"></div>
                                    <div class="srv-inf">
                                        <h5 itemprop="headline" style="margin-top: 15px;"><a href="extinction-automatique.html" title="" itemprop="url">Extinction Automatique</a></h5>
                                        <p itemprop="description">Systèmes d'extinction automatique pour une réponse immédiate aux incendies.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

content = re.sub(old_services_pattern, new_services, content, flags=re.DOTALL, count=1)

# Write back to file
with open('service.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated service.html")
