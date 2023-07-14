import moviepy.editor

path = input('Введите путь до папки, где лежит видеофайл') + '\\'
name = input('Введите название видеофайла (с расширением)')
video = moviepy.editor.VideoFileClip(path + name)
audio = video.audio
name = name.split('.').pop(0)  # получение названия файла
audio.write_audiofile(f'{path}\\{name}.mp3')
