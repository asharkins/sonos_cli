import pytest
from unittest.mock import Mock, patch
from soco import SoCo
import sonos
from sonos import func

@pytest.fixture()
def mock_speaker():
    mock = Mock()
    mock.player_name = 'Bedroom'
    mock.ip_address = '192.1.1.0'
    return mock


@patch.object(func, 'get_speaker')
def test_get_speaker(get_speaker, mock_speaker):

    get_speaker.return_value = mock_speaker
    result = func.get_speaker('Bedroom')
    assert result.player_name == 'Bedroom'


@patch.object(func, 'get_speaker')
def test_get_speaker_lowcase(get_speaker, mock_speaker):
    get_speaker.return_value = mock_speaker
    result = func.get_speaker('bedroom')
    assert result.player_name == 'Bedroom'

@patch.object(func, 'get_speaker')
def test_do_thing(mock_speaker):
    
    result = sonos.__main__.do_thing(None, None, None):
