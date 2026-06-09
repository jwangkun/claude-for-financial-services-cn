---
name: china-kyc-rules
description: Chinese KYC (Know Your Customer) and AML (Anti-Money Laundering) rules for financial services. Adapts the original kyc-rules skill for Chinese regulatory requirements and domestic compliance. Triggers on "A股KYC规则", "中国反洗钱", "AML rules China", "KYC compliance China", "反洗钱规定", or "KYC requirements".
---

# china-kyc-rules

## Purpose

Define **中国KYC与反洗钱规则** — comprehensive KYC/AML requirements for Chinese financial services.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

## Regulatory Framework

### Primary Regulations

| Regulation | Authority | Key Requirement |
|------------|-----------|-----------------|
| 反洗钱法 | 全国人大常委会 | AML framework law |
| 金融机构客户尽职调查和客户身份资料及交易记录保存管理办法 | 央行 | CDD/KYC requirements |
| 金融机构大额交易和可疑交易报告管理办法 | 央行 | STR reporting |
| 法人金融机构洗钱和恐怖融资风险自评估指引 | 央行 | Risk assessment |
| 受益所有人身份识别办法 | 央行 | UBO identification |
| 证券期货业反洗钱工作规程 | 证监会 | Securities-specific AML |

## Customer Identification

### 1. 客户身份识别 (Customer Identification)

**Minimum identification requirements:**

| Customer Type | Required ID | Additional |
|--------------|-------------|------------|
| 中国自然人 | 身份证 (verified) | |
| 外国自然人 | 护照 + 居留许可 | |
| 中国法人 | 营业执照 + 法人身份证 | |
| 外国法人 | 注册证明 + 授权代表 | |
| 合伙企业 | 营业执照 + 合伙协议 | |
| 个体工商户 | 营业执照 + 经营者身份证 | |

### 2. 受益所有人识别 (UBO Identification)

**UBO identification rules:**

| Ownership % | UBO Identification |
|------------|-------------------|
| ≥25% direct | Direct owner |
| ≥25% indirect | Chain through entities |
| No 25% owner | Controlling person (实际控制人) |
| Government | N/A (state entity) |

**UBO information to collect:**

| Field | Content |
|-------|---------|
| 姓名/名称 | Name |
| 身份证件 | ID type and number |
| 地址 | Address |
| 持股比例 | Ownership % |
| 控制方式 | Control mechanism |

### 3. 客户风险分类 (Customer Risk Classification)

**Risk categories:**

| Category | Criteria | Due Diligence |
|----------|----------|--------------|
| 低风险 | Listed companies, government entities | Simplified CDD |
| 中风险 | Private companies, HNW individuals | Standard CDD |
| 高风险 | PEPs, high-risk jurisdictions | Enhanced CDD |

**Risk factors:**

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| 客户类型 | Listed, gov | Private corp | Shell company |
| 行业 | Low risk | Medium | Gambling, MSB |
| 地理位置 | Onshore | Main cities | Offshore, high-risk |
| 交易模式 | Simple, regular | Moderate | Complex, unusual |
| PEP | No | No | Yes |

### 4. 尽职调查程序 (Due Diligence Procedures)

**Simplified CDD (低风险):**

| Step | Action |
|------|--------|
| 1 | Identify customer |
| 2 | Verify identity |
| 3 | Record information |

**Standard CDD (中风险):**

| Step | Action |
|------|--------|
| 1 | Identify customer |
| 2 | Verify identity |
| 3 | Identify UBO |
| 4 | Understand nature of business |
| 5 | Verify source of funds |
| 6 | Ongoing monitoring |

**Enhanced CDD (高风险):**

| Step | Action |
|------|--------|
| 1-6 | Standard CDD |
| 7 | Senior management approval |
| 8 | Enhanced source of wealth |
| 9 | Enhanced ongoing monitoring |
| 10 | PEP approval (if applicable) |

### 5. 持续识别 (Ongoing Monitoring)

**Ongoing CDD requirements:**

| Activity | Frequency |
|----------|-----------|
| 客户信息更新 | Every 3-5 years or upon change |
| 交易监控 | Real-time / Daily |
| 风险等级重估 | Every 1-3 years |
| 受益所有人更新 | Upon change |

## Transaction Monitoring

### 大额交易 (Large Transactions)

**Reporting thresholds:**

| Type | Threshold | Action |
|------|-----------|--------|
| 现金 | RMB 50,000+ | Report |
| 转账 | RMB 200,000+ (individual) | Report |
| 转账 | RMB 500,000+ (entity) | Report |
| 跨境 | RMB 20,000+ | Report |

### 可疑交易 (Suspicious Transactions)

**Suspicious transaction indicators:**

| Pattern | Concern |
|---------|---------|
| 快进快出 | Rapid in-out (layering) |
| 分散转入集中转出 | Multiple in, one out (structuring) |
| 集中转入分散转出 | One in, multiple out |
| 长期休眠账户突然激活 | Dormant account activation |
| 交易对手为高风险地区 | High-risk jurisdiction |
| 交易与客户背景不符 | Mismatch with profile |
| 大额现金交易 | Large cash transactions |
| 频繁跨境交易 | Frequent cross-border |

### 交易记录保存 (Record Keeping)

| Record | Retention Period |
|--------|-----------------|
| 客户身份资料 | Business relationship + 5 years |
| 交易记录 | 5 years from transaction |
| 大额交易报告 | 5 years |
| 可疑交易报告 | 20 years |

## A-share Specific Requirements

### Securities Account KYC

| Requirement | Detail |
|-------------|--------|
| 三方存管 | Third-party custody |
| 身份核验 | Real-name registration |
| 风险测评 | Risk assessment questionnaire |
| 适当性匹配 | Suitability matching |
| 回访 | Follow-up calls |

### Account Opening Process

| Step | Action | Document |
|------|--------|----------|
| 1 | 身份核验 | ID card verification |
| 2 | 风险测评 | Risk questionnaire |
| 3 | 适当性评估 | Suitability assessment |
| 4 | 签署协议 | Account agreement |
| 5 | 三方存管 | Bank linkage |
| 6 | 回访 | Telephone confirmation |

## Sanctions & Restrictions

### 禁止交易名单 (Restricted List)

| Category | Examples |
|----------|---------|
| 失信被执行人 | Debtors in default |
| 资本市场失信 | Market ban list |
| 私募禁止 | Private fund bans |
| 证券业协会 | Industry bans |

### 高风险地区 (High-Risk Jurisdictions)

| Region | Risk Level |
|--------|-----------|
| FATF灰名单 | Enhanced CDD |
| FATF黑名单 | Prohibited |
| OFAC制裁名单 | Prohibited |
| 联合国制裁名单 | Prohibited |

## Quality Checks

Before completing:
- [ ] Customer identified and verified
- [ ] UBO identified
- [ ] Risk classification assigned
- [ ] CDD procedures followed
- [ ] Source of funds verified
- [ ] Transaction monitoring in place
- [ ] Records maintained
- [ ] Reports filed as required
