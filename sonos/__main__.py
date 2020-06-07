import sys
import soco
import click
from .func import get_speaker, perform_action, print_status
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--speaker', '-s', default='', help='Default speaker.')
@click.option('--action', '-a', default='', help='Default action.')
def main(speaker, action):
    print_status()
    selected_speaker = get_speaker(speaker)
    perform_action(selected_speaker, action)



if __name__ == '__main__':
    main()
