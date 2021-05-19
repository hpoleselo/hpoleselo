from moviepy.editor import *
clip = (VideoFileClip("./hello-therefolks.mkv"))
clip.write_gif("output.gif")