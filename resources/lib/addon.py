from libka import Plugin, call, PathArg
from libka.logs import log
from libka.menu import Menu, MenuItems
from libka.resources import Media, Resources
from libka.search import Search, search

from xbmcgui import ListItem
import xbmcplugin

from .site import API
from .channel_ids import channel_ids


class Addon(Plugin):
    def __init__(self) -> None:
        super().__init__()
        self.api = API()

    MENU = Menu(view='addons', items=[
            Menu(title='Search', call='search'),
            Menu(title='Featured', call=call('listing', 1, 'featured')),
            Menu(title='Popculture', call=call('listing', 1, 'popculture')),
            Menu(title='Artists', call=call('listing', 1, 'artists')),
            Menu(title='Education', call=call('listing', 1, 'education')),
            Menu(title='Lifestyle', call=call('listing', 1, 'lifestyle')),
            Menu(title='Spooky', call=call('listing', 1, 'spooky')),
            Menu(title='Gaming', call=call('listing', 1, 'gaming')),
            Menu(title='Tech', call=call('listing', 1, 'tech')),
            Menu(title='Comedy', call=call('listing', 1, 'comedy')),
            Menu(title='Music', call=call('listing', 1, 'music')),
            Menu(title='Sports', call=call('listing', 1, 'sports')),
            Menu(title='Universe', call=call('listing', 1, 'universe')),
            Menu(title='Finance', call=call('listing', 1, 'finance')),
            Menu(title='Spirituality', call=call('listing', 1, 'spirituality')),
            Menu(title='News', call=call('listing', 1, 'news')),
            Menu(title='Docs', call=call('listing', 1, 'docs')),
            Menu(title='Rabbithole', call=call('listing', 1, 'rabbithole'))
        ])

    def home(self):
        self.menu()

    def nop(self):
        pass

    @search.folder
    def search_folder(self, query):
        claim = self.api.searching(query)
        urls = [f"lbry://{x['name']}#{x['claimId']}" for x in claim]

        resolve = self.api.resolve(urls)
        with self.directory(view='movies') as kdir:
            for u in urls:
                title = resolve['result'][u]['value']['title']
                canon_url = resolve['result'][u]['canonical_url']
                meta = resolve['result'][u]['meta']['creation_timestamp']
                kdir.play(title,
                          call(self._play_stream, title, canon_url, meta),
                          art=self.get_art(resolve['result'][u]))

    def get_art(self, response):
        landscape = response['value']['thumbnail']['url']
        return {
            'icon': self.media.image('icon'),
            'fanart': landscape
        }

    def listing(self, page: PathArg[int], ids):
        channels = channel_ids().get(ids, [])
        with self.directory(view='movies') as kdir:
            for cat in self.api.get_category(page, channels):
                kdir.play(cat["value"]["title"],
                          call(self._play_stream,
                               cat["value"]["title"],
                               cat['canonical_url'],
                               cat['meta']['creation_timestamp']),
                          art=self.get_art(cat))
            kdir.menu('Next Page', call(self.listing, page + 1, ids))

    def _play_stream(self, title, canon_url, id):
        stream_url = self.api.streamable(canon_url, id)['result']

        listitem = ListItem(label=title, path=stream_url['streaming_url'])
        xbmcplugin.setResolvedUrl(self.handle, True, listitem)
