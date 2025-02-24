\subsection{E.7.1 Film/Video or TV series/serials}

On the surface these would seem to be aggregates as it could be argued they are made up of different components (episodes) brought together to make a “whole” (series/serial).
However, it is not logical under the definitions of aggregates to structure and view TV or film/video serial/series as aggregating Works.

The starting point of an aggregate is the Manifestation “embodying two or more Works/Variants.” Each episode of a film/video or TV series/serial has its own unique individual release/broadcast Manifestation, not a single aggregate one.
There was never the original intention for all the episodes (independent individual Works/Variants) to be released/broadcast in one single Manifestation.

A later subsequent DVD publication or digital file production may occur, warranting an aggregate Manifestation, but this does not happen with all series/serials.

Where an institution’s cataloguing system has Work Series-Work Monographic hierarchy structure then the aggregate Manifestation of a DVD release/boxed set of the series/serial, or multiple episodes from that series, could be linked as “part of” the Work Series record.

There could then be a clarifying note on the Manifestation where necessary, i.e. to clarify which episodes are included if the series continued with more episodes not on the particular aggregate Manifestation, or the aggregate Manifestation pertained to one particular series/season within the Series.

See example below for The thick of it DVD boxed set:

```pikchr
B1: box rad 5px "The Thick of It" "(Work - Serial)" fit at (2,4) 

B2: box rad 5px "The Thick of It" "The Complete Series 1-3 & Specials" "(DVD Manifestation) (Collection Aggregate)" fit at (0,3) 

B3: box rad 5px "The Thick of It" "The Complete Series 1-3 & Specials" "(DVD Item)" fit at (0,0) 

B4: box rad 5px "The Thick of It" "Episode 1" "(Work - Monographic)" fit at (2,2) 

B5: box rad 5px "The Thick of It. Episode 1" "(TV transmission)" "Manifestation" fit at (2,1) 

B6: box rad 5px "The Thick of It. Episode 1" "(VHS Cassette Item)" fit at (2,0) 

B7: box rad 5px "The Thick of It" "Episode 2" "(Work - Monographic)" fit at (4,2) 

B8: box rad 5px "The Thick of It. Episode 2" "(TV transmission)" "Manifestation" fit at (4,1) 

B9: box rad 5px "The Thick of It. Episode 2" "(VHS Cassette Item)" fit at (4,0) 

arrow <-> left from B1.w then left until even with B2 then down to B2.n

arrow <-> from B2.s to B3.n

arrow <-> from B2.s to B3.n

arrow <-> from B1.s to B4.n

arrow <-> from B4.s to B5.n

arrow <-> from B5.s to B6.n

arrow <-> right from B1.e then right until even with B7 then down to B7.n

arrow <-> from B7.s to B8.n

arrow <-> from B8.s to B9.n


```



Alternatively, a model similar to [E.5.1.2 Model: Collection Aggregate Manifestation within many-to-many Works/Variants-Manifestation](#manual-E.5.1.2) can be used, whereby a single Aggregate Manifestation links to the many individual Works/Variants in “part of” relationship:

```pikchr
B1: box rad 5px "ER (Work - Serial)" fit at (1,3) 

B2: box rad 5px "ER. One Day" "(Season 1, Episode 1)" "(Work – Monographic)" fit at (0,2) 

B3: box rad 5px "ER. Going Home" "(Season 1, Episode 2)" "(Work – Monographic)" fit at (2,2) 

B4: box rad 5px "etc." invis fit at (4,2) 

B5: box rad 5px "ER. The Complete First and Second Season" "(Season 1, Episode 2)" "(DVD Manifestation (Collection Aggregate)" fit at (1,1) 

B6: box rad 5px "ER. The Complete First and Second Season" "(Season 1, Episode 2)" "(DVD Item)" fit at (1,0) 

arrow left 0.2 from B1.w then left until even with B2 then down to B2.n

arrow down 0.2 from B2.s then right until even with B5 then down to B5.n

arrow right 0.2 from B1.e then right until even with B3 then down to B3.n

arrow down 0.2 from B3.s then right until even with B5 then down to B5.n

arrow down 0.34 from B4.s then right until even with B5 then down to B5.n

arrow <-> from B5.s to B6.n
```

Where this Serial Work–Monographic Work hierarchy structure does not exist, then a new aggregating Work may be created and linked via an associated contains/contained in relationship in line with models for any other Collection Aggregate.

```pikchr
B1: box rad 5px "ER – The Complete First" "and Second Season" "(Work – Monographic)" fit at (0,3) 

B2: box rad 5px "ER – The Complete First" "and Second Season" "(DVD Manifestation – 4 disc set)" "(Collection Aggregate)" fit at (0,0) 

B3: box rad 5px "ER. Day One" "(Season 1, Episode 1)"  "(Work – Monographic)" fit at (3,3) 

B4: box rad 5px "ER. Day One" "(TV transmission Manifestation)"  "22/09/1994" fit at (3,2) 

B5: box rad 5px "ER. Going Home" "(Season 1, Episode 2)"  "(Work – Monographic)" fit at (3,1) 

B6: box rad 5px "ER. Going Home" "(TV transmission Manifestation)"  "29/09/1994" fit at (3,0) 

arrow <-> from B1.s to B2.n

arrow <-> from B3.s to B4.n

arrow <-> from B5.s to B6.n

arrow <-> from B1.e to B3.w

arrow right 0.2 from B1.e then down until even with B5 then right to B5.w
```

For how this might be modelled in a flat or single hierarchy system see [I.7 Example 7. Aggregate DVD Television Serial and Episode records in 1-level Hierarchy Models](#manual-I.7)

It is also possible for particular individual episodes from different moving image series/serials to be taken and formed together into a Collection or Augmentation Aggregate, in which case they would then follow the same pattern of structure as any other such aggregate, i.e. with an aggregate Manifestation and aggregating Work record, and associative relationship links to any existing individual Work/Variant episode records.


