# DANeS - Bộ dữ liệu nguồn mở các đầu báo điện tử
![12613](https://user-images.githubusercontent.com/94349957/143620522-2b417ece-2482-4475-a261-120af096cb0d.jpg)
*<sub>Nguồn: <a href="https://www.freepik.com/vectors/technology">Technology vector created by macrovector - www.freepik.com</a>.</sub>*

DANeS là một bộ dữ liệu mở xây dựng dựa trên sự hợp tác của DATASET. JSC và AIV Group. Bộ dữ liệu gồm ~ 500.000 bài báo điện tử tiếng Việt đến từ các trang báo như: tuoitre.vn, baobinhduong.vn, baoquangbinh.vn, kinhtechungkhoan.vn, doanhnghiep.vn, vnexpress.net,... Các bài báo sẽ bao gồm tiêu đề, URL, mô tả tổng quan từng bài báo và được dán nhãn tích cực/tiêu cực/trung tính dựa trên nội dung tiêu đề.

DANeS được đưa ra để phục vụ cộng đồng và các dự án AI tại Việt Nam, với hy vọng thúc đẩy phong trào kiến tạo các bộ dữ liệu mở để giải quyết các bài toán chung của xã hội. Kho dữ liệu tập hợp số lượng lớn các đầu báo để hỗ trợ huấn luyện mô hình AI phân biệt được sắc thái văn bản dựa trên các cấp khác nhau. Bạn có thể chia sẻ dự án/ sản phẩm sử dụng mô hình và kho dữ liệu của DANeS với chúng chúng tôi qua email: info@dataset.vn


<!-- TABLE OF CONTENTS -->
## Mục lục
  <ol>
    <li><a href="#cây-thư-mục">Cây thư mục</a></li>
    <li><a href="#định-dạng-dữ-liệu">Định dạng dữ liệu</a>
    <li><a href="#quy-trình-dán-nhãn">Quy trình dán nhãn</a></li>
    <li><a href="#quy-trình-review">Quy trình review</a></li>
    <li><a href="#quy-trình-cập-nhật">Quy trình cập nhật</a></li>
    <li><a href="#bản-quyền">Bản quyền</a></li>
    <li><a href="#về-chúng-tôi">Về chúng tôi</a></li>
  </ol>
</details>

## Cây thư mục
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
 
## Định dạng dữ liệu
Dữ liệu thô được lưu trữ trong thư mục raw_data dưới định dạng là tệp tin [`.json`](https://www.json.org) và được chia ra làm 8 batch. Mỗi batch bao gồm 1 mảng chứa nhiều json và mỗi json là 1 bản ghi của bộ dữ thô. 

| Key          | Type                   | Description                                  |
| ------------ | -----------------------| -------------------------------------------- |
| text         | string                 | title of the digital news                    |
| meta         | json                   | metadata of the digital news                 |
| uri          | string                 | link to the digital news                     |
| description  | string                 | description of the digital news              |

Dưới đây là ví dụ về định dạng của mỗi bản ghi:
```javascript
{
        "text": "Ba ra đi vào ngày nhận điểm thi, nữ sinh được hỗ trợ học phí",
        "meta": {
            		"description": "Ngày nhận được tin đỗ đại học cũng là lúc bố mất vì Covid-19, L.A dường như gục ngã. Thế nhưng, bên cạnh em đã có các mạnh thường quân hỏi han, hỗ trợ về kinh tế.",
            		"uri": "https://yan.vn/ba-ra-di-vao-ngay-nhan-diem-thi-nu-sinh-duoc-ho-tro-hoc-phi-277328.html"
        	}
}
``` 

Dữ liệu đã được gán nhãn được lưu trữ trong thư mục annotated_data dưới định dạng là tệp tin [`.json`](https://www.json.org) và được chia ra thành nhiều batch. Các batch sẽ được cập nhật theo tháng và dự kiến sẽ không có số lượng bản ghi cố định cho một lần cập nhật. 
Trong một batch, các bản ghi được gán nhãn được lưu trữ dưới dạng các file .json.

| Key          | Type                   |        Include             | Description                                  |
| ------------ | -----------------------| -------------------------- | -------------------------------------------- |
| id           | string                 |         none               | id of each instance                          |
| annotations  | array                  |          id                | id of class belong to specific instance      |
|              |                        |         type               | type of annotation                           |
|              |                        |         value              | value of annotation                          |
|              |                        |        to_name             | type of the value of annotation              |
|              |                        |       from_name            | name of the annotation                       |
| data         | json                   |text, meta, uri, description| contain raw data info                        |

Dưới đây là ví dụ về định dạng của mỗi bản ghi:
```javascript
{
        "id": 785436,
        "annotations": [
            {
                "id": "Eju0SNkpeb",
                "type": "choices",
                "value": {
                    "choices": [
                        "Trung tính"
                    ]
                },
                "to_name": "text",
                "from_name": "sentiment"
            },
            {
                "id": "Hoip8he_f6",
                "type": "choices",
                "value": {
                    "choices": [
                        "Đời sống",
                        "Xã hội",
                        "Hóng biến"
                    ]
                },
                "to_name": "text",
                "from_name": "topic"
            }
        ],
        "data": {
            "meta": {
                "uri": "https://toquoc.vn/cau-ca-nha-dai-nam-khoe-duoc-me-cho-di-choi-ngoi-trong-sieu-xe-rolls-royce-40-ty-ngam-co-ngoi-minh-se-thua-ke-trong-tuong-lai-222021299202526108.htm",
                "description": "(Tổ Quốc) - Được biết, siêu xe mà bà chủ Đại Nam lái chở cậu con trai quý tử đi chơi là chiếc Rolls-Royce Wraith thuộc thế hệ đầu tiên, giá thị trường trước đó khoảng 40 tỷ đồng"
            },
            "text": "\"Cậu cả\" nhà Đại Nam khoe được mẹ chở đi chơi, ngồi trong siêu xe Rolls-Royce 40 tỷ ngắm \"cơ ngơi\" mình sẽ thừa kế trong tương lai"
        }
    }
 ```

## Quy trình dán nhãn
- Bước 1: Đăng nhập.

![DANeS redo 1 1](https://user-images.githubusercontent.com/94349957/145561330-afc13caf-a8ab-42e4-8896-2acf71957a95.gif)

- Bước 2: Dán nhãn.
	+ Tiêu đề được phân loại sắc thái: tích cực, tiêu cực, trung tính.
	+ Tiêu đề được phân loại vào các chủ đề liên quan trong 23 chủ đề: Thế giới, Chính trị, Kinh tế, Thể thao, Văn hoá, Giải trí, Công nghệ, Khoa học, Giáo dục, Đời sống, Pháp luật, Bất động sản, Xã hội, Giao thông, Môi trường, Chứng khoán, Covid-19, Hóng biến, Game, Phim ảnh, Sức khoẻ, Du lịch, Không xác định

![DANeS redo 2](https://user-images.githubusercontent.com/94349957/144919228-fbda5c51-9b7f-47ef-a51e-ca95813419c7.gif)

## Quy trình kiểm soát chất lượng

- Người kiểm tra chất lượng và kiểm tra chéo sẽ được quản lý hoặc chủ sở hữu dự án lựa chọn từ những CTV dựa trên chất lượng công việc và thái độ trong quá trình làm việc.
- Quy trình kiểm soát chất lượng data gồm 2 bước: kiểm tra chéo và kiểm tra chất lượng
     + Mỗi người kiểm tra chéo sẽ được giao cho khoảng 20% số lượng bản ghi của người dán nhãn khác.
        => Nếu người kiểm tra chéo phát hiện được bản ghi không đạt chất lượng thì phải sửa lại để đạt đúng yêu cầu.
     + Người kiểm tra chất lượng, mặt khác, sẽ tiến hành check 20-50% tổng số lượng nhãn được gán của cả dự án.
        => Nếu người kiểm tra chất lượng phát hiện bản ghi được gán nhãn không đạt chất lượng thì có thể lựa chọn sửa lại hoặc chuyển lại cho người gán nhãn/người kiểm tra chéo gán nhãn lại.

## Quy trình cập nhật

- Bộ dữ liệu thô sẽ được cập nhật đầy đủ trên trang chính thức của DANeS tại Github. (https://github.com/dataset-vn/DANeS)

- Phần dữ liệu gồm các bản ghi đã được dán nhãn sẽ được cập hàng tháng trên trang chính thức của DANeS tại Github. (https://github.com/dataset-vn/DANeS)


## Bản quyền

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Giấy phép Creative Commons " style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
Phần dữ liệu được dán nhãn thuộc <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/dataset-vn/DANeS" property="cc:attributionName" rel="cc:attributionURL">DANeS</a> được cấp phép theo <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Giấy phép Creative Commons Ghi công 4.0 Quốc tế</a>.

Với loại giấy phép này bạn có thể:
- Sao chép, chỉnh sửa, phân phối và xây dựng sản phẩm của bạn dựa trên các dữ liệu đã công bố trong dự án này ở bất kì định dạng hoặc bất kỳ phương tiện nào.
- Chỉnh sửa, biến đổi và xây dựng lại cho mọi mục đích, kể cả mục đích thương mại.
Tuy nhiên bạn cần phải trích dẫn nguồn gốc của tài liệu này khi mà bạn sử dụng bất kỳ dữ liệu đã được dán nhãn và công bố trong bộ dữ liệu DANeS này.

Nếu bạn cần trích dẫn tới bộ dữ liệu của chúng tôi, xin hãy sử dụng:
```javascript
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Giấy phép Creative Commons " style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
Phần dữ liệu được dán nhãn thuộc <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/dataset-vn/DANeS" property="cc:attributionName" rel="cc:attributionURL">DANeS</a> được cấp phép theo <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Giấy phép Creative Commons Ghi công 4.0 Quốc tế</a>.
```

## Về chúng tôi

### DATASET .JSC - (+84) 98 442 0826 - info@dataset.vn

Sứ mệnh của DATASET là trở thành nền tảng dữ liệu "nguồn lực cộng đồng" tiên phong tại Việt Nam, hỗ trợ các cá nhân, tổ chức trong việc ứng dụng khoa học dữ liệu để giải quyết các bài toán của xã hội. Với nền tảng phần mềm mạnh mẽ và cộng đồng xử lý dữ liệu đông đảo, DATASET mong muốn đưa đến cho đối tác một giải pháp toàn diện và chất lượng, phù hợp với đặc thù của thị trường công nghệ Việt Nam và thế giới.

Website: [Dataset.vn](http://dataset.vn)

LinkedIn: [Dataset.vn - Data Crowdsourcing Platform](https://www.linkedin.com/company/dataset-vn/about/)

Facebook: [Dataset.vn - Data Crowdsourcing Platform](https://www.facebook.com/dataset.vn)

### AIV Group - (+84) 931 458 189 - marketing@aivgroup.vn

AIV Group hướng đến việc ứng dụng những tiến bộ về công nghệ, đặc biệt là Trí tuệ nhân tạo (AI), Điện toán đám mây (Cloud Computing), Dữ liệu lớn (Big Data) để số hoá, hiện đại hoá các quy trình sản xuất và tiêu thụ thông tin đã tồn tại lâu đời trong xã hội Việt Nam, đồng thời góp phần giải quyết những vấn đề mới phát sinh trong lĩnh vực truyền thông do mặt trái của công nghệ như: vấn nạn tin giả, hình ảnh, video được cắt ghép tự động…

Website: [AIV Group](https://aivgroup.vn/)

Facebook: [AIV Group](https://www.facebook.com/aivgroup.jsc/)