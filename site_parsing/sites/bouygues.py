from datetime import datetime
import re
from site_parsing.data.orm import Offer, OfferGroup, Site
from ._parser import SiteParser
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import urllib.parse

class BouyguesParser(SiteParser):
    
    site: Site = Site.get_by_id(10)
    url: str = site.url
    
    def extract_city(self, adresse):
        # Utilisation d'une expression régulière pour extraire le code postal et la ville
        match = re.search(r'\d{5}\s+([A-Z\s]+)', adresse)
        if match:
            return match.group(1).strip()
        else:
            return None
        
    def extract_offer_id(self, url):
        # Parse the URL to get the query parameters
        query_params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        # Extract the value of 'idOffre'
        offre_id = query_params.get('idOffre', [None])[0]
        return offre_id
    
    def get_offers_(self, offer_groups: dict = {}) -> list[Offer]:
        return self.get_offers(offer_groups)
    
    def get_offers(self, offer_groups: dict = {}) -> list[Offer]:
        job_offers: list[Offer] = []

        ### Récupération des données

        response = requests.get(self.url, timeout=10)
        data = response.text

        soup = BeautifulSoup(data, 'html.parser')

        # Recherche de tous les liens RSS
        rss_links = soup.find_all('a', href=True)

        # Extraction des titres et des liens
        rss_feeds = [(link.text.strip().replace('-', ' '), "https://bouyguestelecom-recrute.talent-soft.com"+link['href']) for link in rss_links if 'rss' in link['href'].lower()]

        ### Récupération des filtres
        for offer_group_id, filters in offer_groups.items():
            offer_group = OfferGroup.get_by_id(offer_group_id)
            
            keywords = filters.get("keyword", [])
            states = filters.get("state", [])
            
            new_offers = []
            for state in states:
                for flux_title, link in rss_feeds:
                    if state.replace('-', ' ').lower() in flux_title.lower():
                        response_feed = requests.get(link, timeout=10)
                        data_feed = response_feed.text #XML format
                        
                        # Parsing du fichier XML
                        root = ET.fromstring(data_feed)
                        
                        for item in root.findall('.//item'):
                            title = item.find('title').text
                            link = item.find('link').text
                            categories = item.findall('category')
                            contract = categories[1].text
                            location = categories[2].text if len(categories) > 2 else "Toulouse"
                            description = item.find('description').text
                            date = item.find('pubDate').text
                            if contract == "CDI" and any(keyword.lower() in description.lower() for keyword in keywords):
                                offer = Offer(
                                    site=self.site,
                                    title=title,
                                    description=description, 
                                    url=link,
                                    date_publication=datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z'),
                                    location=self.extract_city(location),
                                    job_id=self.extract_offer_id(link),
                                    offer_group=offer_group
                                )
                                
                                if not offer.exists():
                                    new_offers.append(offer)
                
            print(f"Found {len(new_offers)} offers for {self.__class__.__name__} (filter: {OfferGroup.get_by_id(offer_group_id).name})")
            job_offers += new_offers
                                                
        return job_offers
