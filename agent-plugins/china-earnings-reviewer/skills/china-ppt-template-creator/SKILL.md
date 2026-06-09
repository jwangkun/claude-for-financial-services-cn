---
name: china-ppt-template-creator
description: Create PowerPoint templates for A-share investment presentations. Adapts the original ppt-template-creator skill for Chinese business presentation standards and firm branding. Triggers on "A股PPT模板", "投资PPT模板", "create ppt template China", "presentation template", "制作PPT模板", or "build template for [purpose]".
---

# china-ppt-template-creator

## Purpose

Create **A股投资分析PPT模板** — standardized PowerPoint templates for Chinese equity research and client presentations.

## Data Sources

N/A (template creation)

## Workflow

### Step 1: Define Template Requirements

**Template specification:**

| Element | Specification |
|---------|--------------|
| 用途 | Research / Client / IC / Roadshow |
| 尺寸 | Standard 16:9 or 4:3 |
| 颜色 | Corporate brand colors |
| 字体 | Chinese-compatible fonts |
| Logo | Firm logo placement |
| 页数 | Base slides + content slides |

### Step 2: Master Slide Design

**Master slide elements:**

| Element | Placement | Specification |
|---------|-----------|--------------|
| Firm logo | Top-right | Transparent PNG |
| Company logo | Top-left (if applicable) | |
| Date | Footer | YYYY年MM月DD日 |
| 页码 | Bottom-center | "第 X 页" |
| 标题栏 | Top | Background color, white text |
| Footer text | Bottom-left | Confidentiality notice |

### Step 3: Slide Layouts

**Standard layouts:**

| Layout | Name | Use |
|--------|------|-----|
| 封面 (Cover) | Title slide | First slide |
| 章节分隔 (Section) | Section divider | Major sections |
| 标题+内容 (Title+Content) | Standard | Most slides |
| 两栏 (Two-column) | Comparison | Pros/cons, before/after |
| 图表 (Chart) | Data visualization | Charts, tables |
| 图片 (Image) | Full image | Screenshots, photos |
| 引用 (Quote) | Highlight | Key quotes, findings |
| 附录 (Appendix) | Backup | Detailed data |

### Step 4: Content Slide Templates

**Pre-built slide templates:**

**1. Executive Summary:**
```
[Header bar with "投资摘要"]

左侧:
• [Point 1]
• [Point 2]
• [Point 3]

右侧:
[图表/数据 highlight]

底部:
目标价: ¥XX | 评级: [X] | 上行/下行: X%
```

**2. Financial Table:**
```
[Header bar with "财务数据"]

[Formatted table]
项目 | 2021 | 2022 | 2023 | 2024E | 2025E
-----|------|------|------|-------|-------
营业收入 | | | | |
归母净利润 | | | | |

底部: 数据来源: 公司年报, iFind/AkShare
```

**3. Chart Slide:**
```
[Header bar with "营业收入及增长"]

[Large chart area]
• Title: Clear and descriptive
• Data: Sourced and accurate
• Format: Consistent colors

底部: 数据来源: [Source]
```

**4. Valuation:**
```
[Header bar with "估值分析"]

[Football field chart]
[Methodology table]
目标价: ¥XX - ¥XX

底部: 数据来源: iFind, AkShare
```

**5. Risk Factors:**
```
[Header bar with "风险提示"]

[Numbered risk list]
1. [Risk category]
   • [Specific risk]
   • [Impact assessment]

底部: 本报告仅供内部参考
```

### Step 5: Style Guide

**Design standards:**

| Element | Standard |
|---------|----------|
| 标题字体 | Bold, 32-44pt |
| 正文字体 | Regular, 18-24pt |
| 行间距 | 1.3-1.5x |
| 配色 | Primary: #1f4e79 (blue), Secondary: #4472c4 |
| 强调色 | Red for negative, green for positive |
| 表格 | Clean, alternating row colors |
| 图表 | Minimal gridlines, clear labels |

### Step 6: Asset Library

**Template assets:**

| Asset | Format | Usage |
|-------|--------|-------|
| Firm logo | PNG (transparent) | Every slide header |
| Section dividers | PNG/JPG | Section breaks |
| Icon set | SVG/PNG | Visual elements |
| Chart templates | Excel-linked | Data slides |
| Footer | PNG/text | Every slide |

### Step 7: Template Files

**Deliverables:**

| File | Description |
|------|-------------|
| [Name]_Template.pptx | Master template file |
| [Name]_Slide_Library.pptx | Pre-built slide library |
| [Name]_Style_Guide.pdf | Design guidelines |
| Assets/ | Logos, icons, backgrounds |

### Step 8: Usage Instructions

**Template usage guide:**

```
使用说明

1. 打开 [Name]_Template.pptx
2. 使用 "新建幻灯片" 选择对应版式
3. 替换占位符内容:
   - [公司名称]
   - [报告标题]
   - [日期]
   - [数据]
4. 更新图表数据链接
5. 替换图片资产
6. 删除说明页

注意事项:
- 不要直接删除母版幻灯片
- 保持颜色和字体一致
- 所有数据需标注来源
```

## China-Specific Considerations

### Font Requirements

| Font | Usage | Fallback |
|------|-------|----------|
| 思源黑体 | Preferred body font | 微软雅黑 |
| 微软雅黑 | Common system font | Arial |
| 方正小标宋 | Chinese formal titles | SimSun |
| Times New Roman | English/number | |

### Color Conventions

| Color | Meaning | Usage |
|-------|---------|-------|
| 红色 | Negative / Loss / Below | Below benchmark, losses |
| 绿色 | Positive / Gain / Above | Above benchmark, gains |
| 蓝色 | Corporate / Primary | Headers, key points |
| 灰色 | Neutral | Secondary text |
| 黄色 | Highlight / Warning | Emphasis, alerts |

### Rating Color Codes

| Rating | Chinese | Color |
|--------|---------|-------|
| Buy | 买入 | Red (A-share convention: red = up) |
| Accumulate | 增持 | Light red |
| Neutral | 中性 | Yellow/Gray |
| Reduce | 减持 | Light green |
| Sell | 卖出 | Green |

## Quality Checks

Before delivering:
- [ ] All layouts functional
- [ ] Design consistent
- [ ] Chinese fonts working
- [ ] Assets embedded/linked
- [ ] Usage instructions clear
- [ ] File tested on PowerPoint
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
