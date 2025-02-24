\subsection{0.8 Errors}

As these guidelines recognise the importance of researched information in the catalogue entry, unintentional errors or inaccuracies from the Item should not be reproduced at the Work or Variant levels.

Begin with what the source of information says and correct it only when it is known to be ambiguous or erroneous.
Correction must be done in such a way that the resource remains recognisable to the users unaware of the error.^[YCR, Principle 3, p.4.] For example, AACR2 recommends transcribing the error followed by “sic” and sometimes the correct text in square brackets.

Example:

```{=latex}
\begin{tcolorbox}[colback=gray!10!white]
Title (Work): À bout de souffle    \\
Title (Item): À bout de souflee [sic] 
\end{tcolorbox}
```

OR

```{=latex}
\begin{tcolorbox}[colback=gray!10!white]
Title (Work): À bout de souffle    \\
Title (Item): À bout de souflee [souffle]  
\end{tcolorbox}
```

In RDA, the title is provided as transcribed without a recognition of the misspelling, with the correct title added in a secondary set of Title and Title Type fields (see [A.2.4.1 Alternative title types](#manual-A.2.4.1)) and a Note explaining the misspelling.

Example:

```{=latex}
\begin{tcolorbox}[colback=gray!10!white]
Title (Work): À bout de souffle    \\
Title (Item): À bout de souflee    \\
Title (Item): À bout de souffle     \\
TitleType (Item): Actual title  \\
Note: Title on item is misspelled. 
\end{tcolorbox}
```

Missing information required to understand and identify a Manifestation, Variant, or Item can be supplied in brackets.   

Record intentionally misspelled words as found.  

Example:

```{=latex}
\begin{tcolorbox}[colback=gray!10!white]
Title (Work): Inglorious Basterds
\end{tcolorbox}
```

