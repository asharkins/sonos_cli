import soco
from .speaker import Speaker
from soco import SoCo


def get_speaker(speaker):
    zone_list = list(soco.discover())
    for zone in zone_list:
        if zone.player_name == speaker:
            print(f'selected_speaker :: {zone.player_name}')
            return zone


def stop_speaker(speaker):
    speaker.stop()


def get_coordinator(speaker):
