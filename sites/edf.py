from data.orm import Offer
from data.orm import Site
from ._parser import SiteParser
import requests
from datetime import datetime

class EDFParser(SiteParser):

    site: Site = Site.get_by_id(8)
    url: str = site.url

    def get_offers(self) -> list[Offer]:
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.edf.fr",
            "referer": "https://www.edf.fr/edf-recrute/rejoignez-nous/voir-les-offers/nos-offers?search%5Bprofil%5D%5B34950%5D=34950&search%5Bkeyword%5D=python",
            "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "cookie": "TCPID=124451519289237561555; _pcid=... (remplacer par les valeurs correctes)"
        }

        data = {
            "location": "Ile-de-France",
            "latitude": "",
            "longitude": "",
            "profil[34950]": "34950",
            "keyword": "python",
            "recherche_bord": "",
            "form_build_id": "form-v1QBcX-pHoE7X7J5n5fXOO9yB9wIg31a29XyuQUIduM",
            "form_id": "rzr_recrute_talentsoft_resultat_form",
            "_triggering_element_name": "op",
            "_triggering_element_value": "Mettre à jour les offers",
            "_drupal_ajax": 1,
            "ajax_page_state[theme]": "nova",
            "ajax_page_state[theme_token]": "",
            "ajax_page_state[libraries]": "core/drupal.autocomplete,core/internal.jquery.form,nova/banner-intro,nova/block-titre,nova/breadcrumbs,nova/button,nova/checkbox,nova/commander_act_footer,nova/commander_act_header,nova/editorial-page,nova/footer,nova/geoloc,nova/global,nova/header,nova/input,nova/label,nova/legend,nova/link,nova/link-home,nova/list-checkboxes-expanded,nova/list-radios-expanded,nova/main-menu,nova/push-text,nova/radio,nova/recrute-offers-list,nova/recrute-result-form,nova/recrute-result-list,nova/secondary-menu,nova/section,nova/state,nova/tag,nova/text-section,nova/title,nova/webform-element,paragraphs/drupal.paragraphs.unpublished,system/base"
        }
        response = requests.post(self.url, headers=headers, data=data)

        try:
            data = response.json()[-1]["data"]
        except:
            return []

        job_offers = self.parse_offers_html(data)
        return job_offers

    def parse_offers_html(self, html_data: str) -> list[Offer]:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_data, 'html.parser')
        
        months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

        job_offers = []
        for offer in soup.select('.offer'):
            title = offer.select_one('.offer-description h3').text.strip()
            url = "https://www.edf.fr" + offer.select_one('.offer-link')['href']
            
            date_str = offer.select_one('.offer-date').text.strip()
            day, month, year = date_str.split()
            month_index = months.index(month) + 1
            date_publication = datetime.strptime(f"{day} {month_index} {year}", '%d %m %Y').date()
            
            location = offer.select_one('.offer-description .offer-detail-description').text.strip()
            job_id = url.split('/')[-1]

            job_offers.append(
                Offer(
                    site=self.site,
                    title=title,
                    description=None,
                    url=url,
                    date_publication=date_publication,
                    location=location,
                    job_id=job_id
                )
            )
        return job_offers


if __name__ == "__main__":
    print(EDFParser().compare_offers())
