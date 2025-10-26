
\newpage
\section[Moving Image Variants]{Moving Image Variants 
    \label{sec:variant_moving_image_variants}
    } 

\newpage
\subsection[Definitions]{Definitions 
    \footnote {For a discussion of other definitions of the “Work” and Variant entities, see \nameref{sec:moving_image_works}.} 
    \label{sec:moving_image_variants_definition}
    } 

Brief definitions of the standard CEN terms Work/Variant/Manifestation/Item used in the Manual were provided at the end of the Introduction (see \nameref{sec:introduction}).
This section provides an in-depth definition of the term Variant.

\subsubsection[Moving Image Variant]{Moving Image Variant 
    \footnote {Adapted from EN 15907, 4.2 Variant.} 
    \label{sec:moving_image_variant}
    } 
    

A moving image Variant is an entity that may be used to indicate any change to content-related characteristics that do not significantly change the overall content of a Work as a whole.
Such Variants can be produced by minor additions, deletions or substitutions to the content.
As a general guideline, changes that would result in a different content description should be treated as a separate Work rather than a Variant, particularly regarding EN15907 standard.

Changes that could be described as Variants are detailed in \nameref{sec:boundaries_between_works_and_variants}, and may include the addition of subtitles, dubbing, and editing as a result of censorship or adjustment of duration, e.g. for TV programming.
For institutions that have made a policy decision not to use the Variant, these changes may constitute Manifestation differences.

The determination of a Variant requires human analysis, and as such is an interpretative practice.
It is not always easy to establish what the Variants may be.
For example, an institution may have a television recording of a motion picture broadcast but no way of comparing it with an original theatrical copy as to whether it has been altered in terms of subtle censorship of content or duration

**Therefore, this entity is optional.** If employed, each instance of a Variant is related to a Work and can have one-to-many relationships with instances of Manifestation(s), and many-to-many relationships with Event(s), Agent(s) and Other Relation(s). If no Variant of a Work exists or is known to exist, then this entity can be omitted, connecting an instance of a Work with one or more instances of Manifestation. The above is the case under EN15907, but please note that the Variant is an integral part of the data architecture of IFLA Library Reference Model (LRM), so if the latter standard is being used in your institution then use of Variants would be expected.


Attributes of a Variant

Variant Description Type

\subsection[Variant Type]{Variant Type
    \footnote {YCR, 2.1.1 Nature of modification (change in content) of expression} 
    \label{sec:appendix_variant_type}
    } 

Identify and describe the kind of change from a Work that gives rise to any instance(s) of a Variant. Selection should be made from a controlled list of values, for example:

* Censored
* Dubbed
* Subtitled
* Abridged/Condensed (e.g. for television)
* Augmented (where additional content is added, such as director’s cuts with restored scenes, or alternate endings, commentaries)
* Preservation/Restoration
* Different sound track
* Sonorized
* Colourized
* Black and white copy of work originally issued in colour

A change in colour, which is a physical property, expresses a different Manifestation according to the data model this manual follows. However, it is recognised that in practice, institutions who employ the Variant entity may consider changes to colour to provoke the creation of a Variant because the colourisation of a black and white Work represents a fundamental change to the visual aspects of the original Work.

Elements of a Variant

Variant Identifier

Identifier Type

Title

Examples:

```{=latex}
\begin{tcolorbox}
Gone with the wind (United States of America, 1939, Victor Fleming) \\
Gone with the wind – Preferred Title of the Work \\
Via col vento – Variant title – Dubbed (Italian) \\
Gejaagd door de win – Variant title – Dubbed (Dutch) \\
Autant en emporte le vent – Variant title – Dubbed – (French) \\
風と共に去りぬ – Variant title – Dubbed (Japanese)    
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Аленький цветочек (USSR, 1952, Lev Atamanov) \\
Аленький цветочек – Title of the Work \\
Alenkiy tsvetochek: Alternative (transliterated) title of Work/ Variant (Preferred title if systems don’t use Cyrillic) \\
Feuerrotes Blümchen – Variant title – Dubbed (German) \\
The Scarlet Flower – Variant title – Dubbed (English)   
\end{tcolorbox}
```

Title Type

Country of Reference

Year/Date of Reference

Date Type

Date Precision

Language(s)


Language Term

Usage Type

Content Description (synopsis, shotlists, etc)

Content Description Type

Notes

History

Custodial History

Censorship History

Other Variant History

Relationships of a Variant (links/associations with other entities/records

A Variant may have relationships with the following:



Works

Express the relationships between a Variant and a Moving Image Work....


Manifestations

