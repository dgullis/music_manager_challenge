class MusicManager():
    
    # initialise an empty dictionary to manage tracks
    def __init__(self):
        self.music_library = {}

    # adds artist and title as keys with values to dictionary
    # if title or artist is an empty string return error message
    # if artist already in dictonary add title to value for that artists key
    def add_track(self, artist, title):
        print("hello, i'm here")
        if not artist or not title:
            
            raise ValueError("Requires valid artist and title")
        
        if artist not in self.music_library:
            self.music_library[artist] = title
        else:
            self.music_library[artist] += f", {title}"

    # returns a list of artists and titles as a string with basic formatting
    # if no tracks have been added returns error message
    def see_tracks(self):
        if not self.music_library:
            raise ValueError("No tracks added!")
        
        list_of_entries = (f"{artist}: {titles}" for artist, titles in self.music_library.items())
        list_of_entries_string = ". ".join(list_of_entries)
        return list_of_entries_string
            
            
    
