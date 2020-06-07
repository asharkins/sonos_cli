import click
from .func import get_speaker, perform_action, print_status, all_speakers, get_coordinator
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group()
@click.option('--action', '-a', default='', help='Default action.')
def main(action):
    print('Sonos CLI')


@main.command()
def stop_all():
    all_speakers('stop')


@main.command()
def status():
    print_status()


@main.command()
@click.option('--speaker', '-s', default='',
              help='Default speaker.')
def play(speaker):
    selected_speaker = get_speaker(speaker)
    perform_action(selected_speaker, 'play')


@main.command()
@click.option('--speaker', '-s', default='',
              help='Default speaker.')
def stop(speaker):
    selected_speaker = get_speaker(speaker)
    selected_speaker = get_coordinator(selected_speaker)
    perform_action(selected_speaker, 'stop')


if __name__ == '__main__':
    main()
