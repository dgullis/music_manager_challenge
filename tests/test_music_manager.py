from lib.music_manager import MusicManager
import pytest

"""
Given no additions
#see_tracks returns error message
"""
def test_no_additions_returns_error_message():
    music_manager = MusicManager()
    with pytest.raises(ValueError) as e:
        music_manager.see_tracks()
    assert str(e.value) == "No tracks added!"

"""
Given artist but no title
#add_track returns error message
"""

def test_empty_title_given():
    music_manager = MusicManager()
    with pytest.raises(ValueError) as e:
        music_manager.add_track("title fight", "") 
    assert str(e.value) == "Requires valid artist and title"

def test_no_title_given():
    music_manager = MusicManager()
    with pytest.raises(ValueError) as e:
        music_manager.add_track("title fight", None)
    error_message = str(e.value)
    print("hello", error_message) 
    assert str(e.value) == "Requires valid artist and title"

def test_empty_artist_given():
    music_manager = MusicManager()
    with pytest.raises(ValueError) as e:
        music_manager.add_track("", "like a ritual")
    assert str(e.value) == "Requires valid artist and title"

def test_no_artist_given():
    music_manager = MusicManager()
    with pytest.raises(ValueError) as e:
        music_manager.add_track("like a ritual")
    assert str(e.value) == "Requires valid artist and title"


"""
Given valid artist and title
#see_tracks returns that artist and title
"""

def test_artist_and_title_added_and_returned():
    music_manager = MusicManager()
    music_manager.add_track("title fight", "like a leaf")
    result = music_manager.see_tracks() 
    assert result == "title fight: like a leaf"

"""
Given two valid artists and titles
#see_tracks returns those artists and titles
"""

def test_two_artists_and_titles_returned():
    music_manager = MusicManager()
    music_manager.add_track("title fight", "like a leaf")
    music_manager.add_track("snail mail", "pristine")
    result = music_manager.see_tracks()
    assert result == "title fight: like a leaf. snail mail: pristine"

"""
Given title form artist already stored
#see_tracks retuns artist with multiple titles
"""

def test_add_return_artist_with_multiple_titles():
    music_manager = MusicManager()
    music_manager.add_track("title fight", "like a leaf")
    music_manager.add_track("title fight", "secret society")
    result = music_manager.see_tracks()
    assert result == "title fight: like a leaf, secret society"

"""
given multiple arists, multiple tracks, some tracks from same artist
#see_tracks retuns correct list
"""

def test_add_return_multiple_artists_and_titles():
    music_manager = MusicManager()
    music_manager.add_track("title fight", "like a leaf")
    music_manager.add_track("title fight", "secret society")
    music_manager.add_track("snail mail", "pristine")
    music_manager.add_track("funeral for a friend", "juneau")
    music_manager.add_track("mom jeans", "something sweet")
    result = music_manager.see_tracks()
    assert result == "title fight: like a leaf, secret society. snail mail: pristine. funeral for a friend: juneau. mom jeans: something sweet"



