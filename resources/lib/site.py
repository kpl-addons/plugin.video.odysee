from libka import Site
from .rpc import json_rpc, stream_rpc


class API(Site):

    base = 'https://api.na-backend.odysee.com/api/v1/'

    def __init__(self, base=base) -> None:
        super().__init__()
        self.base_url = base

    def _post(self, end, page, json=None):
        if json is None:
            json = json_rpc(page=page)
        else:
            json = json
        return self.jpost(self.base_url + end, json=json)

    def streamable(self, canon_url, id):
        url = 'proxy?m=get'
        return self._post(url, json=stream_rpc(canon_url=canon_url, id=id))

    def get_featured(self, page):
        url = 'proxy?m=claim_search'
        return self._post(url, page=page)['result']['items']
