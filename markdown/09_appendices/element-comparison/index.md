---
title: Element Comparison
---
<a id="sec-elements_of_description_comparison"></a>
## Elements of Description comparison
1991 FIAF Cataloguing Rules (ISBD based), EN 15907 and FIAF Moving Image Cataloguing Manual

**Moving Image Work / Variant**

| **FIAF Moving Image Cataloguing Manual** | **EN 15907** | **1991 FIAF Cataloguing Rules (ISBD based)** |
| --- | --- | --- |
| **Attributes of the entity** | **Attributes** |  |
| Description Type <br/>- Analytic <br/>- Monographic <br/>- Serial <br/>- Collection | descriptionLevel <br/>- Analytic <br/>- Monographic <br/>- Serial <br/>- Collection | Series Area |
| Variant type <br/>- Censored <br/>- Dubbed <br/>- Subtitled <br/>- Abridged/Condensed <br/>- Augmented | variantType | Version/variation |
| **Elements (including main attributes)** | **Elements** |  |
| Identifier | Identifier (number) |  |
| Title <br/> **Title type** <br/>- Identifying <br/>- Preferred <br/>- Other title information <br/>- Alternative <br/>- Supplied/Devised | Identifying title (human readable) | Title area |
| Country of reference | Country of reference | Production/distribution area |
| Year/Date | Year of reference | Production/distribution area |
| Language(s) | Language | Production/distribution area |
| Content description | Content description | Notes area |
| Notes |  | Notes area |
| History |  | Notes area |
| **Relationships (including main attributes)** | **Allowed relationships** |  |
| Agents <br/> Agent type (e.g. cast/credits) | HasAgent | Production/distribution area |
| Events <br/> **Event type** <br/>- Publication <br/>- Award(s) or Nomination(s) <br/>- Production <br/>- Rights/Copyright/IPR Registration Preservation (Variant) <br/>- Decision (Variant) | HasEvent | Production/distribution area <br/> Notes area |
| Subject terms | HasSubject | Notes area |
| Other relationships | HasOtherRelation | Notes area |
| Manifestations | HasManifestation | Production/distribution area <br/> Physical description area | 

**Moving Image Manifestation**

| **FIAF Moving Image Cataloguing Manual** | **EN 15907** | **1991 FIAF Cataloguing Rules (ISBD based)** |
| --- | --- | --- |
| **Attributes of the entity** | **Attributes** |  |
| **Manifestation type** <br/>- Pre-release <br/>- Theatrical distribution <br/>- Non-theatrical distribution <br/>- Not for release <br/>- Unreleased <br/>- Home viewing publication <br/>- Broadcast <br/>- Internet <br/>- Preservation <br/>- Restoration <br/>- Unknown | manifestationType | Production/distribution area |
| **Elements (including main attributes)** | **Elements** |  |
| Identifier | Identifier |  |
| Title <br/> **Title type** <br/>- Proper <br/>- Other title information <br/>- Alternative <br/>- Supplied/Devised | Title | Title area |
| Language | Language | Physical description area |
| Format | Format | Physical description area |
| Extent | Extent | Physical description area |
| **Relationships (including main attributes)** | **Allowed relationships** |  |
| Agents <br/> **Agent type** <br/>- Distributor (theatrical) <br/>- Distributor (non-theatrical) <br/>- Broadcaster <br/>- Publisher <br/>- Manufacturer <br/>- Agent responsible for preservation <br/>- Agent responsible for reproduction or transfer <br/>- Agent responsible for archival availability <br/>- Agent responsible for the mere availability <br/>- Agent unclear or undetermined <br/>- Agent not identified | HasAgent | Production/distribution area Notes area |
| Events <br/> **Agent type** <br/>- Publication <br/>- Award(s) or Nomination(s) <br/>- Licensing <br/>- Preservation <br/>- Decision <br/>- Manufacture | HasEvent | Production/distribution area  Physical Description area  Notes area |
| Other relationships | HasOtherRelation | Notes area |
| Item | HasItem | Physical Description area | 

**Moving Image Item**

| **FIAF Moving Image Cataloguing Manual** | **EN 15907** | **1991 FIAF Cataloguing Rules (ISBD based)** |
| --- | --- | --- |
| **Elements (including main attributes)** | **Elements** |  |
| Identifier |  | Production/distribution area |
| Title <br/> **Title type** <br/>- Proper <br/>- Other title information <br/>- Alternative <br/>- Supplied/Devised | Title | Title area |
| Holding institution | Holding institution | Notes area |
| Item Material type | Instantiation type | Physical description area |
| Item-specifics | Item specifics | Physical description area   Notes area |
| Access conditions | Access conditions | Physical description area |
| Notes for moving image |  | Notes area |
| **Relationships (including main attributes)** | **Allowed relationships** |  |
| Agent(s) (e.g., preservation technician, donor, etc.) | HasAgent | Notes area |
| Events <br/> **Event type** <br/>- Licensing <br/>- Preservation <br/>- Inspection <br/>- Acquisition | HasEvent | Notes area |
| Other Relationships | HasOtherRelation | Notes area |
