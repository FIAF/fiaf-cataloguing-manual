# FIAF Cataloguing Manual

Markdown representation of the FIAF Cataloguing Manual.

### Renders

[FIAF Cataloguing Manual (English)](/src/render/manual_en.pdf)

### Edit guide

Required updates should be identified by an "issue" before work is undertaken. Issue list can be found [here](https://github.com/FIAF/fiaf-cataloguing-manual/issues).

From within the issue itself, the editor should assign to themselves (if not already assigned). They should then "Create a branch" for the issue (if not already created).

From the project page, select the appropriate branch and then find the file or files which require editing and make desired edits. The PDF will automatically regenerate on the branch each time (this currently takes a few minutes).

Once edits have resolved the "issue", a "Pull request" can be made to pull the changes into the `development` branch. These will eventually be merged into the primary branch by the manual administrator for a major update.

### Formatting notes

**Sections**

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