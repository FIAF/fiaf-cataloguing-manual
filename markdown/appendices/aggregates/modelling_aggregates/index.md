---
title: Modelling Aggregates
---
An aggregate is a Manifestation, but “the process of aggregating the Works/Variants itself is an intellectual or artistic effort and therefore meets the criteria for a Work.
In the process of creating an aggregate Manifestation, an aggregating Work is produced.
This effort may be relatively minor or represent a major effort resulting in an aggregate that is significantly more than a sum of its parts...
The aggregating Work may or may not be deemed important enough to be recorded.[^1]”

An institution may therefore be able to choose whether to create a new aggregating Work or not, although this flexibility may be restricted by other factors.

In practical terms creating aggregates and how they are modelled, will be determined by structures and capabilities of an institution’s database or other systems.

Under FRBR and CEN an aggregate Manifestation is allowed to have a many-to-many relationship with Works/Variants, i.e., it can have a “part of” relationship with more than one Work/Variant.

However, many database systems are structured in a way that does not allow this and will only permit links or relationships between Manifestation records and a single Work/Variant record at all times, i.e., a one-to-many Work/Variant-Manifestation relationship.

There are also potential implications for those organisations using international identifiers or registration numbers, e.g., ISAN gives a number to what they define “compilation”: “a compilation work is a collection of two or more separate works (each identified with its own ISAN) in a single distribution package”[^2].

This may have a bearing and impact on decisions relating to whether to produce an aggregating Work or not.

The model of creating an aggregating Work is recommended.
With systems that only allow for a one-to-many Work/Variant-Manifestation relationship, then an aggregating Work should always exist (for Collection, Augmented and Parallel Aggregates), and the aggregate Manifestation linked as “part of” it.

In addition, the multiple independently created moving image Works/Variants of the aggregate should also ideally be created as separate individual Works/Variants, and then linked in an associative relationship using “contains/contained in” terms with the aggregating Work.

It is recognised that the ability to do this may be dependent on sufficient information and details about the individual Works/Variants being available to create such individual records.
Where this is insufficient the titles of the individual Works/Variants making up the aggregate may be added as alternative title types to the aggregating Work.
This will assist in accessibility and identification.

For how aggregate records may be structured in a 1-level hierarchy system see [Example 7. Aggregate DVD Television Serial and Episode records in 1-level Hierarchy Models](/appendices/record-examples/example_seven/#sec-example_seven).
Whilst this relates to a television example the same principles can be applied in the case of film collection and augmented collection aggregates.

<a id="sec-collection_aggregates_modelling"></a>
## Collection Aggregates Modelling
Many collection aggregates have their own new title, e.g., The Audrey Hepburn collection (consisting of Breakfast at Tiffany’s, Funny face and Sabrina); Heroes of the sky (consisting of Angels one five, The Dambusters, Aces high); Portrait of a miner (consisting of various Mining review shorts).
These should be the titles of the aggregate Manifestation, and also any new aggregating Work record.

The individual component titles may also be added as alternative title types to the aggregating Work.

Some collection aggregates do not have their own new title, e.g., in 2008, Odeon Entertainment released a DVD double-bill of classic British thrillers, Bond of fear (1956) and Blackout (1950), with no collection title.

The treatment of the aggregate title may differ from institution to institution, especially in cases where multiple Works are contained in the collection aggregate and recording all titles in a single title field would be unwieldy.
There is the option of an institution using a devised/supplied title (see [Supplied/Devised Titles (i.e. Creating titles for untitled/unidentified entities or production material)](/appendices/titles/title_types/#sec-supplied_devised_titles)).

!!! example "Example"
    Bond of fear ; Blackout <br/>
    Odeon Entertainment double feature: Bond of fear and Blackout [DVD double feature] <br/>
    Bond of fear and Blackout (double feature)

<a id="sec-collection_aggregate_manifestation_within_a_one_to_many"></a>
### Model: Collection Aggregate Manifestation within a one-to-many Works/Variants-Manifestations database system
This model involves creation of a new aggregating Work record.
Works link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship.

![](/diagrams/figure_10.png)

<a id="sec-collection_aggregate_manifestation_within_a_many_to_many"></a>
### Model: Collection Aggregate Manifestation within a many-to-many Works/Variants-Manifestation database system
A single Aggregate Manifestation links to the many individual Works/Variants in “part of” relationship.

![](/diagrams/figure_11.png)

<a id="sec-collection_aggregate_manifestation_with_no_aggregated_item"></a>
### Model: Collection Aggregate Manifestation with no aggregated Item, only unaggregated individual Items
This model involves creation of a new aggregating Work record.

The original individual Works and aggregating Work link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship, with individual Items rather than one aggregated Item linking to aggregate Manifestation in “part of” relationship.

This model may occur particularly with internet broadcasts and digital files, whereby an aggregate Internet Manifestation is available as an Internet broadcast, but is streamed in from individual digital files (i.e. individual Items) seamlessly and consecutively, not from a single aggregated digital file, i.e. a thematic compilation of three short films of the late 19th century is devised and entitled “Victorian Cinema 3”[^3].
The internet user views the whole aggregate Manifestation as one entity, but it is streamed from separate digital Items streamed seamlessly one after the other.

![](/diagrams/figure_12.png)

In the above scenario each of the Items could be given the same location/package number and each could have the alternative title of “Victorian Cinema 3”.
Similarly, the individual titles could also be added as alternative titles to the aggregating Work if an institution wishes, to aid searchability and access.

<a id="sec-augmented_collection_aggregate"></a>
## Augmented Collection Aggregate
Augmented Collections can vary considerably from simple augmentations, e.g., the Work(s) plus a selection of special features such as bonus scenes and a photo gallery with some commentary; or, more complex augmentations.

Modelling for Augmented Collection Aggregates follows the same principles as those for Collection Aggregates.

<a id="sec-augmented_aggregate_manifestation_within_a_one_to_many"></a>
### Model: Augmented Aggregate Manifestation within a one-to-many Work/Variants-Manifestations database system
This involves creation of a new aggregating Work record.
Works link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship.

![](/diagrams/figure_13.png)

<a id="sec-augmented_aggregate_manifestation_within_a_many_to_many"></a>
### Model: Augmented Aggregate Manifestation within a many-to-many Work/Variants-Manifestations database system
Single Aggregate Manifestation links to all individual Works/Variants in “part of” relationship.

![](/diagrams/figure_14.png)

An institution can choose whether to create all components of the Augmented aggregate Manifestation as Works, or selected ones.

However, in cases of Augmented Aggregates it is recommended to always create a corresponding aggregating Work, as the Work record will contain relevant fields for extra data such as new credits pertaining just to the aggregate.
Similarly synopsis or notes fields can then be utilised to give full description of contents.

More importantly, it is not always practical or feasible for many cataloguing systems to deal with creating records for non-moving image materials such as booklets, or text.

!!! example "Example"
    Charlie Chaplin. The Mutual films. Volume 1. <br/>
    Contains: 6 short Chaplin Mutual films – Behind the screen, The immigrant, Easy Street, The rink, The cure, The adventurer. Plus DVD extras: Topical Budget newsreel footage of Chaplin on voyage and visit back to Britain; filmed interview with Carl Davis [who did music soundtrack for the aggregate]; on-screen text biographies of Edna Purviance and Eric Campbell. Plus sleeve notes by Frank Scheide.

An aggregating Work record for the above enables adding of credits, for example, the music composer for the soundtrack on the aggregate, the interviewees, etc.; associative “contains/contained in” relationship links to any individual films or newsreel works; and then any other remaining details of the Work that cannot be linked in associative relationships may be added as free text in synopsis or notes fields.

[^1]: Working Group on Aggregates. Final Report of the Working Group on Aggregates, September 12, 2011, [http://www.ifla.org/files/assets/cataloguing/frbrrg/AggregatesFinalReport.pdf](http://www.ifla.org/files/assets/cataloguing/frbrrg/AggregatesFinalReport.pdf)
[^2]: Definition of “Compilation” in [http://www.isan.org/resources/glossary.html#index_A](http://www.isan.org/resources/glossary.html#index_A) (ISAN Glossary of Terms)
[^3]: Example Victorian Cinema 3 is an illustrative example only, and not yet streamed in this way

