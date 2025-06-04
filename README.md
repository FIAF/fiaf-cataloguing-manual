# FIAF Cataloguing Manual

Markdown representation of the [FIAF Cataloguing Manual](https://www.fiafnet.org/pages/E-Resources/Cataloguing-Manual.html).

### PDF Renders

[FIAF Cataloguing Manual (English)](/src/render/manual_en.pdf)

### Edit Guide

Required updates should be identified by an "issue" before work begins. The issue list can be found [here](https://github.com/FIAF/fiaf-cataloguing-manual/issues).

From within the issue itself, the editor should assign to themselves (if not already assigned). They should then "Create a branch" for the issue (if not already created).

From the project page, select the appropriate branch and then find the file or files which require editing and make desired edits. The PDF will automatically regenerate on the branch each time (this currently takes a few minutes).

Once edits have resolved the "issue", a "Pull request" can be made to pull the changes into the `develop` branch. These will eventually be versioned by the manual administrator for a major update.

### Formatting Notes

A good general guide to Markdown can be found [here](https://www.markdownguide.org/). 
There are however some specific syntax choices which have been made to best reflect the desired outcomes of the project.

**Headings**

Headings in the manually are dynamically numbered, which allows for editing without having to completely renumber when sections are added or removed.
The syntax for creating headers is as follows:

```md
\section[HEADER_TEXT]{HEADER_TEXT 
    \label{sec:INTERNAL_LINK}
    } 
```

The first instance of HEADER_TEXT is the section title as it will appear in the table of contents, the second instance of HEADER_TEXT is the text as it will render in the header itself.
Currently these are the same throughout the manual.

The label is the internal link name, a nickname for the section which can be used to link to from other sections.

There is also the option to add a footnote to the header using the follow addition configuration.

```md
\section[HEADER_TEXT]{HEADER_TEXT 
    \footnote {FOOTNOTE} 
    \label{sec:INTERNAL_LINK}
    } 
```

"\section" will indicate that the numbering is incremented by the first number, e.g. 1.x.x.x.x. To indicate subsections you can use the following naming convention: "\subsection" for x.1.x.x.x, "\subsubsection" for x.x.1.x.x, "\paragraph" for x.x.x.1.x, "\subparagraph" for x.x.x.x.1.

A complete example would look like this:

```md
\subsubsection[Extent of a Manifestation]{Extent of a Manifestation 
    \footnote {Partially based on EN 15907, 6.8 except for the physical components/units number, which is not provided for in the standard.} 
    \label{sec:extent_of_a_manifestation}
    }  
```





 see \nameref{sec:moving_image_works}.} 

To save on manually incrementing section numbers when editing, the conversion process automatically generates section numbers based on declaring the type of section.

These are:

```
\section{Moving Image Manifestations}
```

This will render as `1 Moving Image Manifestations`.

```
\subsection{Elements of a Manifestation}
```

This will render as `1.1 Elements of a Manifestation`.

```
\subsubsection{Format of a Moving Image Manifestation}
```

This will render as `1.1.1 Format of a Moving Image Manifestation`.
```
\paragraph{Carrier Type of a Manifestation}
```

This will render as `1.1.1.1 Carrier Type of a Manifestation`.

```
\subparagraph{General Carrier Type}
```

This will render as `1.1.1.1.1 General Carrier Type`.

Note that only sections, subsections and subsubsections will be listed in the Table of Contents.

We also should add a label, for internal links. This can be expressed as 

```
\label{sec:moving_image_manifestations}
```

elaborate example

\newpage
\section[Definitions]{Definitions 
    \footnote {For a discussion of other definitions of the “Work” and Variant entities, see \nameref{sec:moving_image_works}.} 
    \label{sec:moving_image_works_definition}
    } 


Footnote example

^[Adapted from the definition of a Cinematographic Work in EN 15907, 4.1.1, p.8.] 


% links to the section with the variable name Alice showing the name of the Section, here: "Alice in Wonderland"
\nameref{sec:Alice}
