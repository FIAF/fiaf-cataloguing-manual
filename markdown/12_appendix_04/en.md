
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
