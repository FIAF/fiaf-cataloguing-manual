# 1.1 Boundaries between Works and Variants

This section looks at instances of when an entity constitutes a new Work or a Variant of a Work.

Determining boundaries between Works and Variants may sometimes rely upon a cataloguer’s judgment, however, in general: If much of the original textual material remains, most of the original footage remains in roughly the same continuity, however abridged, and  substantially  most  of  the  contributors  are  the  same,  the  existence  of  alterations more  often  than  not  constitute  a  Variant,  rather  than  a  new  Work.  An  institution  will need to set internal policies defining the minimum percentage of a work that has been extensively edited to qualify it as a new Work.

This  decision  tree  is  intended  to  help  cataloguers  determine  when  changes  in  content warrant the creation of a new Work record or a new Variant record. This distinction applies to cataloguing structures using a 4-level hierarchy: Work, Variant, Manifestation, and Item. When using a 3-level hierarchy - Work, Manifestation, and Item – minor changes will indicate new Manifestations rather than new Variants. In all cases, major changes warrant the creation of new Work records.

```mermaid
graph TD;
    
    A[Does the material in question constitute exactly the same content as the original release in the country of origin?] --> N[No];
    A --> Y[Yes];
    N --> Min[Are the differences minor?];
    N --> Maj[Are the differences major?];
    Y --> Yz[Catalogue material as MANIFESTATION of original work];
    Min --> Min1[Catalogue material as VARIANT of original work];
    Min1 --> Min2[Minor changes in performers/performance];
    Min2 --> Min2b[Removal/replacement/addition of some but not most contributors]
    Min2b --> Min2c[Examples Changes to crew/cast related to different language versions. Chages to crew/cast related to restorations/preservations.]
    Min1 --> Min3[Minor changes in footage or continuity];
    Min3 --> Min3a[Editing difference including footage or continuity changes from original work];
    Min3a --> Min3aa[Examples Rules of the Game Blade Runner 1982/2007 Mr Arkadin 1955/1956];
    Min3 --> Min3b[Edits to work for reasons of duration/censorship/augmentation etc];
    Min3b --> Min3ba[Examples Television or airline versions of works edited for duration language content etc Preservation/restoration/alternate ending versions];
    Min1 --> Min4[Minor changes in textual aspect];
    Min4 --> Min4a[Changes/additions/removal of some dialogue, narration, audio or text];
    Min4a --> Min4aa[Examples Addition/removal of explanatory text, dubbing, subtitles etc. Star Wars Episode 2 2002 dubbed into 19 languages Sonorised versions of silent films Cabriria 1914/1931];
    Min4 --> Min4b[Subtitles/dubbing etc of same textual content into different languages]
    Min4b --> Min4ba[Examples Deep Impact 1993 English Dialogue / Impacto Profundo 1998 Portugese dialogue Spanish subtitles];
    



```
