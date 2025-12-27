
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

\subsection{Event Type} 
\label{sec:event_type}

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|L|L|}
\hline
\textbf{Work} & 
\textbf{Variant} & 
\textbf{Manifestation} & 
\textbf{Item} \\
\hline
\nameref{sec:publication} & 
\nameref{sec:publication} & 
\nameref{sec:publication} &  
\\
\hline
\nameref{sec:awards_or_nominations} & 
\nameref{sec:awards_or_nominations} & 
\nameref{sec:awards_or_nominations} & 
\\
\hline
\nameref{sec:production} & 
\nameref{sec:production} & 
& 
\\
\hline
\nameref{sec:values_rights_copyright_ipr_registration} & 
\nameref{sec:values_rights_copyright_ipr_registration} & 
Licensing & 
Licensing \\
\hline
& 
\nameref{sec:preservation} & 
\nameref{sec:preservation} & 
\nameref{sec:preservation} \\
\hline
& 
\nameref{sec:decision} & 
\nameref{sec:decision} & 
\\
\hline
& 
& 
\nameref{sec:manufacture} & 
\\
\hline
& 
& 
& 
\nameref{sec:inspection} \\
\hline
& 
& 
& 
\nameref{sec:acquisition} \\
\hline
\end{xltabular} 

\subsubsection{Publication}  
\label{sec:publication} 

For Works/Variants, a Publication Event corresponds to the first verified release or availability of the Work or Variant, whether theatrical, straight-to-video, broadcast or online transmission, etc.

For Manifestations, a Publication Event corresponds to a screening, broadcast or the release of the Manifestation of a Work/Variant on a physical distribution medium or online.

A Publication Event may be associated with instances of Agent in the role of e.g., publisher, distributor, broadcaster^[Some institutions specifically dealing with TV material may wish to use an actual “TV Transmission Manifestation” for this data.], etc. See \nameref{sec:distributor_theatrical} and \nameref{sec:work_variant_agent_types}.

A Publication Event may be associated with instances of “Other” relationship(s) (e.g., promotional material of the theatrical distribution, the advertising of the home video publication, etc.).

Record all the existing relationships of a Publication Event, if the information is known and considered of relevance.

Publication Event information consists of the following sub-elements:

  - Publication type
  - Publication date
  - Region

- Publication type

For Works/Variants, record the type of Publication Event for Works/Variants, for example, publication, release, distribution, broadcast, online transmission.
Selection should be made from a controlled list of values.
See \nameref{sec:manifestation_publication_types}.

Record the Publication type for Manifestations, for example, “pre-release,” “theatrical distribution,” etc. Selection should be made from a controlled list of terms.
See \nameref{sec:manifestation_publication_types}.

For Manifestations, the Publication Event that originated the embodiment of a specific Work/Variant in a Manifestation, corresponds to criteria individuated to distinguish the boundaries between Manifestations.
For this reason, conceptually, and also in practice, “publication type” overlaps the main definition of “Manifestation type,” as explained in \nameref{sec:boundaries_between_manifestations} and, as such, is already described.
Institutions have the option to decide whether to repeat this information or not.

- Publication date

Record the date on which Work/Variant or Manifestation was released or otherwise made available.
Dates should be formatted according to ISO 8601 or some other recognised standard.

- Region

Record the country or other political or physical geographic entity where the Publication Event took place (e.g. first projection in the framework of a theatrical distribution) or made the Work/Variant or Manifestation available (e.g. distribution area).

If known and considered of relevance, record the name of the city or smaller geographic entity where the Publication Event took place.

For the treatment of the geographical names, see Getty Thesaurus of Geographic Names (TGN), or some other recognised standard.

If known and considered of relevance, record the name of the event that the publication was a part of (e.g., name of a film festival, distribution channel of a broadcaster, etc.)

If known and considered of relevance, record the specific restrictions for accessing the content (e.g. press-screening only, airplanes only, etc.).

\subsubsection[Award(s) or Nomination(s)]{Award(s) or Nomination(s) 
\footnote {EN 15907, 6.12 Award, pp. 25-26.}} 
\label{sec:awards_or_nominations}
  
The bestowal of an award relating to the Work/Variant or Manifestation.
This excludes awards for Agents alone (e.g. “for lifetime achievement”), but includes awards for individual achievements within the context of a Work or Variant (e.g. “Best screenplay”).
Awards will usually be associated at the level of the Work, except for cases where features of a particular Variant are explicitly mentioned (e.g. “Best audio commentary for the visually impaired”) or the award relates to a particular Manifestation (such as a DVD edition).

An Award(s) or Nomination(s) Event may be associated with instances of Agent in the role of e.g. publisher, distributor, broadcaster^[Some institutions specifically dealing with TV material may wish to use an actual “TV Transmission Manifestation” for this data.], etc. See \nameref{sec:distributor_theatrical} and \nameref{sec:work_variant_agent_types}.
If the award was given for the achievement of a specific Agent within the context of the Work/Variant or Manifestation, identify the Agent. Also used to identify Agents that have sponsored the award.

An Award(s) or Nomination(s) Event may be associated with instances of other Events during which award winners were selected (e.g. film festival).

Record all the existing relationships of a Publication Event, if the information is known and considered of relevance.

Award(s) or Nomination(s) Event information consists of the following sub-elements:

  - Award(s)/Nomination(s) date
  - Nomination only
  - Award name
  - Achievement

- Award(s)/Nomination(s) date

Record the date the award was bestowed on an Agent associated with the Work, Variant or Manifestation.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Nomination only

Indicate if the Work, Variant or Manifestation (or a specific achievement in the creation of it) was nominated but not among the winners.
This element can be realised in a system as a “flag.” If there was only a nomination, this element would be set to a logical value of “true.”

- Award name

The name of the award or trophy, possibly including a numeric designation (e.g. 2nd Prize)

- Achievement

A phrase describing a specific achievement for which the award was given, if not for the Work, Variant or Manifestation in total.

\subsubsection[Production]{Production 
\footnote {Adapted from EN 15907 6.11 Production Event, p. 20}} 
\label{sec:production}
  
A distinct event in the course of production of a Work or Variant, including the main production event OR events that are separated in space and/or time from the main production event, or known with a greater amount of detail.
Examples are dates and locations where castings took place; dates and locations of shootings or other recordings; or dates and locations of particular post-production activities.

May include year/date of shooting of non-professional, actuality or unedited footage.

A Production Event may be associated with instances of Agent in the role of e.g. production company, location scout, etc. Selection should be made from a controlled list of values. See \nameref{sec:distributor_theatrical} and \nameref{sec:work_variant_agent_types}.

Record all the existing relationships of a Production Event, if the information is known and considered of relevance.

Production Event information consists of the following sub-elements:

  - Production Event type
  - Location
  - Region
  - Year/Date
  - Event details

- Production Event type

Selection should be made from a controlled list of values. See \nameref{sec:production_event_types}.

- Location

Any geographic name(s) or address(es) of the location(s) where the event took place

- Region

The country or other large-scale geographic entity where the event took place

- Year/Date

The year/date or time-span during which the event took place. Dates should be formatted according to ISO 8601 or some other recognised standard.

- Event details

Any further information about the event either in plain textual form, or as an instance of a data type from another schema

\subsubsection[Rights/Copyright/IPR Registration]{Rights/Copyright/IPR Registration 
\footnote {EN 15907 6.15 IPR Registration, pp. 23-24}} 
\label{sec:values_rights_copyright_ipr_registration}

These are optional, and it is for an institution to choose whether it has the resources or requirement to compile rights data.
Further more detailed information on the subject of rights/copyright/IPR registration can be found in \nameref{sec:appendix_rights_copyright_ipr_registration}.

A Copyright/IPR Registration Event is the act of registering copyright or intellectual property rights for a Work or Variant with an accredited agency.

A Copyright/IPR Registration Event may be associated with instances of Agent in the role of e.g. applicant, etc. Selection should be made from a controlled list of values.

Record all the existing relationships of a Copyright/IPR Registration Event, if the information is known and considered of relevance.

Copyright/IPR Registration Event information consists of the following sub-elements:

  - Registration Date
  - Registration Agency
  - Regional scope
  - Name of applicant
  - Registration number

- Registration date

The date on which the registration was filed or the date on which registration became effective.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Registration agency

Name of the agency issuing the registration certificate (e.g. “UK Intellectual Property Office,” name of a legal deposit library, etc.).

- Regional scope

The geographic region for which copyright is claimed.

- Name of applicant

Name of the Agent claiming copyright in the Work or Variant.

- Registration number

The number assigned by the registration agency.

\subsubsection[Preservation]{Preservation 
\footnote {EN 15907, 6.15 Preservation event, pp. 28-29}}
\label{sec:preservation}

A Preservation Event is associated with a new Variant, Manifestation or Items resulting from the preservation process in which the contents of one or more Items (or fragments thereof) from Manifestations of a Work were transferred with the intention of restoring or reconstructing the content as originally intended, or safeguarding it from decay.

This includes statements about past or future treatments scheduled for the item.^[YCR 6.5, 6.6] If desired and if applicable, record one or more general types of past or future treatment activities (e.g. “added leaders”, “cleaned ultrasonically”, “tears repair”, etc.).
Selection should be made from a controlled list of values.

A Preservation Event has as typical Agent(s) the institution(s) or individual professionals that make preservation decisions.
Selection should be made from a controlled list of values. See \nameref{sec:distributor_theatrical} and \nameref{sec:work_variant_agent_types}.

A Preservation Event can be in relationship with instances of “Other” relationships (such as technical reports, documentation material, promotional material for the specific project, etc.).

Record all the existing relationships of a Preservation Event, if the information is known and considered of relevance.

Preservation Event information consists of the following sub-elements:

  - Preservation type
  - Preservation Date

- Preservation type

Record the general type of the preservation activity performed, for example, duplication, transfer, etc. Selection should be made from a controlled list of terms. See \nameref{sec:manifestation_preservation_types}.

- Preservation Date

Record the date or time span in which the preservation activity was performed.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

Add in a note any information describing the preservation process in detail.

This can include:^[Based on in-house Academy Film Archive preservation documentation.]

  - Genesis of the project or reason why preservation was undertaken
  - Significant challenges
  - Relevant research (documenting sources of information related to content or production techniques)
  - Technical, aesthetic or ethical decisions
  - Recommendations for further work (details concerning limitations due to source material, resources, technology, etc.)

\subsubsection[Decision]{Decision 
\footnote {EN 15907, 6.13 Decision event, pp. 26-27}}
\label{sec:decision}

A Decision Event is an event in which a Manifestation of a certain Work/Variant is evaluated by a censorship body or an accredited rating agency.

A Decision Event may be associated with instances of Agent, e.g. in the role of the agency performing the rating or censorship.

A Decision Event may be associated with instances of “Other” relationship(s) (e.g., the original censorship documents).

Record all the existing relationships for the Decision Event, if the information is known and considered of relevance.

Decision event information consists of the following sub-elements:

  - Decision type
  - Decision date
  - Regional scope
  - Certificate number
  - Verdict
  - Decision type

- Decision type

Record the type or status of the decision event.
Usually the term adopted is “censorship” or “revision” for decisions mandated by law, “rating” for decisions under a voluntary scheme.
Further types may include special forms of evaluation, e.g. for tax privileges, as long as these are distinct from awards.

Selection should be made from a controlled list of terms. See \nameref{sec:manifestation_decision_types}.

- Decision date

Record the date on which the verdict was announced or on which the verdict was declared valid. Dates should be formatted according to ISO 8601 or some other recognised standard.

- Regional scope

Record the geographic region for which the verdict is (was) valid.

- Certificate number

Record in Arabic numerals the number issued by the agency as a unique identifier of the act(s) of rating or censorship such as censorship visas or rating certificates.

- Verdict

Record the outcome of the act of rating or censorship.

\subsubsection{Manufacture}  
\label{sec:manufacture}

A Manufacture Event represents a “common” event within which the embodiment of a Manifestation occurs, owing to the instances of a number of physical items that bear the same characteristics.

Therefore, the manufacture event of a moving image Manifestation corresponds to the activity within which it was fixed on a physical carrier, through particular technical processes such as film printing, telecine, video copying, digitisation, mastering, etc., or where it is saved to an “immaterial” medium, such as a digital file.

A Manufacture Event may be associated with instances of Agent, e.g. a laboratory that prints all the copies for a theatrical distribution or a studio that masters the DVDs for a home video publication.

A Manufacture Event may be associated with instances of “Other” relationship(s).

Record all the existing relationships for the Manufacture Event, if the information is known and considered of relevance.

Manufacture event information consists of the following sub-elements:

  - Manufacture type
  - Manufacture date
  - Manufacture region

- Manufacture type

Record the general type of the manufacture activity performed, for example, film printing, tele-cine, video copying, etc. Selection should be made from a controlled list of terms. See \nameref{sec:manifestation_manufacture_types}.

- Date of Manufacture

Record the date or time span on which the Manufacture Event took place. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Region of Manufacture/embodiment

Record the country or other political or physical geographic entity where the Manufacture Event took place (e.g. the region/place where the laboratory was located).
(For the treatment of the geographical names, see Getty Thesaurus of Geographic Names (TGN), or some other recognised standard.)

If known and considered of relevance, record the name of the city or smaller geographic entity where the Manufacture Event took place.

\subsubsection{Inspection} 
\label{sec:inspection} 

The inspection of a particular Item for the purposes of assessing and recording the condition or treatment of the Item.

An Inspection Event may be associated with instances of Agent in the role of e.g. inventory archivist, projectionist, etc.

An Inspection Event may be associated with instances of “Other” relationship(s).

Record all the existing relationships for the Inspection Event, if the information is known and considered of relevance.

Inspection Event information consists of the following sub-elements:

  - Inspection type
  - Inspection date
  - Inspection detail

- Inspection type

The general type of inspection activity performed.

If desired and if applicable, record one or more general type(s) of the inspection activity performed (e.g. projection prep, inventory). Selection should be made from a controlled list of terms. This includes statements about past or future inspections scheduled for the item.^[YCR 6.5, 6.6]

- Inspection date

The date or time span in which the inspection activity was performed. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Inspection detail

Information describing the condition of the Item in greater detail.

If desired and if applicable, record information about the condition of the Item, including nature and extent of damage. Selection should be made from a controlled list of terms. (See \nameref{sec:item_copy_condition_base_emulsion_film_and_video})

\subsubsection{Acquisition} 
\label{sec:acquisition} 

The acquisition of a particular Item for an institution’s collection.

An Acquisition Event may be associated with instances of Agent in the role of e.g. the institution or a person or set of persons in charge of acquisitions for the institution, etc.

An Acquisition Event may be associated with instances of “Other” relationship(s).

Record all the existing relationships for the Acquisition Event, if the information is known and considered of relevance.

An Acquisition Event information consists of the following sub-elements:

  - Acquisition type
  - Acquisition date
  - Acquisition source
  - Accession date
  - Acquisition detail

- Acquisition type

Describes the means by which the Item was acquired, for example, donation, exchange, loan, etc. Select from a controlled list of terms. See, \nameref{sec:item_acquisition_type}.

- Acquisition date

The date on which the Item was physically acquired. This date is distinct from an Accession date, which should be entered only once any required assessment has been completed, and the Item has been formally added to the inventory of the collection. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Acquisition source

The name of the person or organisation from which the Item was obtained, indicating whether the acquisition was direct from, for example, the donor or via an intermediary or agent. Select from a controlled list of terms. See \nameref{sec:item_acquisition_type}.

- Accession date

The date on which the Item was formally added to the inventory of the collection.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Acquisition detail

Information describing the acquisition of the Item in greater detail.

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

\subsubsection{Manifestation/Item Sound Type}
\label{sec:manifestation_item_sound_type} 

Sound  
Silent  
Mute  
Combined  
Combined as Mute  
Combined as Sound  
Mixed  
Temporary  

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

\subsection{Manifestation Agent Types}
\label{sec:manifestation_agent_types} 

\subsubsection{Distributor (theatrical)}
\label{sec:distributor_theatrical} 

Agent responsible for the theatrical distribution of a Manifestation.

\subsubsection{Distributor (non-theatrical)}
\label{sec:distributor_non_theatrical} 

Agent responsible for the non-theatrical distribution.

\subsubsection{Broadcaster}
\label{sec:broadcaster} 

Agent responsible for the broadcasting of a Manifestation, namely the network or station on which it aired or the network which makes it available on demand.

\subsubsection{Publisher}
\label{sec:publisher} 

Agent responsible for the home video publication or for the web publication of a moving image Manifestation: i.e. the publishing company, which often is the same as the distribution company.

\subsubsection{Manufacturer}
\label{sec:manufacturer} 

(Optionally, this information can be specified directly at the Item level)

Agent responsible for the activities of manufacturing a Manifestation: i.e. a laboratory.

\subsubsection{Agent responsible for preservation}
\label{sec:agent_responsible_for_preservation} 

Agent responsible for the preservation of a Manifestation: namely the rights-owner(s), the distributor(s) or an archive.

\subsubsection{Agent responsible for reproduction or transfer}
\label{sec:agent_responsible_for_reproduction_or_transfer} 

(Optionally, this information can be specified directly at the Item level)

Agent responsible for the activities of duplication/reproduction/transfer (dupes and masters): namely the rights-owner(s), the distributor(s) or an archive. (name: personal, corporate).

\subsubsection{Agent responsible for the archival availability}
\label{sec:agent_responsible_for_the_archival_availability} 

(Optionally, this information can be specified directly at the Item level)

The institution responsible for the availability of a moving image Manifestation intended for consultation or exploitation for cultural “fair” use, on the premises or through the activities of the institution.

For example, in a scenario where a Manifestation or Event occurs within the context of a film being shown for educational, research, cultural event purposes, etc. e.g. where an Archive has a public mediatheque which streams a large number of films and TV programmes on its premises for free which are for educational and cultural purposes, not financial ones.

\subsubsection{Agent responsible for the mere availability}
\label{sec:agent_responsible_for_the_mere_availability} 

(Optionally, this information can be specified directly at the Item level)

Agent responsible for making available a Manifestation not intended for public release (distribution, publication or broadcasting) in private environments.

For example, in a scenario where a Manifestation not intended for public release is shown within a private environment, such as a production company showing a “blooper” reel (off-cuts of amusing things that went wrong during shooting the film) at a cast and crew party on the production company or studio premises. Or a private press preview showing.

\subsubsection{Agent unclear or undetermined}
\label{sec:agent_unclea_or_undetermined} 

(Optionally, this information can be specified directly at the Item level)

Indicate if the Agent is unclear or undetermined, i.e. has not yet been determined.
Also, if the Agent could be one of two or more possibilities then name them and qualify that there is uncertainty as to which is correct.

\subsubsection{Agent not identified}
\label{sec:agent_not_identified} 

(Optionally, this information can be specified directly at the Item level)

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
