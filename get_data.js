const url = 'https://apps.emaillistverify.com/maillists/checksingleemailData';
const headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_gcl_aw=GCL.1696867899.CjwKCAjwyY6pBhA9EiwAMzmfwTOGeqsacnl_e_lFoQ4TpVO05QcwYEe8a3lsLlAVXYRLDLMRtoyI_xoCzEoQAvD_BwE; _gcl_au=1.1.573112456.1696867899; _gac_UA-6916633-42=1.1696867899.CjwKCAjwyY6pBhA9EiwAMzmfwTOGeqsacnl_e_lFoQ4TpVO05QcwYEe8a3lsLlAVXYRLDLMRtoyI_xoCzEoQAvD_BwE; _fbp=fb.1.1696867899771.1589449211; FPID=FPID2.2.FrelJbQIe9xlrd98cQdBQusyRygZSPyd3kjlVgUaG98%3D.1696867899; __ssid=16ecd127dbc2d6b1e7df95afed04c7a; _hjSessionUser_65831=eyJpZCI6ImE4ZTIwZjcxLTkwNmMtNWEwMC04YmIwLTgxMDU3NWRlOGFiMiIsImNyZWF0ZWQiOjE2OTY4Njc5OTYwNzEsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1032129612.1698660337; FPLC=ahe9bALiJ4IbuJWvH3VgNOifhrjRlSMHZgJznJGsWxe77WZm7tMVA2Vf1BMnifh1TX4JlZSuwwqylMeYsCOoPS5JF2dOliEmWugMM1lKYEQcqfTwT8hTma5rHyLR%2Bg%3D%3D; emaillistverify=949j40bkr2he4o0a4j4magmtse; user_id=396895; __ca__chat=mcymitrbggk0; arp_scroll_position=51.33333206176758; FPGSID=1.1698673736.1698673812.G-D36HQSPFPE.F8PGM5tXFLL-euDAM5Gjtw; _gat_UA-6916633-42=1; RefUser=Q2FrZQ%3D%3D.YzhmYWI4MGFmM2F5YmUzNTVlOGMxMTRmZjA5OTlkMzI1YjJhMTdjYWQxNmQ5YjU2NmZjMWY1MGFlMzljY2UyNIwJjIi3kGNFpBN6QUuxaXlDy0VRWKNZzUOjtST5JkQZYPwETf2u3ERxgp%2F7Ap7GzQ%3D%3D; _uetsid=decc02b0770b11ee80f4639e28bdb832; _uetvid=8af3400066be11eea21f27aee7b626df; _ga=GA1.2.666497983.1696867899; _ga_YNTZ4Z1RKV=GS1.2.1698673735.10.1.1698673813.58.0.0; _ga_D36HQSPFPE=GS1.1.1698673734.11.1.1698673830.0.0.0',
    'Origin': 'https://apps.emaillistverify.com',
    'Referer': 'https://apps.emaillistverify.com',
    'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Csrf-Token': 'undefined',
    'X-Requested-With': 'XMLHttpRequest',
};

const formData = new FormData();
formData.append('_method', 'POST');
formData.append('emailtocheck', 'rustomdeveloper@gmail.com');
formData.append('_Token[fields]', '8db1f9d48b4fa5b2dec66a630ad551747a0abf22%3A');
formData.append('_Token[unlocked]', '');

fetch(url, {
    method: 'POST',
    headers: headers,
    body: formData
})
    .then(response => {
        if (!response.ok) {
            throw new Error(`Request failed with status: ${response.status}`);
        }
        return response.text(); // Retrieve the response as text
    })
    .then(responseText => {
        console.log('Response Text:', responseText); // Log the response text
        const data = JSON.parse(responseText); // Attempt to parse the response as JSON
        console.log('Parsed JSON Data:', data); // Log the parsed data
    })
    .catch(error => {
        // Handle errors here
        console.error(error);
    });
