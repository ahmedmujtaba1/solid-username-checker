import requests, json

headers = {
    'Upgrade-Insecure-Requests' : '1',
    'Cookie' : 'PHPSESSID=a569fa40df9d326a5bc6ffa9b67eedd0; _gcl_au=1.1.2058926950.1699189628; AeFirst63b2bb64359b020724026a3a=1699189736523; tarteaucitron=!affilae=true!googleadwordsconversion=true!googleadwordsremarketing=true!googletagmanager=true!recaptcha=true!plausible=true; arp_scroll_position=448',
    # 'Accept' : 'application/json',
    # 'Accept-Encoding' : 'gzip, deflate, br',
    # 'Content-Type' : 'application/json;charset=UTF-8',
    # 'Cookie' : '_vwo_uuid_v2=DC7F2186F8829835CD12E7F0E7E5D2D9A|cdccb975b9a2d21d67a96a7426ed7f82; _vwo_uuid=DC7F2186F8829835CD12E7F0E7E5D2D9A; _vis_opt_exp_594_combi=3; _gcl_au=1.1.1010831537.1696481110; _fbp=fb.1.1696481110832.240098880; _ga=GA1.2.931796954.1696481113; insent-user-id=lTGOLIN1mpzHorpVl1696481115682; _vis_opt_exp_594_goal_3=1; _vis_opt_exp_594_goal_7=1; _vis_opt_exp_594_goal_6=1; _vwo_uuid_v2=DC7F2186F8829835CD12E7F0E7E5D2D9A|cdccb975b9a2d21d67a96a7426ed7f82; _vis_opt_exp_594_goal_2=1; _omappvp=6BE6qcTQSsLoLcQowGGHflclSjXNCZB8lxAiSOe8xFJDPoj8vK6t8ofXhDMUmNxykt5R1Oma7YGeWC1EEyF9kH9gWjeXPhuo; _vis_opt_exp_489_combi=1; _hjSessionUser_579853=eyJpZCI6IjIwOTM2MmZmLTZmNjItNTdmMi04YWYzLTUwZDEyMWY1NDM1NiIsImNyZWF0ZWQiOjE2OTY0ODExMTMyNDQsImV4aXN0aW5nIjp0cnVlfQ==; _vis_opt_exp_489_goal_6=1; _vis_opt_exp_489_goal_3=1; _vis_opt_exp_489_goal_2=1; __stripe_mid=2d046a64-ccbc-4599-8b9a-2ee536ddf936d0729d; _pxvid=517d2f99-7006-11ee-9aaa-785c0991d303; _cfuvid=ZAhnwz7jnYreZAjOfic6uwzIO1TIFEpWPAzlS5MInk0-1699185260401-0-604800000; _vis_opt_s=4%7C; _vis_opt_test_cookie=1; _vis_opt_exp_462_combi=2; _vis_opt_exp_465_combi=1%2C2; _vwo_ds=3%3At_0%2Ca_0%3A0%241696481109%3A17.86330522%3A%3A%3A559_0%2C485_0%2C4_0%2C3_0%3A1; pxcts=1058a77c-7bd2-11ee-900c-76365b42eeed; _vis_opt_exp_465_goal_5=1; _gid=GA1.2.1499064552.1699185266; _hjIncludedInSessionSample_579853=0; _hjSession_579853=eyJpZCI6IjgyY2I1NmUzLTNlOGItNDczNy1iZDcxLTE2YWFjYTQ0NTM2MiIsImNyZWF0ZWQiOjE2OTkxODUyNjYwNDksImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=1; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:2%2Cutc:1699185269201%2Cregion:%27PK%27}; __stripe_sid=8dd826ca-0e03-4764-a1f0-0f9c36bb0dce9482ff; arp_scroll_position=26; _vis_opt_exp_465_goal_1=1; remember_4ed753265105cfbb22a8f6e4e643350e=eyJpdiI6ImhXV3piQ0ZRNm9HaVd6SVU2M3RTSmc9PSIsInZhbHVlIjoiSDF5WktIclVZZ0NNYTRXN09aZDNkdDRhZ0k0ZHozQ2o1TUZwMUhzMGdmY203ZktRdk5FYXplSnNnb0JGQUNmaTE2MzJ3d09seFNZdTRFdm9DNG1kQ2pwcUw5U1hiZ2I1Z0xscFE2NW5ERzhObDA1RG1GTHVXeTZiUmVuMldsRWNLNDZXTUtWV3RkUHZNTlF2TVgwSDNYdnFaaGZ2ZGdGXC9MZENFRTJodk9JSzE2V1NYQ2hJQWJyRHhzazVtOXRUZSIsIm1hYyI6Ijc3MTE2OTBkNDBlMGNjN2ZkNDUxMTljMTE2ZWY0NDQzN2ZiNzQ5NmQyMjQ2ZjA5MjFkYzNlN2Y5Nzc1YzZmODcifQ%3D%3D; _gat=1; _vwo_sn=2704152%3A9%3A%3A%3A1; _ga_MYQ0VJL79L=GS1.2.1699185266.5.1.1699185431.52.0.0; neverbounce_session=eyJpdiI6ImtNeG1JN0hMcTNuMmR6QWphVFdKamc9PSIsInZhbHVlIjoibkFQSTJXb2NWZUlCOEx0djF6WjBtVlY5WnhxelZoR0JQR0UxaHpqZERHODBBcGl3aHFwVlpVS0tHODBEU1VTS2poUnk0KytaZ0tLV2NtekdkQ2EwRFE9PSIsIm1hYyI6IjIzOGM3ZWFiN2FkMTMwYWE3MWNmYWExOTk3NTBiOWViM2I4YTlhMmE4NjM0MjRmNTU2MmZiZDQyYzVlZmFlNTUifQ%3D%3D',
    # 'X-Csrf-Token' : 'tcpkbSLjTD1rs1ESHz4feW4tslPGByPKjOBxeVqO',
    # 'X-Requested-With' : 'XMLHttpRequest',
}

data = {
    'email' : 'fiverr_order123@outlook.com',
    'g-recaptcha-response' : '03AFcWeA4AjpA6BvcW-BGu2T7W7rZu8Mm0oUeiWFO1WgvCKuD7sts3IKTduBQWrlCzUIVwiiY_T1u8u6zXCVHWFwKSANQi8yNN40yPIm2OQL4AtMF6IaeXQynqpKAzQEUOOr47QyLJYJwBAz6BUgZy1YeQ3yDqYg9nSdzHv_tNmm7-QLlv2MpgWb1U51fJ6InubKuG81DgsdFFPx1tDKHBDd6bpMRoYwDp5umMIU_P-rQUDPpHWdJ0uips8GqGLettYYbBs82zZR3wtqyH1JxHXdOyeCVAufmetfoP2amWa2CGOHOIVVr3bof1shtzmSVqMmuy7HxCJQg2RuYKiB8dgK2yzWBErJKra8TMadSS4OVitB3LGib6r3MZGHVw2NDbczN04gfJxomuk1wPEh1Mia-OE1kXCjYS_xIVdzTe5HowzmES1S4O9gkgKvTj4VDu3XVdt3KajV0EPN8GIbxi-ePau1OjuBeWqib4eG-B1_h3rulENH10uP1IO0ON47X6apICSny8sWLsvedqBQjr4M_dl26SDlHjzJOi4y_9_odiR4KfGKx_UP0',
}

json_data = json.dumps(data)

r = requests.post('https://app.neverbounce.com/api/verify/check', headers=headers, data=json_data)
r = requests.post('https://captainverify.com/mail-tester.html', headers=headers, data=json_data)
print(r.content)
