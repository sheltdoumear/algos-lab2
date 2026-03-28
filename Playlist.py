import Track
import random

class Playlist:
    def __init__(self, name):
        self.name = name
        self._tracks = list[Track]



    def add_track(self, track: Track):
        self._tracks.append(track)



    def delete_track(self, track: Track):
        if track in self._tracks:
            self._tracks.remove(track)
        else:
            print("There is no such track in the playlist")



    # удаление трека по имени
    def delete_track_by_name(self, track_name):
        deleted = False
        for track in self._tracks:
            if track_name == track.name:
                self._tracks.remove(track)
                deleted = True

        if (deleted):
            print(f"Track {track_name} deleted")
        else:
            print("There is no such track in the playlist")

    def shuffle_playlist(self):
        random.shuffle(self._tracks)


