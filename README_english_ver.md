# DANeS - Open-source E-newspaper dataset
![12613](https://user-images.githubusercontent.com/94349957/143620522-2b417ece-2482-4475-a261-120af096cb0d.jpg)
*<sub>Source: <a href="https://www.freepik.com/vectors/technology">Technology vector created by macrovector - www.freepik.com</a>.</sub>*


DANeS is an open-source E-newspaper dataset by collaboration between DATASET .JSC (dataset.vn) and AIV Group (aivgroup.vn) that contains over 600.000 online paper's articles. The articles are gathered from a number of Vietnamese Publishing Houses such as: tuoitre.vn, baobinhduong.vn, baoquangbinh.vn, kinhtechungkhoan.vn, doanhnghiep.vn, vnexpress.net, ...

We hope to support the community by providing a multi-purpose set of raw data for different subjects (students, developers, companies, …). So if you create something with this dataset, please share with us through our e-mail: info@dataset.vn



<!-- TABLE OF CONTENTS -->
## Table of Contents
  <ol>
    <li><a href="#folder-tree">Folder Tree</a></li>
    <li><a href="#data-format">Data format</a>
    <li><a href="#labeling-process">Labeling process</a></li>
    <li><a href="#reviewing-process">Reviewing process</a></li>
    <li><a href="#updating-process">Updating process</a></li>
    <li><a href="#license-of-annotated-dataset">License of annotated dataset</a></li>
    <li><a href="#about-us">About-us</a></li>
  </ol>
</details>

## Folder Tree
	DANeS
	  |
	  |____README.md
	  |
	  |____README_english_ver.md
	  |
	  |____raw_data
	  |	   |____ DANeS_batch_#1.json
	  |	   |____ DANeS_batch_#2.json
	  |	   |____ DANeS_batch_#3.json
	  |	   |____ DANeS_batch_#4.json
	  |	   |____ DANeS_batch_#5.json
	  |	   |____ DANeS_batch_#6.json
	  |	   |____ DANeS_batch_#7.json
	  |	   |____ DANeS_batch_#8.json
	  |	   |____ README.md
	  |
	  |____annotated_data
	  |	   |____ #contains annotated data
	  |
	  |____model
		   |____ Train_opensource.py
		   |____ README.md
		   |____ README_english_ver.md
		   |____ LICENSE
 
## Data format
The raw dataset is stored in raw_data folder with [`.json`](https://www.json.org) format and has been divided into 8 batches. Each batch has an array that contains many json and each json is a record of the dataset. Here’s the example of each record's format:

| Key          | Type                   | Description                                  |
| ------------ | -----------------------| -------------------------------------------- |
| text         | string                 | title of the digital news                    |
| meta         | json                   | metadata of the digital news                 |
| uri          | string                 | link to the digital news                     |
| description  | string                 | description of the digital news              |

Example for a record of dataset:
```javascript
{
        "text": "Ba ra đi vào ngày nhận điểm thi, nữ sinh được hỗ trợ học phí",
        "meta": {
            		"description": "Ngày nhận được tin đỗ đại học cũng là lúc bố mất vì Covid-19, L.A dường như gục ngã. Thế nhưng, bên cạnh em đã có các mạnh thường quân hỏi han, hỗ trợ về kinh tế.",
            		"uri": "https://yan.vn/ba-ra-di-vao-ngay-nhan-diem-thi-nu-sinh-duoc-ho-tro-hoc-phi-277328.html"
        	}
}
``` 
 
## Labeling process
- Log in:

![DANeS redo 2 2](https://user-images.githubusercontent.com/94349957/145561486-4058dffd-63a6-4d2e-bac7-0472e90f8973.gif)

- Annotating:

	+ The article should be classified under one out of three sentiment: Negative, Positive and Neutral. 
	+ The article will then be classified by 23 topics: World, Politics, Economics, Sports, Cultures, Entertainment,Technology, Science, Education, Daily life, Regulations, Real estate, Social, Traffic, Environment, Stock market, Covid-19, Breaking news, Game, Movies, Health, Travel, Unidentified. Each article can carry numerous relevant and suitable topics. 

![DANeS 2](https://user-images.githubusercontent.com/94349957/144266113-511ad9c8-6f06-42a6-84be-dd23f7f2b9fa.gif)

## Reviewing process

The admin or the owner of the project will select qualified reviewers based on their attitude and performance. Reviewing process contains two main phases: cross validation and project reviewing.
  - The person who is assigned to cross validating will be given 20% of the annotated records from other annotators. This person will also be in charge of re-correcting the mislabeled records.
  - After the cross validation phase, the person who is assigned to review the project will randomly pick 20 - 50% of the total annotated records. Records that are not meet the given quality can either be:
       + Re-corrected by the project reviewer.
       + Re-assigned and re-corrected by the formal annotator.

## Updating process

- The raw data is expected to be fully uploaded at one time.

- The annotated records are expected to be updated once a month to official repository of DANeS (https://github.com/dataset-vn/DANeS)


## License of annotated dataset

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Giấy phép Creative Commons " style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
The annotated dataset of <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/dataset-vn/DANeS" property="cc:attributionName" rel="cc:attributionURL">DANeS</a> is licensed under <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

This license lets others distribute, remix, tweak, and build upon your work, even commercially, as long as they credit you for the original creation. This is the most accommodating of licenses offered. Recommended for maximum dissemination and use of licensed materials.

If you want to cite our dataset, please use the following:
```javascript
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Giấy phép Creative Commons " style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
The annotated dataset of <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/dataset-vn/DANeS" property="cc:attributionName" rel="cc:attributionURL">DANeS</a> is licensed under <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
```

## About us

### DATASET .JSC - (+84) 98 442 0826 - info@dataset.vn

Dataset’s mission is to support individuals and organizations with data collecting and data processing services by providing tools that simplify and enhance the efficiency of the processes. With the large and professional workers system, Dataset aspires to provide partners with a comprehensive and quality solution, suitable with the characteristics of the technology market.

Website: [Dataset.vn](http://dataset.vn)

LinkedIn: [Dataset.vn - Data Crowdsourcing Platform](https://www.linkedin.com/company/dataset-vn/about/)

Facebook: [Dataset.vn - Data Crowdsourcing Platform](https://www.facebook.com/dataset.vn)

### AIV Group - (+84) 931 458 189 - marketing@aivgroup.vn

AIV Group aims to apply advanced technologies, especially Artificial Intelligence (AI), Cloud Computing, Big Data, … to digitize, modernize the long-established processes of information production and consumption in Viet Nam society. At the same time, we are working on solutions that solve new problems arising in the field of communication that relate to technology’s problems such as: fake news, images, videos are automatically cut and merged ..

Website: [AIV Group](https://aivgroup.vn/)

Facebook: [AIV Group](https://www.facebook.com/aivgroup.jsc/)

