from libka import Plugin, call, PathArg
from libka.logs import log
from libka.menu import Menu, MenuItems
from libka.resources import Media, Resources

from xbmcgui import ListItem
import xbmcplugin

from .site import API


class Addon(Plugin):
    def __init__(self) -> None:
        super().__init__()
        self.api = API()

    MENU = Menu(view='addons', items=[
            Menu(title='Search', call='nop'),
            Menu(title='Featured', call=call('featured', 1)),
            Menu(title='Popculture', call='nop'),
            Menu(title='Artists', call='nop'),
            Menu(title='Education', call='nop'),
            Menu(title='Lifestyle', call='nop'),
            Menu(title='Spooky', call='nop'),
            Menu(title='Gaming', call='nop'),
            Menu(title='Tech', call='nop'),
            Menu(title='Comedy', call='nop'),
            Menu(title='Music', call='nop'),
            Menu(title='Sports', call='nop'),
            Menu(title='Universe', call='nop'),
            Menu(title='Finance', call='nop'),
            Menu(title='Spirituality', call='nop'),
            Menu(title='News', call='nop'),
            Menu(title='Docs', call='nop'),
            Menu(title='Rabbithole', call='nop')
        ])

    def home(self):
        self.menu()

    def nop(self):
        pass

    def get_art(self, response):
        landscape = response['value']['thumbnail']['url']
        return {
            'icon': self.media.image('icon'),
            'fanart': landscape
        }

    def featured(self, page: PathArg[int]):
        with self.directory(view='movies') as kdir:
            for feat in self.api.get_featured(page):
                kdir.play(feat["value"]["title"],
                          call(self._play_stream,
                               feat["value"]["title"],
                               feat['canonical_url'],
                               feat['meta']['creation_timestamp']),
                          art=self.get_art(feat))
            kdir.menu('Next Page', call(self.featured, page + 1))

    def _play_stream(self, title, canon_url, id):
        stream_url = self.api.streamable(canon_url, id)['result']

        listitem = ListItem(label=title, path=stream_url['streaming_url'])
        xbmcplugin.setResolvedUrl(self.handle, True, listitem)
