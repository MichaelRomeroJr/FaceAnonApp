from pathlib import Path

from os import listdir
from os.path import isfile, join

""" add_audio() """
# from moviepy.editor import *
# import moviepy.editor as mp # because I already have VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.video.io.VideoFileClip import VideoFileClip

def files_in_folder(folder):
	files = []
	for f in listdir(folder): 
		if isfile(join(folder, f)):
			file_path = folder / f
			files.append(file_path)
	# return [f for f in listdir(folder) if isfile(join(folder, f))]
	return files


def add_audio(files, root_dir):
	print(f"processing audio ... ")
	for file in files:
		try:
			file_name = file.parts[-1]
			print(f"current file: {file_name}")
			# vid_input = mp.VideoFileClip(str(file)) # create video object of original vid file
			vid_input = VideoFileClip(str(file)) # create video object of original vid file

			audio_path = root_dir / f"output/audio/{file_name[:-3]}mp3"
			vid_input.audio.write_audiofile(str(audio_path)) # create audio file from original vid file

			### merge audio ###
			audio_input = AudioFileClip(str(audio_path)) # create audio object from saved audio file
			audio_comp = CompositeAudioClip([audio_input]) # add audio from mp3 AudioFileClip object
		
			vo = root_dir / "output" / file_name # video out
			vid_output = VideoFileClip(str(vo))
			vid_output.audio = audio_comp
			video_out_path = root_dir / "output/sound" / file_name # final video path
			vid_output.write_videofile(str(video_out_path))
		except Exception as e:
			print(f"file: {file}")
			print(f"error: \n{e}")

	return

