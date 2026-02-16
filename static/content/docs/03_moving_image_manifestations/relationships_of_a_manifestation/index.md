---
title: Relationships of a Manifestation
weight: 4
---
<a id="sec-relationships_of_a_manifestation"></a>
### Relationships of a Manifestation
A relationship associates an instance of Manifestation with another instance of an entity.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.[^fn1] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest.

A Manifestation may have relationships with the following:

- Agent(s)
- Event(s)
- Other
- Item(s)
- Work
- Variant

<a id="sec-manifest_events"></a>
#### Events
An Event characterises occurrences in the life cycle of a moving image Manifestation.
Instances of any Event type can have Agent and “Other” relationships.

Record one or more Event type, for example, “decision,” “manufacture,” etc., to express the nature of the Event’s relationship to the Manifestation.
Selection should be made from a controlled list of terms.
A suggested list, which is open and not exhaustive, can be found in [Event Type](/docs/12_appendix_04/event_type/#sec-event_type).

<a id="sec-manifest_other_relationships"></a>
#### “Other” Relationships
Expresses relationships that are not covered by the Agent and Event relationships.
Aggregation relationships are expressed at the Work/Variant level (see [Aggregates (Compilations, Multi-component productions)](/docs/13_appendix_05/)).

Commonly-occurring relationships include:

*Manifestations that the moving image Manifestation forms part of (e.g. series/serials).*

> [!EXAMPLE]
> Le cryptogramme rouge (35mm print, m 984, m 48’ (18fps) <br/>
> 3° episode of the serial Les vampires (L. Feuillade, 1915).

*Manifestation(s) that the moving image Manifestation has a sequential relationship with (e.g. series/serials).*

*Manifestation(s) that are promotional material(s) (i.e. trailers) for a particular Manifestation.*

> [!EXAMPLE]
> Rashomon (Japan, 1950, A. Kurosawa) “has as promotional material”: Rashomon, Italian trailer (35mm), of the Italian theatrical release (1952).

*Non-moving image Works/Manifestation(s), about or relating to the moving image Manifestation (e.g. objects, articles, documents such as a review relating to a DVD home video publication, advertising materials referring to a specific theatrical distribution, related materials such as censorship visas, laboratory technical papers, etc.)*

> [!EXAMPLE]
> Metro. Issue 157. June 2008. “DVD review: Blade Runner: The Final Cut”, by Steven Aoun.

> [!EXAMPLE]
> Der Dritte Mann (German film poster for the German-language Release Manifestation of the film The third man (United Kingdom, 1949, Carol Reed)

*Pre-release Manifestation(s) relating to a Release Manifestation.*

> [!EXAMPLE]
> Blow-up (UK-Italy, 1966, Michelangelo Antonioni )and Blow-up censorship cuts (35mm) of the Italian theatrical release (1967).

> [!EXAMPLE]
> Othello, Orson Welles, USA- Italy-Morocco-France, 1952 and Otello, dailies and rushes, positive silent and some with sound, 35mm, containing shots included in only a very limited extent in the first theatrical release (their title proper in Italian is: Otello).

Record one or more “Other” relationship type to express the nature of the relationship to the Manifestation, choosing the most specific term possible from existing relator terms lists, for example, “commentary on,” “review of,” etc. 
Selection should be made from a controlled list of values.
A suggested list, which is open and not exhaustive, can be found in [Manifestation Other Relationship Types](/docs/12_appendix_04/other_relationships_for_works_variants_manifestations_items/#sec-manifestation_other_relationship_types).

Or, compose a term to describe the relationship between the Manifestation being catalogued and the related Manifestation.

In a note, add any additional information concerning the relationship considered relevant.

Describe or demonstrate Manifestation-to-Manifestation relationships through linking to the Manifestation identifier of the related Manifestation, through the usage of relator terms, or according to the confines of your data structure.

If the cataloguing system allows the procedure, attach a digital file that reproduces any associated “document.”

<a id="sec-items"></a>
#### Item(s)
Express the relationship between a moving image Manifestation and a moving image Item (e.g. Part/part of).

Here could be listed the unique Item identifiers associated to this Manifestation, noting their “part of “ relationships to the Manifestation.

<a id="sec-work"></a>
#### Work
Express the relationship between a moving image Manifestation and a moving image Work (e.g., Part/part of).
Describe or demonstrate Manifestation-to-Work relationships through linking to the Manifestation identifier, through the usage of relator terms, or according to the confines of your data structure.

<a id="sec-variant"></a>
#### Variant
Express the relationship between a moving image Manifestation and a moving image Variant (e.g., Part/part of).
Describe or demonstrate Manifestation-to-Variant relationships through linking to the Manifestation identifier, through the usage of relator terms, or according to the confines of your data structure.

[^fn1]: EN 15907 8.1 Relationships. General

