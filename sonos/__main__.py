import click
from .func import get_speaker, perform_action, print_status, all_speakers, get_coordinator
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group()
def main(action):
    print('Sonos CLI')


@main.command()
def status():
    print_status()


@main.command()
@click.option('--all', '-a', is_flag=True, default=False, )
@click.option('--speaker', '-s', default='')
def play(speaker, all):
    do_thing(speaker, all, 'play')


@main.command()
@click.option('--all', '-a', is_flag=True, default=False, )
@click.option('--speaker', '-s', default='')
def stop(speaker, all):
    do_thing(speaker, all, 'stop')


def do_thing(speaker, all, func):
    if all:
        all_speakers(func)
    else:
        spkr = get_speaker(speaker)
        spkr = get_coordinator(spkr)
        perform_action(spkr, func)


if __name__ == '__main__':
    main()
