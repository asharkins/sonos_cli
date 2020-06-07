import sys
import soco
import click
from .speaker import Speaker
from .func import get_speaker, stop_speaker


@click.command()
@click.option('--speaker', default='Living Room', help='Default speaker.')
@click.option('--action', default='', help='Default action.')
def main(speaker, action):
    selected_speaker = get_speaker(speaker)
    import ipdb
    ipdb.set_trace()
    stop_speaker(selected_speaker)


if __name__ == '__main__':
    main()
