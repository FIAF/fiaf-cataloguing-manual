---
title: Variants
weight: 3
---
<a id="sec-moving_image_variants_definition"></a>
## Definitions[^fn1]
Brief definitions of the standard CEN terms Work/Variant/Manifestation/Item used in the Manual were provided at the end of the Introduction (see [Introduction](/docs/00_preliminary/#sec-introduction)).
This section provides an in-depth definition of the term Variant.

<a id="sec-moving_image_variant"></a>
### Moving Image Variant[^fn2]
A moving image Variant is an entity that may be used to indicate any change to content-related characteristics that do not significantly change the overall content of a Work as a whole.
Such Variants can be produced by minor additions, deletions or substitutions to the content.
As a general guideline, changes that would result in a different content description should be treated as a separate Work rather than a Variant, particularly regarding EN15907 standard.

Changes that could be described as Variants are detailed in [Boundaries between Works and Variants](/docs/14_appendix_06/#sec-boundaries_between_works_and_variants), and may include the addition of subtitles, dubbing, and editing as a result of censorship or adjustment of duration, e.g. for TV programming.
For institutions that have made a policy decision not to use the Variant, these changes may constitute Manifestation differences.

The determination of a Variant requires human analysis, and as such is an interpretative practice.
It is not always easy to establish what the Variants may be.
For example, an institution may have a television recording of a motion picture broadcast but no way of comparing it with an original theatrical copy as to whether it has been altered in terms of subtle censorship of content or duration

**Therefore, this entity is optional.** If employed, each instance of a Variant is related to a Work and can have one-to-many relationships with instances of Manifestation(s), and many-to-many relationships with Event(s), Agent(s) and Other Relation(s). If no Variant of a Work exists or is known to exist, then this entity can be omitted, connecting an instance of a Work with one or more instances of Manifestation. The above is the case under EN15907, but please note that the Variant is an integral part of the data architecture of IFLA Library Reference Model (LRM), so if the latter standard is being used in your institution then use of Variants would be expected.

[^fn1]: For a discussion of other definitions of the “Work” and Variant entities, see \nameref{sec:moving_image_works
[^fn2]: Adapted from EN 15907, 4.2 Variant.

