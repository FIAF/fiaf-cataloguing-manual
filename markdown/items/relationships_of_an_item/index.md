---
title: Relationships of an Item
---
A relationship associates an instance of an Item with another instance of an entity.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.[^1] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest.

An Item may have relationships with the following:

- Agent(s)
- Event(s)
- Manifestation
- Other relationship(s)
 
<a id="sec-items_agents"></a>
## Agent(s)
For relationships with Agent's see [Agents for Items](/preliminary/core_agents_fof_items/#sec-agents_for_items)

<a id="sec-items_events"></a>
## Event(s)
An Event characterises occurrences in the life cycle of a moving image Item.
Instances of any Event type can have Agent and “Other” relationships.

Record one or more Event types, for example, “preservation,” “inspection,” “acquisition”, etc., to express the nature of the Event’s relationship to the Item.
Selection should be made from a controlled list of terms, see [Event Type For Items](/events/event_types_for_items/#sec-event_types_for_items).

<a id="sec-items_other_relationships"></a>
## Other relationship(s)
For Other relationships see [ADD LINK TO CURRENT 9.3.5 OTHER RELATIONSHIPS CHAPTER]

<a id="sec-items_manifestations"></a>
## Manifestation(s)
 See [ADD LINK TO CURRENT 9.3.2 Item(s)]
[^1]: EN 15907 8.1 Relationships. General

