---
name: china-kyc-doc-parse
description: Parse and extract data from Chinese identity documents for KYC (Know Your Customer) compliance. Adapts the original kyc-doc-parse skill for Chinese ID cards, business licenses, and domestic compliance requirements. Triggers on "A股KYC", "身份文件解析", "parse Chinese ID", "KYC document", "客户身份识别", or "extract [document type]".
---

# china-kyc-doc-parse

## Purpose

Parse **中国身份文件** — extract and verify data from Chinese KYC documents.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
# Not typically used for KYC; for background checks:
get_stock_info(ticker)                    → Company verification (if applicable)
```

### Secondary Sources
- 国家企业信用信息公示系统 — business license verification
- 天眼查 / 企查查 — corporate information
- 公安部 — ID verification (via approved channels)

## Document Types

### 1. 个人身份证 (Personal ID Card)

**Front of ID card:**

| Field | Location | Data Type |
|-------|----------|-----------|
| 姓名 | Upper section | Text |
| 性别 | Below name | 男/女 |
| 民族 | Below gender | Text (e.g., 汉) |
| 出生日期 | Below ethnicity | YYYY年MM月DD日 |
| 住址 | Lower section | Address |
| 公民身份号码 | Lower section | 18-digit number |

**Back of ID card:**

| Field | Description |
|-------|-------------|
| 签发机关 | Issuing authority |
| 有效期限 | Validity period |
| 证件签发 | Issue date |
| 证件失效 | Expiry date |

**ID number structure:**

| Position | Length | Content |
|----------|--------|---------|
| 1-6 | 6 digits | Address code (行政区划) |
| 7-14 | 8 digits | Birth date (YYYYMMDD) |
| 15-17 | 3 digits | Order code + gender (odd=male, even=female) |
| 18 | 1 digit | Check digit |

### 2. 营业执照 (Business License)

**Unified Social Credit Code (统一社会信用代码):**

| Structure | Length | Content |
|-----------|--------|---------|
| 登记管理部门代码 | 1 digit | 9=工商, 1=机构编制, etc. |
| 机构类别代码 | 1 digit | |
| 登记管理机关行政区划码 | 6 digits | |
| 主体标识码 | 9 digits | Org code |
| 校验码 | 1 digit | Check digit |

**Business license fields:**

| Field | Content |
|-------|---------|
| 统一社会信用代码 | 18-digit code |
| 名称 | Company name |
| 类型 | Entity type |
| 法定代表人 | Legal representative |
| 注册资本 | Registered capital |
| 成立日期 | Establishment date |
| 住所 | Registered address |
| 经营范围 | Business scope |
| 登记机关 | Registration authority |
| 登记日期 | Registration date |

### 3. 护照 (Passport)

| Field | Content |
|-------|---------|
| 护照号码 | Letter + 8 digits |
| 姓名 | Chinese + Pinyin |
| 国籍 | Nationality |
| 出生日期 | DD/MM/YYYY |
| 性别 | M/F |
| 出生地点 | Place of birth |
| 签发日期 | Issue date |
| 有效期至 | Expiry date |
| 签发机关 | Issuing authority |

### 4. 港澳通行证 / 台湾通行证

| Field | Content |
|-------|---------|
| 证件号码 | HK/Macau/Taiwan travel permit number |
| 姓名 | Name |
| 出生日期 | DOB |
| 性别 | Gender |
| 有效期至 | Expiry date |

### 5. 外国人居留许可证

| Field | Content |
|-------|---------|
| 姓名 | Name (native + Chinese) |
| 国籍 | Nationality |
| 出生日期 | DOB |
| 性别 | Gender |
| 有效期至 | Expiry date |
| 签发机关 | Issuing authority |

## Parsing Workflow

### Step 1: Document Intake

**Document verification:**

| Check | Pass Criteria |
|-------|--------------|
| 照片清晰 | Photo clear enough to read |
| 文字清晰 | Text legible |
| 无遮挡 | No obstruction of key fields |
| 证件在有效期内 | Not expired |
| 证件真实 | Genuine appearance |

### Step 2: Data Extraction

**Extraction checklist:**

| Document | Fields to Extract |
|----------|------------------|
| 身份证 | Name, ID number, DOB, gender, address |
| 营业执照 | Company name, USCC, legal rep, registered capital, scope |
| 护照 | Passport number, name, nationality, DOB, expiry |
| 其他 | As applicable |

### Step 3: ID Number Validation

**ID number checks:**

| Check | Method | Pass |
|-------|--------|------|
| Length | 18 digits | ✓ |
| Birth date | Valid date | ✓ |
| Gender | Odd/even check | ✓ |
| Check digit | Mod 11 algorithm | ✓ |
| Address code | Valid code | ✓ |

**Check digit algorithm:**
```
Weights: 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2
Remainder → 0-10 → Code: 10→X, 0→1, 1→0, 2→9, ...
```

### Step 4: Address Code Decoding

**Address code lookup:**

| Code | Province/City |
|------|--------------|
| 11 | 北京 |
| 31 | 上海 |
| 44 | 广东 |
| 33 | 浙江 |
| 32 | 江苏 |
| ... | ... |

### Step 5: Data Normalization

**Normalization rules:**

| Field | Normalization |
|-------|--------------|
| Name | Trim whitespace, no middle dots |
| ID number | Uppercase X for check digit |
| DOB | YYYY-MM-DD format |
| Address | Standardize |
| Phone | +86 format |
| Registered capital | Convert to 万元 |
| Dates | YYYY-MM-DD format |

### Step 6: Quality Checks

**Extraction quality:**

| Check | Pass |
|-------|------|
| All required fields extracted | ✓ |
| Data format correct | ✓ |
| ID number validated | ✓ |
| Dates valid | ✓ |
| No OCR errors | ✓ |

## China-Specific Considerations

### Anti-Money Laundering (AML)

| Requirement | Implementation |
|-------------|----------------|
| 客户身份识别 | Identify and verify customer |
| 受益所有人 | Ultimate beneficial owner |
| 持续识别 | Ongoing monitoring |
| 风险分类 | Risk categorization |
| 身份证明文件 | Minimum documents required |

### Required Documents by Customer Type

| Type | Required |
|------|----------|
| 中国个人 | 身份证 |
| 外国个人 | 护照 + 居留许可 |
| 中国企业 | 营业执照 + 法人身份证 |
| 外国企业 | 注册文件 + 授权代表证件 |

### Common Issues

| Issue | Resolution |
|-------|-----------|
| 照片模糊 | Request clearer copy |
| 证件过期 | Request current document |
| 信息矛盾 | Verify with other sources |
| 扫描不全 | Request complete document |

## Quality Checks

Before completing:
- [ ] All fields extracted
- [ ] Data validated
- [ ] Documents verified
- [ ] AML checks performed
- [ ] Records complete
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
