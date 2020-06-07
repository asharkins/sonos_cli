import soco
from soco import SoCo


def get_speaker(speaker):
    zone_list = list(soco.discover())
    for zone in zone_list:
        if zone.player_name == speaker:
            return zone

def all_speakers(action):
    zones = list(soco.discover())
    for zone in zones:
        if action == 'play':  zone.play()
        elif action == 'stop':  zone.stop()
                
def perform_action(speaker, action):
    print(f'Perform...')
    if action == '':
        toggle_playback(speaker)
    if speaker is None:
        all_speakers(action)
    else:
        if action == 'play':  speaker.play()
        elif action == 'stop':  speaker.stop()

def toggle_playback(speaker):
    print('Toggle...')
    state = speaker.get_current_transport_info()['current_transport_state']
    if state == 'PLAYING':
        speaker.stop()
    if state == 'PAUSED_PLAYBACK' or state == 'STOPPED':
        speaker.play()


def get_coordinator(speaker):
    print('Get coordinator...')
    return speaker.get_group_coordinator

def print_status():
    print('Status...')
    zones = list(soco.discover())
    for zone in zones:
        state = zone.get_current_transport_info()
        print(f"{zone.player_name} is {state['current_transport_state']}")

