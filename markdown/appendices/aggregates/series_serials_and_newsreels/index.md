---
title: Series, Serials and Newsreels
---
All the above examples and modelling of aggregates have purposefully not included newsreels or film or TV series/serials.
This is because these do not actually constitute aggregates under the Aggregates definition.

FRBR includes the terms “serials” and “series” within examples of Collection Aggregates.
However, these are in relation to bibliographic materials, and moving image series/serials are not the equivalent of articles written for a periodical, but different in nature.

<a id="sec-film_video_or_tv_series_serials"></a>
## Film/Video or TV series/serials
On the surface these would seem to be aggregates as it could be argued they are made up of different components (episodes) brought together to make a “whole” (series/serial).
However, it is not logical under the definitions of aggregates to structure and view TV or film/video serial/series as aggregating Works.

The starting point of an aggregate is the Manifestation “embodying two or more Works/Variants.” Each episode of a film/video or TV series/serial has its own unique individual release/broadcast Manifestation, not a single aggregate one.
There was never the original intention for all the episodes (independent individual Works/Variants) to be released/broadcast in one single Manifestation.

A later subsequent DVD publication or digital file production may occur, warranting an aggregate Manifestation, but this does not happen with all series/serials.

Where an institution’s cataloguing system has Work Series-Work Monographic hierarchy structure then the aggregate Manifestation of a DVD release/boxed set of the series/serial, or multiple episodes from that series, could be linked as “part of” the Work Series record.

There could then be a clarifying note on the Manifestation where necessary, i.e. to clarify which episodes are included if the series continued with more episodes not on the particular aggregate Manifestation, or the aggregate Manifestation pertained to one particular series/season within the Series.

See example below for The thick of it DVD boxed set:

![](/diagrams/figure_15.png)

Alternatively, a model similar to [Model: Collection Aggregate Manifestation within a many-to-many Works/Variants-Manifestation database system](/appendices/aggregates/modelling_aggregates/#sec-collection_aggregate_manifestation_within_a_many_to_many) can be used, whereby a single Aggregate Manifestation links to the many individual Works/Variants in “part of” relationship:

```{=latex}
\begin{center}
```
![](/diagrams/figure_16.png){ width="300" }
```{=latex}
\end{center}
```

Where this Serial Work–Monographic Work hierarchy structure does not exist, then a new aggregating Work may be created and linked via an associated contains/contained in relationship in line with models for any other Collection Aggregate.

![](/diagrams/figure_17.png)

For how this might be modelled in a flat or single hierarchy system see [Example 7. Aggregate DVD Television Serial and Episode records in 1-level Hierarchy Models](/appendices/record-examples/example_seven/#sec-example_seven)

It is also possible for particular individual episodes from different moving image series/serials to be taken and formed together into a Collection or Augmentation Aggregate, in which case they would then follow the same pattern of structure as any other such aggregate, i.e. with an aggregate Manifestation and aggregating Work record, and associative relationship links to any existing individual Work/Variant episode records.

<a id="sec-newsreels_and_tv_news_current_affairs_programmes"></a>
## Newsreels and TV news/current affairs programmes
These also do not constitute aggregates.

The nature of news/newsreels is that the different stories do not constitute “independently created Works/Variants” and are more akin to multi-component moving images (see [“Hybrid” Aggregates and multi-component moving images (e.g. Anthology/Portmanteau films or TV programmes)](/appendices/aggregates/identifying_aggregates/#sec-hybrid_aggregates_and_multi_component_moving_images)), in that each component is meant to create the whole via filmed links that are an integral planned part and structure of an original single Work concept.

The process of creation of these is with one whole programme in mind made up of different filmed elements – the same as planned different location shooting (and crews) of different scenes in a feature film that are then edited together to create the whole.
It is never envisaged that the individual news stories would ever have an independent individual release/broadcast on their own.

The same principles hold true for film newsreels.

Similarly, many early current affairs TV programmes were designed as “magazine” programmes featuring a balanced mix of stories (often serious and light mix).
These stories also are not “independently created Works/Variants” but filmed by regular crews and personnel associated with a particular current affairs programme, with an overall editorial creative decision and intent of them being one component of a whole individual Work.
The “whole” would then have a Transmission Manifestation.
The component parts do not.

It is possible that only individual components of newsreels/news programmes may be acquired by an institution. In such cases it is simply a matter of a partial/incomplete acquisition, in the same way that only 2 reels of a 3 reel feature film might be acquired. The Item record for that acquisition would be linked as “part of” the whole Manifestation ( see A.2.6.3 Analytics/Components of identified newsreels/cinemagazines )

Where several individual whole components of various newsreels/news programmes have been used to create compilation films or reels, then as described in E.2.1. [ADD LINK] the nature of these should be assessed. As mentioned previously, any aggregate will always have an element of intention, whether simple or complex.

Such compilations constitute Collection Aggregates, i.e. a new Work record would be created for the compilation and then structured in an associative “contains/contained in” relationship with the original whole newsreel issue Work records from which they came.[ADD LINK TO SECTION  E.5.1.3 Collection Aggregates model].

In instances of untitled reels containing multiple different newsreel/cinemagazine story elements, then a partially or fully supplied/devised title can be created, along with any useful additional alternative or help titles (see ADD LINK TO SECTION A.2.5.1 AND A.2.5.2)
