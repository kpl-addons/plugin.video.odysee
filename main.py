import sys  # noqa
from resources.lib.addon import Addon
from libka.logs import log


if __name__ == '__main__':
    log(f' === [ODYSEE] === : {sys.argv}')

    # Create and run plugin.
    Addon().run()
