import requests, json

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Cookie' : 'ezosuibasgeneris-1=f7b821e6-a08c-46ed-6e09-3e24daf6cd64; ezds=ffid%3D1%2Cw%3D1280%2Ch%3D720; _ga=GA1.2.962618215.1696476488; _pbjs_userid_consent_data=3524755945110770; _cc_id=92d4ba24cc9b55e738f266608f182737; _au_1d=AU1D-0100-001696476490-FVLXLVNU-PIEJ; _ga_77QZRN3T9T=GS1.2.1696476488.1.1.1696476535.0.0.0; __qca=P0-1775450144-1696476542373; ezoadgid_325089=-2; ezoref_325089=google.com; ezoab_325089=mod51-c; ezepvv=0; lp_325089=https://www.verifyemailaddress.org/; ezovuuid_325089=6492c776-ae9b-448d-6e47-21a44013eefb; ezouspvv=0; panoramaId=ebc86507ee95f50dbcbf65acd18616d539381d08ece3de83f9aa3e71e87c4be7; panoramaIdType=panoIndiv; panoramaId_expiry=1699803571669; __gads=ID=ee56057d2c8299b5:T=1696476489:RT=1699198771:S=ALNI_Ma2OwDRc3XUX-FoxDZzkr-_FeDRdA; __gpi=UID=00000c8e1d88938f:T=1696476489:RT=1699198771:S=ALNI_MYXAhX3CxGKwf-2tuZot1RUxtRh0A; _gid=GA1.2.1203228603.1699198775; ntvSession={}; ntv_as_us_privacy=1---; _au_last_seen_pixels=eyJhcG4iOjE2OTkxOTg3NzIsInR0ZCI6MTY5OTE5ODc3MiwicHViIjoxNjk5MTk4NzcyLCJydWIiOjE2OTkxOTg3NzIsInRhcGFkIjoxNjk5MTk4NzcyLCJhZHgiOjE2OTkxOTg3NzIsImdvbyI6MTY5OTE5ODc3MiwiYW1vIjoxNjk5MTk4Nzc4LCJpbXByIjoxNjk5MTk4Nzc4LCJ1bnJ1bHkiOjE2OTkxOTg3NzgsIm9wZW54IjoxNjk5MTk4Nzc4LCJhZG8iOjE2OTkxOTg3NzgsInNvbiI6MTY5OTE5ODc3Miwic21hcnQiOjE2OTkxOTg3NzgsImNvbG9zc3VzIjoxNjk5MTk4Nzc4LCJiZWVzIjoxNjk5MTk4NzcyLCJpbmRleCI6MTY5OTE5ODc3OCwidGFib29sYSI6MTY5OTE5ODc3MiwicHBudCI6MTY5OTE5ODc3OH0%3D; cto_bundle=; ezux_ifep_325089=true; ezouspva=0; active_template::325089=pub_site.1699198856; ezopvc_325089=5; ezovuuidtime_325089=1699198856; ezohw=w%3D609%2Ch%3D559; connectId=%7B%22ttl%22%3A86400000%2C%22lastUsed%22%3A1699198872839%2C%22lastSynced%22%3A1699198772769%7D; ezux_lpl_325089=1699198872860|5e50babb-c25b-4cbe-6148-acc2e5241671|true; _tfpvi=MWQ5NTljZTktZWEzNC00Yjc4LTk3ZjAtZjkyZDVkOGUyMDU4IzgtNg%3D%3D; arp_scroll_position=53.33333206176758; _sharedid=edc5cce6-eef7-4ca9-a97f-37c2b2a10773; _sharedid_cst=VyxHLMwsHQ%3D%3D; cto_bidid=4PHgXl8wSk5KTmo3ejRocFFkRHpzOWdpTnl4UWtnRmNybHh5d054aUJtblN1dDFidXJMaCUyQktoN1hlYmklMkZSTGpiSXVFdVVNVmxTbXY2d3d3UEJYSmdCUUdiTXpHRVhucSUyRktXJTJGMmJOb3BYZTFzWXRhcXhBZDNXbkEwZXU4UmIzMktQMERU; cto_bundle=EQB8VF9QSDZuc1JvTDJwd1d5VjNEVVdxRnglMkJPejA3a2VORFhQSFBSVXZYT2U4am80VWZXZFhSVCUyRiUyQkx1Z0J2QXNvSCUyRmZoVmtscGM3ekV0dnQ0MDR4YXlNbVdMTWx5b1pKa0xRRXkyUHdPUGkxRnF4OTdySzklMkIyZXVBcGNOblpQbHR1QVF4VnptVm42NmxXY1o3eiUyRkdzSEVTZDVrMyUyQkFDcWFybXJCZmkwT1ZBckFnayUzRA; cto_bundle=EQB8VF9QSDZuc1JvTDJwd1d5VjNEVVdxRnglMkJPejA3a2VORFhQSFBSVXZYT2U4am80VWZXZFhSVCUyRiUyQkx1Z0J2QXNvSCUyRmZoVmtscGM3ekV0dnQ0MDR4YXlNbVdMTWx5b1pKa0xRRXkyUHdPUGkxRnF4OTdySzklMkIyZXVBcGNOblpQbHR1QVF4VnptVm42NmxXY1o3eiUyRkdzSEVTZDVrMyUyQkFDcWFybXJCZmkwT1ZBckFnayUzRA; ezux_et_325089=70; ezux_tos_325089=89; _publink=%7B%22publink%22%3A%22ec1aWeogOeaqZ6l_M0PCLjOQWgfnaB68mo5hh2oc-RFs3PtDDGrfAkMzuM08WGraDvSRf8-alNXIUc8%22%2C%22refresh%22%3A1699285292%2C%22cv%22%3A1%7D',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',

}

data = {
    'email' : 'fiverr_order123@outlook.com',
    'rc': 'cd4b62de9500c18ce20b139bbadde51cb66c1b62c5be70609781131ff901118d',
}

json_data = json.dumps(data)

r = requests.post('https://www.verifyemailaddress.org/email-validation', headers=headers, data=json_data)
print(r.content)
