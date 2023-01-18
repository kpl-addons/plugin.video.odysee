from libka import Plugin, call, PathArg
from libka.logs import log
from libka.menu import Menu, MenuItems
from libka.resources import Media, Resources
from libka.search import Search, search

from xbmcgui import ListItem
import xbmcplugin
import datetime

from .site import API
from .channel_ids import channel_ids


class Addon(Plugin):
    def __init__(self) -> None:
        super().__init__()
        self.api = API()

    MENU = Menu(view='addons', items=[
            Menu(title='Search', call='search'),
            Menu(title='Featured', call=call('listing', 1, 'featured',
                                             'trending')),
            Menu(title='Popculture', call=call('listing', 1, 'popculture',
                                               'trending')),
            Menu(title='Artists', call=call('listing', 1, 'artists',
                                            'trending')),
            Menu(title='Education', call=call('listing', 1, 'education',
                                              'trending')),
            Menu(title='Lifestyle', call=call('listing', 1, 'lifestyle',
                                              'trending')),
            Menu(title='Spooky', call=call('listing', 1, 'spooky',
                                           'trending')),
            Menu(title='Gaming', call=call('listing', 1, 'gaming',
                                           'trending')),
            Menu(title='Tech', call=call('listing', 1, 'tech', 'trending')),
            Menu(title='Comedy', call=call('listing', 1, 'comedy', 'trending')),
            Menu(title='Music', call=call('listing', 1, 'music', 'trending')),
            Menu(title='Sports', call=call('listing', 1, 'sports', 'trending')),
            Menu(title='Universe', call=call('listing', 1, 'universe',
                                             'trending')),
            Menu(title='Finance', call=call('listing', 1, 'finance',
                                            'trending')),
            Menu(title='Spirituality', call=call('listing', 1, 'spirituality',
                                                 'trending')),
            Menu(title='News', call=call('listing', 1, 'news', 'trending')),
            Menu(title='Docs', call=call('listing', 1, 'docs', 'trending')),
            Menu(title='Rabbithole', call=call('listing', 1, 'rabbithole',
                                               'trending'))
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
                summary = resolve['result'][u]['value'].get('description', '')
                canon_url = resolve['result'][u]['canonical_url']
                meta = resolve['result'][u]['meta']['creation_timestamp']
                premiered = datetime.datetime.fromtimestamp(int(meta))
                tags = ' / '.join(resolve['result'][u]['value'].get('tags', []))
                info = {
                    'title': title,
                    'plot': summary,
                    'premiered': premiered.strftime("%Y-%m-%d"),
                    'date': premiered.strftime("%Y-%m-%d"),
                    'year': premiered.strftime("%Y"),
                    'genre': tags
                }
                art = self.get_art(resolve['result'][u])
                kdir.play(title,
                          call(self._play_stream, title, canon_url, meta),
                          art=art,
                          info=info)

    def get_art(self, response):
        thumbnail = response['value'].get('thumbnail', {}).get('url')
        return {
            'icon': self.media.image('icon'),
            'fanart': thumbnail
        }

    def listing(self, page: PathArg[int], ids, sorting):
        channels = channel_ids().get(ids, [])
        with self.directory(view='movies') as kdir:
            kdir.menu('Back to [B]main menu[/B]', call(self.home))
            kdir.menu('[B]== Order by ==[/B]', call(self.sort_listing, ids))
            for cat in self.api.get_category(sorting, page, channels):
                ts = cat['meta']['creation_timestamp']
                premiered = datetime.datetime.fromtimestamp(int(ts))
                info = {
                    'title': cat['value']['title'],
                    'plot': cat['value'].get('description', ''),
                    'premiered': premiered.strftime("%Y-%m-%d"),
                    'date': premiered.strftime("%Y-%m-%d"),
                    'year': premiered.strftime("%Y"),
                    'genre': ' / '.join(cat['value'].get('tags', []))
                }
                art = self.get_art(cat)
                kdir.play(cat["value"]["title"],
                          call(self._play_stream,
                               cat["value"]["title"],
                               cat['canonical_url'],
                               cat['meta']['creation_timestamp']),
                          art=art,
                          info=info)
            kdir.menu('Next Page', call(self.listing, page + 1, ids, sorting))

    def sort_listing(self, ids):
        with self.directory(view='addons') as kdir:
            kdir.menu('Back to [B]main menu[/B]', call(self.home))
            kdir.menu('Sort by [B]newest[/B]', call(self.listing, 1, ids,
                                                    'newest'))
            kdir.menu('Sort by [B]popular[/B]', call(self.listing, 1, ids,
                                                     'trending'))
            kdir.menu('Sort by [B]top[/B]', call(self.listing, 1, ids,
                                                 'top'))

    def _play_stream(self, title, canon_url, id):
        stream_url = self.api.streamable(canon_url, id)['result']

        listitem = ListItem(label=title, path=stream_url['streaming_url'])
        xbmcplugin.setResolvedUrl(self.handle, True, listitem)
