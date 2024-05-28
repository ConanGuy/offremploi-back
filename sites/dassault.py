from data.orm import Offer
from data.orm import Site

from ._parser import SiteParser

import requests
from datetime import datetime


class DassaultParser(SiteParser):

    site: Site = Site.get_by_id(2)
    url: str = site.url

    def get_offers(self) -> list[Offer]:
        payload = {
            "context": "synthesis%3Ddisabled%26q%3D%2523all%2Bcard_content_lang%253Afr%2B%2B%2528python%2529%2B%2B%2528card_content_type%253D%2522career%2522%2529%2B%2Bcard_content_categories%253A%2528%2528%2522year%252F0%2Bto%2B3%2Byears%2522%2529%2BAND%2B%2528%2522type%2Bde%2Bcontrat%252Fcdi%2522%2529%2BAND%2B%2528%2522pays%252Ffrance%2522%2529%2529%2B%26b%3D0%26s%3Ddesc%2528card_content_start_datetime%2529%26output_format%3Djson%26q.visibility_restriction%3Dcard_visibility%253A%2528True%2BOR%2Bpartnerportal%2BOR%2B3dscom_live%2529NOT%2528card_content_type%253APremiumArticle%2529%26hf%3D15%26q.class_restriction%3Dclass_hierarchy%253Acard",
            "nhits": 4,
            "nmatches": 4,
            "start": 0,
            "ellql": '#query{nbdocs=151051, text_relevance.expr="@term.score*@proximity+@b", proximity.maxDistance=1000, term.score=RANK_TFIDF}(#and(#and(#True() #alphanum{source="MOT",seqid=0,nbdocs=1068639,groupid=1,k=2}(card_content_lang,"fr") #alphanum{source="MOT",seqid=0,nbdocs=60009,groupid=2,k=2}(text,"python") #alphanum{source="MOT",seqid=0,groupid=3,k=2}(card_content_type,"career") #and(#seq(#alphanum{source="MOT",seqid=0,groupid=4,k=2}(card_content_categories,"year") #alphanum{source="MOT",seqid=1,groupid=4,k=2}(card_content_categories,"0") #alphanum{source="MOT",seqid=2,groupid=4,k=2}(card_content_categories,"to") #alphanum{source="MOT",seqid=3,groupid=4,k=2}(card_content_categories,"3") #alphanum{source="MOT",seqid=4,groupid=4,k=2}(card_content_categories,"years") ) #seq(#alphanum{source="MOT",seqid=0,groupid=5,k=2}(card_content_categories,"type") #alphanum{source="MOT",seqid=1,groupid=5,k=2}(card_content_categories,"de") #alphanum{source="MOT",seqid=2,groupid=5,k=2}(card_content_categories,"contrat") #alphanum{source="MOT",seqid=3,groupid=5,k=2}(card_content_categories,"cdi") ) #seq(#alphanum{source="MOT",seqid=0,groupid=6,k=2}(card_content_categories,"pays") #alphanum{source="MOT",seqid=1,groupid=6,k=2}(card_content_categories,"france") ) ) ) #category(categories,"Top/datamodelclasshierarchy/card") #and(#or(#alphanum{source="MOT",seqid=0,nbdocs=242513,groupid=1,k=2}(card_visibility,"True") #alphanum{source="MOT",seqid=0,nbdocs=41,groupid=2,k=2}(card_visibility,"partnerportal") #alphanum{source="MOT",seqid=0,groupid=3,k=2}(card_visibility,"3dscom_live") ) #not(#alphanum{source="MOT",seqid=0,groupid=4,k=2}(card_content_type,"premiumarticle")) ) ))',
            "executor": None,
            "estimated": False,
            "autocorrected": False,
            "hits": [
                {
                    "did": 117585,
                    "url": "CARD_ID=539007&CONTENT_LANG=fr&",
                    "buildGroup": "bg0",
                    "source": None,
                    "slice": 0,
                    "score": 65064942332,
                    "sort": 0,
                    "groups": [
                        {
                            "id": "card_content_categories_facet",
                            "root": "Top/classproperties/card/content_categories_facet",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "cards language",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards language",
                                    "id": "Top/classproperties/card/content_categories_facet/cards language",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards language",
                                    "title": "Cards Language",
                                    "categories": [
                                        {
                                            "path": "fr",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "id": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "title": "fr",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "cards type",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards type",
                                    "id": "Top/classproperties/card/content_categories_facet/cards type",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards type",
                                    "title": "Cards type",
                                    "categories": [
                                        {
                                            "path": "career",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "id": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "title": "career",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                        {
                            "id": "card_content_type",
                            "root": "Top/classproperties/card/content_type",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "career",
                                    "fullPath": "Top/classproperties/card/content_type/career",
                                    "id": "Top/classproperties/card/content_type/career",
                                    "zapId": "Top/classproperties/card/content_type/career",
                                    "title": "career",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "dataModelClass",
                            "root": "Top/datamodelclass",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "card",
                                    "fullPath": "Top/datamodelclass/card",
                                    "id": "Top/datamodelclass/card",
                                    "zapId": "Top/datamodelclass/card",
                                    "title": "card",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "card_content_categories",
                            "root": "Top/classproperties/card/content_categories",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "type de contrat",
                                    "fullPath": "Top/classproperties/card/content_categories/type de contrat",
                                    "id": "Top/classproperties/card/content_categories/type de contrat",
                                    "zapId": "Top/classproperties/card/content_categories/type de contrat",
                                    "title": "Type de contrat",
                                    "categories": [
                                        {
                                            "path": "cdi",
                                            "fullPath": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "id": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "zapId": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "title": "CDI",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "produits",
                                    "fullPath": "Top/classproperties/card/content_categories/produits",
                                    "id": "Top/classproperties/card/content_categories/produits",
                                    "zapId": "Top/classproperties/card/content_categories/produits",
                                    "title": "Produits",
                                    "categories": [
                                        {
                                            "path": "dassault systemes",
                                            "fullPath": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "id": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "zapId": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "title": "Dassault Systèmes",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "year",
                                    "fullPath": "Top/classproperties/card/content_categories/year",
                                    "id": "Top/classproperties/card/content_categories/year",
                                    "zapId": "Top/classproperties/card/content_categories/year",
                                    "title": "Year",
                                    "categories": [
                                        {
                                            "path": "0 to 3 years",
                                            "fullPath": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "id": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "zapId": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "title": "0 to 3 years",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "pays",
                                    "fullPath": "Top/classproperties/card/content_categories/pays",
                                    "id": "Top/classproperties/card/content_categories/pays",
                                    "zapId": "Top/classproperties/card/content_categories/pays",
                                    "title": "Pays",
                                    "categories": [
                                        {
                                            "path": "france",
                                            "fullPath": "Top/classproperties/card/content_categories/pays/france",
                                            "id": "Top/classproperties/card/content_categories/pays/france",
                                            "zapId": "Top/classproperties/card/content_categories/pays/france",
                                            "title": "France",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "ville",
                                    "fullPath": "Top/classproperties/card/content_categories/ville",
                                    "id": "Top/classproperties/card/content_categories/ville",
                                    "zapId": "Top/classproperties/card/content_categories/ville",
                                    "title": "Ville",
                                    "categories": [
                                        {
                                            "path": "france, 78, velizy-villacoublay",
                                            "fullPath": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "id": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "zapId": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "title": "France, 78, Vélizy-Villacoublay",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "metier",
                                    "fullPath": "Top/classproperties/card/content_categories/metier",
                                    "id": "Top/classproperties/card/content_categories/metier",
                                    "zapId": "Top/classproperties/card/content_categories/metier",
                                    "title": "Métier",
                                    "categories": [
                                        {
                                            "path": "r&d",
                                            "fullPath": "Top/classproperties/card/content_categories/metier/r&d",
                                            "id": "Top/classproperties/card/content_categories/metier/r&d",
                                            "zapId": "Top/classproperties/card/content_categories/metier/r&d",
                                            "title": "R&D",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                    ],
                    "metas": [
                        {
                            "name": "url",
                            "type": 2,
                            "value": "CARD_ID=539007&CONTENT_LANG=fr&",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards Language/fr",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards type/career",
                        },
                        {"name": "card_id", "type": 2, "value": "539007"},
                        {"name": "card_score", "type": 2, "value": "0"},
                        {
                            "name": "card_update_timestamp",
                            "type": 2,
                            "value": "2024/05/15 18:23:53",
                        },
                        {
                            "name": "content_categories",
                            "type": 2,
                            "value": "Métier/R&D Type de contrat/CDI Pays/France Ville/France, 78, Vélizy-Villacoublay Produits/Dassault Systèmes Year/0 to 3 years",
                        },
                        {
                            "name": "content_cta_1_label",
                            "type": 2,
                            "value": "Découvrir",
                        },
                        {
                            "name": "content_cta_1_url",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/ingenieur-de-recherche-en-calibration-de-simulations-anatomiques-f-h-539007",
                        },
                        {"name": "content_cta_2_label", "type": 2, "value": "Postulez"},
                        {
                            "name": "content_cta_2_url",
                            "type": 2,
                            "value": "https://talentacquisition.3ds.com/careersection/qa/jobapply.ftl?job=539007&lang=fr-FR",
                        },
                        {"name": "content_funnel", "type": 2, "value": "539007"},
                        {
                            "name": "content_img_big_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_img_medium_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_img_small_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_info_1_label",
                            "type": 2,
                            "value": "||ds-ico-suitcase-mini",
                        },
                        {"name": "content_info_1_type", "type": 2, "value": "text"},
                        {"name": "content_info_1_value", "type": 2, "value": "CDI"},
                        {
                            "name": "content_info_2_label",
                            "type": 2,
                            "value": "||ds-ico-location-mini",
                        },
                        {"name": "content_info_2_type", "type": 2, "value": "text"},
                        {
                            "name": "content_info_2_value",
                            "type": 2,
                            "value": "France, 78, Vélizy-Villacoublay",
                        },
                        {"name": "content_lang", "type": 2, "value": "fr"},
                        {
                            "name": "content_start_datetime",
                            "type": 2,
                            "value": "2024/05/15 11:05:32",
                        },
                        {
                            "name": "content_summary",
                            "type": 2,
                            "value": "<p>Au c&oelig;ur de l'innovation &agrave; Dassault Syst&egrave;mes, vous int&eacute;grerez une &eacute;quipe sous la direction de la Recherche, d&eacute;di&eacute;e aux nouvelles approches de mod&eacute;lisation 3D et simulation anatomique.</p>\n<p>Afin de renforcer la strat&eacute;gie de Dassault Syst&egrave;mes en tant qu'acteur de la sant&eacute; num&eacute;rique, nous nous int&eacute;ressons notamment aux challenges de la mod&eacute;lisation du vivant, afin d'&ecirc;tre en mesure de fournir des solutions &agrave; m&ecirc;me de concevoir le jumeau num&eacute;rique 3D de n'importe quel patient. Un tel jumeau num&eacute;rique peut s'av&eacute;rer crucial, autant pour la compr&eacute;hension des pathologies (m&eacute;decine descriptive), que pour l'&eacute;laboration de traitements plus s&ucirc;rs et personnalis&eacute;s (m&eacute;decine pr&eacute;dictive), afin de pr&eacute;dire l'&eacute;volution d'une maladie ou la r&eacute;ponse d'un organe &agrave; une chirurgie.</p>\n<p style=\"font-family: Arial;\">Pour en savoir davantage : https://www.3ds.com/fr/newsroom/press-releases/meditwin-launch</p>\n<p>La mod&eacute;lisation automatis&eacute;e d'un jumeau num&eacute;rique de l'&ecirc;tre humain n&eacute;cessite ainsi plusieurs axes de d&eacute;veloppement, de la reconstruction 3D d'organes &agrave; partir d'images m&eacute;dicales bruit&eacute;es, &agrave; la simulation num&eacute;rique du jumeau sous divers contraintes. Cette derni&egrave;re &eacute;tape est essentielle afin que le jumeau num&eacute;rique ne soit pas utilis&eacute; &agrave; des fins de visualisation uniquement, mais puisse &ecirc;tre analys&eacute; dans le contexte d&rsquo;une pathologie et d&rsquo;un traitement, en testant diff&eacute;rentes hypoth&egrave;ses et en explorant dynamiquement son comportement selon les sc&eacute;narios &eacute;valu&eacute;s.</p>\n<p>Pour r&eacute;pondre &agrave; la probl&eacute;matique d'obtenir un mod&egrave;le d'organe simulable, il est essentiel de pouvoir calibrer les simulations employ&eacute;es. Plusieurs challenges se posent alors, les lois anatomiques ne sont pas toujours bien connues, les propri&eacute;t&eacute;s des tissus sont propres &agrave; chaque patient, les donn&eacute;es d'observation (imagerie m&eacute;dicale, signaux temporels, etc.) sont bruit&eacute;s ; mais il est primordial, pour que le m&eacute;decin puisse fonder une d&eacute;cision m&eacute;dicale &agrave; l'aide des simulations produites, de pouvoir calibrer les simulations sur chaque patient et quantifier l'incertitude li&eacute;e &agrave; ces simulations.</p>\n<p>&nbsp;</p>\n<p style=\"font-family: Arial;\"></p>\n<p>Votre r&ocirc;le consistera &agrave; concevoir et impl&eacute;menter, en C++ et possiblement en Python, des algorithmes de calibration pour nos simulations anatomiques qui peuvent &ecirc;tre aussi bien bas&eacute;es sur des solveurs haute fid&eacute;lit&eacute; que sur des mod&egrave;les surrogate ou d'IA. L'objectif est de fournir une librairie de calibration int&eacute;gr&eacute;e dans notre infrastructure de simulation anatomique.</p>\n<p>La calibration peut n&eacute;cessiter le d&eacute;veloppement de m&eacute;thodes tr&egrave;s diverses et innovantes, touchant &agrave; un large spectre de math&eacute;matiques selon les situations : probl&egrave;me inverse, optimisation non diff&eacute;rentiable, contr&ocirc;le optimal, filtrage de Kalman, estimation Monte-Carlo, pr&eacute;diction par r&eacute;seaux de neurones, etc.</p>\n<p>Vous aurez l'opportunit&eacute; de mettre en &oelig;uvre ces diverses m&eacute;thodes en priorit&eacute; dans le cadre de la calibration de jumeaux num&eacute;riques cardiovasculaires, pouvant coupler de la simulation &eacute;lectrophysiologique, &eacute;lectrochimique, fluide, ou encore m&eacute;canique, dans le cadre de diff&eacute;rents sc&eacute;narios m&eacute;dicaux, o&ugrave; l'on chercherait par exemple &agrave; calibrer sur des &eacute;l&eacute;ctrocardiogrammes, des &eacute;chographies, des mesures de fluide, etc.</p>\n<p style=\"font-family: Arial;\"></p>\n<p style=\"font-family: Arial;\"></p>\n<p><strong>Vos missions:</strong></p>\n<ul>\n<li>&Eacute;tat de l'art de la simulation anatomique et des mod&egrave;les de simulation cardiovasculaire (simulation &eacute;l&eacute;ctrophysiologique, &eacute;l&eacute;ctrom&eacute;canique, fluide-structure, etc.).</li>\n<li>&Eacute;tat de l'art des m&eacute;thodes de calibration au sens large.</li>\n<li>Conception et impl&eacute;mentation&nbsp;de composants algorithmiques de calibration des mod&egrave;les de simulation d&eacute;velopp&eacute;s au sein de l'&eacute;quipe.</li>\n<li>Int&eacute;gration continue dans l'architecture logicielle de l'&eacute;quipe, mise en place de tests unitaires.</li>\n<li>&Eacute;valuation des r&eacute;sultats de calibration et illustration de la cha&icirc;ne de simulation sur sc&eacute;narios m&eacute;dicaux.</li>\n</ul><p style=\"font-family: Arial;\"></p>\n<p style=\"font-family: Arial;\"></p>\n<p style=\"font-family: Arial;\"><strong>Vos qualifications:</strong></p>\n<ul>\n<li>Master, dipl&ocirc;me d'ing&eacute;nieur, ou th&egrave;se de doctorat en math&eacute;matiques appliqu&eacute;es.</li>\n<li>Comp&eacute;tences avanc&eacute;es en math&eacute;matiques appliqu&eacute;es &agrave; la calibration de mod&egrave;les (optimisation num&eacute;rique, simulation num&eacute;rique, probabilit&eacute;s, th&eacute;orie du controle, etc.).</li>\n<li>Pratique significative du d&eacute;veloppement logiciel associ&eacute;e &agrave; une culture de l'informatique et de l'algorithmique.</li>\n<li>Ma&icirc;trise du C++ moderne et de la programmation orient&eacute;e objet. Des connaissances en Python seront &eacute;galement valoris&eacute;es.</li>\n<li>Une exp&eacute;rience de l'utilisation de diverses librairies de simulations num&eacute;riques sera particuli&egrave;rement appr&eacute;ci&eacute;e.</li>\n<li>Ma&icirc;trise de l'anglais &agrave; l'&eacute;crit comme &agrave; l'oral</li>\n</ul>\n<p style=\"font-family: Arial;\"></p>\n<p style=\"font-family: Arial;\"></p>\n<p style=\"font-family: Arial;\"></p>\n<p style=\"margin: 0px 0px 12px; color: rgb(0, 0, 0); font-size: 13.02px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial;\"><strong style=\"font-weight: bold;\">Nous rejoindre c'est aussi:</strong>&nbsp;<br>Int&eacute;grer une entreprise scientifique au c&oelig;ur de l&rsquo;innovation technologique, port&eacute;e par une forte croissance depuis plus de 40 ans.<span style=\"text-decoration: underline;\"></span></p>\n<p style=\"margin: 0px 0px 12px; color: rgb(0, 0, 0); font-size: 13.02px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial;\"><span style=\"text-decoration: underline;\">Principaux avantages et b&eacute;n&eacute;fices:</span></p>\n<ul style=\"margin: 12px 0px; padding: 0px 0px 0px 20px; color: rgb(0, 0, 0); font-family: 'Open Sans', 'Segoe UI', Frutiger, 'Frutiger Linotype', 'Dejavu Sans', 'Helvetica Neue', Arial, sans-serif; font-size: 13.02px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;\">\n<li style=\"line-height: 1.25; font-family: Arial;\">Environnement multiculturel</li>\n<li style=\"line-height: 1.25; font-family: Arial;\">Cadre de travail convivial ax&eacute; sur le bien-&ecirc;tre et la sant&eacute; (salles de sport &amp; de musique, conciergerie&hellip;)</li>\n<li style=\"line-height: 1.25; font-family: Arial;\">Engagement en faveur de la diversit&eacute; et de l&rsquo;inclusion</li>\n<li style=\"line-height: 1.25; font-family: Arial;\">Politique dynamique de d&eacute;veloppement de carri&egrave;re : plan de formation, mobilit&eacute;s internes, etc&nbsp;</li>\n</ul>",
                        },
                        {
                            "name": "content_title",
                            "type": 2,
                            "value": "Ingénieur de recherche en calibration de simulations anatomiques - F/H",
                        },
                        {"name": "content_type", "type": 2, "value": "career"},
                        {
                            "name": "content_type_display_text",
                            "type": 2,
                            "value": "CAREERS - R&D",
                        },
                        {"name": "content_cta_1_linker", "type": 2, "value": "3dscom"},
                        {"name": "visibility", "type": 2, "value": "True"},
                        {"name": "content_full_text", "type": 2, "value": "None"},
                        {"name": "code_lang", "type": 2, "value": "fr"},
                        {"name": "meta_cat", "type": 2, "value": "Métier/R&D"},
                        {"name": "meta_cat", "type": 2, "value": "Type de contrat/CDI"},
                        {"name": "meta_cat", "type": 2, "value": "Pays/France"},
                        {
                            "name": "meta_cat",
                            "type": 2,
                            "value": "Ville/France, 78, Vélizy-Villacoublay",
                        },
                        {
                            "name": "meta_cat",
                            "type": 2,
                            "value": "Produits/Dassault Systèmes",
                        },
                        {"name": "meta_cat", "type": 2, "value": "Year/0 to 3 years"},
                        {
                            "name": "content_cta_1_url_id",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/ingenieur-de-recherche-en-calibration-de-simulations-anatomiques-f-h-539007",
                        },
                        {"name": "content_keywords", "type": 2, "value": "FRA016"},
                    ],
                },
                {
                    "did": 8323,
                    "url": "CARD_ID=531525&CONTENT_LANG=fr&",
                    "buildGroup": "bg0",
                    "source": None,
                    "slice": 0,
                    "score": 65062321442,
                    "sort": 0,
                    "groups": [
                        {
                            "id": "card_content_categories_facet",
                            "root": "Top/classproperties/card/content_categories_facet",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "cards language",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards language",
                                    "id": "Top/classproperties/card/content_categories_facet/cards language",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards language",
                                    "title": "Cards Language",
                                    "categories": [
                                        {
                                            "path": "fr",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "id": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "title": "fr",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "cards type",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards type",
                                    "id": "Top/classproperties/card/content_categories_facet/cards type",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards type",
                                    "title": "Cards type",
                                    "categories": [
                                        {
                                            "path": "career",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "id": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "title": "career",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                        {
                            "id": "card_content_type",
                            "root": "Top/classproperties/card/content_type",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "career",
                                    "fullPath": "Top/classproperties/card/content_type/career",
                                    "id": "Top/classproperties/card/content_type/career",
                                    "zapId": "Top/classproperties/card/content_type/career",
                                    "title": "career",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "dataModelClass",
                            "root": "Top/datamodelclass",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "card",
                                    "fullPath": "Top/datamodelclass/card",
                                    "id": "Top/datamodelclass/card",
                                    "zapId": "Top/datamodelclass/card",
                                    "title": "card",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "card_content_categories",
                            "root": "Top/classproperties/card/content_categories",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "type de contrat",
                                    "fullPath": "Top/classproperties/card/content_categories/type de contrat",
                                    "id": "Top/classproperties/card/content_categories/type de contrat",
                                    "zapId": "Top/classproperties/card/content_categories/type de contrat",
                                    "title": "Type de contrat",
                                    "categories": [
                                        {
                                            "path": "cdi",
                                            "fullPath": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "id": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "zapId": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "title": "CDI",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "produits",
                                    "fullPath": "Top/classproperties/card/content_categories/produits",
                                    "id": "Top/classproperties/card/content_categories/produits",
                                    "zapId": "Top/classproperties/card/content_categories/produits",
                                    "title": "Produits",
                                    "categories": [
                                        {
                                            "path": "dassault systemes",
                                            "fullPath": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "id": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "zapId": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "title": "Dassault Systèmes",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "year",
                                    "fullPath": "Top/classproperties/card/content_categories/year",
                                    "id": "Top/classproperties/card/content_categories/year",
                                    "zapId": "Top/classproperties/card/content_categories/year",
                                    "title": "Year",
                                    "categories": [
                                        {
                                            "path": "0 to 3 years",
                                            "fullPath": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "id": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "zapId": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "title": "0 to 3 years",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "pays",
                                    "fullPath": "Top/classproperties/card/content_categories/pays",
                                    "id": "Top/classproperties/card/content_categories/pays",
                                    "zapId": "Top/classproperties/card/content_categories/pays",
                                    "title": "Pays",
                                    "categories": [
                                        {
                                            "path": "france",
                                            "fullPath": "Top/classproperties/card/content_categories/pays/france",
                                            "id": "Top/classproperties/card/content_categories/pays/france",
                                            "zapId": "Top/classproperties/card/content_categories/pays/france",
                                            "title": "France",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "ville",
                                    "fullPath": "Top/classproperties/card/content_categories/ville",
                                    "id": "Top/classproperties/card/content_categories/ville",
                                    "zapId": "Top/classproperties/card/content_categories/ville",
                                    "title": "Ville",
                                    "categories": [
                                        {
                                            "path": "france, 78, velizy-villacoublay",
                                            "fullPath": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "id": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "zapId": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "title": "France, 78, Vélizy-Villacoublay",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "metier",
                                    "fullPath": "Top/classproperties/card/content_categories/metier",
                                    "id": "Top/classproperties/card/content_categories/metier",
                                    "zapId": "Top/classproperties/card/content_categories/metier",
                                    "title": "Métier",
                                    "categories": [
                                        {
                                            "path": "r&d",
                                            "fullPath": "Top/classproperties/card/content_categories/metier/r&d",
                                            "id": "Top/classproperties/card/content_categories/metier/r&d",
                                            "zapId": "Top/classproperties/card/content_categories/metier/r&d",
                                            "title": "R&D",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                    ],
                    "metas": [
                        {
                            "name": "url",
                            "type": 2,
                            "value": "CARD_ID=531525&CONTENT_LANG=fr&",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards Language/fr",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards type/career",
                        },
                        {"name": "card_id", "type": 2, "value": "531525"},
                        {"name": "card_score", "type": 2, "value": "0"},
                        {
                            "name": "card_update_timestamp",
                            "type": 2,
                            "value": "2024/04/16 10:31:57",
                        },
                        {
                            "name": "content_categories",
                            "type": 2,
                            "value": "Métier/R&D Type de contrat/CDI Pays/France Ville/France, 78, Vélizy-Villacoublay Produits/Dassault Systèmes Year/0 to 3 years",
                        },
                        {
                            "name": "content_cta_1_label",
                            "type": 2,
                            "value": "Découvrir",
                        },
                        {
                            "name": "content_cta_1_url",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/developpeur-c-h-f-531525",
                        },
                        {"name": "content_cta_2_label", "type": 2, "value": "Postulez"},
                        {
                            "name": "content_cta_2_url",
                            "type": 2,
                            "value": "https://talentacquisition.3ds.com/careersection/qa/jobapply.ftl?job=531525&lang=fr-FR",
                        },
                        {"name": "content_funnel", "type": 2, "value": "531525"},
                        {
                            "name": "content_img_big_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_img_medium_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_img_small_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_info_1_label",
                            "type": 2,
                            "value": "||ds-ico-suitcase-mini",
                        },
                        {"name": "content_info_1_type", "type": 2, "value": "text"},
                        {"name": "content_info_1_value", "type": 2, "value": "CDI"},
                        {
                            "name": "content_info_2_label",
                            "type": 2,
                            "value": "||ds-ico-location-mini",
                        },
                        {"name": "content_info_2_type", "type": 2, "value": "text"},
                        {
                            "name": "content_info_2_value",
                            "type": 2,
                            "value": "France, 78, Vélizy-Villacoublay",
                        },
                        {"name": "content_lang", "type": 2, "value": "fr"},
                        {
                            "name": "content_start_datetime",
                            "type": 2,
                            "value": "2024/04/16 03:04:02",
                        },
                        {
                            "name": "content_summary",
                            "type": 2,
                            "value": '<p style="font-family: Arial;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" frameborder="0" height="315" src="https://www.youtube.com/embed/fSNL-JzrVko" title="YouTube video player" width="560"></iframe></p>\n<p style="font-family: Arial;"></p>\n<p style="font-family: Arial;"><span style="font-family: arial, helvetica, sans-serif;">Pour accompagner sa croissance et celle de ses clients via des univers virtuels, Dassault Syst&egrave;mes, la 3DEXPERIENCE Company, renforce aujourd\'hui ses &eacute;quipes. En tant que concepteur / d&eacute;veloppeur au sein de l\'&eacute;quipe R&amp;D, vous participerez &agrave; l\'ad&eacute;quation de la solution aux besoins m&eacute;tier, de la robustesse et de la pertinence des choix techniques sur toutes les phases des projets : sp&eacute;cifications, d&eacute;veloppement, int&eacute;gration&hellip;&nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">&nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">&nbsp;</span></p>\n<p style="font-family: Arial;"><span style="font-family: arial, helvetica, sans-serif;"><strong>Vos missions</strong></span></p>\n<p style="font-family: Arial;"><br><span style="font-family: arial, helvetica, sans-serif;">Participation au d&eacute;veloppement et &agrave; l\'&eacute;volution des solutions Dassault Syst&egrave;mes&nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">Vous participerez &agrave; des ateliers de cadrage technique pour r&eacute;pondre aux cahier des charges &eacute;tabli (client interne ou externe)&nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">Vous contribuerez &agrave; la r&eacute;daction de la documentation technique des applicatifs d&eacute;velopp&eacute;s. &nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">Vous participerez &agrave; la d&eacute;finition des tests unitaires et d\'int&eacute;gration et de leur mise en &oelig;uvre&nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">Vous serez force de proposition sur de nouvelles solutions techniques trouv&eacute;es lors de votre veille technologique.</span><br>&nbsp;</p><p><span style="font-family: arial, helvetica, sans-serif;"><strong>Vos qualifications</strong></span></p>\n<p><span style="font-family: arial, helvetica, sans-serif;">Issu d\'une formation sup&eacute;rieure de type Ing&eacute;nieur ou Universitaire de niveau Bac +5, vous disposez d\'une premi&egrave;re exp&eacute;rience professionnelle (apprentissage ou stage inclus) en d&eacute;veloppement C++ et Javascript</span><br><span style="font-family: arial, helvetica, sans-serif;">De bonnes connaissances en math&eacute;matiques et algorithmique sont de r&eacute;els avantages. &nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">Vous cherchez constamment &agrave; &eacute;largir votre culture informatique. Des connaissances dans les technologies web (ReactJS&hellip;), langages de scripting (PERL, Python&hellip;) ou un int&eacute;r&ecirc;t pour la d&eacute;marche DevOps sont de r&eacute;els atouts. &nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">La maitrise de l\'anglais (oral et &eacute;crit) est indispensable.</span></p>\n<p style="font-family: Arial;"></p>\n<p style="font-family: Arial;"><span style="font-family: arial, helvetica, sans-serif;"><strong>Nous rejoindre c\'est aussi</strong></span></p>\n<p style="font-family: Arial;"><br><span style="font-family: arial, helvetica, sans-serif;">Int&eacute;grer une entreprise scientifique au c&oelig;ur de l&rsquo;innovation technologique, port&eacute;e par une forte croissance depuis plus de 40 ans</span><br><span style="font-family: arial, helvetica, sans-serif;">Principaux avantages et b&eacute;n&eacute;fices :</span><br><span style="font-family: arial, helvetica, sans-serif;">&nbsp; &nbsp; &middot; Environnement multiculturel</span><br><span style="font-family: arial, helvetica, sans-serif;">&nbsp; &nbsp; &middot; Cadre de travail convivial ax&eacute; sur le bien-&ecirc;tre et la sant&eacute; (salles de sport &amp; de musique, conciergerie&hellip;)&nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">&nbsp; &nbsp; &middot; Engagement en faveur de la diversit&eacute; et de l&rsquo;inclusion&nbsp;</span><br><span style="font-family: arial, helvetica, sans-serif;">&nbsp; &nbsp; &middot; Politique dynamique de d&eacute;veloppement de carri&egrave;re : plan de formation, mobilit&eacute;s internes, etc&nbsp;</span></p>\n<div>\n<div>&nbsp;</div>\n</div>',
                        },
                        {
                            "name": "content_title",
                            "type": 2,
                            "value": "Dévéloppeur C++ H/F",
                        },
                        {"name": "content_type", "type": 2, "value": "career"},
                        {
                            "name": "content_type_display_text",
                            "type": 2,
                            "value": "CAREERS - R&D",
                        },
                        {"name": "content_cta_1_linker", "type": 2, "value": "3dscom"},
                        {"name": "visibility", "type": 2, "value": "True"},
                        {"name": "content_full_text", "type": 2, "value": "None"},
                        {"name": "code_lang", "type": 2, "value": "fr"},
                        {"name": "meta_cat", "type": 2, "value": "Métier/R&D"},
                        {"name": "meta_cat", "type": 2, "value": "Type de contrat/CDI"},
                        {"name": "meta_cat", "type": 2, "value": "Pays/France"},
                        {
                            "name": "meta_cat",
                            "type": 2,
                            "value": "Ville/France, 78, Vélizy-Villacoublay",
                        },
                        {
                            "name": "meta_cat",
                            "type": 2,
                            "value": "Produits/Dassault Systèmes",
                        },
                        {"name": "meta_cat", "type": 2, "value": "Year/0 to 3 years"},
                        {
                            "name": "content_cta_1_url_id",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/developpeur-c-h-f-531525",
                        },
                        {"name": "content_keywords", "type": 2, "value": "FRA016"},
                    ],
                },
                {
                    "did": 10032,
                    "url": "CARD_ID=538586&CONTENT_LANG=fr&",
                    "buildGroup": "bg0",
                    "source": None,
                    "slice": 0,
                    "score": 65061295440,
                    "sort": 0,
                    "groups": [
                        {
                            "id": "card_content_categories_facet",
                            "root": "Top/classproperties/card/content_categories_facet",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "cards language",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards language",
                                    "id": "Top/classproperties/card/content_categories_facet/cards language",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards language",
                                    "title": "Cards Language",
                                    "categories": [
                                        {
                                            "path": "fr",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "id": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "title": "fr",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "cards type",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards type",
                                    "id": "Top/classproperties/card/content_categories_facet/cards type",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards type",
                                    "title": "Cards type",
                                    "categories": [
                                        {
                                            "path": "career",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "id": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "title": "career",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                        {
                            "id": "card_content_type",
                            "root": "Top/classproperties/card/content_type",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "career",
                                    "fullPath": "Top/classproperties/card/content_type/career",
                                    "id": "Top/classproperties/card/content_type/career",
                                    "zapId": "Top/classproperties/card/content_type/career",
                                    "title": "career",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "dataModelClass",
                            "root": "Top/datamodelclass",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "card",
                                    "fullPath": "Top/datamodelclass/card",
                                    "id": "Top/datamodelclass/card",
                                    "zapId": "Top/datamodelclass/card",
                                    "title": "card",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "card_content_categories",
                            "root": "Top/classproperties/card/content_categories",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "type de contrat",
                                    "fullPath": "Top/classproperties/card/content_categories/type de contrat",
                                    "id": "Top/classproperties/card/content_categories/type de contrat",
                                    "zapId": "Top/classproperties/card/content_categories/type de contrat",
                                    "title": "Type de contrat",
                                    "categories": [
                                        {
                                            "path": "cdi",
                                            "fullPath": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "id": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "zapId": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "title": "CDI",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "produits",
                                    "fullPath": "Top/classproperties/card/content_categories/produits",
                                    "id": "Top/classproperties/card/content_categories/produits",
                                    "zapId": "Top/classproperties/card/content_categories/produits",
                                    "title": "Produits",
                                    "categories": [
                                        {
                                            "path": "dassault systemes",
                                            "fullPath": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "id": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "zapId": "Top/classproperties/card/content_categories/produits/dassault systemes",
                                            "title": "Dassault Systèmes",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "year",
                                    "fullPath": "Top/classproperties/card/content_categories/year",
                                    "id": "Top/classproperties/card/content_categories/year",
                                    "zapId": "Top/classproperties/card/content_categories/year",
                                    "title": "Year",
                                    "categories": [
                                        {
                                            "path": "0 to 3 years",
                                            "fullPath": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "id": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "zapId": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "title": "0 to 3 years",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "pays",
                                    "fullPath": "Top/classproperties/card/content_categories/pays",
                                    "id": "Top/classproperties/card/content_categories/pays",
                                    "zapId": "Top/classproperties/card/content_categories/pays",
                                    "title": "Pays",
                                    "categories": [
                                        {
                                            "path": "france",
                                            "fullPath": "Top/classproperties/card/content_categories/pays/france",
                                            "id": "Top/classproperties/card/content_categories/pays/france",
                                            "zapId": "Top/classproperties/card/content_categories/pays/france",
                                            "title": "France",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "ville",
                                    "fullPath": "Top/classproperties/card/content_categories/ville",
                                    "id": "Top/classproperties/card/content_categories/ville",
                                    "zapId": "Top/classproperties/card/content_categories/ville",
                                    "title": "Ville",
                                    "categories": [
                                        {
                                            "path": "france, 78, velizy-villacoublay",
                                            "fullPath": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "id": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "zapId": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "title": "France, 78, Vélizy-Villacoublay",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "metier",
                                    "fullPath": "Top/classproperties/card/content_categories/metier",
                                    "id": "Top/classproperties/card/content_categories/metier",
                                    "zapId": "Top/classproperties/card/content_categories/metier",
                                    "title": "Métier",
                                    "categories": [
                                        {
                                            "path": "r&d",
                                            "fullPath": "Top/classproperties/card/content_categories/metier/r&d",
                                            "id": "Top/classproperties/card/content_categories/metier/r&d",
                                            "zapId": "Top/classproperties/card/content_categories/metier/r&d",
                                            "title": "R&D",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                    ],
                    "metas": [
                        {
                            "name": "url",
                            "type": 2,
                            "value": "CARD_ID=538586&CONTENT_LANG=fr&",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards Language/fr",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards type/career",
                        },
                        {"name": "card_id", "type": 2, "value": "538586"},
                        {"name": "card_score", "type": 2, "value": "0"},
                        {
                            "name": "card_update_timestamp",
                            "type": 2,
                            "value": "2024/04/05 00:27:37",
                        },
                        {
                            "name": "content_categories",
                            "type": 2,
                            "value": "Métier/R&D Type de contrat/CDI Pays/France Ville/France, 78, Vélizy-Villacoublay Produits/Dassault Systèmes Year/0 to 3 years",
                        },
                        {
                            "name": "content_cta_1_label",
                            "type": 2,
                            "value": "Découvrir",
                        },
                        {
                            "name": "content_cta_1_url",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/developpeur-web-h-f-538586",
                        },
                        {"name": "content_cta_2_label", "type": 2, "value": "Postulez"},
                        {
                            "name": "content_cta_2_url",
                            "type": 2,
                            "value": "https://talentacquisition.3ds.com/careersection/qa/jobapply.ftl?job=538586&lang=fr-FR",
                        },
                        {"name": "content_funnel", "type": 2, "value": "538586"},
                        {
                            "name": "content_img_big_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_img_medium_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_img_small_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/corporate.png",
                        },
                        {
                            "name": "content_info_1_label",
                            "type": 2,
                            "value": "||ds-ico-suitcase-mini",
                        },
                        {"name": "content_info_1_type", "type": 2, "value": "text"},
                        {"name": "content_info_1_value", "type": 2, "value": "CDI"},
                        {
                            "name": "content_info_2_label",
                            "type": 2,
                            "value": "||ds-ico-location-mini",
                        },
                        {"name": "content_info_2_type", "type": 2, "value": "text"},
                        {
                            "name": "content_info_2_value",
                            "type": 2,
                            "value": "France, 78, Vélizy-Villacoublay",
                        },
                        {"name": "content_lang", "type": 2, "value": "fr"},
                        {
                            "name": "content_start_datetime",
                            "type": 2,
                            "value": "2024/04/04 06:04:00",
                        },
                        {
                            "name": "content_summary",
                            "type": 2,
                            "value": '<p style="font-family: Arial;">Vous int&eacute;grerez l&rsquo;&eacute;quipe "Process &amp; Operations Transformation" de l\'organisation "R&amp;D Customer Experience Success".<br>L&rsquo;organisation R&amp;D Customer Experience Success est en charge d&rsquo;accompagner le d&eacute;ploiement des clients strat&eacute;gique de Dassault Syst&egrave;mes en menant la d&eacute;finition de nos solutions en &eacute;troite collaboration avec ces derniers.<br>L&rsquo;organisation Process &amp; Operations Transformation est en charge de sp&eacute;cifier et d&eacute;ployer les outils n&eacute;cessaires &agrave; l&rsquo;organisation R&amp;D Customer Experience Success permettant le suivi et le reporting de son activit&eacute;, la gestion des plans du portfolio et du Strategic Define.</p>\n<p style="font-family: Arial;"><strong>Vos missions :</strong></p>\n<p style="font-family: Arial;">Vous serez en charge de sp&eacute;cifier et d&eacute;velopper les outils de dashboarding n&eacute;cessaires au suivi quotidien de l\'activit&eacute; de l\'organisation.<br>La sp&eacute;cification se fera en collaboration avec les diff&eacute;rents publics utilisateurs de chaque dashboard sur un axe fonctionnel.<br>Une analyse technique permettra ensuite d\'identifier les composants standards r&eacute;utilisables ou adaptables &agrave; int&eacute;grer et les composants &agrave; d&eacute;velopper.<br>Un suivi du d&eacute;ploiement de ces dashboards et plusieurs it&eacute;rations permettront de s\'assurer de la pertinence des &eacute;l&eacute;ments d&eacute;livr&eacute;s et de l\'adoption de ces dashboards.<br>Une partie de la mission comprendra l\'utilisation de ces dashboards ainsi que des roles Data Science Experiences dans le cadre du suivi des clients g&eacute;r&eacute;s par l\'organisation.<br>Cette mission vous permettra d\'&eacute;voluer dans un contexte international, en d&eacute;couvrant et en apprenant les enjeux des diff&eacute;rentes Industries au sein de Dassault Syst&egrave;mes, les diverses activit&eacute;s associ&eacute;es et aussi de r&eacute;aliser des t&acirc;ches en utilisant les diff&eacute;rents processus, outils et m&eacute;thodes mis en place au sein de l\'organisation en g&eacute;n&eacute;ral et de l\'&eacute;quipe en particulier.<br>Vous travaillerez avec l&rsquo;&eacute;quipe Operations Excellence R&amp;D Customer Strategic Partnerships, les R&amp;D Industry leaders, les &eacute;quipes Outils R&amp;D et IT.</p><p style="font-family: Arial;"><strong>Vos qualifications:</strong></p>\n<p style="font-family: Arial;">Diplom&eacute; d&rsquo;un Bac+5 d&rsquo;&eacute;cole d&rsquo;ing&eacute;nieur ou d&rsquo;universit&eacute;<br>Vous avez de bonnes connaissances :</p>\n<ul>\n<li style="font-family: Arial;">en d&eacute;veloppement FrontEnd: HTML / CSS / JavaScript (ReactJS serait un plus)</li>\n<li style="font-family: Arial;">en d&eacute;veloppement BackEnd : Docker / Python / nodeJS</li>\n</ul>\n<p style="font-family: Arial;">Vous avez un int&eacute;r&ecirc;t pour la data science : Traitement, qualit&eacute; de donn&eacute;es et consolidation (NETVIBES Data Perspectives serait un plus)<br>Vous connaissez l&rsquo;automatisation des t&acirc;ches, les aspects DevOps : GitLab<br>Vous savez faire preuve de capacit&eacute; r&eacute;dactionnelle<br>Vous maitrisez le fran&ccedil;ais et l\'anglais, &agrave; l\'&eacute;crit comme &agrave; l\'oral</p>\n<p style="font-family: Arial;"><strong>Nous rejoindre c\'est aussi</strong><br>Int&eacute;grer une entreprise scientifique au c&oelig;ur de l&rsquo;innovation technologique, port&eacute;e par une forte croissance depuis plus de 40 ans<br>&nbsp;<br>Principaux avantages et b&eacute;n&eacute;fices :<br>&bull; &nbsp; &nbsp;Environnement multiculturel<br>&bull; &nbsp; &nbsp;Cadre de travail convivial ax&eacute; sur le bien-&ecirc;tre et la sant&eacute; (salles de sport &amp; de musique, conciergerie&hellip;)<br>&bull; &nbsp; &nbsp;Engagement en faveur de la diversit&eacute; et de l&rsquo;inclusion&nbsp;<br>&bull; &nbsp; &nbsp;Politique dynamique de d&eacute;veloppement de carri&egrave;re : plan de formation, mobilit&eacute;s internes, etc</p>',
                        },
                        {
                            "name": "content_title",
                            "type": 2,
                            "value": "Développeur web (H/F)",
                        },
                        {"name": "content_type", "type": 2, "value": "career"},
                        {
                            "name": "content_type_display_text",
                            "type": 2,
                            "value": "CAREERS - R&D",
                        },
                        {"name": "content_cta_1_linker", "type": 2, "value": "3dscom"},
                        {"name": "visibility", "type": 2, "value": "True"},
                        {"name": "content_full_text", "type": 2, "value": "None"},
                        {"name": "code_lang", "type": 2, "value": "fr"},
                        {"name": "meta_cat", "type": 2, "value": "Métier/R&D"},
                        {"name": "meta_cat", "type": 2, "value": "Type de contrat/CDI"},
                        {"name": "meta_cat", "type": 2, "value": "Pays/France"},
                        {
                            "name": "meta_cat",
                            "type": 2,
                            "value": "Ville/France, 78, Vélizy-Villacoublay",
                        },
                        {
                            "name": "meta_cat",
                            "type": 2,
                            "value": "Produits/Dassault Systèmes",
                        },
                        {"name": "meta_cat", "type": 2, "value": "Year/0 to 3 years"},
                        {
                            "name": "content_cta_1_url_id",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/developpeur-web-h-f-538586",
                        },
                        {"name": "content_keywords", "type": 2, "value": "FRA016"},
                    ],
                },
                {
                    "did": 125173,
                    "url": "CARD_ID=538383&CONTENT_LANG=fr&",
                    "buildGroup": "bg0",
                    "source": None,
                    "slice": 0,
                    "score": 65060521380,
                    "sort": 0,
                    "groups": [
                        {
                            "id": "card_content_categories_facet",
                            "root": "Top/classproperties/card/content_categories_facet",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "cards language",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards language",
                                    "id": "Top/classproperties/card/content_categories_facet/cards language",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards language",
                                    "title": "Cards Language",
                                    "categories": [
                                        {
                                            "path": "fr",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "id": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards language/fr",
                                            "title": "fr",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "cards type",
                                    "fullPath": "Top/classproperties/card/content_categories_facet/cards type",
                                    "id": "Top/classproperties/card/content_categories_facet/cards type",
                                    "zapId": "Top/classproperties/card/content_categories_facet/cards type",
                                    "title": "Cards type",
                                    "categories": [
                                        {
                                            "path": "career",
                                            "fullPath": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "id": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "zapId": "Top/classproperties/card/content_categories_facet/cards type/career",
                                            "title": "career",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                        {
                            "id": "card_content_type",
                            "root": "Top/classproperties/card/content_type",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "career",
                                    "fullPath": "Top/classproperties/card/content_type/career",
                                    "id": "Top/classproperties/card/content_type/career",
                                    "zapId": "Top/classproperties/card/content_type/career",
                                    "title": "career",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "dataModelClass",
                            "root": "Top/datamodelclass",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "card",
                                    "fullPath": "Top/datamodelclass/card",
                                    "id": "Top/datamodelclass/card",
                                    "zapId": "Top/datamodelclass/card",
                                    "title": "card",
                                    "categories": [],
                                }
                            ],
                        },
                        {
                            "id": "card_content_categories",
                            "root": "Top/classproperties/card/content_categories",
                            "refinable": True,
                            "categories": [
                                {
                                    "path": "type de contrat",
                                    "fullPath": "Top/classproperties/card/content_categories/type de contrat",
                                    "id": "Top/classproperties/card/content_categories/type de contrat",
                                    "zapId": "Top/classproperties/card/content_categories/type de contrat",
                                    "title": "Type de contrat",
                                    "categories": [
                                        {
                                            "path": "cdi",
                                            "fullPath": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "id": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "zapId": "Top/classproperties/card/content_categories/type de contrat/cdi",
                                            "title": "CDI",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "year",
                                    "fullPath": "Top/classproperties/card/content_categories/year",
                                    "id": "Top/classproperties/card/content_categories/year",
                                    "zapId": "Top/classproperties/card/content_categories/year",
                                    "title": "Year",
                                    "categories": [
                                        {
                                            "path": "0 to 3 years",
                                            "fullPath": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "id": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "zapId": "Top/classproperties/card/content_categories/year/0 to 3 years",
                                            "title": "0 to 3 years",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "pays",
                                    "fullPath": "Top/classproperties/card/content_categories/pays",
                                    "id": "Top/classproperties/card/content_categories/pays",
                                    "zapId": "Top/classproperties/card/content_categories/pays",
                                    "title": "Pays",
                                    "categories": [
                                        {
                                            "path": "france",
                                            "fullPath": "Top/classproperties/card/content_categories/pays/france",
                                            "id": "Top/classproperties/card/content_categories/pays/france",
                                            "zapId": "Top/classproperties/card/content_categories/pays/france",
                                            "title": "France",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "ville",
                                    "fullPath": "Top/classproperties/card/content_categories/ville",
                                    "id": "Top/classproperties/card/content_categories/ville",
                                    "zapId": "Top/classproperties/card/content_categories/ville",
                                    "title": "Ville",
                                    "categories": [
                                        {
                                            "path": "france, 78, velizy-villacoublay",
                                            "fullPath": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "id": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "zapId": "Top/classproperties/card/content_categories/ville/france, 78, velizy-villacoublay",
                                            "title": "France, 78, Vélizy-Villacoublay",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "metier",
                                    "fullPath": "Top/classproperties/card/content_categories/metier",
                                    "id": "Top/classproperties/card/content_categories/metier",
                                    "zapId": "Top/classproperties/card/content_categories/metier",
                                    "title": "Métier",
                                    "categories": [
                                        {
                                            "path": "r&d",
                                            "fullPath": "Top/classproperties/card/content_categories/metier/r&d",
                                            "id": "Top/classproperties/card/content_categories/metier/r&d",
                                            "zapId": "Top/classproperties/card/content_categories/metier/r&d",
                                            "title": "R&D",
                                            "categories": [],
                                        }
                                    ],
                                },
                                {
                                    "path": "produits",
                                    "fullPath": "Top/classproperties/card/content_categories/produits",
                                    "id": "Top/classproperties/card/content_categories/produits",
                                    "zapId": "Top/classproperties/card/content_categories/produits",
                                    "title": "Produits",
                                    "categories": [
                                        {
                                            "path": "netvibes",
                                            "fullPath": "Top/classproperties/card/content_categories/produits/netvibes",
                                            "id": "Top/classproperties/card/content_categories/produits/netvibes",
                                            "zapId": "Top/classproperties/card/content_categories/produits/netvibes",
                                            "title": "NETVIBES",
                                            "categories": [],
                                        }
                                    ],
                                },
                            ],
                        },
                    ],
                    "metas": [
                        {
                            "name": "url",
                            "type": 2,
                            "value": "CARD_ID=538383&CONTENT_LANG=fr&",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards Language/fr",
                        },
                        {
                            "name": "content_categories_facet",
                            "type": 2,
                            "value": "Cards type/career",
                        },
                        {"name": "card_id", "type": 2, "value": "538383"},
                        {"name": "card_score", "type": 2, "value": "0"},
                        {
                            "name": "card_update_timestamp",
                            "type": 2,
                            "value": "2024/04/16 18:32:04",
                        },
                        {
                            "name": "content_categories",
                            "type": 2,
                            "value": "Métier/R&D Type de contrat/CDI Pays/France Ville/France, 78, Vélizy-Villacoublay Produits/NETVIBES Year/0 to 3 years",
                        },
                        {
                            "name": "content_cta_1_label",
                            "type": 2,
                            "value": "Découvrir",
                        },
                        {
                            "name": "content_cta_1_url",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/ingenieur-e-machine-learning-f-h-538383",
                        },
                        {"name": "content_cta_2_label", "type": 2, "value": "Postulez"},
                        {
                            "name": "content_cta_2_url",
                            "type": 2,
                            "value": "https://talentacquisition.3ds.com/careersection/qa/jobapply.ftl?job=538383&lang=fr-FR",
                        },
                        {"name": "content_funnel", "type": 2, "value": "538383"},
                        {
                            "name": "content_img_big_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/netvibes.png",
                        },
                        {
                            "name": "content_img_medium_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/netvibes.png",
                        },
                        {
                            "name": "content_img_small_url",
                            "type": 2,
                            "value": "https://assets.3ds.com/invest/icon-logos/netvibes.png",
                        },
                        {
                            "name": "content_info_1_label",
                            "type": 2,
                            "value": "||ds-ico-suitcase-mini",
                        },
                        {"name": "content_info_1_type", "type": 2, "value": "text"},
                        {"name": "content_info_1_value", "type": 2, "value": "CDI"},
                        {
                            "name": "content_info_2_label",
                            "type": 2,
                            "value": "||ds-ico-location-mini",
                        },
                        {"name": "content_info_2_type", "type": 2, "value": "text"},
                        {
                            "name": "content_info_2_value",
                            "type": 2,
                            "value": "France, 78, Vélizy-Villacoublay",
                        },
                        {"name": "content_lang", "type": 2, "value": "fr"},
                        {
                            "name": "content_start_datetime",
                            "type": 2,
                            "value": "2024/03/26 07:03:00",
                        },
                        {
                            "name": "content_summary",
                            "type": 2,
                            "value": '<p style="font-family: Arial;"><em>machine learning = apprentissage automatique</em></p>\n<p style="font-family: Arial;"><em></em></p>\n<p>Nous recherchons un(e)<strong> Ing&eacute;nieur(e) Machine Learning (F/H)</strong> pour int&eacute;grer notre &eacute;quipe. Vous participerez au d&eacute;veloppement de nouvelles fonctionnalit&eacute;s d\'aide &agrave; la d&eacute;cision int&eacute;gr&eacute;es &agrave; la 3DEXPERIENCE Platform, bas&eacute;es sur des m&eacute;thodes d\'IA et de traitement de donn&eacute;es avanc&eacute;es.</p>\n<p>Poste bas&eacute; &agrave; V&eacute;lizy-Villacoublay (CDI)</p>\n<p></p>\n<p><strong>Vos missions</strong></p>\n<p>- La compr&eacute;hension des cas d\'usage industriels, en lien avec les &eacute;quipes clients et portfolio / strat&eacute;gie.</p>\n<p>- La conception et le test de solutions algorithmiques, en Python, via tout type d\'algos de Machine Learning et Data Mining; y compris via l\'utilisation de LLMs et mod&egrave;les fondation et le cas &eacute;ch&eacute;ant via du fine-tuning et/ou de l\'orchestration de LLMs (exp&eacute;rimentations et entra&icirc;nements sur DGX A100).</p>\n<p>- L\'industrialisation, int&eacute;gration et la maintenance de vos d&eacute;veloppements sous forme de composants et / ou d\'applications sur la 3DEXPERIENCE Platform Cloud.</p>\n<p>- La r&eacute;alisation de d&eacute;monstrateurs sur la 3DEXPERIENCE Platform, le plus souvent aliment&eacute;s par des donn&eacute;es client, et pr&eacute;sent&eacute;s &agrave; des clients.</p>\n<p style="font-family: Arial;"></p>\n<p>Par ailleurs vous participerez &agrave; l\'&eacute;volution des services techniques de la 3DEXPERIENCE Platform pour supporter l\'ex&eacute;cution de LLM, RAGs, mod&egrave;les fondations, orchestrateurs de LLMs.</p>\n<p>Vous int&eacute;grerez une &eacute;quipe avec des comp&eacute;tences analogues aux v&ocirc;tres, qui vous &eacute;paulera dans votre apprentissage du m&eacute;tier, des produits et des outils internes.</p><p><strong>Vos qualifications</strong><o:p></o:p></p>\n<p style="font-family: Arial;"><strong></strong></p>\n<p>De formation BAC+5 en Ecole d\'ing&eacute;nieur ou cycle universitaire. Vous b&eacute;n&eacute;ficiez d\'une sp&eacute;cialisation en IA ou en Data Science.&nbsp;<o:p></o:p></p>\n<p>Vous b&eacute;n&eacute;ficiez d\'une exp&eacute;rience en ing&eacute;nierie de projets logiciels importants.&nbsp;<o:p></o:p></p>\n<p style="font-family: Arial;"></p>\n<p style="font-family: Arial;"><span style="text-decoration: underline;">Comp&eacute;tences requises pour ce poste :</span></p>\n<ul>\n<li style="font-family: Arial;">Python</li>\n<li style="font-family: Arial;">Deep Learning&nbsp;</li>\n<li style="font-family: Arial;">NLP</li>\n<li style="font-family: Arial;">Mod&egrave;les de langage&nbsp;</li>\n<li style="font-family: Arial;">Structure de donn&eacute;es&nbsp;</li>\n<li style="font-family: Arial;">Complexit&eacute; des algorithmes&nbsp;</li>\n</ul>\n<p>Rigueur, Autonomie, Sens du relationnel, Dynamisme, Curiosit&eacute;.</p>\n<p style="font-family: Arial;"><o:p></o:p>Niveau d&rsquo;anglais professionnel/courant tant &agrave; l&rsquo;&eacute;crit qu&rsquo;&agrave; l&rsquo;oral.<o:p></o:p></p>\n<p style="font-family: Arial;"></p>\n<p style="font-family: Arial;"></p>\n<p><strong>Nous rejoindre c\'est aussi</strong><o:p></o:p></p>\n<p style="font-family: Arial;"><strong></strong></p>\n<p>Int&eacute;grer une entreprise scientifique au c&oelig;ur de l&rsquo;innovation technologique, port&eacute;e par une forte croissance depuis plus de 40 ans<o:p></o:p></p>\n<p><span style="text-decoration: underline;">Principaux avantages et b&eacute;n&eacute;fices :</span></p>\n<ul>\n<li style="font-family: Arial;"><o:p></o:p>Environnement multiculturel.</li>\n<li style="font-family: Arial;">Cadre de travail convivial ax&eacute; sur le bien-&ecirc;tre et la sant&eacute; (salles de sport &amp; de musique, conciergerie&hellip;).</li>\n<li style="font-family: Arial;">Engagement en faveur de la diversit&eacute; et de l&rsquo;inclusion.</li>\n</ul>\n<p><o:p></o:p></p>\n<p class="MsoListParagraphCxSpLast" style="margin-bottom: .0001pt; mso-add-space: auto; text-indent: -18.0pt; line-height: normal; mso-list: l0 level1 lfo1; background: white; vertical-align: middle;"><!-- [if !supportLists]-->&middot;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <!--[endif]-->Politique dynamique de d&eacute;veloppement de carri&egrave;re : plan de formation, mobilit&eacute;s internes, etc.<o:p></o:p></p>\n<ul></ul>\n<p></p>\n<p></p>',
                        },
                        {
                            "name": "content_title",
                            "type": 2,
                            "value": "Ingénieur(e) Machine Learning (F/H)",
                        },
                        {"name": "content_type", "type": 2, "value": "career"},
                        {
                            "name": "content_type_display_text",
                            "type": 2,
                            "value": "CAREERS - R&D",
                        },
                        {"name": "content_cta_1_linker", "type": 2, "value": "3dscom"},
                        {"name": "visibility", "type": 2, "value": "True"},
                        {"name": "content_full_text", "type": 2, "value": "None"},
                        {"name": "code_lang", "type": 2, "value": "fr"},
                        {"name": "meta_cat", "type": 2, "value": "Métier/R&D"},
                        {"name": "meta_cat", "type": 2, "value": "Type de contrat/CDI"},
                        {"name": "meta_cat", "type": 2, "value": "Pays/France"},
                        {
                            "name": "meta_cat",
                            "type": 2,
                            "value": "Ville/France, 78, Vélizy-Villacoublay",
                        },
                        {"name": "meta_cat", "type": 2, "value": "Produits/NETVIBES"},
                        {"name": "meta_cat", "type": 2, "value": "Year/0 to 3 years"},
                        {
                            "name": "content_cta_1_url_id",
                            "type": 2,
                            "value": "https://www.3ds.com/fr/careers/jobs/ingenieur-e-machine-learning-f-h-538383",
                        },
                        {"name": "content_keywords", "type": 2, "value": "FRA016"},
                    ],
                },
            ],
            "groups": [],
            "stats": {
                "status": "ok",
                "queueTime": 0,
                "queryProcessingElapsedTime": 988,
                "queryProcessingCPUTime": 980,
                "queryExecElapsedTime": 5780,
                "queryExecIndexCPUTime": 2736,
                "queryExecSearcherCPUTime": 179,
                "synthesisAndFullHitsElapsedTime": 2254,
                "synthesisIndexCPUTime": 0,
                "synthesisSearcherCPUTime": 0,
                "fullHitsIndexCPUTime": 622,
                "fullHitsSearcherCPUTime": 154,
                "totalProcessingTime": 8139,
            },
            "slicesInfo": [
                {
                    "instance": "i1",
                    "slice": 0,
                    "internalGeneration": 110,
                    "lastCommit": 1715876919887,
                    "lastjob_id": 1715876917822,
                }
            ],
        }
        headers = {
            "Content-Type": "application/json",
        }

        response = requests.post(self.url, json=payload, headers=headers)
        data = response.json()

        job_offers = []
        for hit in data["hits"]:
            offer = Offer(
                site=self.site,
                title=next(
                    (
                        meta["value"]
                        for meta in hit["metas"]
                        if meta["name"] == "content_title"
                    ),
                    None,
                ),
                description=None,
                url=next(
                    (
                        meta["value"]
                        for meta in hit["metas"]
                        if meta["name"] == "content_cta_1_url"
                    ),
                    None,
                ),
                date_publication=datetime.strptime(
                    next(
                        (
                            meta["value"]
                            for meta in hit["metas"]
                            if meta["name"] == "content_start_datetime"
                        ),
                        None,
                    ),
                    "%Y/%m/%d %H:%M:%S",
                ).date(),
                location=next(
                    (
                        meta["value"]
                        for meta in hit["metas"]
                        if meta["name"] == "content_info_2_value"
                    ),
                    None,
                ),
                job_id=next(
                    (
                        meta["value"]
                        for meta in hit["metas"]
                        if meta["name"] == "card_id"
                    ),
                    None,
                ),
            )

            job_offers.append(offer)
        return job_offers


if __name__ == "__main__":
    print(DassaultParser().compare_offers())
