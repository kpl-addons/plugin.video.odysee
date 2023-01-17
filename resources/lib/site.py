from libka import Site
from .rpc import json_rpc, stream_rpc


class API(Site):

    base = 'https://api.na-backend.odysee.com/api/v1/'

    def __init__(self, base=base) -> None:
        super().__init__()
        self.base_url = base

    def _post(self, end, json=None):
        if json is None:
            json = json_rpc()
        else:
            json = json
        return self.jpost(self.base_url + end, json=json)

    def streamable(self, canon_url, id):
        url = 'proxy?m=get'
        return self._post(url, json=stream_rpc(canon_url=canon_url, id=id))

    def get_featured(self):
        url = 'proxy?m=claim_search'
        return self._post(url)['result']['items']
