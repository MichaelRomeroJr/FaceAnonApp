## Face Anonymizer - FaceAnonApp v1.0
Blur faces from image and video files in `/data/files` folder.<br>

### Contents
Repo of the source files for the FaceAnonApp. <br>
`run.exe` file was created with [pyinstaller](https://pypi.org/project/pyinstaller/) command: `$ pyinstaller run.py --onefile` <br>
which creates the 1.64 GB run.exe file. <Br>
(for this method you would also have to download [crowdhuman_yolov5m.pt](https://drive.google.com/file/d/1gglIwqxaH2iTvy6lZlXuAcMpd_U0GCUb/view?usp=sharing) 
and place in same directory as `run.py`)<br>

### Useage
Google drive link of Folder contains working App (so you don't have to wrap this as an .exe yourself). 
1. Download the folder of the [FaceAnonApp Here](https://drive.google.com/file/d/1gskbA1EkMdQ2LZ7-f40dxMYGZqEfC_eD/view?usp=sharing)
2. Place images/videos you'd like to annomize in the `data/files` sub-folder 
3. Double click `run.exe` file <br>
  or open cmd terminal, cd to FaceAnonApp directory, and run `$ run.exe`. <br>

Result images will be in `/output/` and videos with sound will be in `/output/sound/`

### App Demo
Click image view Youtube video<br>
[<img src="https://i3.ytimg.com/vi/wRkt-qNl5Uk/maxresdefault.jpg" width="640" height="360" target="_blank">](https://www.youtube.com/watch?v=wRkt-qNl5Uk)<br>
Demo navigating through the FaceAnonApp Folder<br>
showing where to put the input videos<br>
how to launch the program<br>
and where the results are stored.
