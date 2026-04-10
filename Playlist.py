from Track_file import Track
import random
from enum import Enum


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
        else:   # если трек - послдений, то всключается первый трек
            self._current_index = 0


        return self.current_track()

    def display(self):

        headers = ["Название", "Длительность", "Жанр", "Рейтинг"]

        rows = []
        for track in self._tracks:
            minutes = track.duration // 60
            seconds = track.duration % 60
            duration_str = f"{minutes:02d}:{seconds:02d}"
            rating_str = f"{track.rating:.1f}"
            rows.append([track.name, duration_str, track.genre, rating_str])

        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(cell))

        def print_separator():
            print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

        print_separator()

        header_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
        print(header_line)
        print_separator()

        for row in rows:
            data_line = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row)) + " |"
            print(data_line)
        print_separator()

