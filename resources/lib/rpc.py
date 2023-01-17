from libka.logs import log


def json_rpc():
    return {
        "jsonrpc": "2.0",
        "method": "claim_search",
        "params": {
            "page_size": 24,
            "page": 1,
            "claim_type": ["stream", "repost", "channel"],
            "no_totals": True,
            "not_channel_ids": [],
            "not_tags":
                ["porn", "porno", "nsfw", "mature", "xxx", "sex", "creampie",
                 "blowjob", "handjob", "vagina", "boobs", "big boobs",
                 "big dick", "pussy", "cumshot", "anal", "hard fucking",
                 "ass", "fuck", "hentai"],
                "order_by": ["trending_group", "trending_mixed"],
                "remove_duplicates": True,
                "has_source": True,
                "limit_claims_per_channel":
                    1, "channel_ids":
                        ["1c6dff2c2c2eb2d68b43c8e769bdf2a9cfb7e49e",
                         "a8d1094b9c6624f59f19f6e139152d1e00caa9f4",
                         "d4d17e20bec31c971b1ab6370a11203ccec095a4",
                         "5b0b41c364c89c5cb13f011823e0d6ee9b89af26",
                         "5a1b164d0a2e7adf1db08d7363ea1cb06c30cd74",
                         "7566c26e4b0e51d84900b8f153fc6f069ad09ef7",
                         "3346a4ff80b70ee7eea8a79fc79f19c43bb4464a",
                         "2b6c71a57bad61e17276ba9b9e4c58959cad1d7b",
                         "273163260bceb95fa98d97d33d377c55395e329a",
                         "c5cd9b63e2ba0abc191feae48238f464baecb147",
                         "96043a243e14adf367281cc9e8b6a38b554f4725",
                         "719b2540e63955fb6a90bc4f2c4fd9cfd8724e1a",
                         "589276465a23c589801d874f484cc39f307d7ec7",
                         "39065ea36ccf9789327aab73ea88f182c8b77bd3",
                         "5e0333be82071767a3aa44a05bb77dcec4c30341",
                         "32d4c07ecf01f2aeee3f07f9b170d9798b5e1d37",
                         "25f384bd95e218f6ac37fcaca99ed40f36760d8c",
                         "48c7ea8bc2c4adba09bf21a29689e3b8c2967522",
                         "18b0d45be9f72c3c20a47f992325cb0f8af0fe7c",
                         "fee415182e20af42122bea8d1682dc6a4d99a0d6",
                         "d2af9d4cec08f060dfe47510f6b709ebf01d5686",
                         "49fe7ca8bb2f7a794b1cba1d877d98dae520ac73",
                         "ba79c80788a9e1751e49ad401f5692d86f73a2db",
                         "c1a5fd043a1dbc8ff4ec992aefc482c970e7568e",
                         "b6e207c5f8c58e7c8362cd05a1501bf2f5b694f2",
                         "fb364ef587872515f545a5b4b3182b58073f230f",
                         "beddc710e4a9f8f296fa3a6d7ea13f816422ffa5",
                         "e4264fc7a7911ce8083a61028fe47e49c74100cf",
                         "f3e79bf8229736a9f3ae208725574436e9d4ac03",
                         "f1dff225e758dd5bc8ab8b91894096215297b2be",
                         "468aa10ee3f12f0ba6cf2641f11e558c841f12fa",
                         "b6a8abdc754fd7f86d571fd98a04deaac4cef889",
                         "3808a556e5994e51b7e6b86f1173fdaf558dfd4e",
                         "af927bd2092e7383789df183ff1eaf95c7041ee9",
                         "7566c26e4b0e51d84900b8f153fc6f069ad09ef7",
                         "3f89fd1bb05eb81f1b159d7f9d3cf15431ede280",
                         "15627c8d79e7c45b15fbe726b34d47accf11b8e2",
                         "a3e35f723d9ad82159b4858ad628e090d0e372df",
                         "6f3940e512a40f2ac8068103bd9195fa07107043",
                         "1487afc813124abbeb0629d2172be0f01ccec3bf",
                         "76283e4cd0168e392128124a013c8335a987186d",
                         "a87ee0c50662b13f11b6fdd3eefd4cee17930599",
                         "abf8c3b0426cd89fce01770a569d525c648a92b5",
                         "9d37b138c50014eaaf9d5e6110d58250acc521fd",
                         "8d497e7e96c789364c56aea7a35827d2dc1eea65",
                         "e5872eb7237883e4158cf88e96a465f7a674c968",
                         "3e63119a8503a6f666b0a736c8fdeb9e79d11eb4",
                         "a29db3ebf677f1fe317ca4ecf0a65a172d4735be",
                         "871ba605db0cad46e43081c4b3d942b80696359f",
                         "4a7f6709df6770e0786b04599fb00262a98d220b",
                         "d273a5d2b57785d19d4c123255bc54f9e45f7e83",
                         "7667bf94424f30ad4d2b77d86e9c0cbbc4a9925d",
                         "1a3d19924669c4e2cbeb04d879a58fae714386f6",
                         "13d66a5f9188e890ef62487bc4a3c785047f7528",
                         "3511b71e5843ae53c35a5fff3e6ef7a3377dd0f7"],
                        "release_time": ">1672164000"
                        }}


def stream_rpc(**kwargs):
    return {
        "jsonrpc": "2.0",
        "method": "get",
        "params": {"uri": kwargs['canon_url'],
                   "environment": "live"}}

