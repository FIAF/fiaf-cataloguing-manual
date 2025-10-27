# FIAF Cataloguing Manual

Markdown representation of the [FIAF Cataloguing Manual](https://www.fiafnet.org/pages/E-Resources/Cataloguing-Manual.html).

### PDF Renders

[FIAF Cataloguing Manual (English)](https://f003.backblazeb2.com/file/cataloguing-manual/develop-manual_en.pdf)

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
    \footnote {Partially based on EN 15907, 6.8 except for the physical components/units number.} 
    \label{sec:extent_of_a_manifestation}
    }  
```

**Footnotes**

When used outside a header, in general text, the syntax for footnotes is a "^" symbol followed immediately by the footnote text in square brackets.

```md
^[FOOTNOTE TEXT]
```

As with the section numbering, this will render dynamically and will automatically update the sequence numbering when footnotes are added or removed.

**Links**

There are two different syntaxes for external links (linking to resources outside the PDF) and internal links (linking to sections of the PDF).

External links can be expressed with the regular Markdown syntax for links, highlighted text in square brackets, followed immediately by the link address in regular brackets.

```md
[FIAF Cataloguing Manual](https://www.fiafnet.org/pages/E-Resources/Cataloguing-Manual.html)
```

Internal links use the following non-standard syntax, `\nameref{sec:LABEL}` with the label name to the relevant section.

```md
\nameref{sec:moving_image_works}
```

**Tables**

Formatting tables follows the standard markdown syntax: column headers are separated by "|" symbols, as are the rows, with the requirement for a row between headers and cells with cell dividers separated by "-".

An example would the follow markdown

```md
| A | B | C |
| - | - | - |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
```

which will render as

| A | B | C |
| - | - | - |
| 1 | 2 | 3 |
| 4 | 5 | 6 |


**Diagrams**

Diagrams are currently rendered by a distinct process which produces discrete image files, which are then inserted into the document when the PDF is rendered. 
Please contact the manual administrator for the creation of new diagrams.
