---
title: Relationships of a Manifestation
---
A relationship associates an instance of Manifestation with another instance of an entity.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.[^1] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest.

A Manifestation may have relationships with the following:

- Agent(s)
- Event(s)
- Other
- Item(s)
- Work
- Variant

<a id="sec-manifest_events"></a>
## Events
An Event characterises occurrences in the life cycle of a moving image Manifestation.
Instances of any Event type can have Agent and “Other” relationships.

Record one or more Event type, for example, “decision,” “manufacture,” etc., to express the nature of the Event’s relationship to the Manifestation.
Selection should be made from a controlled list of terms.
A suggested list, which is open and not exhaustive, can be found in [Event Type](/07_events/event_type/#sec-event_type).

[^1]: EN 15907 8.1 Relationships. General

