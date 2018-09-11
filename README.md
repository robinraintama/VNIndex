# VNIndex
DOM Filter or HTML Extraction Service 
FLASK+RESTful+MongoDB

### Companies
This endpoint fetch list of all companies without applying any filter
```sh
/companies
```

### Request
| BODY | VALUE |
| ------ | ------ |
| url | http://127.0.0.1:5000/companies |

### Response
```json
{
    "status_code": 200,
    "message": "successful",
    "data": [
        {
            "ticker symbol": "ACL",
            "company name": "CUU LONG FISH JOINT STOCK COMPANY",
            "uid": "http://stock.vietnammarkets.com/food-processing/ACL/",
            "business": "Food processing",
            "crawled_at": "2018-09-11",
            "Listing bourse": "HOSE",
            "company_address": "90 Hùng Vương, Khóm Mỹ Thọ, P. Mỹ Quý, Tp. Long Xuyên, Tỉnh An Giang",
            "country": "Vietnam",
            "company_state": "Tỉnh An Giang",
            "company_city": "Tp. Long Xuyên",
            "company_street": "90 Hùng Vương Khóm Mỹ Thọ",
            "company phone number": [
                "+84",
                "+8476931000",
                "+84932821",
                "+84",
                "+8476932446",
                "+84932099"
            ],
            "company phone number raw": "(84-76) 931000 - 932821 \n\t\t\t\t\t\t(84-76) 932446 - 932099",
            "company email": "clfish@vnn.vn",
            "company website": "http://www.clfish.com",
            "financial summary": {
                "Capital Currency": "VND",
                "Market Cap": 11000000000,
                "Par Value": 10000,
                "Equity": 0,
                "Listing Volume": 9000000,
                "Listed Date": "09-05-2007",
                "Initial Listed Price": 81000
            },
            "company description": "- Chế biến, bảo quản thủy sản và sản phẩm từ thủy sản; - Mua bán cá và thủy sản; - Mua bán hóa chất, dụng cụ dùng trong sản xuất và chế biến thủy sản; - Nuôi trồng thủy sản; - Mua bán nông sản (nếp, gạo, hạt điều...); - Mua bán thực phẩm (đậu nành, đậu bắp, rau quả,... đông lạnh); - Sản xuất bao bì; - Mua bán các loại nguyên vật tư trong ngành bao bì; - Chế biến thức ăn thủy sản; - Mua bán nguyên liệu, vật tư phục vụ chăn nuôi thủy sản (cám bã đậu nành, bột cá, bột xương thịt, vitamin); - Đầu tư cơ sở hạ tầng khu công nghiệp, khu du lịch, khách sạn, cao ốc văn phòng; - Chế biến thức ăn gia súc.",
            "auditing company": {
                "company_name": "Công ty TNHH Kiểm toán và Tư vấn (A&C)",
                "address": "Địa chỉ: 229 Đồng Khởi - Q.1 - TP. Hồ Chí Minh",
                "Fax": "(84-8) 8272300"
            },
            "business registration": {
                "Established License": "  00-00-0000  ",
                "Business License": "5203000065  04-17-2007   Sở Kế hoạch và Đầu tư Tỉnh An Giang"
            }
        },
        {...}
    ]
}
```

### Company Filter by Name
This endpoint  fetch a specific company given its name
```sh
/companies?company_name=<name>
```

### Request
| BODY | VALUE |
| ------ | ------ |
| url | http://127.0.0.1:5000/companies?company_name=ben%20tre%20aquaproduct |

### Response
```json
{
    "status_code": 200,
    "message": "successful",
    "data": [
        {
            "ticker symbol": "ABT",
            "company name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC",
            "uid": "http://stock.vietnammarkets.com/food-processing/ABT/",
            "business": "Food processing",
            "crawled_at": "2018-09-11",
            "Listing bourse": "HOSE",
            "company_address": "Village 9, Tan Thach Commune, Chau Thanh District, Ben Tre Province",
            "country": "Vietnam",
            "company_state": "Ben Tre Province",
            "company_city": "Chau Thanh District",
            "company_street": "Village 9 Tan Thach Commune",
            "company phone number": [
                "+8475860265",
                "+8475860346"
            ],
            "company phone number raw": "(84.75) 860 265 \n\t\t\t\t\t\t(84.75)860 346",
            "company email": "aquatex@hcm.vnn.vn",
            "company website": "www.aquatexbentre.com",
            "financial summary": {
                "Capital Currency": "VND",
                "Market Cap": 81000000000,
                "Par Value": 10000,
                "Equity": 0,
                "Listing Volume": "3,300,000",
                "Listed Date": "12-25-2006",
                "Initial Listed Price": 90000
            },
            "company description": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "auditing company": {
                "company_name": "Auditing and Informatic Services Company",
                "address": "Address: 142 Nguyen Thi Minh Khai Street - District 3",
                "Tel": "(84.8) 9 305 163 (10 lines)",
                "Fax": "(84.8) 9 304 28 ",
                "Website": "http://www.aisc.com.vn",
                "Email": "aisc@aisc.com.vn"
            },
            "business registration": {
                "Established License": "3423/QD-UB  12-01-2003  Ben Tre Province People's Committee",
                "Business License": "553000010  12-25-2003   Department of Planning and Investment of Ben Tre Province"
            }
        }
    ]
}
```

### Companies Filter by Industry
This endpoint fetch companies of a particular industry
```sh
/companies?business=<business>
```

### Request
| BODY | VALUE |
| ------ | ------ |
| url | http://127.0.0.1:5000/companies?business=Food%20processing |

### Response
```json
{
    "status_code": 200,
    "message": "successful",
    "data": [
        {
            "ticker symbol": "ACL",
            "company name": "CUU LONG FISH JOINT STOCK COMPANY",
            "uid": "http://stock.vietnammarkets.com/food-processing/ACL/",
            "business": "Food processing",
            "crawled_at": "2018-09-11",
            "Listing bourse": "HOSE",
            "company_address": "90 Hùng Vương, Khóm Mỹ Thọ, P. Mỹ Quý, Tp. Long Xuyên, Tỉnh An Giang",
            "country": "Vietnam",
            "company_state": "Tỉnh An Giang",
            "company_city": "Tp. Long Xuyên",
            "company_street": "90 Hùng Vương Khóm Mỹ Thọ",
            "company phone number": [
                "+84",
                "+8476931000",
                "+84932821",
                "+84",
                "+8476932446",
                "+84932099"
            ],
            "company phone number raw": "(84-76) 931000 - 932821 \n\t\t\t\t\t\t(84-76) 932446 - 932099",
            "company email": "clfish@vnn.vn",
            "company website": "http://www.clfish.com",
            "financial summary": {
                "Capital Currency": "VND",
                "Market Cap": 11000000000,
                "Par Value": 10000,
                "Equity": 0,
                "Listing Volume": 9000000,
                "Listed Date": "09-05-2007",
                "Initial Listed Price": 81000
            },
            "company description": "- Chế biến, bảo quản thủy sản và sản phẩm từ thủy sản; - Mua bán cá và thủy sản; - Mua bán hóa chất, dụng cụ dùng trong sản xuất và chế biến thủy sản; - Nuôi trồng thủy sản; - Mua bán nông sản (nếp, gạo, hạt điều...); - Mua bán thực phẩm (đậu nành, đậu bắp, rau quả,... đông lạnh); - Sản xuất bao bì; - Mua bán các loại nguyên vật tư trong ngành bao bì; - Chế biến thức ăn thủy sản; - Mua bán nguyên liệu, vật tư phục vụ chăn nuôi thủy sản (cám bã đậu nành, bột cá, bột xương thịt, vitamin); - Đầu tư cơ sở hạ tầng khu công nghiệp, khu du lịch, khách sạn, cao ốc văn phòng; - Chế biến thức ăn gia súc.",
            "auditing company": {
                "company_name": "Công ty TNHH Kiểm toán và Tư vấn (A&C)",
                "address": "Địa chỉ: 229 Đồng Khởi - Q.1 - TP. Hồ Chí Minh",
                "Fax": "(84-8) 8272300"
            },
            "business registration": {
                "Established License": "  00-00-0000  ",
                "Business License": "5203000065  04-17-2007   Sở Kế hoạch và Đầu tư Tỉnh An Giang"
            }
        },
        {...}
    ]
}
```

### Companies Filter by Revenue
This endpoint fetch contacts based on company revenue
```sh
/companies?revenue_gte=<int revenue>
```

### Request
| BODY | VALUE |
| ------ | ------ |
| url | http://127.0.0.1:5000/companies?revenue_gte=100000 |

### Response
```json
{
    "status_code": 200,
    "message": "successful",
    "data": [
        {
            "ticker symbol": "ACL",
            "company name": "CUU LONG FISH JOINT STOCK COMPANY",
            "uid": "http://stock.vietnammarkets.com/food-processing/ACL/",
            "business": "Food processing",
            "crawled_at": "2018-09-11",
            "Listing bourse": "HOSE",
            "company_address": "90 Hùng Vương, Khóm Mỹ Thọ, P. Mỹ Quý, Tp. Long Xuyên, Tỉnh An Giang",
            "country": "Vietnam",
            "company_state": "Tỉnh An Giang",
            "company_city": "Tp. Long Xuyên",
            "company_street": "90 Hùng Vương Khóm Mỹ Thọ",
            "company phone number": [
                "+84",
                "+8476931000",
                "+84932821",
                "+84",
                "+8476932446",
                "+84932099"
            ],
            "company phone number raw": "(84-76) 931000 - 932821 \n\t\t\t\t\t\t(84-76) 932446 - 932099",
            "company email": "clfish@vnn.vn",
            "company website": "http://www.clfish.com",
            "financial summary": {
                "Capital Currency": "VND",
                "Market Cap": 11000000000,
                "Par Value": 10000,
                "Equity": 0,
                "Listing Volume": 9000000,
                "Listed Date": "09-05-2007",
                "Initial Listed Price": 81000
            },
            "company description": "- Chế biến, bảo quản thủy sản và sản phẩm từ thủy sản; - Mua bán cá và thủy sản; - Mua bán hóa chất, dụng cụ dùng trong sản xuất và chế biến thủy sản; - Nuôi trồng thủy sản; - Mua bán nông sản (nếp, gạo, hạt điều...); - Mua bán thực phẩm (đậu nành, đậu bắp, rau quả,... đông lạnh); - Sản xuất bao bì; - Mua bán các loại nguyên vật tư trong ngành bao bì; - Chế biến thức ăn thủy sản; - Mua bán nguyên liệu, vật tư phục vụ chăn nuôi thủy sản (cám bã đậu nành, bột cá, bột xương thịt, vitamin); - Đầu tư cơ sở hạ tầng khu công nghiệp, khu du lịch, khách sạn, cao ốc văn phòng; - Chế biến thức ăn gia súc.",
            "auditing company": {
                "company_name": "Công ty TNHH Kiểm toán và Tư vấn (A&C)",
                "address": "Địa chỉ: 229 Đồng Khởi - Q.1 - TP. Hồ Chí Minh",
                "Fax": "(84-8) 8272300"
            },
            "business registration": {
                "Established License": "  00-00-0000  ",
                "Business License": "5203000065  04-17-2007   Sở Kế hoạch và Đầu tư Tỉnh An Giang"
            }
        },
        {...}
    ]
}
```

# Dillinger

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

Dillinger is a cloud-enabled, mobile-ready, offline-storage, AngularJS powered HTML5 Markdown editor.

  - Type some Markdown on the left
  - See HTML in the right
  - Magic