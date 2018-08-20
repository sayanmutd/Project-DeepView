# deepView (sandbox demo v0.0.1)
## -harnessing the preventive power of cctv networks 

![](https://raw.githubusercontent.com/RishavR/deepView/master/Images/project_Deep_View.png)


Project deepView uses localized CNN, Part Affinity Field based sekeleton generation and casule CNN (ongoing) to **classify & label real-time CCTV footage** as 'Violent' or 'Non-Violent' - acting as an interface that can **detect crime in real-time** and alert law enforcement authorities. 

## Latest release: 
please check out our [releases section](https://github.com/rishavr/deepview/releases) to download the v0.0.1 release of the demo. 

## Full source: 
entire source is present in the release itself apart from the classifier and deeppose code. full code to be uploaded soon in this repo. 

## Dependencies: 

the following dependencies are necessary for the demo to work - 
1) python3 
2) scikit learn 
3) pandas 
4) pickle 
5) g++ 

we also recommend downloading the full anaconda library as it contains all the above libraries. 

## System Requirements: 

1) demo only works in windows os.
2) minimum 6 gb of free ram. 
3) minimum nvidia gtx or higher (cuda enabled) graphics. 


## How To Run: 
```
1) run models/models.bat 
2) run gui.py 
```
![Graphical User Interface Demo](https://raw.githubusercontent.com/RishavR/deepView/master/Images/rsz_1screenshot_from_2018-08-19_19-21-31.png)
## Troubleshoot Help: 
email: rishav_201500204@smit.smu.edu.in

## References: 
```
[1] Yun, Kiwon, et al. "Two-person interaction detection using body-pose features and multiple instance learning." Computer Vision and Pattern Recognition Workshops (CVPRW), 2012 IEEE Computer Society Conference on. IEEE, 2012.

[2]
@inproceedings{cao2017realtime,
  author = {Zhe Cao and Tomas Simon and Shih-En Wei and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields},
  year = {2017}
}
[3]
@inproceedings{simon2017hand,
  author = {Tomas Simon and Hanbyul Joo and Iain Matthews and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Hand Keypoint Detection in Single Images using Multiview Bootstrapping},
  year = {2017}
}
[4]
@inproceedings{wei2016cpm,
  author = {Shih-En Wei and Varun Ramakrishna and Takeo Kanade and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Convolutional pose machines},
  year = {2016}
}
```
![Graphical User Interface Demo](https://raw.githubusercontent.com/RishavR/deepView/master/Images/collage.jpg)
