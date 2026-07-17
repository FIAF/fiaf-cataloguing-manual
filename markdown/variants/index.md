---
title: Moving Image Variants (i.e. Versions)
---

!!! abstract "Definition"
    An entity that may be used to indicate any change to content-related characteristics that do not significantly change the overall content of a Work as a whole.
    This is similar to a Work since it does not yet describe physical or digital embodiments of the content.
    For example: A film edited for television broadcast will contain most of the content of the original Work, but have some parts edited out.


<a id="sec-moving_image_variant"></a>
# Moving Image Variant[^2]
A moving image Variant is an entity that may be used to indicate any change to content-related characteristics that do not significantly change the overall content of a Work as a whole.
Such Variants can be produced by minor additions, deletions or substitutions to the content.
As a general guideline, changes that would result in a different content description should be treated as a separate Work rather than a Variant, particularly regarding EN 15907 standard.

Changes that could be described as Variants are detailed in [Boundaries between Works and Variants](/boundaries/boundaries_between_works_and_variants/), and may include the addition of subtitles, dubbing, and editing as a result of censorship or adjustment of duration, e.g. for TV programming.
For institutions that have made a policy decision not to use the Variant, these changes may constitute Manifestation differences.

The determination of a Variant requires human analysis, and as such is an interpretative practice.
It is not always easy to establish what the Variants may be.
For example, an institution may have a television recording of a motion picture broadcast but no way of comparing it with an original theatrical copy as to whether it has been altered in terms of subtle censorship of content or duration

**Therefore, this entity is optional.** If employed, each instance of a Variant is related to a Work and can have one-to-many relationships with instances of Manifestation(s), and many-to-many relationships with Event(s), Agent(s) and Other Relation(s). **If no Variant of a Work exists or is known to exist, then this entity can be omitted, connecting an instance of a Work with one or more instances of Manifestation.** The above is the case under EN 15907, but please note that the Variant (aka Expression) is an integral part of the data architecture of IFLA Library Reference Model (LRM), so if the latter standard is being used in your institution then use of Variants (Expressions) would be expected.

[^1]: For a discussion of other definitions of the “Work” and Variant entities, see [Moving Image Works](/other-relationships/#sec-moving_image_works).
[^2]: Adapted from EN 15907, 4.2 Variant.

