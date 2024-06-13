from site_parsing.sites import *
from site_parsing.data.orm import OfferGroup, get_filters
import datetime
import traceback

def run(site, filters: dict = {}):
    print(f"Adding offers from {site.__name__}")
    try:
        parser: SiteParser = site()
        offers = parser.get_offers_(filters)
        
        parser.add_offers(offers)
    except Exception as e:
        print(f"An error occurred while adding offers from {str(site.__name__).replace('Parser', '')}")
        error_filename = f"./errors/error_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(site.__name__).replace('Parser', '')}.log"
        with open(error_filename, "w") as f:
            f.write(f"Exception: {str(e)}\n")
            f.write("Traceback:\n")
            traceback.print_exc(file=f)

def run_all():
    # Loop through all the sites and add new job offers to the database
    filters = get_filters()
    for _, site in enumerate(PARSERS):
        run(site, filters)
        print("-" * 20)

if __name__ == "__main__":
    driver = SiteParser().driver
    driver.close()
    print()
    print("-" * 20)
    
    run_all()
    
    # p = SiteParser()
    # print(p.departement_from_nom("Haute-Garonne"))