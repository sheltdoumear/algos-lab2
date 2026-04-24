from Track_file import Track
import random
from enum import Enum
from tabulate import tabulate



class RepeatMode(Enum):
    NONE = "none"
    ONE = "one"
    ALL = "all"


class Playlist:
    def __init__(self, name):
        self.name = name
        self._tracks = []
        self._current_index = 0
        self.repeat_mode = RepeatMode.NONE



    def add_track(self, track: Track):
        self._tracks.append(track)



    def delete_track(self, track: Track):
        if track in self._tracks:
            self._tracks.remove(track)
            if self._current_index >= len(self._tracks):
                self._current_index = max(0, len(self._tracks) - 1)
        else:
            print("There is no such track in the playlist")



    # удаление трека по имени
    # def delete_track_by_name(self, track_name):
    #     deleted = False
    #     for track in self._tracks:
    #         if track_name == track.name:
    #             self._tracks.remove(track)
    #             deleted = True
    #
    #     if (deleted):
    #         print(f"Track {track_name} deleted")
    #     else:
    #         print("There is no such track in the playlist")

    def shuffle_playlist(self):
        random.shuffle(self._tracks)
        self._current_index = 0

    # получаем текущий трек (возвращает экземпляр Track)
    def current_track(self):
        if self._tracks and 0 <= self._current_index < len(self._tracks):
            return self._tracks[self._current_index]
        return None

    # получаем следующий трек
    def next_track(self):

        if self.repeat_mode == RepeatMode.ONE:
            self.repeat_mode = RepeatMode.NONE
            return self.current_track()

        next_index = self._current_index + 1
        if next_index < len(self._tracks):
            self._current_index = next_index
        elif self.repeat_mode == RepeatMode.ALL:
            self._current_index = 0
        else:   # если трек - послдений, то включается первый трек
            self._current_index = 0


        return self.current_track()

    def display(self):
        headers = ["Название", "Длительность", "Жанр", "Рейтинг"]

        rows = []
        for track in self._tracks:
            minutes = track.duration // 60
            seconds = track.duration % 60
            duration_min_sec = f"{minutes:02d}:{seconds:02d}"
            rating = f"{track.rating:.1f}"
            rows.append([track.name, duration_min_sec, track.genre, rating])

        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def find_tracks_in_time_range(self, n, min_duration, max_duration):
        result = []
        for track in self._tracks:
            if min_duration <= track.duration <= max_duration:
                result.append(track.name)
                if len(result) == n:
                    break
        return result




