---
title: Value Lists
weight: 13
---
The value lists provided in this appendix are not definitive and are usually limited to a minimum of five examples if more comprehensive lists are available.
If no pre-existing and authoritative lists are available, a non-exhaustive but more comprehensive set of terms is provided.[^fn1] The example terms have come from a variety of institutions.

<a id="sec-work_variant_description_types"></a>
## Work/Variant Description Types
The Types below reflect terms used in Section 4.1.2 Attributes in the CEN standard EN15907. (INSERT LINK TO EN15907 IN A FOOTNOTE along with "The terms and their definitions used in the EN15907 Standard itself are rooted in those from UNESCO CCF/B (Common Communications Format / Bibliographic, UNESCO PGI-92/WS/9, Paris, 1992,(INSERT LINK) which related to bibliographic information.)

**Analytic (component part)**: content that is contained in another content. 
A component part may itself be either monographic or serial. Component here means intentional component part not fragments or excerpts of a moving image, e.g. an individual element from a larger newsreel issue.

> [!EXAMPLE]
> Work [Monographic] – Harry wird Millionär <br/>
> <br/>
> Variant [Analytic (component part)] – Harry wird Millionär. Incomplete German version <br/>
> Manifestation 1: Internet – digital file – [2013] – Deutsches Filminstitut – DIF (internet publisher))http://www.filmportal.de/en/node/640472/video/1227323 – 0 h 16’ 59’’ <br/>
> Item – Harry wird Millionär <br/>
> <br/>
> Variant [Analytic (component part)] – Harry wordt Millionair. Incomplete Dutch version <br/>
> Manifestation 1: Internet – digital file – [2013] – Deutsches Filminstitut – DIF (internet publisher)) http://www.filmportal.de/en/node/27915/video/1227322 – 0 h 15’ 44’’ <br/>
> Item – Harry wordt Millionair <br/>
> <br/>
> Variant [Monographic] – Harry wird Millionär. Reconstructed version <br/>
> Manifestation 1: Internet – digital file – [2013] – Deutsches Filminstitut – DIF (internet publisher)) http://www.filmportal.de/en/node/27915/video/1227166 – 0 h 38’ 56’’ <br/>
> Item – Harry wird Millionär

**Monographic**: Complete content in one part or intended to be completed in a finite number of parts.

This is also applicable to television episodes.
The record for the television series itself is catalogued as a Serial.

> [!EXAMPLE]
> Coronation Street [1960-12-09] <br/>
> Spaced. Series 1 Episode 1. 1999-09-02

**Serial**: Content issued in successive parts and intended to be continued indefinitely, or across a span of time.
A Work record for a television series is catalogued as a “Serial.” Individual episodes may be catalogued as a Monographic record.

> [!EXAMPLE]
> Gaumont British News (1934-) <br/>
> Flash Gordon’s Trip to Mars (1938) <br/>
> Chemistry Essentials (1996) <br/>
> Breaking Bad (2008-01-20 – 2013-09-29)

**Collection**: Content issued in several independent parts; an ‘umbrella’ work title covering a number of different Works/Variants/Manifestations[^fn2].

> [!EXAMPLE]
> Pleasure (Joan Littlewood, c1963) (Footage shot on behalf of Joan Littlewood as part of her ‘Fun Palace’ project.) <br/>
> The ‘Dogme’ films (Each individually numbered.) <br/>
> Shadows of progress: documentary film in post-war Britain 1951-1977

Other uses for Collection:[^fn3]

Archive-acquired collections of works not originally intended for general release or broadcast all have component parts that form the collection as a whole, usually acquired on a series of numerous film reels or videotapes, etc. each with an identifying title.

> [!EXAMPLE]
> David Lean home movies <br/>
> William Butlin personal films <br/>
> Hollywood interviews (unedited production material for series Hollywood) <br/>
> BFI London Film Festival Awards 2010 – production material, etc. <br/>
> Fifties features (videotape collection of production material, with each of the tapes given an identifying acquisition title: <br/>
> B1-3 Sylvia Syms I/V <br/>
> B4-6 Sylvia Syms I/V \& Jill Craigie I/V <br/>

“David Lean home movies,” “Fifties features,” etc. would be the Work titles for the collection-level description, with Collection as its description level.

The individual components of this collection would also be created as individual Monographic Works.

> [!EXAMPLE]
> Egypt <br/>
> India <br/>
> India no.2 <br/>
> Kenya

These titles should then be linked to the collection-level description and assigned “part of” relationship.

Aggregate compilation videos/DVDs that are collections of individual works existing as entities in their own right, e.g. Portrait of a miner is a DVD of various Mining review shorts which had their own individual release as complete entities or works.

- Portrait of a miner would be created as the work title, with the description level of Collection.

- Each of the Mining review Works used in Portrait of a miner would then be linked to it and assigned a “contained in” relationship (see [Modelling Aggregates](/docs/13_appendix_05/modelling_aggregates/#sec-modelling_aggregates)).

Provide a list of the compiled works contained in the Collections Work in its Synopsis or Summary field.

[^fn1]: It is recognised that vocabulary lists often require frequent updates, additions or amendments. For this reason, should resources permit, it would be ideal to separate value lists from the rules and locate them in a central, online repository, like metadataregistry.org. RDF-based repositories like this can supply up-to-date vocabularies on demand and have additional advantages over traditional value lists such as those found in this Appendix.
[^fn2]: This aligns with EN15907 definitions relating to Work types and is different and distinct from Collection Aggregates
[^fn3]: BFI CID Stylistics Manual, A.1.3 Filmographic Level, p. 8

