
\newpage
\section{Value Lists} 
\label{sec:value_lists} 

The value lists provided in this appendix are not definitive and are usually limited to a minimum of five examples if more comprehensive lists are available.
If no pre-existing and authoritative lists are available, a non-exhaustive but more comprehensive set of terms is provided.^[It is recognised that vocabulary lists often require frequent updates, additions or amendments. For this reason, should resources permit, it would be ideal to separate value lists from the rules and locate them in a central, online repository, like metadataregistry.org. RDF-based repositories like this can supply up-to-date vocabularies on demand and have additional advantages over traditional value lists such as those found in this Appendix.] The example terms have come from a variety of institutions.

\subsection{Work/Variant Description Types} 
\label{sec:work_variant_description_types} 

The Types below reflect terms used in Section 4.1.2 Attributes in the CEN standard EN15907. (INSERT LINK TO EN15907 IN A FOOTNOTE along with "The terms and their definitions used in the EN15907 Standard itself are rooted in those from UNESCO CCF/B (Common Communications Format / Bibliographic, UNESCO PGI-92/WS/9, Paris, 1992,(INSERT LINK) which related to bibliographic information.)

**Analytic (component part)**: content that is contained in another content. 
A component part may itself be either monographic or serial. Component here means intentional component part not fragments or excerpts of a moving image, e.g. an individual element from a larger newsreel issue.

```{=latex}
\begin{tcolorbox}
Work [Monographic] – Harry wird Millionär \\
\\
Variant [Analytic (component part)] – Harry wird Millionär. Incomplete German version \\
Manifestation 1: Internet – digital file – [2013] – Deutsches Filminstitut – DIF (internet publisher))http://www.filmportal.de/en/node/640472/video/1227323 – 0 h 16’ 59’’ \\
Item – Harry wird Millionär \\
\\
Variant [Analytic (component part)] – Harry wordt Millionair. Incomplete Dutch version \\
Manifestation 1: Internet – digital file – [2013] – Deutsches Filminstitut – DIF (internet publisher)) http://www.filmportal.de/en/node/27915/video/1227322 – 0 h 15’ 44’’ \\
Item – Harry wordt Millionair \\
\\
Variant [Monographic] – Harry wird Millionär. Reconstructed version \\
Manifestation 1: Internet – digital file – [2013] – Deutsches Filminstitut – DIF (internet publisher)) http://www.filmportal.de/en/node/27915/video/1227166 – 0 h 38’ 56’’ \\
Item – Harry wird Millionär
\end{tcolorbox}
```

**Monographic**: Complete content in one part or intended to be completed in a finite number of parts.

This is also applicable to television episodes.
The record for the television series itself is catalogued as a Serial.

```{=latex}
\begin{tcolorbox}
Coronation Street [1960-12-09] \\
Spaced. Series 1 Episode 1. 1999-09-02
\end{tcolorbox}
```

**Serial**: Content issued in successive parts and intended to be continued indefinitely, or across a span of time.
A Work record for a television series is catalogued as a “Serial.” Individual episodes may be catalogued as a Monographic record.

```{=latex}
\begin{tcolorbox}
Gaumont British News (1934-) \\
Flash Gordon’s Trip to Mars (1938) \\
Chemistry Essentials (1996) \\
Breaking Bad (2008-01-20 – 2013-09-29)
\end{tcolorbox}
```

**Collection**: Content issued in several independent parts; an ‘umbrella’ work title covering a number of different Works/Variants/Manifestations^[This aligns with EN15907 definitions relating to Work types and is different and distinct from Collection Aggregates].

```{=latex}
\begin{tcolorbox}
Pleasure (Joan Littlewood, c1963) (Footage shot on behalf of Joan Littlewood as part of her ‘Fun Palace’ project.) \\
The ‘Dogme’ films (Each individually numbered.) \\
Shadows of progress: documentary film in post-war Britain 1951-1977
\end{tcolorbox}
```

Other uses for Collection:^[BFI CID Stylistics Manual, A.1.3 Filmographic Level, p. 8]

Archive-acquired collections of works not originally intended for general release or broadcast all have component parts that form the collection as a whole, usually acquired on a series of numerous film reels or videotapes, etc. each with an identifying title.

```{=latex}
\begin{tcolorbox}
David Lean home movies \\
William Butlin personal films \\
Hollywood interviews (unedited production material for series Hollywood) \\
BFI London Film Festival Awards 2010 – production material, etc. \\
Fifties features (videotape collection of production material, with each of the tapes given an identifying acquisition title: \\
B1-3 Sylvia Syms I/V \\
B4-6 Sylvia Syms I/V \& Jill Craigie I/V \\
\end{tcolorbox}
```

“David Lean home movies,” “Fifties features,” etc. would be the Work titles for the collection-level description, with Collection as its description level.

The individual components of this collection would also be created as individual Monographic Works.

```{=latex}
\begin{tcolorbox}
Egypt \\
India \\
India no.2 \\
Kenya
\end{tcolorbox}
```

These titles should then be linked to the collection-level description and assigned “part of” relationship.

Aggregate compilation videos/DVDs that are collections of individual works existing as entities in their own right, e.g. Portrait of a miner is a DVD of various Mining review shorts which had their own individual release as complete entities or works.

- Portrait of a miner would be created as the work title, with the description level of Collection.

- Each of the Mining review Works used in Portrait of a miner would then be linked to it and assigned a “contained in” relationship (see \nameref{sec:modelling_aggregates}).

Provide a list of the compiled works contained in the Collections Work in its Synopsis or Summary field.

\subsection{Language Usage Types}
\label{sec:language_usage_types} 

  Dialogue language(s)
    Spoken language
    Sung language
    Signed language
    No dialogue
  Written languages
    Subtitles
    Captions
    Intertitles
  Language(s) of summaries on containers
  Language(s) of accompanying material

\subsection{Manifestation/Item Physical Description}
\label{sec:manifestation_item_physical_description} 

Many of the physical description elements are considered specific to Manifestations and are inherited properties of the Items associated with the Manifestations.
This approach is recommended where possible so that the data only need be captured once in order to eliminate redundancies.
However, it is understood that many elements may be repeated at the Item level due to systems designs.
Therefore, the list of elements below indicates those that can be conceivably recorded at the Manifestation level only, at the Manifestation or Item level, and at the Item level only.


\subsubsection{Item Copy Condition Perforations – Film} 
\label{sec:item_copy_condition_perforations_film}

* Foil Patches
* Torn
* Pulled
* Missing

\subsubsection{Item Surface Deposit – Film and Video}
\label{sec:item_surface_deposit_film_and_video} 

* Mould
* Rust
* Oil deposits
* Dirt
* Drying marks

\subsubsection{Image – Film and Video} 
\label{sec:image_film_and_video}

For film, this relates to the inherent qualities of the Emulsion rather than the physical
condition of the Emulsion.

For video, refer to AV Artifact Atlas for guidance on terms.

http://avaa.bavc.org/artifactatlas/index.php/A/V_Artifact_Atlas

* Discolouration
* Magenta Bias
* Faded
* Print through in mould
* Drop-outs

\subsubsection{Item Decomposition – Film and Video}
\label{sec:item_decomposition_film_and_video} 

* Powder
* Sticky
* Sticky at head


