# Real Time Speech Recognition for Nigerian Church Sermons
This is a research work that aims to improve the speech recognition of Nigerian speakers, streamlining to Biblical preachers.

## Approach:
- Data Collection: 
We adopted the community data-curation approach, where Christain volunteers offered to transcribe the recordings of sermons.
This exercise resulted to about 24 hours data, which is now open-sourced. 

- Speech Recognition Experiment:
Two pretrained models were experimented with:
  - NeMo QuartzNet
  - wav2vec2 XLS-R
  
After training on these models, their results were quite similar. However, the latter was more easier to deploy. wav2vec2 XLS-R has a test WER of 0.235. The model is pushed to the HuggingFace Hub and can be found [there](https://huggingface.co/sharonibejih/wav2vec2-large-xlsr-ng-en-sermon). 

Below is a snippet of the wav2vec2 XLS-R mode prediction version the actual text:
 
<img width="1365" alt="Screenshot 2022-09-28 at 15 51 03" src="https://user-images.githubusercontent.com/55222856/192811437-65f3a548-88fb-4098-88ae-63b5f90fbe1f.png">

`The model performs better on an actual church sermon (with some musical background sounds, like a typical church) than on a normal voice record.`

- Deployment:
The model is downloaded from the Hub and is used to transcribe real-time speech. This project is dockerized and deployed to a DockerHub.


### Citation:
The 24h Church sermon dataset can be found [here](https://drive.google.com/drive/folders/1d4FBNmr3fUFwvfovdeGi9Bz1uch2q2Ix?usp=sharing).

Please reference our [paper](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=6sZXvpAAAAAJ&citation_for_view=6sZXvpAAAAAJ:UeHWp8X0CEIC) if you make use of this data.
```
@inproceedings{
oyewusi2022tcnspeech,
title={{TCNS}peech: A Community-Curated Speech Corpus for Sermons},
author={Wuraola Fisayo Oyewusi and Sharon Ibejih and Soromfe Uzomah and Elizabeth Mawutin Joseph and Jon Cynthia and Folakunmi Ojemuyiwa and Benedicta Johnson-Onuigwe and Omolola Taiwo and Akintunde Akinpelumi and Olabisi Adesina and Ayodele Noutouglo and Adeola Adeleke Adeoba and Andrew Akoh and Chukwuemeka Nwachukwu and Opeyemi Agbabiaje and Itunu Falade and Olukemi Erhunmwunsee and Oluwatobiloba Dada and Ol{\'u}wat{\'o}bi David OSIBELUWO and Ehis Akene and Udim Akpan and Moira Amadi-Emina and Jaiyeola Marquis and Michael Senapon Bojerenu and Gbolahan Olumade and Oluwagbemi Lesi and Timothy Ezeh and Oluwadamilola Oguntoyinbo and Tosan Mogbeyiteren and Felicia Oresanya and Samuel Chika and Sodiq Akinjobi},
booktitle={3rd Workshop on African Natural Language Processing},
year={2022},
url={https://openreview.net/forum?id=r_-PYcf4LZc}
}
```
