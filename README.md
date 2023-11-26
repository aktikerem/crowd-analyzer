
# crowd-analyzer

python tool for counting and analyzing large crowds from a video file or a live source using yolov8 models

## Examples

example below is from a tedx conference with moderate accuracy


![screenshotone](https://github.com/aktikerem/crowd-analyzer/assets/64261277/6c8a8176-8054-4b82-89b3-934cdd428409)


here is another example from a big music concert


![screenshot2](https://github.com/aktikerem/crowd-analyzer/assets/64261277/5de1fcff-224c-4e6a-9bbf-f8384243f885)

* manycam logo in provided images is from my virtural camera software to demonstrate live video source and wont be present.


## Installation/Setup

* first clone repo to your folder
```
$ git clone https://github.com/aktikerem/crowd-analyzer.git
```
* go inside the repo and install requirements
```
$ pip install -r requirements.txt
```

## Finaly unzip the .pt file from the model folder according to images below

* first go to model folder

![Desktop Screenshot 2023 11 26 - 21 56 02 38(1)](https://github.com/aktikerem/crowd-analyzer/assets/64261277/eb0ba7e1-7090-42a1-b9aa-0b377e8513c4)

* right click any of them and unzip the splited files
  
![Desktop Screenshot 2023 11 26 - 21 56 20 44](https://github.com/aktikerem/crowd-analyzer/assets/64261277/b9af3fa5-55be-4dae-ac53-fc1ddec8a4a1)

* then move the resulting file back to the repo
  
![Desktop Screenshot 2023 11 26 - 22 03 47 05](https://github.com/aktikerem/crowd-analyzer/assets/64261277/21eefc95-4659-4ea2-ac5c-a02811dfc7fd)

## Execute the program

if u succsesfully complete the steps on top u should be able to run main.py file 
```
$ python main.py
```

and that's it! GUI will open with the first detected video input device in the system.
Please note that this is a personal project, and I wouldn't recommend it for professional use at the moment due to several issues.
