import random

ilksifre = "Esrarzaan"
ikincisifre = "iyigeceler"

ultrakill = {
    "Gabriel" : ["https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/00f39406-ea15-4816-a71f-48c412d96de6/dhefk1v-ce8e57ec-6ccd-4daa-a2d5-b9a9650a8b71.png/v1/fill/w_1019,h_785/_ultrakill__gabriel__render__3__by_wtfbooomsh_dhefk1v-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTg2IiwicGF0aCI6IlwvZlwvMDBmMzk0MDYtZWExNS00ODE2LWE3MWYtNDhjNDEyZDk2ZGU2XC9kaGVmazF2LWNlOGU1N2VjLTZjY2QtNGRhYS1hMmQ1LWI5YTk2NTBhOGI3MS5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.EzIcV_GPBvL-AYTn8BNXdZ4-uvTWoEls5xImYFzLQ2s",
                 "https://i1.sndcdn.com/artworks-qYkiwZoEnE6xYcHZ-fTyHVQ-t1080x1080.jpg","https://static.wikia.nocookie.net/ultrakill/images/e/e3/Gabriel_Ultrakill_Render.webp/revision/latest?cb=20241027004733"
    ],

    "V1" : [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6IKsCVtLo1-8dCHNWrAmBb0gAp-P4dPLxrg&s","https://i.namu.wiki/i/4mjyAdfvMNAyVdEwiYzhrGW4jeT3QPssSRiq9agnFTenw4E8BabK-DtJj1KqGNVmvS6KxXGKweOhmbssSo0hlA.webp",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiitRtrfhu-yZ6rx2WlmwqMUIIGV2W7X_8pQ&s"
    ],

    "V2" : [
        "https://static.wikia.nocookie.net/ultrakill/images/1/13/V2Sitting.png/revision/latest?cb=20230219072619",
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d4781b81-c845-4a59-a2dc-a2bdf2e91683/dg5m8xz-11111146-3a65-4485-b0f7-452196f129f4.png/v1/fill/w_1280,h_1684,q_80,strp/v2_4_4_ultrakill_by_curseorder_dg5m8xz-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTY4NCIsInBhdGgiOiJcL2ZcL2Q0NzgxYjgxLWM4NDUtNGE1OS1hMmRjLWEyYmRmMmU5MTY4M1wvZGc1bTh4ei0xMTExMTE0Ni0zYTY1LTQ0ODUtYjBmNy00NTIxOTZmMTI5ZjQucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.T40isUrE-EANiTJUKDr7iFe1Uez_zPf1jRcDL0Tt4e0",
        "https://i.namu.wiki/i/zzdue411YH_ImTmuwwhSQ2m1OIVFPrHlukk7eDVAPSgzt0PGA8Twtl3YBkUkIEk5yVzFBJ4z8gJe7-it5fV2sg.webp"
    ],

    "Leviathan" : [
        "https://static.wikia.nocookie.net/ultrakill/images/c/c1/Ryann-victoria-leviathan.jpg/revision/latest?cb=20220824133101",
        "https://art.ngfiles.com/images/5401000/5401546_431807_elcuevo_untitled-5401546.23897fe0ea2fc04d98c27cc174a24f86.webp?f1706320084"
    ],

    "1000-THR Earthmover" : [
        "https://static.wikia.nocookie.net/ultrakill/images/1/1d/0earthmover.jpg/revision/latest/scale-to-width-down/250?cb=20240508201740",
        "https://static.wikia.nocookie.net/villains/images/6/6a/1000-THR_Earthmover.webp/revision/latest?cb=20240213035302"
    ],

    "Minos Prime" : [
        "https://images.steamusercontent.com/ugc/2027225799698789803/90C51DDACB8C4A501C4B6F0377CE090DDA2091B8/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
        "https://static.wikia.nocookie.net/ultrakill/images/d/de/Ryann-victoria-minosprime.jpg/revision/latest/scale-to-width-down/250?cb=20230528205531"
    ],

    "Sisyphus Prime" : [
        "https://static.wikia.nocookie.net/ultrakill/images/1/13/Sisyphus_superherolanding.jpg/revision/latest/scale-to-width-down/250?cb=20240204044900",
        "https://ella.janitorai.com/bot-avatars/186c281d-66c2-48fe-a0c8-bc375a3b6754_8546d166-3178-4570-801d-83f705820b67.webp?width=1200"
    ]

}


def ultrakillrandom():
    ultrakill_bosses = random.choice(list(ultrakill.keys()))  # Rastgele bir karakter seç
    image_url = random.choice(ultrakill[ultrakill_bosses])  # O karakterin rastgele bir görsel URL'sini seç
    return ultrakill_bosses, image_url
