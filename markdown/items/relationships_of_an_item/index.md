---
title: Relationships of an Item
---
A relationship associates an instance of an Item with another instance of an entity.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.[^1] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest.

An Item may have relationships with the following:

- Agent(s), see [Agents for Items](/preliminary/core_agents_fof_items/#sec-agents_for_items)
- Event(s)
- Other
- Manifestation

<a id="sec-items_events"></a>
## Events
An Event characterises occurrences in the life cycle of a moving image Item.
Instances of any Event type can have Agent and “Other” relationships.

Record one or more Event types, for example, “preservation,” “inspection,” “acquisition”, etc., to express the nature of the Event’s relationship to the Item.
Selection should be made from a controlled list of terms.
A suggested list, which is open and not exhaustive, can be found in [Event Type](/events/event_type/#sec-event_type).

[^1]: EN 15907 8.1 Relationships. General

