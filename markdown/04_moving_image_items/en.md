
\newpage
\section{Moving Image Items} 
\label{sec:moving_image_items} 

\subsection{Definitions} 
\label{sec:moving_image_items_definition}

A moving image Item is the physical or digital product of a Manifestation of a Work or Variant, i.e. the actual copy of a Work or Variant.
Whereas the Manifestation record describes the “ideal” of a particular format or publication, the Item record represents the actual holding in a repository’s collection.

An Item may consist of one or more components, i.e. the whole Item may consist of 1 reel or 5 reels, 2 VHS tapes or 1 DVD.
An Item record may contain fields or scope for separate barcodes and condition information for each component of the item (each reel for example) if required.

The Item may be whole or incomplete or a fragment.
In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.^[Digital medium definition taken from CEN’s “Film Identification – enhancing interoperability of metadata. Element sets and structures. FprEN 15907:2010 (E)]

\subsection{Elements of a Moving Image Item} 
\label{sec:elements_of_a_moving_image_item}

A majority of the physical and digital description elements of moving image Items are intended to be inherited from the Manifestations, as they serve as the exemplars of Manifestations.
In some databases, selection of a physical carrier type initiates provision of element fields relevant to that type at a Manifestation level, or an Item level, or both (e.g. in a 2 Level hierarchy.
See “Shallow hierarchy model: 2 levels” in \nameref{sec:elements_of_description}).

Ideally the information need only be recorded once irrespective of where in the data structure an institution must place it.
Therefore guidelines for the treatment of physical/digital description elements are explained fully in the Manifestation chapter.

This chapter contains Item-specific physical/digital description elements beginning at Section 3.1.5 (see \nameref{sec:item_specifics_extent}.
For example, properties such as Extent and Format at the Manifestation level represent the “ideal,” and item-specific information will capture where it differs from this ideal.
Only elements that are considered Item-specific have guidelines for the recording of data.
Physical/digital description elements that are considered Manifestation-specific, but which may be repeated at the Item level, contain hyperlinks to the relevant sections in the Manifestation chapter.

\subsubsection{Identifier} 
\label{sec:item_identifier}

Create an unambiguous numerical or alphanumerical reference to the moving image Item, such as a call number, barcode, shelf mark or similar, to uniquely identify the copy.^[EN 15907, “Inventory number,” p. 12] This may be in addition to separate Acquisition and Accession number(s) or identifier(s).

For digital files, the filename is not an identifier since filenames can change. Filenames are unreliable for uniquely identifying digital objects due to several limitations: users or systems may rename files, causing loss of reference; different versions of the same files from multiple sources can share identical names; and, changing storage locations makes filenames unreliable for tracking. Moreover different systems and organisations may use varying file-naming schemes and have limited interoperability.

Digital systems use UUID (Universally Unique Identifier), Internal Database IDs and Persistent Identifiers, which, unlike UUIDs, may not be globally unique but are essential for internal collection management and control. They play a crucial role in organising and archiving digital content, ensuring unambiguous identification within asset management systems.  This means that the filename is tracked as part of the technical metadata associated with a digital item.

As with Work and Manifestation Identifiers, besides its one unique identifier an Item can have more than one Identifier.

For example, a film Item may have a barcode for the can and a shelf number for its location.
Note the type of Identifier using Identifier Type.

\paragraph{Identifier Type} 
\label{sec:item_identifier_type} \

If an institution’s system allows, a “Type” can be applied with an Identifier to define the source of the Identifier.
Examples: Barcode, Shelf mark, Accession number, UUID (Universally Unique Identifiers), Persistent Identifiers (PID), Internal Database IDs.

\subsubsection{Title} 
\label{sec:item_title} 

Record at least one title, identifying phrase, or name for the moving image Item Title.

If multiple titles are recorded, where allowable, associate a “Title Type” to a title for differentiation between the various types of titles (see \nameref{sec:title_types}).

In most cases the title of an Item will be the same as that of the Manifestation to which it pertains.

The title of an Item can sometimes differ, either slightly or wholly from the title of the Manifestation, and/or Work/Variant to which it is linked.
In particular, this may be the case where an incomplete physical product of the Manifestation has been acquired.
For example, if a film in the collection is missing the first reel where opening title credits usually appear, the Item will not have a title to be transcribed.

For creating titles for untitled or unidentified entities see \nameref{sec:supplied_devised_titles}

For the treatment of Aggregates (e.g. compilations of whole Manifestations) as applied to Items, see Appendix [E.4 Titling of Aggregates] for titling of Aggregates.

For guidance on wording, order, spelling, punctuation, accentuation and capitalisation, see \nameref{sec:purpose}.

For sources of information for the Title, see \nameref{sec:prelim_sources_of_information}.

\paragraph{Title Type} 
\label{sec:item_title_type} \

Items can have more than just the title transcribed from the opening credits.
There can be title information written on leader, cans, and video containers.
Sometimes this information is different to what is in the credits; sometimes it is the only source of information to help identify an Item’s content.

Note the source of title information.
For Items where the only title information is found on a can or leader, use an Acquisition Title Type(s) (see \nameref{sec:alternative_title_types}) or descriptive words such as “Title on can” or “Title on leader.”

\subsubsection[Holding Institution]{Holding Institution 
\footnote {Based on EN 15907, Holding institution}} 
\label{sec:holding_institution}

Record the name of the institution possessing the moving image Item or authorised to make it available.

Optionally, if available, record a suitable repository identifier or a registered namespace identifier for the institution.

\subsubsection[Item Element Type]{Item Element Type 
\footnote {Based on EN 15907, Instantiation type}} 
\label{sec:item_item_element_type}

Record the nature or function of the moving image Item, describing its place in the photochemical or digital production or duplication process. Selection should be made from a controlled list of terms, e.g.:
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

\subsubsection{Item Specifics/Extent (e.g. physical/Digital description)} 
\label{sec:item_specifics_extent} 

All moving image Item descriptions should contain details of the physical/digital characteristics of the Items, their location, treatment and condition.

Institutions with archival moving images need to describe their holdings accurately for preservation, copying and reconstruction purposes.
Often there will be physically separate Items, for example image, track, music, different colour bases, etc., which are all essential parts of a single moving image.^[See The FIAF Cataloguing Rules for Film Archives (1991). 5. Physical Description. Introduction] Descriptive terminology covering all areas of physical description and attributes should be established in controlled lists of terms, to be applied in the relevant categories.
The range of these and what they are can be established in-house or utilising an established list, for example, the [FIAF Glossary of Technical Terms](https://www.fiafnet.org/pages/E-Resources/Technical-Terms.html).

Each Item should have its own description, whether the physical/digital characteristics between Items differ in one way or another, for example, in length, gauge, base, sound, etc., or, the Items acquired are duplicate identical copies.

Institutions may record as much technical information as they wish or need, but the Physical and Digital Description elements of an Item should ideally consist of the elements listed in the sub-sections below where discernible.

Further data relating to the condition, preservation, location, and, acquisition, accessioning, and source of the Item are also recommended elements for the Item (see \nameref{sec:access_conditions}).

These may be either added to the Item description itself or, where this is not possible, related to other separate files or databases, via physical link or text indication.

\paragraph{Carrier Type} 
\label{sec:carrier_type} \

Carrier type is the medium on or the encoding format in which the Item is fixed.

Its description consists of a general carrier type, which describes the basic proper- ties of the Item’s physical format, for example, film, video tape, digital file, etc., and a specific carrier type, which corresponds to the gauge, in case of films and tapes, and for digital files, to the physical carrier on which the file is stored.

\subparagraph{General Carrier Type} 
\label{sec:item_general_carrier_type} \

The broad media type of the Item (e.g., film, video, audio, optical, digital file).
Re- cording this high-level information will enable simple searching for only film, video, digi- tal, etc. elements rather than searching by all possible formats and carriers.

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

A suggested list can be found in \nameref{sec:manifest_general_carrier_type}.

For reasons of clarity and to avoid redundancy, optionally, institutions can decide to skip the general carrier type description for film and video, since it is already implicit in the specific carrier type.

\subparagraph{Specific Carrier Type} 
\label{sec:item_specific_carrier_type} \

Record the specific carrier type, by indicating

1. For film and video: the width of the film stock or of the magnetic tape on which the Item is fixed;

2. For digital files: The physical carrier storing the digital file.

For digital files, it is most important for users to immediately identify the file container or wrapper (MXF, MOV, DPX, etc.) rather than the physical media on which it is stored.
Physical media storing a file can change, but that does not necessarily mean that the file format has changed.
It is the digital file format that is the important distinguishing factor.
Information on the specific codecs and resolution are captured in other Item elements.

For optical media, only add commercially produced media here.
If the optical media is “writable” and is being used to store a digital file, put the digital file format in the gen- eral carrrier type, and the optical storage media in specific media type.

Record the specific carrier type, selecting from a suitable controlled list.
A suggested list, which is open and not exhaustive, can be found in \nameref{sec:manifestation_item_specific_carrier_type}.

\paragraph{Item Status} 
\label{sec:item_status} \

Description of the preservation or access status of the Item. Select term from a controlled list, e.g.  

Master   
Viewing   
Accessioned   
On Loan  
Status pending   
Removed

\paragraph{Sound}  
\label{sec:sound} \

Technical specifications relating to the fixation of sound in a moving image Manifestation/Item (see \nameref{sec:sound_characteristics_of_a_manifestation}).
This element is for high-level description of sound on the item; i.e., noting whether it has sound, is silent, etc.

Indicate the presence or absence of sound in the Item. Selection should be made from a controlled list of terms, e.g.:
Sound  
Silent  
Mute  
Combined  
Combined as Mute  
Combined as Sound  
Mixed  
Temporary 

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

\paragraph{Sound Channel Configuration}  
\label{sec:item_sound_channel_configuration} \

If the Item has sound, note here the track configuration (e.g., mono, stereo, etc.) Selection should be made from a controlled list of terms.

\paragraph{Sound System}
\label{sec:sound_system} \

See also \nameref{sec:sound_characteristics_of_a_manifestation}

Describes the technical or proprietary system used to record the sound on a Item. Select from a controlled list, e.g.:
Dolby SR
Dolby Digital
Mute
Combined Magnetic Sound
Combined Optical Sound
VA RCA Duplex

\paragraph{Colour}   
\label{sec:colour} \

For full instructions, see \nameref{sec:colour_characteristics_of_a_manifestation}.

The presence of colour(s), tone(s), etc. in an Item.^[RDA 7.17.3 Colour of Moving Image]

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

\paragraph{Unit Number}   
\label{sec:unit_number} \

For full instructions see \nameref{sec:logical_extent_of_a_manifestation}

The number of discrete logical units that make up the moving image Item.
Item unit number(s) may differ from that of the associated Manifestation.
The unit number in Manifestation relates to the ideal, whereas the Item unit number refers to the actual units held by the institution, e.g. an institution may have only acquired 3 reels of a 4-reel film.

\paragraph{Extent}   
\label{sec:extent} \

The actual physical/digital extent is a characteristic of a singular Item, since it can be different for multiple Items exemplifying the same moving image Manifestation.

For film, record footage for the film reel in feet or metres.
This footage represents actual length, rather than the “ideal” length, which is recorded for Manifestations (see \nameref{sec:physical_extent_of_a_manifestation}).
If your system allows, provide the Unit of Measurement – feet or metres – in another element.
Having separate numeric fields can facilitate calculations in determining the amount of footage that will be preserved.

For digital files, enter the numerical measurement indicating the size of the digital asset’s file(s), in KB, MB, GB, or TB.

As above, the Unit of Measurement (feet, metres, GB, etc.) may be provided in a separate field.
This could be two separate fields side by side – one for numbers and one for size measurement.

If the length of an Item is uncertain, use a question mark following the unit count or record the uncertain number preceded by “approximately.” In a note, give an explanation for the estimated footage or metre count, where known.

If the length of an Item is indeterminate, record the information using a value of “unknown.”

Alternatively, provide for a distinguishing “precision” field specifying if the length is exact, approximate or unknown.

\paragraph{Projection Characteristics}   
\label{sec:projection_characteristics} \

For full instructions, see \nameref{sec:projection_characteristics_of_a_manifestation}

The projection characteristics of a Manifestation/Item include aspect ratio and aperture or image format.

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

\paragraph{Broadcast Standard - Video}   
\label{sec:broadcast_standard_video} \

The broadcast standard for a video or DVD/BluRay: NTSC, PAL, SECAM.

\paragraph{Duration}    
\label{sec:duration} \

Duration in minutes of the moving image(s) contained in the Item, not the total dura- tion of the Manifestation.
Optionally, include minutes and seconds, or, for a higher level of precision and to enable calculations, use the format HH:MM:SS.
This numeric format will help to calculate estimated digital storage in analogue-to-digital transfer projects.

This duration represents actual temporal extent, rather than the “ideal” temporal extent, which is recorded for Manifestations (see \nameref{sec:duration_of_a_manifestation}).
Actual duration is a characteristic of a singular Item, since it can differ among multiple Items exemplifying the same Manifestation.

If the duration/running time of an Item is uncertain, use a question mark following the unit count or record the uncertain number preceded by “approximately.” If necessary, in a note, give an explanation for the estimated duration/running time, where known.

If the duration/running time of an Item is indeterminate, record the information using a value of “unknown.”

Alternatively, provide for a distinguishing “precision” field specifying if the duration/ running time is exact, approximate or unknown.
If the Item is a video or audio tape where the tape stock maximum duration is identified (e.g., Fuji M321-SP 30M is a Betacam SP tape of 30 minutes duration), that maximum duration can be noted in the “precision” field as “stock maximum.” This information can be helpful since it implies the Item can- not be longer than the maximum duration of the stock.

\subparagraph{Duration Precision}    
\label{sec:item_duration_precision} \

In this qualifier, note whether the duration is exact, approximate, estimated, or stock maximum.

\paragraph{Frame Rate}    
\label{sec:frame_rate} \


Frame rate is the native frame rate for the Item.
Information related to the frame rate used during a digitisation process is added to Transfer Speed (see \nameref{sec:transfer_speed}).

Frame Rate and Transfer Speed can sometimes be the same thing, and at other times different, depending on whether it is an Item that is being scanned into a digital file or an Item that is a digital file to start with.
For example, a silent film that was shot at a 16 fps frame rate could be transferred at 23.98 fps.
In this case, the resulting digital file would have a frame rate of 23.98, even though the original film is 16 fps.

Precision can be added to this element by adding a “Type” qualifier to note if the frame rate is original, or the transfer rate.

Note that in digital cinema, a film can have Variable frame rates.

\paragraph{Base}    
\label{sec:base} \

The physical material or video format on which the Item is captured, for example, describing the flexible transparent material that supports a film items’ emulsion (e.g.  acetate, nitrate, polyester) or a magnetic track, (e.g. CTA).
Select from controlled list of terms, if possible, keep separate lists for analogue film material and analogue video.

\paragraph{Stock}    
\label{sec:stock} \

Describes the specific stock/brand on which the Item is captured. This element should be used for all media: film, video, audio, optical, digital tape, external hard drives.
Selection should be made from a controlled list of terms, e.g.:

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

\paragraph{Stock Batch}    
\label{sec:stock_batch} \

The stock batch number of the media the Item is captured on.
This can be a video, audio, optical media, or digital tape stock.
Identifying the batch number can assist in identifying problems related to specific manufactured batches.

\paragraph{Video Codec}    
\label{sec:video_codec} \

The video compression standard used in the digital video Item, for example, D10, MP4, etc.

Video and digital cinema formats contained in wrappers have separate audio files contained in the format with the video file.
For example, DCPs (contained in MXF files) are comprised of a JPEG2000 video file and a WAV audio file (along with textual information in an XML file), The audio codec is described separately.

Examples for value lists:

PBCore essenceTrackEncoding vocabulary:    
http://metadataregistry.org/concept/list/vocabulary_id/156.html

EBUCore Video Compression Code:    
https://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm

\paragraph{Audio Codec}    
\label{sec:audio_codec} \

The audio compression standard used in the audio file, whether it is contained in a wrapper with a video file or as a standalone audio file.

Examples for value lists:

PBCore essenceTrackEncoding vocabulary:      
http://metadataregistry.org/concept/list/vocabulary_id/156.html

EBUCore Video Compression Code:     
https://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm

\paragraph{Resolution}    
\label{sec:resolution} \

Note whether the Item’s resolution is Standard Definition, High Definition, etc.

\paragraph{Line Standard – Video}    
\label{sec:line_standard_video} \

Describes the number of scan lines which make up the image and indicates the resolution, for example, 405, 525, 1080.

\paragraph{Bit Depth}    
\label{sec:bit_depth} \

Selection should be made from a controlled list of terms.

Note that bit depth can be used in describing both video and audio files.

\paragraph{Source Device}    
\label{sec:source_device} \

Record the source playback device used in transfer projects.
This can be a video deck, film printer, or hardware.

\paragraph{Source Software}    
\label{sec:source_software} \

Record the source software used in playing a digital file.

\paragraph{Transfer Speed}    
\label{sec:transfer_speed} \

If the Transfer Speed is the same as the \nameref{sec:frame_rate}, these values should be the same.
However, silent films might be transferred at a higher speed than the original frame rate.
For example, a silent film that was shot at a 16fps frame rate could be transferred at 23.98 fps.
It is important to note the transfer speed so an institution can identify how the transferred Item compares to the source Item.
If the transfer speed is faster than the source frame rate, the target Item could have a shorter duration than the source Item.

\subsubsection{Access Conditions}    
\label{sec:access_conditions} 

Record any information on how and to whom the moving image Item can be made available, including details of the condition of the Item and of its treatment, preservation or restoration Events.
This creates a condition and preservation history for the Item,
and is also important for assessing conservation conditions and establishing and prioritising collections care and preservation activities.

\paragraph{Item Condition}    
\label{sec:item_condition} \

Observations about conditions will typically happen in the course of an Event such as inspection of an Item.
These observations should aim to be as clear and concise as possible, avoiding abbreviations and initials, and as far as possible using controlled vocabulary.
For example, establish whether to use “scratched”, “scratches” or “scratch marks” and be as consistent as possible.
This enables better searching and accessibility of data.

Record these actions as an Event (see \nameref{sec:items_events}), with the person or entity performing the action as an Agent (see \nameref{sec:items_agents}).

Ideally, elements covering information and details regarding the condition of an acquired Item would include those listed below.

This could be recorded using single or multiple specific headed fields (i.e., covering Base, Emulsion, Image, Perforations, etc.), and then sub-sections of the latter, to incorporate data ranging from graded scales designations (either numerical or alphabetical, for example 1-5, A-G, Perfect – Very Poor) with clear definitions of what each designation means; condition terms selected from a controlled list; free text additional qualification or clarification in observations or comments sections; identification of technical assessor; and, dates.

Record the condition of the Item including its base and/or emulsion and/or perforations, where applicable.
Selection should be made from a controlled list of terms, for example, “brittle”, “buckled”, “tears,” etc. A suggested list, which is open and not exhaustive, can be found in \nameref{sec:item_copy_condition_base_emulsion_film_and_video}.

Capture the date on which the condition of the Item was recorded (using ISO standard^[ISO 8601]).
The identification of the individual who carried out the technical assessment and has recorded the condition should also be given.
Any names should be given in full, rather than initials or abbreviations.
As stated above, people or companies performing inspections are Agents.

Note any indication that the Item is in need of servicing prior to being accessed for use.

\paragraph{Item Location}    
\label{sec:item_location} \

Item descriptions should indicate a storage location number in order to provide access and retrieval.
Movements and changes of location should also be logged in order to ascertain the precise location of an Item at any given time.
If possible, use the Item Identifier and Identifier Type fields to note an Item’s location (see \nameref{sec:item_identifier}).

This could be a single simple field, or could include multiple fields to reflect various electronic package or barcode numbers that may be attached to each individual can or container, shelf, or whatever is applicable to an individual institution.

\subsubsection{Notes for Items}    
\label{sec:notes_for_items} 

Notes for Items are an annotation providing additional information relating specifically to Item attributes and relationships.^[Based on RDA 2.20.1.Basic Instructions on Making Notes on Manifestations or Items] See \nameref{sec:cataloguers_notes}.

\subsection{Boundaries between Items}    
\label{sec:boundaries_between_items} 

The boundaries between moving image Items is determined primarily by the boundaries between Manifestations (see \nameref{sec:boundaries_between_manifestations}).
There may be multiple Items associated to a Manifestation that are, for all intents and purposes, exact copies, but which may have small differences that do not necessitate representation as a Manifestation.
For example, an institution may have two DVD-R copies of the same Manifestation, with cosmetic differences in their labels.

\subsection{Relationships of an Item}    
\label{sec:relationships_of_an_item} 

A relationship associates an instance of an Item with another instance of an entity.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.^[EN 15907 8.1 Relationships. General] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest.

An Item may have relationships with the following:

- Agent(s)
- Event(s)
- Other
- Manifestation

\subsubsection{Events}    
\label{sec:items_events} 

An Event characterises occurrences in the life cycle of a moving image Item.
Instances of any Event type can have Agent and “Other” relationships.

Record one or more Event types, for example, “preservation,” “inspection,” “acquisition”, etc., to express the nature of the Event’s relationship to the Item.
Selection should be made from a controlled list of terms.
A suggested list, which is open and not exhaustive, can be found in \nameref{sec:event_type}.

\subsubsection{Other Relationships}    
\label{sec:item_other_relationships} 

Express relationships that are not covered by the Agent and Event relationships.
These may include compilations of convenience, i.e. where an institution has transferred copies
of two or more films onto one reel/tape/DVD etc. for convenient storage.^[See Appendix \nameref{sec:aggregate_or_carrier}]

*Item(s) associated with the moving image Item.*

It is possible for a moving image Item to have a horizontal relationship with another Item as a related object.
Such associative relationships are more prevalent and varied at the Work level, but there are instances where Items need to be related, for example, where an institution has separate Items for Yellow, Cyan and Magenta Separation Negatives, each of which have to be combined in Technicolor Three Colour Strip Process to make a new colour print.
Or, hold separate sound and image Items that would both be needed to make a new print.
Similarly, in the case of restorations where separate Items or elements have been used to create a new restored Item.

```{=latex}
\begin{tcolorbox}
The Wizard of Oz (United States of America, 1939, Victor Fleming) \\
Yellow Separation Negative, Cyan Separation Negative, Magenta Separation Negative
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Local hero (United Kingdom, 1983, Bill Forsyth) \\
DPX sequence, WAV audio file
\end{tcolorbox}
```

*An Item that contains other Items (e.g. two or more separate Items are held on the same reel/tape/DVD etc. for convenient storage).*

```{=latex}
\begin{tcolorbox}
Selezione Fregoli 2002 \\
Compilation of 16 short Fregoli films, spliced together for projection convenience.
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Laughing gas (United States of America, 1914, Charlie Chaplin) \\
Those love pangs (United States of America, 1914, Charlie Chaplin) \\
(two Charlie Chaplin short comedies spliced together on one reel - for storage convenience).
\end{tcolorbox}
```

*Item that is the source of a moving image Item (e.g. In-house copying of an Item to create a new Item for preservation or access)*

```{=latex}
\begin{tcolorbox}
  35mm CTA Duplicating Postive copy of Carnival (c.1927) made from a 35mm \\
  Nitrate Negative copy of Carnival (c.1927)
\end{tcolorbox}
```

*Non-moving image Works/Items (e.g. Objects, documents, etc. relating to a specific Item)*

```{=latex}
\begin{tcolorbox}
  Shots of 1932 (United Kingdom, 1932) (home movie) 9.5mm Safety film Item related to paper donor agreement
\end{tcolorbox}
```

Record one or more “Other” relationship type terms to express the nature of the relationship to the Item, choosing the most specific term possible from existing relator terms lists, for example, “accompanied by,” “contained in,” etc. Selection should be made from a controlled list of values.
A suggested list, which is open and not exhaustive, can be found in \nameref{sec:item_other_relationship_types}.

In a note, add any additional information concerning the relationship considered relevant.

If the cataloguing system allows, attach a digital file that reproduces any associated “document”.

\subsubsection{Manifestation}    
\label{sec:manifestation} 

Express the relationship between a moving image Manifestation and a moving image Item (e.g. Part/part of).
