# DANeS - Open-source E-newspaper dataset
![12613](https://user-images.githubusercontent.com/94349957/143620522-2b417ece-2482-4475-a261-120af096cb0d.jpg)
*<sub>Source: <a href="https://www.freepik.com/vectors/technology">Technology vector created by macrovector - www.freepik.com</a>.</sub>*


DANeS is an open-source E-newspaper dataset by collaboration between DATASET .JSC (dataset.vn) and AIV Group (aivgroup.vn) that contains over 600.000 online papers’ articles. The articles are gathered from a number of Vietnamese Publishing Houses such as: tuoitre.vn, baobinhduong.vn, baoquangbinh.vn, kinhtechungkhoan.vn, doanhnghiep.vn, vnexpress.net, ...

We hope to support the community by providing a multi-purpose set of raw data for different subjects (students, developers, companies, …). So if you create something with this dataset, please share with us through our e-mail: info@dataset.vn



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#data-format">Data format</a>
    <li><a href="#labeling-process">Labeling process</a></li>
    <li><a href="#reviewing-process">Reviewing process</a></li>
    <li><a href="#updating-process">Updating process</a></li>
    <li><a href="#license-of-annotated-dataset">License of annotated dataset</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Data format
The dataset is stored in [`.json`](https://www.json.org) format and has been divided into multiple batches. Here’s the example of each record's format:

| Key          | Type                   | Description                                  |
| ------------ | -----------------------| -------------------------------------------- |
| title        | string                 | title of the digital news                    |
| url          | string                 | link to the digital news                     |
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

- The article should be classified under one out of three sentiment: Negative, Positive and Neutral. 
	
- The article will then be classified by topics: (em đính các topics sau ạ). Each article can carry numerous relevant and suitable topics. 

## Reviewing process

- 20% of the annotated records will be assigned to different annotator to re-annotate and compare with the original version.

- Quality Assurance members will randomly check 20-50% of the total annotated records.

## Updating process

- The raw data is expected to be fully uploaded at one time.

- The annotated records are expected to be updated once a month to official repository of DANeS (https://github.com/dataset-vn/DANeS)


## License of annotated dataset

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Giấy phép Creative Commons " style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
The annotated dataset of DANeS is licensed under Creative Commons Attribution 4.0 International License.

## About us

### DATASET.JSC - (+84) 98 442 0826 - info@dataset.vn

Website: [Dataset.vn](http://dataset.vn)

LinkedIn: [Dataset.vn - Data Crowdsourcing Platform](https://www.linkedin.com/company/dataset-vn/about/)

Facebook: [Dataset.vn - Data Crowdsourcing Platform](https://www.facebook.com/dataset.vn)

### AIV Group - (+84) 931 458 189 - marketing@aivgroup.vn

Website: [AIV Group](https://aivgroup.vn/)

Facebook: [AIV Group](https://www.facebook.com/aivgroup.jsc/)

