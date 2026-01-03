
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

\subsection[Work/Variant Agent Types]{Work/Variant Agent Types 
\footnote {More relator terms can be found in YCR, 1.3.2. Other creators, pp. 42-43; and, OLAC TF, Part II, Core Attributes and Relationships, Commonly-Occurring Roles, pp. 16-18.}} 
\label{sec:work_variant_agent_types}

Cast (or actor/actress)
Cinematographer/Director of Photography/Videographer
Presenter
Producer
Director
Production company
See [FIAF Glossary of Filmographic Terms](http://www.fiafnet.org/pages/E-Resources/Glossary.html)^[http://www.fiafnet.org/pages/E-Resources/Glossary.html]


\subsection{Manifestation Types} 
\label{sec:manifestation_types} 

The Manifestation types below can be used with Manifestations associated with either Works or Variants.

EN15907 does not specify any Manifestation types other than Unknown. The Manifestation types listed below are based on existing types widely used by various archives and used with Manifestations associated with either Works or Variants. They are not the only possible types that can be used - this is not a definitive list of types. Institutions should use the types and terminologies best suited for their requirements and collections.

\subsubsection{Pre-Release (or Production)} 
\label{sec:pre_release} 

A moving image Manifestation type that may be used to represent any embodiments of a moving image Work that exist before the finalisation or release of the moving image Work. Also use for partially realised projects, i.e. productions that started filming but then project ceased before completion, for which footage exists and may have been acquired by an institution.

A Pre-Release Manifestation is effectively a Production Manifestation for which acquired Items used in the production of a film can be linked. Technically, a Pre-Release Manifestation does not refer to any release at all, but rather to embodiments of the creative process that goes into the creation or construction of the Work itself, i.e. raw or semi-edited footage that has been shot in the making of a moving image, whether it has been used in the ultimate finished Work or not. Its use also maintains the EN15907 structure when cataloguing production materials and not confusing Items that constitute these with Items that are simply copies of the completed, released film.

It applies to production material in general, including: original shooting elements (i.e. original camera negative, working print, original video, editing file) and/or the first recording/mixing of the sound (separate original soundtracks – dialogues, sound, music, – or the first mixed soundtrack).

It may also include, censorship submission prints, working assembly prints, rushes, costume tests, lighting tests, make-up tests, etc. where an institution may need or prefer to group together all production material, i.e. an institution may usually create rushes and tests as separate individual associated records but, where these are acquired as part of a large collection of production material for one particular moving image it prefers, for practical reasons, to keep records together for ease of access or for restoration work purposes.

A Pre-Release Manifestation is effectively a Production Manifestation for which acquired Items used in the production of a film can be linked. Technically, a Pre-Release Manifestation does not refer to any release at all, but rather to embodiments of the creative process that goes into the creation or construction of the Work itself, i.e. raw or semi-edited footage that has been shot in the making of a moving image, whether it has been used in the ultimate finished Work or not. Effectively, it is a convenient device in order to maintain the EN15907 structure when cataloguing production materials and not to confuse Items that constitute these with Items that are simply copies of the completed, released film.

Pre-Release Manifestation can also be used with moving images which started production but were never finished and for which footage exists and may have been acquired by an institution.

Depending on the quantity and nature of materials, an institution may create Works in their own right for different in-production filmed aspects, e.g. Screen Tests, Rushes, etc. which are then related to the main, final moving image Work in an associative relationship. Each of these Works would then have their own linked Pre-Release Manifestation.

Equally, an institution may choose to link all acquired production Items (whether analogue or digital) to a single Pre-Release Manifestation linked to the main complete Work, or possibly to several different Pre-Release Manifestations such as one for Screen Tests, one for Rushes, one for general production material, etc.

It may also be used for initial record creation purposes prior to material being viewed and catalogued, which may then result in separate Work/Variant records for Rushes and Tests material to which the Manifestation record will link.

```{=latex}
\begin{tcolorbox}
Something’s got to give (Rushes)
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Beauty jungle: Artist Test – Shirley Ann Field
\end{tcolorbox}
```

Depending on the quantity and nature of materials, an institution may create Works in their own right for different in-production filmed aspects, e.g. Screen Tests, Rushes, etc. which are then related to the main, final moving image Work in an associative relationship. Each of these Works would then have their own linked Pre-Release Manifestation.

[CREATE AND INSERT DIAGRAM TO ILLUSTRATE HERE]

Equally, an institution may choose to link all acquired production Items (whether analogue or digital) to a single Pre-Release Manifestation linked to the main complete Work, or possibly to several different Pre-Release Manifestations such as one for Screen Tests, one for Rushes, one for general production material, etc.

[CREATE AND INSERT DIAGRAM TO ILLUSTRATE HERE]

It may also be used for initial record creation purposes prior to material being viewed and catalogued, which may then subsequently result in further Pre-Release Manifestations and/or Works/Variants

In addition, it may be applied to moving image Manifestations assembled for submission to censorship/ratings bodies, or moving image Manifestations with cuts resulting from those censorship activities.

Detail on the specific nature of the Pre-Release Manifestation (e.g. censorship cuts, working assembly edit, etc.) can be added as a property of the Manifestation Type, from controlled vocabulary or free text, as preferred.

Manifestation Types can represent a unique instance (e.g. the original negative, the first recording/mixing of the sound, censorship cuts, the working assembly edit, etc.) or, more than one instance.

```{=latex}
\begin{tcolorbox}
Censorship submission print
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Censorship cuts
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Make-up tests
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Costume tests
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Screen tests general
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Camera negative
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Assembly edit
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Rushes/Dailies
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Sound mixes
\end{tcolorbox}
```

These describe the context, not the format. For example, a censorship print may exist as multiple Items (35mm print, ProRes, MP4)

As mentioned previously, some of these could also be achieved by creating separate Works, rather than capturing these as Manifestations of the film work.

```{=latex}
\begin{tcolorbox}
Il gattopardo (Luchino Visconti, 1963)
Pre-release, original camera negative – 35mm – Technirama (horizontal frame 8 perf) – Anamorphic – aspect ratio 2,55:1
Work: Il gattopardo (Italy, 1963, Luchino Visconti)
Variant “first cut”: 206’ – first projection – 1963/03/28 (date of first projection) – Rome, Italy
Manifestation 1: Pre-release (original camera negative) – Film – 35mm – 2,55: 1 Anamorphic – Technirama (horizontal frame 8 perf) – Colour Technicolor
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
La voce del silenzio (Georg Wilhelm Pabst, 1953)
Pre-release, Censorship cuts – 35mm – sound positive – 1,37: 1 – black and white
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Work: La voce del silenzio (Italy, 1953, Georg Wilhelm Pabst)
Manifestation1: Pre-release (censorship cuts) – Film – 35mm – sound positive – 1,37:1 – black and white
\end{tcolorbox}
```

\subsubsection{Theatrical distribution} 
\label{sec:theatrical_distribution} 

A moving image Manifestation type representing Manifestations distributed and exhibited in cinema theatres. The classic examples are 35mm positive prints, or the DCP (Digital Cinema Package).

These Manifestation types can be more than one instance, created at the same time or in a different moment, from the same “reproduction” masters.

```{=latex}
\begin{tcolorbox}
L’aigle à deux têtes (France, 1948, Jean Cocteau)

Manifestation 1 : Theatrical distribution (France – 1948 – 22/09/1948 – first projection) – 35mm French – Les Films Ariane (producer, distributor)
Manifestation 2 : Home Video Publication (France – 2010) – TF1 Vidéo (Boulogne-Billancourt) (publisher)

Dubbed Variant
Manifestation 1: Theatrical distribution (Italy – 1949 – censorship visa) – 35mm – Italian (dubbed) – title “L’aquila a due teste” – Italfrancofilm (distributor)
Manifestation 2: Home Video Publication (Italy – 2009 – 25/09/2009) - DVD – French and dubbed Italian (spoken languages), Italian subtitles – Gruppo Editoriale Minerva Raro Video (publisher) – DVD edition by Gabrielle Lucantonio.
\end{tcolorbox}
```

If required there are also further sub-categories of Theatrical distribution which can be used.

\subsubsection{Non-theatrical distribution}
\label{sec:non_theatrical_distribution} 

A moving image Manifestation screened or exhibited outside the public theatrical context. For example, industrial film, training film, medical film, where screening often takes place within a private institutional context; film club screenings; educational screenings.

```{=latex}
\begin{tcolorbox}
The Queen (United Kingdom, 2006, Stephen Frears)
Variant: Censored for airplanes (UK and USA?)
Manifestation: Non-theatrical distribution (USA – Delta Airlines).
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Che cos’è la geografia (Italy, 1953) (genre: Educational Film)
Manifestation 1: Non-theatrical distribution – 16mm- silent with Italian intertitles –b/n – 20’
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
United Nations peacekeeping: situation report, United States of America, 1978 (United Nations Film)(genre: Educational film)
Manifestation 1: Non-theatrical distribution – 16mm- sound– colour
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Stevie Wonder salutes Nelson Mandela, United States of America, 1985 (United Nations Film) (genre: educational film)
Manifestation 1: Non-theatrical distribution– 16mm- sound– color – 8’
\end{tcolorbox}
```

\subsubsection{Not for release}
\label{sec:not_for_release} 

Any moving image Manifestation where the viewing activity was private, due to the nature of the work or the nature of the viewing. For example, amateur film / home movies, where screening usually takes place in a private familial context only; or an uncut manifestation of a feature film screened for crew only.

```{=latex}
\begin{tcolorbox}
Albert Einstein at country home, Caputh, near Berlin, May 1931. (genre: home movie)
Manifestation 1: Not for release– film – 16mm 
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Incontro con Paolo e Vittorio Taviani, Italy, 2004 (genre: event record)
Manifestation 1 (Original): Not for release – MiniDV – 2004 – Italy –CSC-Cineteca Nazionale
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Viaggio in Congo (Italy, 1912, Guido Piacenza) shots not edited)
Augmented / Preservation Variant – (ordering of the shots and addition of explaining intertitles based on the personal diary records of the director) (ordering and editing, including new explaining intertitles, based on personal diary records of the director)
Manifestation 1: Not for release (archival access) – film 35mm – b/n – silent
\end{tcolorbox}
```

\subsubsection{Unreleased}
\label{sec:unreleased} 

Refers to Manifestations which do not represent a release/distribution event, but where the work was intended for release (therefore, distinct from “Not for release”, see above), e.g. the film was made, completed and intended for release, but was not then released due to censorship or political impediments, or other reason.

```{=latex}
\begin{tcolorbox}
Robinson Warszawksi (Poland, 1948, Jerzy Zarzycki)
Film was never released. It ran into censorship problems for portraying the heroism of non-Communist underground movement that also fought against the Nazis. Film was re-edited with major plot changes and released as Miasto Nieujarzmione in 1950.
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Primavera (Italy, ca. 1920, Licurgo Tioli) (Italian silent film, which is not included in the censorship records and according to the sources, was never released/distributed, but it exists as a nitrate tinted 35mm print at the CSC-Cineteca Nazionale in Rome).
\end{tcolorbox}
```

\subsubsection{Home viewing publication}
\label{sec:home_viewing_publication} 

A published Manifestation for viewing in the home or similar small-scale private context, of any type of work. For example, a Blu-ray release of a feature film, for viewing in the home; or a DVD compilation release of a set of non-fiction film works.

```{=latex}
\begin{tcolorbox}
A day in the life. Four portraits of post-war Britain (UK, DVD/Blu-ray, 2010)
\end{tcolorbox}
```

The most used formats are VHS, DVD, and Laserdisc, but this definition can also include 9.5mm Pathé Baby or 8mm packages in use from the 1950s-1980s (e.g.. the 1977 Star Wars home video in 8mm).

NOTE: When the production process involves changes related to the publication, marketing, etc. (e.g., a change in publisher, a repackaging, a new distributor and so on), the resulting product may be considered a new Manifestation as well (see \nameref{sec:boundaries_between_manifestations}).

```{=latex}
\begin{tcolorbox}
Fellini Satyricon (Italy, 1969, Federico Fellini)
Manifestation 1: Home Video Publication – VHS (Italy – 1987 – De Laurentiis/ Ricordi Video (publisher)
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
The Queen (United Kingdom, 2006, Stephen Frears)
Manifestation 1: Theatrical distribution (UK – 2006 – first projection) – 35mm – English
Manifestation 2: TV Broadcast (UK 2007-09-02)
Manifestation 3: Home video – DVD (UK distribution – 2007-03-12)
Manifestation 4: Home video – DVD Blue Ray (USA – 2007-04-24)
\end{tcolorbox}
```

\subsubsection{Broadcast}
\label{sec:broadcast} 

A moving image Manifestation type for TV transmission. It encompasses professional video and digital formats, i.e. Digital Betacam, HDCam, etc.

```{=latex}
\begin{tcolorbox}
The Queen (United Kingdom, 2006, Stephen Frears)
Manifestation 2: TV Broadcast (UK 2007-09-02)
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
It happened one night (United States of America, 1934, Frank Capra)
Manifestation 1: Theatrical distribution (United States of America, 1934): 35mm – black and white – 105 minutes – Columbia Pictures Corp. (producer, distributor) –
Manifestation 2: Broadcast (broadcast on Turner Classic Movies – 2013-11-01, 08:00) black and white – mono – 105 minutes.
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Lazarus rising, (in the series Supernatural), Season 4 Episode 1 (United States of America, 2008, Kim Manners)
Manifestation 1: TV Broadcast (USA 2008-09-18, 21:00-21:55, The CW) colour – stereo – 55 minutes (slot); 40 minutes (actual running time)
Manifestation 2: TV Broadcast (UK, 2009-01-25, 21:00-22:00, ITV2) colour – stereo – 60 minutes (slot); 40 minutes (actual running time)
\end{tcolorbox}
```

\subsubsection{Internet}
\label{sec:internet} 

A moving image Manifestation distributed on the Internet (stream or download) for works of any type, those conceived as Internet works or those conceived in other type but subsequently distributed on the internet (for free or paid subscription).

```{=latex}
\begin{tcolorbox}
Amor pedestre (Italy, 1914, Marcel Fabre)
Manifestation 1: Theatrical distribution – Italian intertitles – film – 35mm – silent – tinted – 1914 – Italy
Manifestation 2: Internet – digital file – [201-?] – Cineteca Italiana (internet publisher) 
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
A film Johnnie (United States of America, 1914, George Nichols)
Translated Variant: Danish intertitles -35mm silent – tinted – Denmark 191[?] -Title: Chaplin fridsstöraren
Preservation Variant: (of Translated Variant)
Manifestation 1: Internet – digital file – [201-?] – European Film Gateway (internet publisher) http://www.europeanfilmgateway.eu/it/node/33/detail/A+film+Johnnie/video:MTU4Yzg1OWUtZGJhZC00ZGUxLTg2MWYtZDEyM2Y0YTA3ODQ0X1VtVndiM05wZEc5eWVWTmxjblpwWTJWU1pYTnZkWEpqWlhNdlVtVndiM05wZEc5eWVWTmxjblpwWTJWU1pYTnZkWEpqWlZSNWNHVT06OmF2Q3JlYXRpb24uZGZpLmRrL0RGSV9hdkNyZWF0aW9uXzQwNjM0/paging:dmlkZW8tMS00LWltYWdlLTEtNC1zb3VuZC0xLTQtcGVyc29uLTEtNC10ZXh0LTEtNA== 13’)
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Brennende Grenze (Germany, 1926-27, Erich Waschneck)
Manifestation 1: Internet –digital file – [200-?] –Deutsches Filminstitut – DIF (internet publisher) http://www.filmportal.de/node/42289/video/1219949 – 2h 26’ 18’’
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Hollywood Stadium mystery (USA 1938, David Howard )
Manifestation 1: Theatrical distribution – English (spoken language) – film – 35mm b/n – 1938 -USA
Manifestation 2: Internet – digital file – 619.3 MB – [200-?] – United States of America – archive.org (internet publisher)  
Manifestation: Internet – digital file – 512Kb MPEG4 – [200-?] – United States of America – archive.org (internet publisher) 
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Cat-Women of the Moon (United States of America, 1953, Arthur Hilton)
Manifestation 1 : Theatrical distribution: English (spoken language) – film – 35mm – b/n – 1953 – USA
Manifestation 2: Internet – English (spoken language) digital file – DivX – [200-?] – United States of America; – 442.1 MB
Manifestation 3: Internet – English (spoken language) – digital file – 512Kb MPEG4 – [200-?] – United States of America; – 259.6 MB
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
A Syrian love story (United Kingdom, Sweden, Denmark, 2015, Sean McAllister)
Manifestation 1: Theatrical distribution: Arabic, English, French (spoken language); English subtitles – Digital – Digital Cinema Package (DCP) – colour – 2015-09-18 – United Kingdom
Manifestation 2: Internet: Arabic, English, French (spoken language); English subtitles – digital file
\end{tcolorbox}
```

\subsubsection{Preservation}
\label{sec:preservation} 

Refers to manifestations which represent the outcome(s) of an institution’s internal copying of moving image items held in their collection for preservation purposes. This often involves copying of the moving image onto a different format, e.g. digitised file(s), for preservation and/or access purposes.  

[ADD LINK TO ILLUSTRATIVE DIAGRAM IN NEW APPENDIX WHEN ADDED]

\subsubsection{Restoration}
\label{sec:restoration} 

Refers to manifestations which represent the outcome(s) of restoration events/activities, usually involving selection and aggregation of materials from diverse source elements to replicate an ‘original’ or ‘ideal’ manifestation.
Some institutions may use this to refer to restorations undertaken by the institution (not to be confused with the actual published Variant, resulting from reconstruction made by aggregating different sources, see \nameref{sec:boundaries_between_works_and_variants}.

If required there is the option of creating more than one Restoration Manifestation to group specific outcomes of the project, e.g. a Manifestation for a Demonstration Reel, Raw scans, final digital DCP and DCDM materials resulting from the restoration process, etc. particularly where there may be several Items, or copies, relating to these on different formats.

    Example:

A very ambitious application might result in the following structure, where separate Manifestations are created for different stages of the restoration process with the key categories:
1. Raw Scan: linked to its item source via a Preservation event (type: digitisation).
2. DCDM (Digital Cinema Distribution Master) and DCP (Digital Cinema Package) under one Manifestation
3. Blu-ray/DVD - ISO as Manifestations and burned physical discs as a items
4. Viewing file for internet publication

Each of these Manifestations differs from the others in terms of its technical parameters (e.g., encoding, resolution, compression, file formats), which justifies the separation into different Manifestations.

  Example:

```{=latex}
\begin{tcolorbox}
The great white silence (United Kingdom, Herbert Pointing, 1924) (DVD –Dual Format Edition – BFI) (2010 restoration)
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Metropolis (Germany, Fritz Lang, 1927)
The Complete Metropolis – Blu Ray – (2010 restoration – Kino International, USA, 2010)
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Nosferatu. Eine Symphonie des Grauens (Germany, 1922, Friedrich Wilhelm Murnau) Blu-Ray of the Restoration Variant: 2005-2006 restoration – Murnau Stiftung/Transit Classics – Deluxe Edition – 2014 – EAN 888430505797
\end{tcolorbox}
```

\subsubsection{Unknown}
\label{sec:unknown} 

Use only when there is insufficient contextual information to enable informed use of any specific Manifestation type from the list above.
For example, to be used when undertaking data cleaning of obsolete legacy Manifestations, when no information is available and it is not practical to examine the primary source to establish context.

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

\subsubsection{Manifestation/Item General Carrier Type}
\label{sec:manifestation_item_general_carrier_type} 

Film
Video Tape
Video Disc
Digital Tape
Digital Disc
Digital File

\subsubsection{Manifestation/Item Specific Carrier Type}
\label{sec:manifestation_item_specific_carrier_type} 

Institutions should develop standard lists of terms to indicate the specific carrier type or refer to authoritative existing lists.

For optical media, only add commercially produced media here. If the optical media is “writable” and is being used to store a digital file, put the digital file format in the General Carrier Type, and the optical storage media in Specific.

```{=latex}
\begin{tcolorbox}
YEE (http://myee.bol.ucla.edu/catrul.doc 5.3.3 (physical carriers)
AMIM2 5D, pp. 18-19 (for gauges/width values)
AMIM2 5B7, pp. 10-11 (including both “tape” and “disc” based video formats).
RDA 3.20; YEE (http://myee.bol.ucla.edu/catrul.doc 5.3.14 (for encoding formats).
PBCore instantiationPhysical http://metadataregistry.org/concept/list/vocabulary\_id/145.html (for physical carriers)
PBCore instantiationDigital (http://pbcore.org/pbcoreinstantiation/instantiationdigital/) (for broad digital formats)
\end{tcolorbox}
```

Additional sources of information include several SMPTE standards, engineering guidelines, and recommended practices. These are some of the most common terms, but not a complete or definitive list.

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|L|L|L|L|}
\hline
\textbf{Film Gauge} & 
\textbf{Video} & 
\textbf{Audio} & 
\textbf{Optical} & 
\textbf{Digital File} & 
\textbf{Digital File Encoding} \\
\hline
35mm & 
1-inch C Format & 
2” audioreel & 
CD & 
DPX & 
MPEG-4 \\
\hline
16mm & 
Digital Betacam & 
1” audioreel & 
DVD & 
MOV & 
Quicktime \\
\hline
Super 16mm & 
Betacam SP & 
½” audioreel & 
Blu-Ray & 
MP4 & 
Real video \\
\hline
8mm & 
2-inch Quadruplex & 
¼” audioreel & 
Laser Disc & 
MXF & 
SVCD \\
\hline
Super8mm & 
HDCAM SR & 
audiocassette & 
& 
AVI & 
VCD \\
\hline
9.5mm & 
D1 & 
35mm magnetic track & 
& 
& 
Windows Media \\
\hline
17.5mm & 
D5 & 
16mm magnetic track & 
& 
& 
\\
\hline
70mm & 
DVCPRO HD & 
& 
& 
& 
\\
\hline
\end{xltabular} 

For digital files, list the physical carrier on which the file is stored. For all other materials, use this element to provide more specific information on the physical carrier.

Institutions should develop standard lists of terms to indicate the specific carrier type or refer to authoritative existing lists.

These are some of the most common terms, but not a complete or definitive list.

LTO5
LTO6
T10000D
HDD (abbreviated for “external hard drive”)
DVD-R
Blu-Ray

\subsubsection{Item Preservation/Access status}
\label{sec:item_preservation_access_status} 

Master   
Viewing   
Accessioned   
On Loan  
Status pending   
Removed  

\subsubsection{Manifestation/Item Sound Fixation Type}
\label{sec:manifestation_item_sound_fixation_type} 

Needle sound
Optical
Magnetic
Analogue sound
Digital

\subsubsection{Manifestation Unit Types}
\label{sec:manifestation_unit_types} 

Reel
Roll
Cassette
Cartridge
Loop
Disc
File
Digital tape

\subsubsection{Item Element Type}
\label{sec:appendix_item_element_type}

Colour Positive
Colour Negative
Copper Toned Positive
Cyan Matrix
Direct BW Positive
Original negative
Duplicate negative
Positive
Original positive (reversal film)
Duplicate positive
Lavender
Image negative
Sound negative
DCP

\subsubsection{Manifestation/Item Colour Type} 
\label{sec:manifestation_item_colour_type}

Colour
Colour + Black & White
Tinted
Black and white
Black and white (tinted)
Black and white (toned)
Black and white (tinted and toned)
Sepia

\subsubsection{Manifestation/Item Colour Standard}
\label{sec:manifestation_item_colour_standard} 

Pathécolor
Technicolor
Kinemacolor
Anscocolor
Ferraniacolor
Fujicolor
Kodachrome

Eastmancolor
RGB
YUV

\subsubsection{Item Sound System}
\label{sec:item_sound_system} 

Dolby SR
Dolby Digital
Mute
Combined Magnetic Sound
Combined Optical Sound
VA RCA Duplex


\subsubsection{Item Stock}
\label{sec:item_stock} 

This is a preliminary list, and not exhaustive.

**FILM**

Eastman Kodak
Fuji
Agfa

**VIDEO**

3M
Agfa
Agfa Gavaert
Akai
Ampex
Ansco
BASF
Brifco
Fuji
Sony

**AUDIO**

Ampex
Scotch
3M
Shamrock

**OPTICAL**

Maxell
Memorex
Philips
Verbatim

**DIGITAL TAPE**

Fuji
HP
Oracle
Sony

**HARD DRIVES**

Hitachi
Seagate
Toshiba
Western Digital

\subsection{Work/Variant Publication Types}
\label{sec:work_variant_publication_types} 

These are not pertinent as both Works and Variants have Manifestations and it is the latter that are published.

\subsection{Manifestation Publication Types} 
\label{sec:manifestation_publication_types}

* Release
* Publication
* Distribution
* Broadcast
* Online Transmission (e.g. Internet, Intranet)
* Pre-Release
* Theatrical distribution
* Non-theatrical distribution
* Not for release
* Home video publication
* Broadcast
* Unknown

\subsection{Production Event Types}
\label{sec:production_event_types}
     

* Casting
* Outdoor shooting
* Indoor shooting
* Post-Production

\subsection{Manifestation Preservation Types}
\label{sec:manifestation_preservation_types} 

Duplication (Printing / Recording)
Transfer
Reproduction
Digitisation
Reconstruction
Restoration

\subsection{Manifestation Decision Types}
\label{sec:manifestation_decision_types} 

Censorship
Revision
Rating

\subsection{Manifestation Manufacture Types}
\label{sec:manifestation_manufacture_types} 

* Film printing
* Telecine
* Video copying
* Scanning
* Mastering
* Uploading

\subsection{Manifestation/Item Acquisition, Accessioning and Source}
\label{sec:manifestation_item_acquisition_accessioning_and_source} 

\subsubsection{Item Acquisition type}
\label{sec:item_acquisition_type} 

* Donation
* Exchange
* Loan
* Purchase
* Off-air recording

\subsubsection{Item Acquisition source type}
\label{sec:item_acquisition_source_type} 

Donor
Agent
Intermediary

\subsection{Manifestation/Item Condition, Preservation and Restoration}
\label{sec:manifestation_item_condition_preservation_and_restoration} 

\subsubsection{Item Copy Condition Base/Emulsion – Film and Video}
\label{sec:item_copy_condition_base_emulsion_film_and_video} 

* Brittle
* Buckled
* Light Scratches
* Heavy Scratches
* Tears
* Warped
* Hydrolysis

\subsubsection{Item Copy Condition Perforations – Film} 
\label{sec:item_copy_condition_perforations_film}

Foil Patches
Torn
Pulled
Missing

\subsubsection{Item Surface Deposit – Film and Video}
\label{sec:item_surface_deposit_film_and_video} 

Mould
Rust
Oil deposits
Dirt
Drying marks

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

Powder
Sticky
Sticky at head

\subsection{Other Relationships for Works, Variants, Manifestations, Items}
\label{sec:other_relationships_for_works_variants_manifestations_items} 

\subsubsection{Work/Variant Other Relationship Types} 
\label{sec:work_variant_other_relationship_types}

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|}
\hline
\textbf{Work/Variant Other Relationship Types} & 
\textbf{Term list} \\
\hline
“Is based on” & 
Adaptation from novels, plays, etc. \\
\hline
“Is a performance of” & 
Recording of live stage presentations of music, plays, dance, etc. \\
\hline
“Contains” & Compilation, series/serial, (see \nameref{sec:aggregates_compilations_multi_component_productions}). \\
\hline
“Is Contained in”/ “is part of” & 
Episode, number, part, extra (see \nameref{sec:aggregates_compilations_multi_component_productions}). \\
\hline
“Has a sequential relationship with” & 
Sequel, prequel, serial/series (see \nameref{sec:aggregates_compilations_multi_component_productions}). \\
\hline
“Has a relationship to promotional material ” & 
Trailer, promo, banner, press-kit, poster, etc. \\
\hline
“Has a relationship to an “object” (a non-moving image resource)” & 
Book, photos, drawings, paintings, etc. \\
\hline
“Has a relationship to an archival document” & 
Script, production papers, author/agent personal papers, etc. \\
\hline
“Has a relationship to a Work “about” the Work/Variant in question” & 
Review, study, article, commentary, “making of” documentary, restoration report, etc. \\
\hline
\end{xltabular} 

\subsubsection{Manifestation Other Relationship Types} 
\label{sec:manifestation_other_relationship_types}

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|}
\hline
\textbf{Other Relationship Types (strictly pertaining to the Manifestation)} & 
\textbf{Term list} \\
\hline
“is part of” & 
part \\ 
\hline
“Has a relationship to promotional material ” & 
trailer, promo, banner, press-kit, poster, etc. \\ 
\hline
“Has relationship to an “object” (a non-moving image resource)” & 
Accompanying booklet, image (i.e. photo of the cover), poster, a metadata set (i.e. for a digital file), etc. \\ 
\hline
“Has a relationship to an archival document” & 
Censorship visa, release/distribution agreement, laboratory technical paper, author/agent personal paper, etc. \\ 
\hline
“Has a relationship to a Work “about” the Manifestation in question” (not only moving image Works) & 
Review, study, article, commentary, restoration report, etc. \\ 
\hline
“Has a relationship to a pre-release Manifestation” & 
Censorship cuts, Make-up tests, Costume tests, Screen tests general, Camera negative --- Assembly edit --- Rushes/Dailies --- Sound mixes \\ 
\hline
\end{xltabular} 

\subsubsection{Item Other Relationship Types}
\label{sec:item_other_relationship_types} 

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|}
\hline
\textbf{Item Other Relationship Types} & 
\textbf{Term list}  \\
\hline
“Has a relationship to another Item” & 
\\ 
\hline
“Contains” & 
Compilation (unintentional – mere use of the same carrier: see \nameref{sec:aggregates_compilations_multi_component_productions}) \\ 
\hline
“Is Contained in”/ “is part of” & 
Episode, number, part, etc. included in an unintentional/convenient compilation (see \nameref{sec:aggregates_compilations_multi_component_productions}). \\ 
\hline
“Associated separation negative” & 
Different colour elements held on separate Items whereby each Item would be needed to create a whole new print of the moving image, e.g. Yellow, Cyan and Magenta Separation Negatives, each of which have to be combined in Technicolor Three Colour Strip Process to make a new colour print. \\ 
\hline
“Associated Sound/Associated image” & 
Where sound and image components are held on separate Item, and would both be needed to create a whole new print e.g. On DPX and Wav, 35mm Mute Pos and Magnetic track \\ 
\hline
“Preservation clone of/Has preservation clone” & 
Reflecting association of 2 identical master digital copies, as per best practice for digital collections \\ 
\hline
“Access copy of/Has Access copy” & 
E.g. an MP4 viewing access copy created from a preservation of a master DPX AND “Source of/Has Source” AND In-house copying of held Items creating new Items, e.g. to create a viewing copy, copy on a different format, copy Nitrate to Safety etc. \\ 
\hline
“Has a relationship to an “object” (a non-moving image resource)” & 
Can/container and label (description of, photo of, etc); punch tapes FCC (frames count cue) found in the can/container \\ 
\hline
“Has a relationship to an archival document” & 
Censorship visa, laboratory report, projection instructions (in general papers in the can/container or related to the specific item and held in separate archive), acquisition contract, DCP key \\ 
\hline
“Has a relationship to a Work “about” the Item in question” & 
Inspection report, restoration report, etc. (in general papers in the can or related to the specific item and held in separate archive) \\ 
\hline
\end{xltabular} 

\subsection{List of form terms for Supplied/Devised titles
\footnote {Adapted from UCLA Film \& Television Archive, Cataloging Procedure Manual—Voyager, Section 5, Filmographic Record – Body of the Description, http://old.cinema.ucla.edu/CPM%20Voyager/CPMV05.html#5.2}} 
\label{sec:list_of_form_terms_for_supplied_devised_titles} 

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|L|}
\hline
\textbf{FORM TERM} & 
\textbf{USE} & 
\textbf{EXAMPLES}  \\
\hline
announcement(s) --- TV announcement(s) -- Theatre announcement(s) & 
Television or theatrical announcements (short, non-commercial content shown to theatre audiences for various purposes, including requesting the audience not to smoke, talk, etc.) Does not include Public Service Announcements. Archives may use the general term “announcements” or more specific description such as “TV announcement.” For announcements clearly designed to be aired during a particular programme or for a particular moving image work, create a partially supplied/devised Title. & 
- Announcements. NBC - Announcements. AMC Theatres - Theatre announcements. Animated no smoking announcements - Theatre announcements. Burnley Collection - Forever Amber. Theater announcement - The Adventures of Ozzie and Harriet. Announcement. Special message. Salesman greetings \\
\hline
blooper(s)/gag reel(s) & 
Also known as blow-ups. For blooper(s)/gag reel(s) associated to a particular program or for a particular moving image work, create a partially supplied/devised Title. & 
- Bloopers. CBS - McCabe \& Mrs. Miller. - International House. Gag reel. W.C. Fields earthquake sequence - Burn Notice. Bloopers. Season 1 \\
\hline
commercial(s) - TV commercial(s) - Internet commercial(s) & 
When possible, add: - name of the product; - kind of the product (if not clear from the name of the product); - name of the company (if not clear from the name of the product). At the moving image work level include additional information, if available: - the year it was broadcast or released; - actors, actresses or other prominent people who appear; - whether the commercial is animated or is a singing commercial (i.e. includes a jingle); - whether the item catalogued is a demo reel or part of a demo reel (a sample of the commercials made by a particular agency, for example). For commercials designed to be aired during a particular television or Internet programme, create a partially supplied/devised Title. & 
- Commercials. Ajax - Commercials. Alka-Seltzer. Spanish - Commercials. Animated. United World Films - Commercials. Bel Air and Raleigh cigarettes. 1962 - Commercials. Box no. 16 - Commercials. Carnation evaporated milk. Burns and Allen - Commercials. Cigarettes - Commercials. Classic TV commercials - Commercials. Colgate toothpaste. If you had a million - Commercials. IBA Awards, 21st. Animated - Commercials. Kellogg’s cereals. Beverly Hillbillies cast - The Burns and Allen Show. Commercials - Naught For Hire. Internet commercials \\
\hline
debate(s) & 
For a formal debate between two people; do not use for, e.g. ‘U.N. Cypress debates’. For fully supplied/devised titles only. & 
- Debates. California gubernatorial. Jerry Brown-Evelle Younger, no. 1 - Debates. California’s gubernatorial. Minority candidates, no. 1 - Debates. Democratic presidential candidates. 1984-04-05 - Debates. Presidential candidates. Gerald R. Ford and Jimmy Carter, no. 1 \\
\hline
electronic press kit(s) & 
Use fully supplied/devised titles for unidentifiable videos. For electronic press kits created for a particular moving image (theatrical, television or Internet programme). & 
- Unidentified electronic press kit. - A League of Their Own. Electronic Press Kit - 61st Annual Academy Awards Show. Electronic Press Kit \\
\hline
excerpt(s) & 
For moving image content identified as being sequence(s), segment(s), clip(s), or fragment(s) (except, for “newsclip(s),” and “study fragment(s),” see below). Not for content that is simply incomplete. For excerpts clearly associated to a particular moving image work, create a partially supplied/devised Title. & 
- Unidentified Rudolph Maté fragments - Unidentified television programme. Segment. Interview with Evans Frankenheimer - Gone With the Wind. Excerpt - King of Jazz. Excerpts. Dancing sequences - Toast of the town. Excerpt. Imogene Coca segment - Unfaithfully yours. Excerpts - Dark half. Excerpts. Review clips \\
\hline
fight(s) & 
For an official fight between two or more people; do not use for, e.g. Ultimate Fighting Championship fights. For fully supplied/devised titles only. & 
- Fights. Dempsey vs. Levinsky - Fights. Moore vs. Martinez. Archie Moore, Martinez fight, Buenos Aires, Argentina. \\
\hline
home movies/personal record(s)/domestic record(s) & 
Do not use merely for footage shot by an amateur; amateur-shot factual footage should be treated as ‘unedited footage’ (see Unedited footage below). “Home movies” should be used only for moving images recording personal or family events, usually filmed or recorded by an amateur (FIAF Glossary). For fully supplied/devised titles only. & 
- Home movies. Brisson, Kryssing - Home movies. Robert A. Taft, Sr. \\
\hline
infomercial(s) & 
For a commercial presentation that combines advertising with information, and is very similar in appearance to a news programme, talk show, or other non-advertising programme content. Generally is much longer than a commercial. Common on cable networks. When possible, add: - name of the product; - kind of the product; - name of the company, in that order of preference. For fully supplied/devised titles only. & 
- Infomercial. Household products - Infomercial. Eggies System. Hassle-free hard boiled eggs. - Infomercial. Happy Nappers. Play pillows. \\
\hline
interview(s) & 
For an interview related to a particular moving image (theatrical, television or Internet programme), create a partially supplied/devised title. & 
- Interview. Paul Coates interviews John F. Kennedy - Interview. Walt Disney - George Stevens: A Filmmaker’s Journey. Interviews. Ann Del Valle, John Del Valle, Rouben Mamoulian \\
\hline
music & 
For soundtracks or scores associated with a particular moving image; includes supplementary music such as overtures, intermission music and exit music. & 
- Olimpiada en Mexico. Overture - Broken Blossoms. Music \\
\hline
music cuts & 
Use only for fully supplied/devised titles (see “trims” for partially supplied/devised Titles). & 
- Music cuts. Big band - Music cuts. Lyn Murray Orchestra - Music cuts. Themes for sports announcements - Music cuts. Unidentified orchestra \\
\hline
music video(s) & 
For video shorts, such as those shown on MTV, designed to exhibit a musical work. Includes videos related to moving image works, (i.e. a song from a soundtrack and having images of the moving image work). Use fully supplied/devised titles for unidentifiable music videos. & 
Dancing in the Street. Music video. - Wild Wild West. (1999). Music video. - Unidentified music video. \\
\hline
newsclip(s) & 
Use for edited news segments from newsreels and/or television broadcasts (FIAF 1.5.2.2.) For clips from a particular news programme, use a partially supplied/devised title. & 
Newsclips from various newsreels. No. 5 - Newsclips. CBS News. No. 5 - Newsclips. Kinograms - Newsclip. WRC-TV News. Cagney, James - CBS News. Newsclips. 2011 U.S. recession \\
\hline
outtakes & 
For content identified as being cuts or outtakes from a particular moving image. & 
Casablanca. Outtakes \\
\hline
pilot & 
For television or Internet programmes. & 
The Brady bunch. Pilot \\
\hline
political programme(s) & 
For fully supplied/devised titles only. & 
- Political programme. Illinois gubernatorial campaign, 1990. Steven Baer for Governor \\
\hline
political spot(s) & 
For fully supplied/devised titles only. & 
- Political spots. California gubernatorial campaign, 1966. Ronald Reagan and Edmund G. Brown - Political spots. California State Assembly campaign, 1973. Bill Lockyear for 14th Assembly - Political spots. Kennedy presidential campaign. Adlai Stevenson for Kennedy \\
\hline
press conference(s) & 
For fully supplied/devised titles only. & 
- Press conference. Kennedy presidential campaign. Los Angeles, Ambassador Hotel - Press conference. President Richard Nixon \\
\hline
promotional(s) promotional film (s) promotional video (s) & 
Also known as Demo reel(s)/demo tape(s) for advertisements and convention films prepared for exhibitors, industry people, etc. rather than audiences. For content publicising a particular moving image, including 1) a compilation of scenes from a moving image, used to sell the idea of making the moving image to potential backers, or prepared for exhibitors, industry people, etc., rather than audiences, or, 2) promotional content that is too long to be considered a trailer, e.g. a featurette or behind-the-scenes film or profile of the actor(s) or director(s). & 
- The arrangement. Promotional film - Frenzy. Promotional film. Rushes - Thelma \& Louise. Promotional video for DVD release - Promotional film. Cinemascope. Demo reel - Promotional film. NBC (a film about NBC for exhibitors) \\ 
\hline
publicity & 
For information disseminated in order to attract public notice, promoting a network or collection of programmes; separate from theatrical or TV trailers, announcements, or promotionals. For information disseminated in order to attract public notice in relationship with a particular moving image, use a partially supplied/devised title; separate from theatrical or TV trailers, announcements, or promotionals. Includes short publicity spots designed for television that promotes a particular, upcoming television show. & 
- Promos - Promos. CBS (advertisements for the network itself) - Promos. NBC programs (a collection of promos for NBC programs) - The Three Musketeers. (1993). Publicity - 62nd Annual Academy Awards Show. TV publicity \\ 
\hline
public service announcement(s) & 
For television or theatrical PSAs. For PSAs designed to be aired during a particular television or Internet programme or theatrical screening, use a partially supplied/devised title. & 
- Public service announcements - Public service announcements. Army. Join the people who’ve joined the Army - Public service announcements. Community and church groups - Public service announcements. Filmex - Public service announcements. Handicapped children - Public service announcements. March of Dimes theatrical spot - The Snake Pit. Public service announcement. Statement by Department of Public Health, Province of Saskatchewan \\ 
\hline
rehearsal(s) & 
For content showing rehearsals of a particular moving image. Use fully supplied/devised titles for unidentifiable rehearsals. & 
- The adventures of Ellery Queen. Prescription for Treason. Rehearsal - Unidentified television programme. Rehearsal \\ 
\hline
rushes & 
For content identified as being the first print made of a day’s filming for a particular moving image. & 
- An act of murder. Rushes \\ 
\hline
sound effects & 
For sound effects related to a particular moving image. Use fully supplied/devised titles for sound effects where the moving image work is not known, or for unedited sound effects. & 
- Das Boot. Sound effects. - Unidentified feature film. Sound effects. - Unidentified sound effects. Compilation \\ 
\hline
speech(es) & 
For fully supplied/devised titles only. & 
- Speech. Kennedy presidential campaign. A time for greatness - Speech. Kennedy presidential campaign. Louisville, Ky - Speech. Kennedy presidential campaign. United Auto Workers \\ 
\hline
study fragment(s) & 
For excerpted content from a particular moving image to be used for the purposes of teaching. & 
- Some Like It Hot. Study fragment \\ 
\hline
test(s) & 
For content identified as being screentests, wardrobe tests, prop tests, etc., for a particular moving image, create a partially supplied/devised title. & 
- Tests. Buzz Henry screen test - Tests. UCLA acting, directing, camera tests - Gone With the Wind. Color test. - À bout de souffle. Screen test. Jean-Paul Belmondo. \\ 
\hline
theatre advertising & 
& 
Theater advertising. Bennett and Bedell advertisement \\ 
\hline
trailer(s) theatrical trailer(s) TV trailer(s) Internet trailer(s) & 
For an advertisement for a particular moving image, to be screened in theatres, on television or streamed on the Web; includes teaser trailers. Archives may use the general term “trailers” or more specific description such as “TV trailer.” For multi-part Manifestations/items formed by more than one trailers. For trailers connected to a particular moving image work, create a partially supplied/devised Title. Do not confuse with public service announcements, theatre advertising, announcements, political spots, etc. & 
- Trailers. Republic titles - La Haine. Trailer - Three on a match. Theatrical trailer - Dai-Nihonjin. TV trailer \\ 
\hline
trims & 
For portions of a moving image scene or soundtrack (e.g. music cuts) left over after the selected section has been used in final cutting. & 
- The Exorcist. Trims - Directed by William Wyler. Interview trims. \\ 
\hline
unedited footage & 
For unedited footage shot for a particular moving image programme, or series. & 
- 60 minutes. 1969-01-07. Unedited footage. Smothers Brothers reading. Newhart, airport controller \\ 
\hline
unedited newsfilm & 
For unedited footage shot for a news programme or news series; includes television and newsreels. & 
- Movietone News. Lowell Thomas Remembers. Unedited newsfilm. \\ 
\hline
unedited sound track & 
For unedited sound track recorded for a particular moving image. & 
- Stargate: The Ark of Truth. Unedited sound track \\ 
\hline
\end{xltabular}
