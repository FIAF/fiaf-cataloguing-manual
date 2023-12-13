E.5.1 Collection Aggregates Modelling

Many collection aggregates have their own new title, e.g., The Audrey Hepburn col-
lection (consisting of Breakfast at Tiffany’s, Funny face and Sabrina); Heroes of the sky
(consisting of Angels one five, The Dambusters, Aces high); Portrait of a miner (consist-
ing of various Mining review shorts). These should be the titles of the aggregate Manifes-
tation, and also any new aggregating Work record.

The individual component titles may also be added as alternative title types to the

aggregating Work.

Some collection aggregates do not have their own new title, e.g., in 2008, Odeon En-
tertainment released a DVD double-bill of classic British thrillers, Bond of fear (1956) and
Blackout (1950), with no collection title.

The  treatment  of  the  aggregate  title  may  differ  from  institution  to  institution,  es-
pecially  in  cases  where  multiple  Works  are  contained  in  the  collection  aggregate  and
recording all titles in a single title field would be unwieldy. There is the option of an insti-
tution using a devised/supplied title (see A.2.5 Supplied/Devised Titles).

Examples

Bond of fear ; Blackout
Bond of fear; [other segment]
[Odeon Entertainment double feature: Bond of fear and
Blackout [DVD double feature]]



E.5.1.1 Model: Collection Aggregate Manifestation with-
in one-to-many Works/Variants-Manifestations

This model involves creation of a new aggregating Work record. Works link together in
associative  relationship  “contains/contained  in”  and  aggregate  Manifestation  links  to
aggregating Work in “part of” relationship.

Sabrina
(1954) (Work)

The Audrey Hepburn Collection
(2008) (Work)

Funny Face
(1956) (Work)

Breakfast at
Tiffanys
(1961) (Work)

The Audrey Hepburn Collection
(DVD Manifestation, 2008) (Collection Aggregate)

The Audrey Hepburn Collection
(DVD Item)



E.5.1.2 Model: Collection Aggregate Manifestation with-
in many-to-many Works/Variants-Manifestation

A single Aggregate Manifestation links to the many individual Works/Variants in “part
of” relationship.

Sabrina
(1954) (Work)

Funny Face
(1956) (Work)

Breakfast at Tiffanys
(1961) (Work)

The Audrey Hepburn Collection
(DVD Manifestation, 2008) (Collection Aggregate)

The Audrey Hepburn Collection
(DVD Item)



E.5.1.3 Model: Collection Aggregate Manifestation with
no aggregated Item, only unaggregated individual
Items

This model involves creation of a new aggregating Work record.

The original individual Works and aggregating Work link together in associative rela-
tionship “contains/contained in” and aggregate Manifestation links to aggregating Work
in “part of” relationship, with individual Items rather than one aggregated Item linking
to aggregate Manifestation in “part of” relationship.

This model may occur particularly with internet broadcasts and digital files, where-
by  an  aggregate  Internet  Manifestation  is  available  as  an  Internet  broadcast,  but  is
streamed in from individual digital files (i.e. individual Items) seamlessly and consecu-
tively, not from a single aggregated digital file, i.e. a thematic compilation of three short
films of the late 19th century is devised and entitled “Victorian Cinema 3”228. The internet
user views the whole aggregate Manifestation as one entity, but it is streamed from sep-
arate digital Items streamed seamlessly one after the other.

Pierrots
(Work, c.1902)

Victorian Cinema 3
(Work, 1998)

Lady Cyclists
(Work, 1899)

Victorian Cinema 3
(Internet Manifestation, 2014)

Washing
the Sweep
(Work, 1898)

Pierrots
(Digital Item)

Lady Cyclists
(Digital Item)

Washing the Sweep
(Digital Item)

228  Example Victorian Cinema 3 is an illustrative example only, and not yet streamed in this way



In the above scenario each of the Items could be given the same location/package num-
ber and each could have the alternative title of “Victorian Cinema 3”. Similarly, the in-
dividual  titles  could  also  be  added  as  alternative  titles  to  the  aggregating  Work  if  an
institution wishes, to aid searchability and access.
