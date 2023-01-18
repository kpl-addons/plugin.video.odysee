from libka import Site
from .rpc import json_rpc, stream_rpc, resolve_rpc


class API(Site):

    base = 'https://api.na-backend.odysee.com/api/v1/'

    def __init__(self, base=base) -> None:
        super().__init__()
        self.base_url = base
        self.search_link = 'https://lighthouse.odysee.tv/search'

    def _post(self, end, page=None, ids=None, sorting=None, json=None):
        if json is None:
            json = json_rpc(page=page, channel_ids=ids, sorting=sorting)
        else:
            json = json
        return self.jpost(self.base_url + end, json=json)

    def _get_search(self, query):
        return self.jget(self.search_link + query)

    def streamable(self, canon_url, id):
        url = 'proxy?m=get'
        return self._post(url, json=stream_rpc(canon_url=canon_url, id=id))

    def get_category(self, sort, page, *args):
        url = 'proxy?m=claim_search'
        return self._post(url, sorting=sort, page=page,
                          ids=args[0])['result']['items']

    def searching(self, query):
        param = f'?s=${query}&size=40&from=0&nsfw=false&uid=744469412'
        return self._get_search(param)

    def resolve(self, urls):
        url = 'proxy?m=resolve'
        return self._post(url, json=resolve_rpc(urls))
