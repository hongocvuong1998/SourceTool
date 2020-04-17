from moviepy.video.io.VideoFileClip import VideoFileClip

input_video_path = "/home/vuonghn/my_data/study/toeic/video_lectures/KENHTOEIC/GIAI_DE_TOEIC_PART_1/Bai1.mp4"
output_video_path = '/home/vuonghn/my_data/te.mp4'

with VideoFileClip(input_video_path) as video:
    new = video.subclip(10, 20)
    new.write_videofile(output_video_path, audio_codec='aac')