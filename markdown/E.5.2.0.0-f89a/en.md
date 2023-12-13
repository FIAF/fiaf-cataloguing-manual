E.5.2 Augmented Collection Aggregate

Augmented Collections can vary considerably from simple augmentations, e.g., the
Work(s)  plus  a  selection  of  special  features  such  as  bonus  scenes  and  a  photo  gallery
with some commentary; or, more complex augmentations.

Modelling for Augmented Collection Aggregates follows the same principles as those

for Collection Aggregates.

E.5.2.1 Model: Augmented Aggregate Manifestation
with one-to-many Work/Variants-Manifestations

This involves creation of a new aggregating Work record. Works link together in asso-
ciative relationship “contains/contained in” and aggregate Manifestation links to aggre-
gating Work in “part of” relationship.

Casablanca
(1943) Work

Casablanca. Special Edition
(2003) [Aggregating] Work

Casablanca
(TV Episode,
1955) Work

You Must
Remember
This (1989)
(Work)

Bacall on Bogart
(1988) Work

Carrotblanca
(1995) Work

Casablanca. Trailer
(1942) Work

Casablanca. Special Edition
(DVD Manifestation, 2003)
(Augmented Aggregate)



E.5.2.2 Model: Augmented Aggregate Manifestation for
many-to-many Work/Variants-Manifestations

Single Aggregate Manifestation links to all individual Works/Variants in “part of” rela-
tionship.

Casablanca
(1943) Work

Casablanca
(TV episode 1955)
Work

You Must Remember This
(1989) Work

Bacall on Bogart
(1988) Work

Carrotblanca
(1995) Work

Casablanca Trailer
(1942) Work

Casablanca. Special Edition
(DVD Manifestation, 2003)
(Augmented Aggregate)

An institution can choose whether to create all components of the Augmented aggre-

gate Manifestation as Works, or selected ones.

However, in cases of Augmented Aggregates it is recommended to always create a
corresponding aggregating Work, as the Work record will contain relevant fields for extra
data  such  as  new  credits  pertaining  just  to  the  aggregate.  Similarly  synopsis  or  notes
fields can then be utilised to give full description of contents.

More importantly, it is not always practical or feasible for many cataloguing systems
to deal with creating records for non-moving image materials such as booklets, or text.



Example:

Charlie Chaplin. The Mutual films. Volume 1.
Contains:  6  short  Chaplin  Mutual  films  –  Behind  the  screen,  The  immigrant,
Easy Street, The rink, The cure, The adventurer. Plus DVD extras: Topical Budget
newsreel footage of Chaplin on voyage and visit back to Britain; filmed inter-
view with Carl Davis [who did music soundtrack for the aggregate]; on-screen
text  biographies  of  Edna  Purviance  and  Eric  Campbell.  Plus  sleeve  notes  by
Frank Scheide.

An aggregating Work record for the above enables adding of credits, for example,
the  music  composer  for  the  soundtrack  on  the  aggregate,  the  interviewees,  etc.;  as-
sociative  “contains/contained  in”  relationship  links  to  any  individual  films  or  newsreel
works; and then any other remaining details of the Work that cannot be linked in asso-
ciative relationships may be added as free text in synopsis or notes fields.
