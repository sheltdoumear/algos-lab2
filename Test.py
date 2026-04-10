from Playlist import Playlist
from Playlist import RepeatMode
from Track_file import Track

playlist = Playlist("My first playlist")
track_1 = Track("Track 1", 230, "hip-hop", 4.7)
track_2 = Track("Track 2", 164, "rock", 4.9)
track_3 = Track("Track 3", 189, "jazz", 3.8)
playlist.add_track(track_1)
playlist.add_track(track_2)
playlist.add_track(track_3)

playlist.display()

print(playlist.current_track().name)  # вернет имя первого добавленого трека
print(playlist.next_track().duration) # вернет продолжительность второго добавленого трека
print(playlist.current_track().genre) # вернет жанр второго добавленого трека
print(playlist.next_track().rating) # вернет рейтинг третьего  добавленого трека
print(playlist.next_track().rating)# вернет рейгинт первого добавленого трека, тк когда мы берем  next_track()
# от последнего плейлист начнется сначала, те current_track будет первый трек в плейлисте


playlist.shuffle_playlist() # перемешиываем

print(playlist.current_track().name, "\n") # первый трек в перемешанном плейлисте

playlist.repeat_mode = RepeatMode.ONE  # вклчюаем повтор
print(playlist.current_track().name) # трек играет первый раз
print(playlist.next_track().name)# второй раз
print(playlist.next_track().name, "\n")# уже следующий трек



playlist.repeat_mode = RepeatMode.ALL


playlist.delete_track(track_2)  #удаляем второй трек
playlist.display()


