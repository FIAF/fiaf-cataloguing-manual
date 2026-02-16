---
title: Relationships of an Item
weight: 3
---
<a id="sec-relationships_of_an_item"></a>
### Relationships of an Item
A relationship associates an instance of an Item with another instance of an entity.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.[^fn1] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest.

An Item may have relationships with the following:

- Agent(s)
- Event(s)
- Other
- Manifestation

<a id="sec-items_events"></a>
#### Events
An Event characterises occurrences in the life cycle of a moving image Item.
Instances of any Event type can have Agent and “Other” relationships.

Record one or more Event types, for example, “preservation,” “inspection,” “acquisition”, etc., to express the nature of the Event’s relationship to the Item.
Selection should be made from a controlled list of terms.
A suggested list, which is open and not exhaustive, can be found in [Event Type](/docs/12_appendix_04/event_type/#sec-event_type).

<a id="sec-item_other_relationships"></a>
#### Other Relationships
Express relationships that are not covered by the Agent and Event relationships.
These may include compilations of convenience, i.e. where an institution has transferred copies
of two or more films onto one reel/tape/DVD etc. for convenient storage.[^fn2](/docs/13_appendix_05/identifying_aggregates/#sec-aggregate_or_carrier)]

*Item(s) associated with the moving image Item.*

It is possible for a moving image Item to have a horizontal relationship with another Item as a related object.
Such associative relationships are more prevalent and varied at the Work level, but there are instances where Items need to be related, for example, where an institution has separate Items for Yellow, Cyan and Magenta Separation Negatives, each of which have to be combined in Technicolor Three Colour Strip Process to make a new colour print.
Or, hold separate sound and image Items that would both be needed to make a new print.
Similarly, in the case of restorations where separate Items or elements have been used to create a new restored Item.

> [!EXAMPLE]
> The Wizard of Oz (United States of America, 1939, Victor Fleming) <br/>
> Yellow Separation Negative, Cyan Separation Negative, Magenta Separation Negative

> [!EXAMPLE]
> Local hero (United Kingdom, 1983, Bill Forsyth) <br/>
> DPX sequence, WAV audio file

*An Item that contains other Items (e.g. two or more separate Items are held on the same reel/tape/DVD etc. for convenient storage).*

> [!EXAMPLE]
> Selezione Fregoli 2002 <br/>
> Compilation of 16 short Fregoli films, spliced together for projection convenience.

> [!EXAMPLE]
> Laughing gas (United States of America, 1914, Charlie Chaplin) <br/>
> Those love pangs (United States of America, 1914, Charlie Chaplin) <br/>
> (two Charlie Chaplin short comedies spliced together on one reel - for storage convenience).

*Item that is the source of a moving image Item (e.g. In-house copying of an Item to create a new Item for preservation or access)*

> [!EXAMPLE]
> 35mm CTA Duplicating Postive copy of Carnival (c.1927) made from a 35mm <br/>
>   Nitrate Negative copy of Carnival (c.1927)

*Non-moving image Works/Items (e.g. Objects, documents, etc. relating to a specific Item)*

> [!EXAMPLE]
> Shots of 1932 (United Kingdom, 1932) (home movie) 9.5mm Safety film Item related to paper donor agreement

Record one or more “Other” relationship type terms to express the nature of the relationship to the Item, choosing the most specific term possible from existing relator terms lists, for example, “accompanied by,” “contained in,” etc. Selection should be made from a controlled list of values.
A suggested list, which is open and not exhaustive, can be found in [Item Other Relationship Types](/docs/12_appendix_04/other_relationships_for_works_variants_manifestations_items/#sec-item_other_relationship_types).

In a note, add any additional information concerning the relationship considered relevant.

If the cataloguing system allows, attach a digital file that reproduces any associated “document”.

<a id="sec-manifestation"></a>
#### Manifestation
Express the relationship between a moving image Manifestation and a moving image Item (e.g. Part/part of).

[^fn1]: EN 15907 8.1 Relationships. General
[^fn2]: See Appendix [Aggregate or Carrier

