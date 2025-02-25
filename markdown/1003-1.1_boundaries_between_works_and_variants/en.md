\subsection{1.1 Boundaries between Works and Variants}
\label{sec:manual-1.1}

This section looks at instances of when an entity constitutes a new Work or a Variant of a Work.

Determining boundaries between Works and Variants may sometimes rely upon a cataloguer’s judgment, however, in general: If much of the original textual material remains, most of the original footage remains in roughly the same continuity, however abridged, and substantially most of the contributors are the same, the existence of alterations more often than not constitute a Variant, rather than a new Work.
An institution will need to set internal policies defining the minimum percentage of a work that has been extensively edited to qualify it as a new Work.

This decision tree is intended to help cataloguers determine when changes in content warrant the creation of a new Work record or a new Variant record.
This distinction applies to cataloguing structures using a 4-level hierarchy: Work, Variant, Manifestation, and Item.
When using a 3-level hierarchy - Work, Manifestation, and Item – minor changes will indicate new Manifestations rather than new Variants.
In all cases, major changes warrant the creation of new Work records.

```pikchr
B1: box rad 5px "Does the material in question constitute exactly the same content as the" "original release in the country of origin?" fit at (3.5,0)

B2: box rad 5px "No" fit at (0,-0.5); arrow down 0.1 from B1.s then left until even with B2 then down to B2.n

B3: box rad 5px "Are the differences minor?" fit at (0,-1); arrow from B2.s to B3.n

B4: box rad 5px "Catalogue material as" "VARIANT of original work" fit at (0,-1.5); arrow from B3.s to B4.n

B5: box rad 5px "Minor changes in" "performers/performance" fit at (1,-2)
arrow down from B4.s then down until even with B5 then right to B5.w

B6: box rad 5px "Removal/replacement/addition of" "some but not most contributors" fit at (2.5,-2.5); arrow down 0.1 from B5.s then down until even with B6 then right to B6.w

B7: box rad 5px "Examples" "Changes to crew/cast related to different language versions." "Changes to crew/cast related to restorations/preservations." fit at (2.5,-3.5); arrow from B6.s to B7.n

B8: box rad 5px "Minor changes in footage" "or continuity" fit at (1,-4.5); arrow down from B4.s then down until even with B8 then right to B8.w

B9: box rad 5px " Editing differences including footage" "or continuity changes from" "original work. " fit at (2.5,-5); arrow down from B8.s then down until even with B9 then right to B9.w

B10: box rad 5px "Examples" "- Rules of the Game" "- Blade Runner (1982/2007)" "- Mr. Arkadin (1955/1956)" fit at (2.5,-6); arrow from B9.s to B10.n

B11: box rad 5px " Edits of work for reasons of duration/" "censorship/augmentation etc " fit at (2.5,-7); arrow down from B8.s then down until even with B11 then right to B11.w

B12: box rad 5px "Examples" "Television or airline versions of works edited" "for duration, language, content, etc" "Preservation/restoration/alternate ending versions." fit at (2.5,-8); arrow from B11.s to B12.n

B13: box rad 5px "Minor changes in" "textual aspect" fit at (1,-9); arrow from B11.s to B12.n; arrow down from B4.s then down until even with B13 then right to B13.w

B14: box rad 5px " Changes/additions/removal " " of some dialogue," "narration, audio or text" fit at (2.5,-9.5); arrow down from B13.s then down until even with B14 then right to B14.w

B15: box rad 5px "Examples" "Addition/removal of explanatory text, dubbing," " subtitles etc. Star Wars Episode 2 (2002)""(dubbed into 19 languages). Sonorized" "versions of silent films: Cabirira (1914/1931)" fit at (2.5,-10.5); arrow from B14.s to B15.n

B16: box rad 5px "Subtitles/dubbing etc of"  "same textual content into" "different languages" fit at (2.5,-11.5); arrow down from B13.s then down until even with B16 then right to B16.w

B17: box rad 5px "Examples" "- Deep Impact (1998, EnglishDialogue) /" "Impacto Profundo (1998," "Portuguese dialogue,Spanish subtitles)" fit at (2.5,-12.5); arrow from B16.s to B17.n

B18: box rad 5px "Are the differences major? " fit at (5,-1); arrow down 0.1 from B2.s then right until even with B18 then down to B18.n

B19: box rad 5px "Catalogue material as"  "NEW WORK"fit at (5,-1.5);
arrow from B18.s to B19.n

B20: box rad 5px "Major changes in" "performers/performance" fit at (6,-2); arrow down 0.2 from B19.s then down until even with B20 then right to B20.w

B21: box rad 5px "Each filming of" "a performance-based work" fit at (7.5,-2.5); arrow down 0.2 from B20.s then down until even with B21 then right to B21.w

B22: box rad 5px "Example" "Filmed stage performances" "of Macbeth or Hamlet" fit at (7.5,-3); arrow from B21.s to B22.n

B23: box rad 5px "Removal/replacement of" "most contributors" fit at (7.5,-3.5); arrow down 0.2 from B20.s then down until even with B23 then right to B23.w

B24: box rad 5px "Example" "- Chickens Come Home (1931)" fit at (7.5,-4); arrow from B23.s to B24.n

B25: box rad 5px "Major changes in" "footage or continuity" fit at (6,-4.5); arrow down 0.2 from B19.s then down until even with B25 then right to B25.w

B26: box rad 5px "Remakes of the same story/plot" fit at (7.5,-5); arrow down 0.2 from B25.s then down until even with B26 then right to B26.w

B27: box rad 5px "Examples" "- Planet of the Apes (1968/2001)" "- Scarface (1932/1983)" "- The Man Who Knew Too Much(1934/1956)" fit at (7.5,-5.75); arrow from B26.s to B27.n

B28: box rad 5px "Different language versions" "shot at the same time" fit at (7.5,-6.5); arrow down 0.2 from B25.s then down until even with B28 then right to B28.w

B29: box rad 5px "Examples" "- Dracula (1931): English and Spanish" "- Anna Christie (1930/1931): English and German" fit at (7.5,-7.25); arrow from B28.s to B29.n

B30: box rad 5px "Major changes in" "textual aspect" fit at (6,-8); arrow down 0.2 from B19.s then down until even with B30 then right to B30.w

B31: box rad 5px "Complete change of dialogue" "or narration to an existing" "work" fit at (7.5,-8.5); arrow down 0.2 from B30.s then down until even with B31 then right to B31.w

B32: box rad 5px "Example" "- What's Up, Tiger Lily? (1966)" fit at (7.5,-9.25); arrow from B31.s to B32.n

B33: box rad 5px "Edits of the same footage by different" "people into new sequences."  fit at (7.5,-10); arrow down 0.2 from B30.s then down until even with B33 then right to B33.w

B34: box rad 5px "Example" "- 1910-13 Scott Arctic footage"  fit at (7.5,-10.5); arrow from B33.s to B34.n

B35: box rad 5px "Yes" fit at (7,-0.5); arrow down 0.1 from B1.s then right until even with B35 then down to B35.n

B36: box rad 5px "Catalogue material as" "MANIFESTATION of original" fit at (7,-1); arrow from B35.s to B36.n
```