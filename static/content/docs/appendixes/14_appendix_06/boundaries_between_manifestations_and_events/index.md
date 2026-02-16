---
title: Boundaries between Manifestations and Events
weight: 1
---
<a id="sec-boundaries_between_manifestations_and_events"></a>
### Boundaries between Manifestations and Events
As mentioned at [INSERT INTERNAL LINK TO RELEVANT SECTION IN MANUAL], there is no rule within EN15907 as to the categories of Manifestation Type there can be, only that its values come from a controlled vocabulary list. The only one stipulated value that exists is that of a category of ‘Unknown’.

Overlaps that have evolved between use of Manifestations and Events, and Manifestation types and Event Publication types, have partly been due to some ambiguity within the EN15907 standard itself. But also, how the latter has been interpreted and evolved since it was conceived in order to deal with the nature and range of actual moving image material and technological developments; as well as the realities and practicalities for institutions using different cataloguing systems and databases, and user access needs.

| **Manifestation types** | **Event Publication types** |
| --- | --- |
| Theatrical distribution | Theatrical distribution |
| Non-theatrical distribution | Non-theatrical distribution |
| Broadcast | Broadcast |
| Internet | Online transmission |
| Pre-release | Pre-release |
| Home viewing | Home video publication |
| Unknown | Unknown | 

The boundaries between Manifestations and Events and structuring decisions will be dependent on the types of records, architecture, and concatenation and display capabilities of multiple linked data within an institution’s database or other cataloguing system. 

Some system databases may not have the ability or full functionality to have Events records, but do have Manifestations; in which case they may make use of a wider list of Manifestation Types and have fields relating to EN15907 Events data embedded within the Manifestation record itself. These systems will be more likely to make use of a structure of multiple Manifestations rather than one Manifestation with multiple publication Events.
For example:

```pikchr
W: box rad 5px "Work" at (2.5,1) 
M1: box rad 5px "Theatrical Manifestation." "Germany, January 1995." "35mm film, 96 minutes, in German" at (0,0) fit
M2: box rad 5px "Theatrical Manifestation." "Austria, March 1995." "35mm film, 96 minutes, in German" at (2.5,0) fit
M3: box rad 5px "Theatrical Manifestation." "Switzerland, February 1995." "35mm film, 96 minutes, in German"  at (5,0) fit
arrow down 0.2 from W.s then right until even with M1 then down to M1.n
arrow from W.s to M2.n
arrow down 0.2 from W.s then left until even with M3 then down to M3.n
```

The EN15907 standard does not have date or release country as being core elements of a Manifestation, envisaging that information being in an associated Event. However, many systems do include those fields within their Manifestation records, as actual attributes of the Manifestation, as can be seen in some of the examples featured in Appendix I.[ADD LINK] In systems with no, or minimal, Events records capabilities it is the most logical alternative place to capture that important relevant data.

Other systems may have developed and utilise Events more in line with EN15907 to reflect data about different releases in various countries, e.g.   

```pikchr
W: box rad 5px "Work" at (0,2) 
M: box rad 5px "Theatrical Manifestation." "35mm film, 96 minutes, in German" at (0,0.75) fit 
E1: box rad 5px "Theatrical publication." "Event in Germany," "January 1995" at (2.5,1.5) fit
E2: box rad 5px "Theatrical publication." "Event in Austria," "March 1995" at (2.5,0.75) fit
E3: box rad 5px "Theatrical publication." "Event in Switzerland," "February 1996 " at (2.5,0) fit
arrow from W.s to M.n
arrow right 0.2 from M.e then up until even with E1 then right to E1.w
arrow from M.e to E2.w
arrow right 0.2 from M.e then down until even with E3 then right to E3.w
```

Structuring decisions around Manifestations and Events may also depend on the nature, size, use, and user needs of an institution’s moving image collections.

In many cases, an institution is only going to create those Manifestations that pertain to acquired Item(s) in their collections, rather than add data about all international releases generally, so there will not usually be a need for a complexity of multiple linked Manifestations and/or Events records and data.  

A broadcast as a Publication Event could suit where collections consist solely of cinematographic films. However, several institutions have collections consisting of both films and television programmes, where there needs to be a consistency and standardisation in structuring hierarchical metadata .

For a television programme, its broadcast is the actual primary manifestation of its Work not simply an event in the life-cycle of the Work. With the flexibility offered by Manifestation type it is possible and preferable to have a ‘Broadcast’ Manifestation type that can be used with television programme Works, thus maintaining the integrity of the EN15907 hierarchical structure. 
 
This means that the one standard and structuring can be applied with mixed collections within the one moving image database system, rather than try to use EN15907 with films and another standard, such as PBCore, with television programmes. 

Institutions may also not only collect and acquire items, but develop their own VOD (Video on Demand) channels, e.g. BFIplayer which provides a mixture of Free, Subscription and Transactional VOD, using digital items to stream the content.
Thus, having an Internet Manifestation type means that both acquired or produced VOD materials can be captured within an EN15907 structure. The actual digital Items held and representing records for the files used in streaming can then be linked to these Manifestations.

There is also the consideration of a pure EN15907 structure approach meaning disparate pieces of relevant and related data sitting in the Manifestation and the Event and how that may impact user access. Also, how to cope with a potential tangle of complex structuring with a variety of materials in a collection for the same Work, and realistic resourcing and capabilities of differing database systems used by Archives and institutions. This manual recognises both the purist and pragmatic approaches.

For those cataloguing in non-relational databases, paper or card catalogues, or Excel,  then many of the elements that EN15907 sees as being linked “related” records, including Events, will always be an attribute of the main 1-level hierarchy moving image record.

As with the ability to utilise EN15907 within a 4, 3, 2 or 1-level hierarchy, the same fundamental principle applies with use and structure of Events with Works, Variants, Manifestations or Items; namely, that it does not matter what data systems or structures an institution uses – whether index card or complex computer systems -  as long as their records capture the relevant data concerned.

With a fundamental aim of EN15907 being interoperability, then use of types such as those in the list of Manifestation Types at [INSERT INTERNAL LINK TO RELEVANT SECTION] is key to the flexibility and use of the data architecture reflecting the standard and makes this a lot more achievable; especially in systems where Events structures are minimal or do not exist. Because there is an overlap in Manifestation and Event type terms it could make potential mapping and interoperability achievable.
