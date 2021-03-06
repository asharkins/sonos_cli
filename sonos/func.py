import soco


def get_speaker(speaker):
    zones = soco.discover()
    for zone in zones:
        if zone.player_name.lower() == speaker.lower():
            return zone


def all_speakers(action):
    zones = soco.discover()
    for zone in zones:
        if action == 'play':
            zone.play()
        elif action == 'stop':
            zone.stop()


def perform_action(speaker, action):
    print(f'Perform...')
    if action == '' or None:
        toggle_playback(speaker)
    if speaker is None:
        all_speakers(action)
    else:
        if action == 'play':
            speaker.play()
        elif action == 'stop':
            speaker.stop()


def toggle_playback(speaker):
    print('Toggle...')
    state = speaker.get_current_transport_info()
    status = state['current_transport_state']
    if status == 'PLAYING':
        speaker.stop()
    if status == 'PAUSED_PLAYBACK' or status == 'STOPPED':
        speaker.play()


def get_coordinator(speaker):
    print('Get coordinator...')
    return speaker.group.coordinator


def print_status():
    print('Status...')
    zones = soco.discover()
    for zone in zones:
        state = zone.get_current_transport_info()
        print(f"{zone.player_name} is {state['current_transport_state']}")
