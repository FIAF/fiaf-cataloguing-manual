\newpage
\subsection{E.5.1.3 Model: Collection Aggregate Manifestation with no aggregated Item, only unaggregated individual Items}

This model involves creation of a new aggregating Work record.

The original individual Works and aggregating Work link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship, with individual Items rather than one aggregated Item linking to aggregate Manifestation in “part of” relationship.

This model may occur particularly with internet broadcasts and digital files, whereby an aggregate Internet Manifestation is available as an Internet broadcast, but is streamed in from individual digital files (i.e. individual Items) seamlessly and consecutively, not from a single aggregated digital file, i.e. a thematic compilation of three short films of the late 19th century is devised and entitled “Victorian Cinema 3”[^228].
The internet user views the whole aggregate Manifestation as one entity, but it is streamed from separate digital Items streamed seamlessly one after the other.

```pikchr
B1: box rad 5px "Pierrots" "(Work, c.1902)" fit at (0,3) 

B2: box rad 5px "Victorian Cinema 3" "(Work, 1998)" fit at (1.5,3) 

B3: box rad 5px "Lady Cyclists" "(Work, 1899)" fit at (3,3) 

B4: box rad 5px "Washing the Sweep" "(Work, 1898)" fit at (3,2) 

B5: box rad 5px "Victorian Cinema 3" "(Internet Manifestation, 2014)" fit at (1.5,1) 

B6: box rad 5px "Pierrots" "(Digital Item)" fit at (0,0) 

B7: box rad 5px "Lady Cyclists" "(Digital Item)" fit at (1.5,0) 

B8: box rad 5px "Washing the Sweep" "(Digital Item)" fit at (3,0) 

arrow <-> from B1.e to B2.w

arrow <-> from B2.e to B3.w

arrow <-> from B2.s to B5.n

arrow right 0.2 from B2.e then down until even with B4 then right to B4.w

arrow left from B5.w then left until even with B6 then right to B6.n

arrow <-> from B5.s to B7.n

arrow right 0.2 from B5.e then right until even with B8 then right to B8.n
```



In the above scenario each of the Items could be given the same location/package number and each could have the alternative title of “Victorian Cinema 3”.
Similarly, the individual titles could also be added as alternative titles to the aggregating Work if an institution wishes, to aid searchability and access.

[^228]: Example Victorian Cinema 3 is an illustrative example only, and not yet streamed in this way
