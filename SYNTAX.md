### Syntax Guide

This iteration of the FIAF Cataloguing Manual has been mostly formatted using Markdown. A good general guide for this format can be found [here](https://www.markdownguide.org/). Due to some complex formatting requirements, we are also using some [LaTeX](https://en.wikipedia.org/wiki/LaTeX) syntax, detailed below.

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

We are currently using the [xltabular](https://ctan.org/pkg/xltabular) package to render tables.

The following table:

| **Work** | **Manifestation** | **Item** |
| - | - | - |
| 1  | 2 | 3 |
| 4 | 5 | 6 |

Can be achieved with this syntax:

```latex
\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|L|}
\hline
\textbf{Work} & 
\textbf{Manifestation} & 
\textbf{Item} \\
\hline
1 & 
2 &  
3 \\
\hline
4 & 
5 & 
6 \\
\hline
\end{xltabular} 
```

Some additional formatting options:

- Footnotes within cells can be achieved with `\footnote{FOOTNOTE}`.
- Cell backgrounds can be coloured with `\cellcolor{gray!25}`.
- Lists can be added with `\begin{tabitemize} \item ITEM \end{tabitemize}`.
- Linebreaks within text can be generated with `\linebreak`.

**Diagrams**

Diagrams are currently rendered by a distinct process which produces discrete image files, which are then inserted into the document when the PDF is rendered. 
Please contact the manual administrator for the creation of new diagrams.
