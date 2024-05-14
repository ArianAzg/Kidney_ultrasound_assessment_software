# Kidney Ultrasound Assessment Software

<h1 align="center">
  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://github.com/ArianAzg/Kidney_ultrasound_assessment_software/assets/48659018/60e8896d-4e0c-44ca-b255-97cc1b5e9591">
  </a>
</h1>
<h1 align="center">
  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Language-Python 3.10-informational?style=flat&logo=Python&color=2bbc8a">
  </a>
  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Tools-Numpy-informational?style=flat&logo=Numpy&color=ffde57">
  </a>
  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Tools-OpenCV-informational?style=flat&logo=#5C3EE8&color=2bbc8a">
  </a>
  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Tools-Tkinter-informational?style=flat&logo=Tkinter&color=ff0000">
  </a>

  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Operating System-Windows 10-informational?style=flat&logo=#0078D6&color=2bbc8a">
  </a>


</h1>

## Introduction 
First, the backbone components for processing VHL study data will be explained. The kidney ultrasound scans saved on ultrasound machine in _**DICOM**_ format first converted into a common video format, i.e., _**AVI**_. For each subject participated in the study, the best scans for each kidney were selected for both B-mode and contrast enhanced imaging modalities. Overall, **116** scans were selected and compiled for the evaluation phase of this study belonging to 15 subjects. As part of the pre-processing steps, the videos were categorized into “B-mode only” and “B-mode + contrast enhanced” folders separately. It is due to the study protocol to evaluate the data in this format. The naming conventions for each folder of the study were then changed and randomly generated with an associated look-up table. This part is a requirement of the evaluation phase to keep the readers fully-blind and unbiased towards each subject. Three independent radiologist readers were asked to analyze the dataset. A user-friendly graphical user interface (GUI) was developed and distributed to the readers for more reliable and faster assessment of the dataset. The GUI was developed with the Tkinter package of Python and packaged as a standalone executable software for Windows users. Below, the step-by-step installation is provided. As part of the assessment phase of the dataset, a series of important questions were given to the software developer by the project lead to be incorporated into the GUI. Apart from that, the program is capable of displaying several videos at the same time to help the readers confirm their assessments. For the outcome of each individual scan assessment, the provided answers were saved into one single _**CSV**_ file. The lines in the _**CSV**_ files were then assessed for agreement between the readers at different aspects. Summary of study pipeline is shown in Figure 1.

<p align="center">
<img width="100%" src="https://github.com/ArianAzg/Kidney_ultrasound_assessment_software/assets/48659018/f8ca5b51-1fa5-4f1c-a4eb-192bd75a6044"></a>
    <br>
    <em>Figure 1. Processing steps in analysis of kidney ultrasound scans.</em>
</p>

## Installation 
The software requires `Python >= 3.10` for best performance. Create an environment in your `Anaconda` using the following command: 

    conda create --name VHL_software python==3.10

All the required Python packages can be installed using the following command in the new environment (i.e., VHL_software):

    pip install -r requirements.txt

## Dataset Organization
For this study, the dataset is organized in the following structure (`LT: Left kidney`, `RT: Right kidney`, `B: B-mode`, `C: Contrast`, `LN: Longitudinal view`, `TR: Transverese view`):

```
├── VHL Study Recordings
|   ├── 0YZ
|   |   ├── LT-B-LN, LT-B-TR, RT-B-LN, RT-B-TR
|   ├── 1C0
|   |   ├── LT-B-LN, LT-B-TR, RT-B-LN, RT-B-TR, LT-C-LN, LT-C-TR, RT-C-LN, RT-C-TR
|   ├── AA0
|   |   ├── LT-B-LN, LT-B-TR, RT-B-LN, RT-B-TR
|   ├── BBX
|   |   ├── LT-B-LN, LT-B-TR, RT-B-LN, RT-B-TR
.
.
.
|   ├── ZYX
|   |   ├── LT-B-LN, LT-B-TR, RT-B-LN, RT-B-TR, LT-C-LN, LT-C-TR, RT-C-LN, RT-C-TR
```
## How to Run?
