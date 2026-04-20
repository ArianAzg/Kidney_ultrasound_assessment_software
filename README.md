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
    <img src="https://img.shields.io/badge/Tools-Numpy-informational?style=flat&logo=Numpy&color=FAC205">
  </a>
  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Tools-OpenCV-informational?style=flat&logo=opencv&color=2bbc8a">
  </a>
  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Tools-Tkinter-informational?style=flat&logo=python&color=DC143C">
  </a>

  <a href="https://github.com/ankitwasankar/mftool-java">
    <img src="https://img.shields.io/badge/Operating System-Windows 10 & 11-informational?style=flat&logo=Windows10&color=E6DAA6">
  </a>
</h1>

## Introduction 
#### Backbone components for processing imaging data for this study 
The kidney ultrasound scans saved on ultrasound machine in _**DICOM**_ format were converted into a common video format, i.e., _**AVI**_. For each subject who participated in the study, the best scans for each kidney were selected for both B-mode and contrast enhanced imaging modalities. Overall, **116** scans belonging to 15 subjects were selected and compiled for the evaluation phase of this study. As part of the pre-processing steps, the videos were categorized into “B-mode only” and “B-mode + contrast enhanced” folders separately. The naming conventions for each folder of the study were then changed and randomly generated with an associated look-up table in order to keep the readers fully-blind and unbiased towards each set of images in the evaluation phase. 
#### Evaluation phase
Three independent radiology board certified readers were asked to analyze the dataset. A user-friendly graphical user interface (GUI) was developed and distributed to the readers. The GUI was developed with the Tkinter package of Python and packaged as a standalone executable software for Windows users. Below, the step-by-step installation is provided. As part of the assessment phase of the dataset, a series of questions were given to the software developer by the project lead to be incorporated into the GUI. Additionally, the program is capable of displaying several videos at the same time to help the readers confirm their assessments. For each individual scan assessment, the provided answers were saved into one single _**CSV**_ file. The lines in the _**CSV**_ files were then assessed for agreement between the readers on different aspects. A summary of the study pipeline is shown in Figure 1.

<p align="center">
<img width="100%" src="https://github.com/user-attachments/assets/134a0a01-8401-4e34-9dea-da9cf5eaf8c4"></a>
    <br>
    <em>Figure 1. Processing steps in analyzing the kidney ultrasound scans.</em>
</p>

## Installation 
The software requires `Python >= 3.10` for best performance. Create an environment in your `Anaconda` using the following command: 

    conda create --name VHL_software python==3.10

All the required Python packages can be installed using the following command in the new environment (i.e., VHL_software):

    pip install -r requirements.txt

## Dataset Organization
For this study, the dataset is organized in the following structure (`LT: Left kidney`, `RT: Right kidney`, `B: B-mode`, `C: Contrast`, `LN: Longitudinal view`, `TR: Transverse view`):

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
Initial `Anaconda Prompt` and activate the `VHL_software` environment. Download this repository and redirect the current working directory to the location of the `VHL_Study_Program.py` file. Run the program with the following command: 

    python VHL_Study_Program.py

The main page of the sotware should pop up, as shown in Figure 2:

<p align="center">
<img width="50%" src="https://github.com/ArianAzg/Kidney_ultrasound_assessment_software/assets/48659018/7d08adf3-6daa-49fb-abf4-c1bd44a77be1"></a>
    <br>
    <em>Figure 2. Homepage of the VHL study software.</em>
</p>

First, click on the `Select a folder` button and in the newly opened window, one of the data folders listed above should be selected, as shown in Figure 3:

<p align="center">
<img width="70%" src="https://github.com/ArianAzg/Kidney_ultrasound_assessment_software/assets/48659018/2098449d-89f3-41bf-8c6b-23321a936d4c"></a>
    <br>
    <em>Figure 3. Selection of a desired folder to start the assessment.</em>
</p>

After this step, click on the `Show files` button to display the available videos to process. As you may have noticed, the list box will be updated with the available scans, shown in Figure 4:

<p align="center">
<img width="50%" src="https://github.com/ArianAzg/Kidney_ultrasound_assessment_software/assets/48659018/0bbe511e-1351-4c02-a6e5-857edc31580d"></a>
    <br>
    <em>Figure 4. Available videos to assess.</em>
</p>
From this list, select the video to assess by `double-clicking` on the video name and click on the `Show series` button to play the video in a new window, as shown in Figure 5. Please note that the questions only need to be answered once for each kidney and for the highlighted video name in the list (highlighted as **_green_**). The reader can open the other un-highlighted videos at the same time as supportive videos to help you make their decision. Please note that a `sliding bar` is integrated in the video display window where the reader can swipe in time for better analysis.

<p align="center">
<img width="90%" src="https://github.com/ArianAzg/Kidney_ultrasound_assessment_software/assets/48659018/1ae202d8-6e9f-4ee2-812b-b5bc000034ae"></a>
    <br>
    <em>Figure 5. Displaying the selected video with sliding bar for swinging in time.</em>
</p>

Next, the reader should answer the questions which appear under the `Show series` button. Once the entire assessment is complete, the reader should click on `Save assessment` button. This step saves all the human reader input in an associated CSV file, named “FinalScores.csv” located in the current working directory. After each successful assessment, a new message will be shown on the screen that displays `Please select the new video!`. At this point, another highlighted video in the list box should be selected for assessment or if all the kidneys in that folder have been assessed, then it is time to select the next folder.


## Citation 

For any utilization of the code content of this repository, the following paper needs to get cited by the user:
> 1. A. Azarang, et al., Feasibility of CEUS as a Screening Tool for Patients at High Risk for Kidney Malignancies (in revision)

## License

This project is licensed under the [MIT License](http://opensource.org/licenses/MIT).

## Contact 

For bug reports and feature requests please contact us at: arianazaang@gmail.com & aazarang@unc.edu. 
