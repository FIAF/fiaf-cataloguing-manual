---
title: Relationships of a Work/Variant (links/associations with other entities/records)
weight: 3
---
<a id="sec-relationships_of_a_work_variant"></a>
### Relationships of a Work/Variant (links/associations with other entities/records)
A relationship associates an instance of a Variant with another instance of an entity.
Entities are described in subsequent sections, but examples of entities are people or companies associated with a Variant (eg, studio, director, cast), events (copyright registration), subjects (other Works/Variants are about the same subject), and records.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.[^fn1] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest, i.e., whether by physical associative record linking or “see also” text conventions.

A Variant may have relationships with the following:

- Agent(s)
- Event(s)
- Subject(s)/Genre(s)/Form(s)
- Work(s)
- Manifestation(s)
- Other (including other Variants)

<a id="sec-Works"></a>
#### Works
Express the relationship between a Work and a Variant (e.g., Part/part of).
Describe or demonstrate Work-to-Variant relationships through linking to the Work identifier, through the usage of relator terms, or according to the confines of your data structure.

<a id="sec-manifestations"></a>
#### Manifestations
Express the relationship between a Variant and a Manifestation (e.g., Part/part of).
Describe or demonstrate Variant-to-Manifestation relationships through linking to the Variant identifier, through the usage of relator terms, or according to the confines of your data structure.

[^fn1]: EN 15907 8.1 Relationships. General

