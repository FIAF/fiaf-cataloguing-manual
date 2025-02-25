\subsection{E.5.2.2 Model: Augmented Aggregate Manifestation within a many-to-many Work/Variants-Manifestations database system}
\label{sec:manual-E.5.2.2}

Single Aggregate Manifestation links to all individual Works/Variants in “part of” relationship.

```pikchr
C1: box rad 5px "Casablanca" "(1943) Work" fit at (0,3) 

C2: box rad 5px "Casablanca" "(TV Episode, 1955) Work" fit at (4,3) 

C3: box rad 5px "You Must Remember This" "(1989) (Work)" fit at (0,2) 

C4: box rad 5px "Bacall on Bogart" "(1988) Work" fit at (4,2) 

C5: box rad 5px "Carrotblanca" "(1995) Work" fit at (0,1) 

C6: box rad 5px "Casablanca. Trailer" "(1942) Work" fit at (4,1) 

C7: box rad 5px "Casablanca. Special Edition" "(DVD Manifestation, 2003)" "(Augmented Aggregate)" fit at (2,0)

arrow right from C1.e then right until even with C7 then down to C7.n

arrow right from C3.e then right until even with C7 then down to C7.n

arrow right from C5.e then right until even with C7 then down to C7.n

arrow left from C2.w then left until even with C7 then down to C7.n

arrow left from C4.w then left until even with C7 then down to C7.n

arrow left from C6.w then left until even with C7 then down to C7.n
```

An institution can choose whether to create all components of the Augmented aggregate Manifestation as Works, or selected ones.

However, in cases of Augmented Aggregates it is recommended to always create a corresponding aggregating Work, as the Work record will contain relevant fields for extra data such as new credits pertaining just to the aggregate.
Similarly synopsis or notes fields can then be utilised to give full description of contents.

More importantly, it is not always practical or feasible for many cataloguing systems to deal with creating records for non-moving image materials such as booklets, or text.


```{=latex}
\begin{tcolorbox}[colframe=blue!50!white, colback=blue!10!white, coltitle=black, title=Example]
Charlie Chaplin. The Mutual films. Volume 1. \\
Contains: 6 short Chaplin Mutual films – Behind the screen, The immigrant, Easy Street, The rink, The cure, The adventurer. Plus DVD extras: Topical Budget newsreel footage of Chaplin on voyage and visit back to Britain; filmed interview with Carl Davis [who did music soundtrack for the aggregate]; on-screen text biographies of Edna Purviance and Eric Campbell. Plus sleeve notes by Frank Scheide.
\end{tcolorbox}
```

An aggregating Work record for the above enables adding of credits, for example, the music composer for the soundtrack on the aggregate, the interviewees, etc.; associative “contains/contained in” relationship links to any individual films or newsreel works; and then any other remaining details of the Work that cannot be linked in associative relationships may be added as free text in synopsis or notes fields.

