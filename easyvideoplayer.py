{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting opencv-python\n",
      "  Downloading opencv_python-4.5.3.56-cp38-cp38-macosx_10_15_x86_64.whl (42.6 MB)\n",
      "\u001b[K     |████████████████████████████████| 42.6 MB 58 kB/s  eta 0:00:011    |███████████                     | 14.5 MB 8.8 MB/s eta 0:00:04     |████████████████████▉           | 27.8 MB 18.7 MB/s eta 0:00:01     |██████████████████████▏         | 29.5 MB 18.7 MB/s eta 0:00:01\n",
      "\u001b[?25hRequirement already satisfied: numpy>=1.17.3 in /Users/ijcm122/opt/anaconda3/lib/python3.8/site-packages (from opencv-python) (1.19.2)\n",
      "Installing collected packages: opencv-python\n",
      "Successfully installed opencv-python-4.5.3.56\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install opencv-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting ffpyplayer\n",
      "  Downloading ffpyplayer-4.3.2-cp38-cp38-macosx_10_9_x86_64.macosx_10_9_intel.macosx_10_10_intel.macosx_10_10_x86_64.whl (26.9 MB)\n",
      "\u001b[K     |████████████████████████████████| 26.9 MB 3.6 MB/s eta 0:00:01\n",
      "\u001b[?25hInstalling collected packages: ffpyplayer\n",
      "Successfully installed ffpyplayer-4.3.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install ffpyplayer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import os\n",
    "from pathlib import Path\n",
    "from ffpyplayer.player import MediaPlayer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# User input for the name of the image file.\n",
    "video_name = input(\"Name of the video file that you want to play:    \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# User input for the path of the image file.\n",
    "video_directory_guess = input(\"Directory that may contain the video:    \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This function finds your file. If you don't know the directory just type '/'\n",
    "def find_the_video(file_name, directory_name):\n",
    "    files_found = []\n",
    "    for path, subdirs, files in os.walk(directory_name):\n",
    "        for name in files:\n",
    "            if(file_name == name):\n",
    "                file_path = os.path.join(path, name)\n",
    "                files_found.append(file_path)\n",
    "\n",
    "    print(files_found)\n",
    "    return files_found[0]  # Return the path.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize the path of the image file.\n",
    "video_directory = Path(find_the_video(video_name, video_directory_guess))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize the parent directory of the image path.\n",
    "new_working_directory = video_directory.parent\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Change the working directory of the script.\n",
    "os.chdir(new_working_directory)\n",
    "\n",
    "\n",
    "video_path = find_the_video(video_name, video_directory_guess)\n",
    "\n",
    "\n",
    "def PlayVideo(video_path):\n",
    "\n",
    "    video = cv2.VideoCapture(video_path)\n",
    "    player = MediaPlayer(video_path)\n",
    "\n",
    "    while True:\n",
    "        grabbed, frame = video.read()\n",
    "        audio_frame, val = player.get_frame()\n",
    "        if not grabbed:\n",
    "            print(\"End of video\")\n",
    "            break\n",
    "        if cv2.waitKey(28) & 0xFF == ord(\"q\"):\n",
    "            break\n",
    "        cv2.imshow(\"Video\", frame)\n",
    "        if val != 'eof' and audio_frame is not None:\n",
    "            img, t = audio_frame\n",
    "    video.release()\n",
    "    cv2.destroyAllWindows()\n",
    "\n",
    "\n",
    "PlayVideo(video_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
