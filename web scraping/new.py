import requests
import pandas as pd

competitor_list = [
    {
        'url':"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=apple&secondary_results=true&unified_search_shadow_test_enabled=false",
        'cookie':"osano_consentmanager_uuid=4d3bac53-4f82-4de2-a2d9-d5ccc812b3a1; osano_consentmanager=ky7ara8EiINlqyuvzdKN9CuyKnqdqeWUP2tmoWfAfNW-45E1KlmIjC1lYjEWuQGbxtSEjd7VEryG8EfD8mFDHLApL1mtwGwGcAuUtnOzrrtVO7Y7hmCybWHfDqR7l2_hG3yvObUC8cUVGMKTQxEG8IcPnCnDC4A6gt74186F9OV230c5sgY-4Bp0lt9ApqS-GsF67jk1K9HWCHP5CJVZfy8K_nDLg2SrWq3-Q2fJc7lQc6HrVR5dwPnwsttxY0M-BRjjewJnFIECM5euJrdlMR3LK7SKS9bpREtRCQ==; _gcl_au=1.1.35412247.1706764222; _fbp=fb.1.1706764222798.1856152528; _pin_unauth=dWlkPU9UQXlNek0zT0dNdE9HTmxOUzAwTnpsbUxUazFOR1F0WkdVMlpHWTJaamRtT0RFMw; ajs_anonymous_id=8f07fd39-1a22-4d72-9da2-071358a37a1f; __stripe_mid=a4b4de33-fd76-4e3c-9627-88e07dbdb80b73397b; fw_se={%22value%22:%22fws2.719fd5c8-fdca-48fb-aa1d-7430ba56229c.2.1707115038976%22%2C%22createTime%22:%222024-02-05T06:37:18.976Z%22}; _gid=GA1.2.137339529.1707115039; _uetsid=02c20760c3f111eeb9a39302efcf1119; _uetvid=339d4d40c0c011ee98120b37d99d5b6e; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-02-05T06:37:20.810Z%22}; _ga_EMDXDP2N4W=GS1.2.1707115039.2.0.1707115061.38.0.0; __cf_bm=pfHYximU42fzUB6iMK3X.ieOA_V3ozGoagsjUaGo8Uw-1707115064-1-AWR70nGnsUMkK270tVkxNXopnEzsFBdZC/YJsAJuCN1FrvIf4efDW/K2E/P8qh9piT7BoYb7iHPL8VVQBcK2n3M=; __stripe_sid=cfde6266-6802-40a4-b068-2ab1bfd43764b722ef; _gat=1; _gat_UA-000000000-1=1; _ga=GA1.1.1194549165.1706764222; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-02-05T06:39:47.077Z%22}; session-prd-tfm=.eJxNi01vgjAAQP9Lz8bQLjXCbUFlRSjiVNZeCIUyypdKQQdm_30cd3iX9_JeIM47qQtg5Umt5QLEN9k1SSvbHlh9N8xGS63VtY37ayVbYAE5uoVwUhUol5wnAqlyzeUsYYou48yUovohavPGbbIijW9wh6FgQyvvFGKGWE83PqIjVLwsCi86Kv_EK3oimE3f4_xo0l4m_uXmSRSqoDyPwWY7U2HPdgvuwJv43xsMhfPUpNkNAmEsIhOmI1llHy7kn0-VRDuDlNcfOr0jOjHDL32Yh8uBFgfPDu4d78Ld22OIanZ5RvnE9vvMTrfxYT-sxT3rj2cDLMCgZRerDFgYrSFam-bvHwNcaPA.GKIUMg.Mm9Kv-N0bGAPSAn-EFt_HV9vBwE; fw_uid={%22value%22:%2213da95ae-a1ac-41ac-854e-517c01598d97%22%2C%22createTime%22:%222024-02-05T06:39:47.088Z%22}; _ga_2NZ40CS25B=GS1.1.1707115039.3.1.1707115187.22.0.0; _dd_s=rum=1&id=49be38b8-1f3f-41f1-905c-9898be5269d8&created=1707115066362&expire=1707116087314"
        },
    {
        'url':"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_provider=ic&search_term=apple&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false",
        'cookie':"_gcl_au=1.1.1864338757.1707115024; _gid=GA1.2.1328348272.1707115025; BVBRANDID=f736c84d-9524-47f7-96ae-587233e2bb04; BVBRANDSID=9eac89ed-ec3f-4a0c-9644-3911f2f19ec6; _fbp=fb.1.1707115024977.740446327; _pin_unauth=dWlkPU9UQXlNek0zT0dNdE9HTmxOUzAwTnpsbUxUazFOR1F0WkdVMlpHWTJaamRtT0RFMw; __cf_bm=wwBGGQpSJscQ7_ootTs0HmD92cirCn0RPiqF50x4L5A-1707115026-1-AQOugU0KwpZSIZOJrMUINlf+5bMvQ9yhJbcEtIJYIfr3mxBuoGTXG49pPmGhCIfKcEsjLmXL8cRc8KVtqjWTm74=; loyaltyID=undefined; ajs_anonymous_id=7bda6609-2589-49ae-9a52-d68bdcf949a3; dotcomSearchId=634e3a4c-02ce-4d43-9188-8c096f981344; _pin_unauth=dWlkPU9UQXlNek0zT0dNdE9HTmxOUzAwTnpsbUxUazFOR1F0WkdVMlpHWTJaamRtT0RFMw; ajs_anonymous_id=7bda6609-2589-49ae-9a52-d68bdcf949a3; __stripe_mid=840754bb-241d-434e-88a5-74fcc20182b1f3840c; __stripe_sid=dae9b0e3-0b0e-4073-be49-3d5b704254f7050623; _ga=GA1.2.1020516947.1707115025; _gat_UA-47434162-1=1; session-sprouts=.eJwdjt1ugjAARt-l184IqBPuFNhSImUaocIN4aeMllINBbGYvfvYku_cnJvvvEBadUTWwKoyLskCpHfStZkgogdW3w2zkURKehNpf2uIABYgyqvzz4IG1IPhBDVEPXM5S63QIzUzFTp_5Ny8JzbcQhaqmPEaOQk7XqImZrBHTmggutokrKRH7HHfcbWk9RrknKZYQQlFNCVXr8rwiQYMrgLnD3cd2CON8bnP8Ob_66rzBrL7UOKnPNpzVGsOBGuP8urTQJxViUMJW16Xc4d_KUY0uU902StkrJbf8QH5H9sc0rQaxrP7hG-s2Op7PoxcocN7JtDBNr6oqUmwAIMkXUpLYOnr3Txtt_v5BXrAafk.GKIVhw.4kli8_hFuV5B1XH4Cjafa0sU0ZE; _uetsid=faa7a440c3f011ee9b7981d6fa42af57; _uetvid=faa812c0c3f011eea244c969ea0d5b76; _ga_LPZ816BHL5=GS1.1.1707115024.1.1.1707115527.58.0.0; _dd_s=rum=1&id=eb335600-e959-4aee-833a-e1825a579c6c&created=1707115455440&expire=1707116427560"
        },
    {
        'url':"https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frecency&sort=rank&allow_autocorrect=true&search_is_autocomplete=true&search_provider=ic&search_term=apple&secondary_results=true&unified_search_shadow_test_enabled=false",
        'cookie':"__cf_bm=NCwN.iGPAlQb0dIPz8tWaHzJ3fMtd6hgph4ImnyLyXA-1707115044-1-AW7rx3U9CvYhcaI807FkdXRZvTYkzgCYKZVa3ZqS6cVF2gKXGaoCkEGXSAd1Vq6pqZDYaPFsovEslZRfWdwb3bo=; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiYzMjM3MTY5NTQzMTU1MjkzODk4MzU2MDAxNzQwMTk1MjQ0MTI3OFIRCMXN8b_XMRgBKgRJTkQxMAPwAcXN8b_XMQ==; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; _fbp=fb.1.1707115046977.378014044; _pin_unauth=dWlkPU9UQXlNek0zT0dNdE9HTmxOUzAwTnpsbUxUazFOR1F0WkdVMlpHWTJaamRtT0RFMw; _gcl_au=1.1.1836328569.1707115047; wfm.tracking.sessionStart=1707115047421; wfmStoreId=16; at_check=true; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19759%7CMCMID%7C32371695431552938983560017401952441278%7CMCAAMLH-1707719849%7C12%7CMCAAMB-1707719849%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1707122249s%7CNONE%7CMCSYNCSOP%7C411-19766%7CMCCIDH%7C0%7CvVersion%7C5.5.0; ajs_anonymous_id=c0ad7071-268b-47ee-adb2-6c03728c878e; inRedirectYogurtAudience=1; inRedirectGoldPanAudience=1; wfm.tracking.s10=1; dotcomSearchId=8dd920e4-7598-4546-9535-20b0f4ca67e1; lux_uid=170711562425403194; wfm.tracking.x2p=1; at_check=true; _pin_unauth=dWlkPU9UQXlNek0zT0dNdE9HTmxOUzAwTnpsbUxUazFOR1F0WkdVMlpHWTJaamRtT0RFMw; sa-user-id=s%253A0-c314a846-e95f-585a-6855-a77ea7494746.c%252Bm2vFrjOJYA1sYoLYpwpcTqmsRJa9XSFm%252FAeDCH3uA; sa-user-id-v2=s%253AwxSoRulfWFpoVad-p0lHRjEvxIg.eO161Pv2GS7ZMzG%252Faepi77Le1Nb3MhczPa4ejo7Ogrk; sa-user-id-v3=s%253AAQAKIFKNxEq2ttky7EgHck7mfumscKSUBmuIpSGXkEGmPYwFEAEYAyCmhIKuBjABOgSE7j3kQgQ4URYa.qI8N7IbFGU0EfUoj0o05IUcbIXrhjMNxscxZlAqYI1w; __stripe_mid=cde46b93-c09c-425b-a21f-24e989c8da5b562a74; __stripe_sid=6e26f77b-6516-418d-9f1a-140054051f9c9e7598; ajs_anonymous_id=c0ad7071-268b-47ee-adb2-6c03728c878e; s_gpv=Search%20Results:%20apple%20|%20Wegmans; _uetsid=07952790c3f111ee846881a60ff2521b; _uetvid=079550f0c3f111eeba706f86f11592c4; session-prd-weg=.eJwdjt1vgjAAxP-XPhsDiE55U5muhLZBwQovBKGOKh-O8tll__u6PVwu90sud98gvjdM5MC6J4VgMxC_WFMmFataYLVNp4hgQvC6itv6ySpgATY5-e2YcsIdGEioY-5s5grqqXGZlGRqFP2t2LyiPVzBEklkhwvkbweXemb0CFpsQxme9Vz56Pqejmk4hvRSIpURhwJWFxldnXtCPU4env7XJ_bnhKaBh_TUJnT5v3U1iid8vLqMjsLdq1PlpmNU77Mr4qQ6TRkNBCyLPFM_kJ8OWL6P2N9q5EObH3ZrLDPdTG7RLo92NXFJeZTuUB8OWofxuf-aGlvr7RSZYAY6wZqYZ8Ayl9rqbb02Fj-_agZqKQ.GKIWDQ.Hzt75Jh67US_moW-Z_PWJu0cPiw; _dd_s=rum=1&id=0c2f0638-068b-4210-a84c-c78a196225f2&created=1707115624838&expire=1707116561838; mbox=session#368fb15d2ed645598b1877d27997768e#1707117523|PC#368fb15d2ed645598b1877d27997768e.41_0#1770360441"
        }
    ]
searchterm = "Apple"
cookie = competitor_list[1]['cookie']



HEADERS ={
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie 
}
URL = competitor_list[1]['url']+"apple"
responses = requests.get(URL,headers=HEADERS)
data = responses.json()
items=data.get('items')
for item in items:
    print(item.get('name'))
    
print('------------------------')

for item in items:
    for category in item.get('categories'):
        if (category.get('name')=='Fruits'):
            if (searchterm in item.get('name')):
                print(item.get('name'))
        # if (searchterm in item.get('name')):
        #     print(item.get("name"))
            
