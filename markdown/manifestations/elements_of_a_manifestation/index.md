---
title: Elements of a Manifestation
---
<a id="sec-manifest_identifier"></a>
## Identifier
Create an unambiguous reference to the Manifestation, such as a specific standard number issued by an official body (i.e.
V-ISAN[^4] or DOI[^5]), or a system-automated assigned ID number.
These should be different identifiers than those for Works/Variants, since they are for specific embodiments of the Work/Variant.

If one or more identifiers are available, record each according to its standardised syntax, where allowable.
The following examples reflect both 3 and 4 level hierarchies, i.e. ones that use Variants and ones that do not have Variants but utilise Manifestations instead.

!!! example "Example"
    Lola rennt (Germany, 1998, Tom Tykwer) 

    Work identifier: ISAN 0000-0000-606A-0000-0-0000-0000-3 

    Variant identifier (original German): ISAN 0000-0000-606A-0000-0-0000-0002-0 

    Manifestation identifier: Home video publication (2007) – Run Lola Run – DVD – English – V-ISAN: ISAN 0000-0000-606A-0000-0-0000-0001-1 (DVD-31943)

!!! example "Example"
    Shichinin no samurai (Japan, 1954, Akira Kurosawa) 

    Work identifier: ISAN 0000-0001-61AE-0000-1-0000-0001-W 

    Variant identifier (Dubbed Spanish – Castellano): Los Siete Samurai: ISAN 0000-0001-61AE-0000-1-0000-0001-W

!!! example "Example"
    Les chevaliers du ciel (France, 2005, Gérard Pirès) 

    Manifestation identifier: Home video publication – DVD – Fox Pathé Europa (publisher) – 2006 – ISAN 0000-0001-8CFA-0000-I-0000-000-

!!! example "Example"
    8 1/2 (Italy, 1962, Federico Fellini) Otto e mezzo – Alternative title of the Work 

    Work identifier: ISAN 0000-0000-161F-0000-W-0000-0000-F 

    Manifestation identifier: V- ISAN 0000-0000-161F-0000-W-0000-0002-B – Italian (spoken); Japanese (subtitles) – DVD – Blu-ray – 2013/01/11 – Japan)

<a id="sec-manifest_identifier_type"></a>
### Identifier Type
If an institution’s system allows, as with the Work/Variant Identifiers a “Type” can be applied with an Identifier to define the source of the Identifier.

<a id="sec-manifest_title"></a>
## Title
Record at least one title, identifying phrase, or name for the Manifestation Title.
This is a transcribed element, reflecting the actual title as it appears on screen.
The original release title would be added under the Work/Variant Title field.

If multiple titles are recorded, where allowable, associate a “Title Type” to a title for differentiation between the various types of titles (see [Title Type](/manifestations/elements_of_a_manifestation/#sec-manifest_title_type) and [Title Types](/appendices/titles/title_types/#sec-title_types)).

The title of a Manifestation can sometimes differ, either slightly or wholly from the title of the Variant or Work to which it is linked.
This may be the case, for example, with the acquisition of an incomplete Manifestation lacking a title or with a title added by the source of the acquisition.

See [Title](/appendices/titles/#sec-appendix_title) for further titling details and information.

For creating titles for untitled or unidentified entities see [Supplied/Devised Titles (i.e. Creating titles for untitled/unidentified entities or production material)](/appendices/titles/title_types/#sec-supplied_devised_titles)

See [Definition](/appendices/aggregates/#sec-definition) for titling of Aggregates.

For guidance on wording, order, spelling, punctuation, accentuation and capitalisation, see [Purpose](/preliminary/purpose_scope_and_use/#sec-purpose).

For sources of information for the Manifestation Title, see [Sources of Information](/preliminary/prelim_sources_of_information/#sec-prelim_sources_of_information).

<a id="sec-manifest_title_type"></a>
### Title Type
Where relevant for an institution, if the Manifestation includes multiple titles, such as a title in another language for a dubbed or subtitled variant, record the relevant titles and associate a “Title Type” to each title for differentiation between the various types of titles (see [Titles and Title Types](/appendices/titles/)).

<a id="sec-manifest_language"></a>
## Language
“Language” should ideally be presented as a set of two elements: the language term, and its usage in a particular Manifestation.
Language can be present in a Manifestation as written, spoken or sung.
Its usage qualifies whether the specific language is dialogue, dubbed, subtitles, intertitles, etc.

<a id="sec-language_terms"></a>
### Language Terms
Where possible, record the language(s) using the full form of name, e.g., French, Italian, etc. rather than abbreviations or codes, by taking the most suitable value(s) from a controlled list.
This can be an in-house list but it is preferable to use a standard language list such as ISO 639 ([http://www.loc.gov/standards/iso639-2/php/code_list.php](http://www.loc.gov/standards/iso639-2/php/code_list.php)).

Optionally, record the language code as found in ISO 639.

If no language can be determined, the information can be omitted or indicated by a value of “not known”.

<a id="sec-item_usage_type"></a>
### Usage Type
More than one language can occur in different forms, depending on how the content is expressed: the usage type of the languages defines the form with which the language is expressed, for example, spoken, sung, written, etc.

Record the usage type of a language by taking the most suitable value from a controlled list.
A suggested list, which is open and not exhaustive, can be found in [Language Usage Types](/works/elements_of_a_work_variant/#sec-languages).

If usage type(s) cannot be determined, indicate a value of “unknown”.

!!! example "Example"
    Caccia tragica (Italy, Giuseppe De Santis, 1947) 

    Not for release (archival) – 35mm – Italian (spoken), Romanian (intertitles)

!!! example "Example"
    New York stories, (United States of America, Woody Allen, Francis Ford Coppola, Martin Scorsese, 1989 

    Home video publication – DVD, English (spoken); – Italian, German; English, Italian, German, French, Spanish (subtitles) – Buena Vista (publisher), 2002/05/16

!!! example "Example"
    The Bridge. Episode 1 (Sweden, Denmark, Charlotte Sieling, 2011) 

    TV broadcast – United Kingdom, 2012-04-21 - Swedish (Dialogue (original)), Danish (Dialogue (original)), English (Subtitles)

### Multiple language options for Digital Manifestations/Items

The above examples of language term and usage type relate to instances of one particular manifestation or print on analogue media or a recording of a particular broadcast, where there would be multiple individual instances of different language dialogue and subtitle/dubbed combinations (i.e. an individual Manifestation and Item(s) for each). However, with digital media, including digital streaming files, DVDs, Blu Rays, etc. there are often multiple language choices all on the one entity.

There are different options for capturing this, depending on the systems used, materials acquired, and decisions made by your institution on the extent of data to be captured.

Ideally, if desiring to capture all the language options of a digital entity, it would be best to have a further separate language section and fields within the Manifestation record. This is in order to distinguish clearly between the actual presence of particular spoken and/or subtitled languages on the soundtrack of the original moving image (or particular Manifestation of the moving image) and the selective choice options of other dubbed or subtitled alternative language(s), i.e. fields for Language and Usage and fields for alternative Selectable Language and Usage.

    !!! example "Example"
    New York stories, (United States of America, Woody Allen, Francis Ford Coppola, Martin Scorsese, 1989 

    Home video publication – DVD, English (spoken); – Selectable language alternatives Italian, German (dubbed); English, Italian, German, French, Spanish, (subtitles) – Buena Vista (publisher), 2002/05/16

The same language field could be utilised for both, but there is a high risk of ambiguity and lack of clarity regarding what language(s) actually feature on the original release and what are selectable alternative language options chosen by the individual viewer. It could imply that all the languages indicated appeared at the same time within the moving image. If used, then some form of qualifying note on the record would also be necessary for clarity.

It is not necessary to create a new Variant/Manifestation for each selectable language. In systems that only allow for single parent records, or have a 2-level hierarchy, this would mean having to create multiple Item records as well for what is effectively the same Item, i.e. giving an impression of multiple Items of the moving image held in a collection, when in fact there may only be one physical Item. In systems that allow one Item to link to multiple parent Manifestations then each language option could be reflected with its own Manifestation, or Variant plus Manifestation, if desired.

If capturing Selectable language(s) information it is also important to have the same fields and fill in this same information on the Item record too, as it may sometimes be different to the Manifestation. An acquired digital file of a streamed moving image may be a recording of what was streamed, which is likely to default to the most appropriate language version for the streaming country in which it was recorded, and as a recording will not therefore necessarily include all the other language options as well. Equally, if acquired directly from the streaming company, then an institution's deliverable specifications in agreements with the company may only be to include one, or a few, set(s) of language subtitles, namely just those in the language(s) of the institution's own country.

Alternatively, an insitution may take the stance that multiple language choice options are a known integral part of any DVD, Blu Ray, and digital streaming - whether one or two dubbed/subtitled language options, or twenty plus options - and do not necessarily all need to be captured on the Manifestation/Item in their records. If the focus or interest of their users is most likely to be for accessing a moving image in their own spoken or subtitled language then an institution may decide to prioritise just that in the Language and Usage fields of their relevant Manifestation/Item records.

<a id="sec-format_of_a_moving_image_manifestation"></a>
## Format of a Moving Image Manifestation
As previously mentioned, a Manifestation is defined on the basis of two criteria: changes in the publication context and changes in format.
The format of a Manifestation is the description of the physical artefact or the digital file on which it is fixed.
The concept of format as applied to Manifestations is the “ideal” representation of all the physical items or computer files that bear the same characteristics and descend from a common Work/Variant, regardless of what is actually held in a collection.

A majority of the physical and digital description elements of moving image Manifestations are intended to be inherited by the Items, as they serve as the exemplars of Manifestations.
In some databases, selection of a physical media type initiates provision of element fields relevant to that type at a Manifestation level, or an Item level, or both (e.g.
in a 2-Level hierarchy.
See “Shallow hierarchy model: 2 levels” found at [Elements of description across Works, Variants, Manifestations, and Items](/preliminary/core_elements_of_description/#sec-elements_of_description)).

Ideally the information need only be recorded once irrespective of where in the data structure an institution must place it.
Therefore guidelines for the treatment of high-level physical and digital description elements are explained fully in the Manifestation chapter.
The Item chapter contains a detailed listing of item-specific elements.
Physical properties such as Extent and Format at the Manifestation level represent the “ideal,” and item-specific elements will capture where it differs from this “ideal” at the Item level.

The information about the format of a Manifestation plays a relevant role because any change in format represents a criterion to determine the boundaries between one Manifestation and another (see [Boundaries between Manifestations](/boundaries/boundaries_between_manifestations/#sec-boundaries_between_manifestations)).

Record a new Manifestation of a Work/Variant when there is evidence of at least one, or more than one, of the following changes associated with the format:

- Changes to the physical artefact or the digital file on which it is fixed
- Changes to the display characteristics (i.e. in aspect ratio, sound or colour characteristics, etc.)
- Change in the container (i.e. cassette to cartridge as container for a tape).

In a note (See [Cataloguer’s Notes](/appendices/cataloguers-notes/)), explain the format changes used to determine the Manifestation in hand as different and “new” in comparison with any other, already identified and described Manifestation.

The description of the format of a Manifestation is articulated in the following elements:

- Media type
- Projection characteristics
- Sound characteristics
- Colour characteristics

<a id="sec-media_type_of_a_manifestation"></a>
### Media Type of a Manifestation
The media type is the medium on or the encoding format in which the Manifestation is fixed.

Its description consists of a general media type, which describes the basic proper- ties of the Item’s physical format, for example, film, video tape, digital file, etc., and a specific media type, which corresponds to the gauge, in case of films and tapes, and for digital files, to the physical carrier on which the file is stored or containers, when carriers for files are not separately catalogued.

<a id="sec-manifest_general_media_type"></a>
#### General Media Type
The broad media type of the Manifestation (e.g., film, video, audio, optical, digital file).
Recording this high-level information will enable simple searching for only film, video, digital, etc. elements rather than searching by all possible formats and carriers. A suggested list, which is open and not exhaustive, can include:

- Film
- Video Tape
- Video Disc
- Digital Tape
- Digital Disc
- Digital File

<a id="sec-manifest_specific_media_type"></a>
#### Specific Media Type
The specific media type for analogue film can be the width of the film stock or of the magnetic tape on which the Item is fixed.
For digital files, it is most important for users to immediately identify the file container or wrapper (MXF, MOV, DPX, etc.) rather than the physical media on which it is stored, because the physical media storing a file can change, but that does not necessarily mean that the file format has changed.
It is the digital file format that is the important distinguishing factor.
Information on the specific codecs and resolution are captured in other Item properties.

For optical media, only add commercially produced media here.
If the optical media is “writable” and is being used to store a digital file, put the digital file format in the general media type, and the optical storage media in specific media type.

Institutions should develop standard lists of terms to indicate the specific carrier type or refer to authoritative existing lists.

!!! example "Example"
    YEE ([http://myee.bol.ucla.edu/catrul.doc](http://myee.bol.ucla.edu/catrul.doc)) 5.3.3 (physical carriers) 

    AMIM2 5D, pp. 18-19 (for gauges/width values) 

    AMIM2 5B7, pp. 10-11 (including both “tape” and “disc” based video formats). 

    RDA 3.20; YEE ([http://myee.bol.ucla.edu/catrul.doc](http://myee.bol.ucla.edu/catrul.doc)) 5.3.14 (for encoding formats). 

    PBCore instantiationPhysical [http://metadataregistry.org/concept/list/vocabulary_id/145.html](http://metadataregistry.org/concept/list/vocabulary_id/145.html) (for physical carriers) 

    PBCore instantiationDigital ([http://pbcore.org/pbcoreinstantiation/instantiationdigital/](http://pbcore.org/pbcoreinstantiation/instantiationdigital/)) (for broad digital formats)

Additional sources of information include several SMPTE standards, engineering guidelines, and recommended practices. These are some of the most common terms, but not a complete or definitive list.

| **Film Gauge** | **Video** | **Audio** | **Optical** | **Digital File** | **Digital File Encoding** |
| --- | --- | --- | --- | --- | --- |
| 35mm | 1-inch C Format | 2” audioreel | CD | DPX | MPEG-4 |
| 16mm | Digital Betacam | 1” audioreel | DVD | MOV | Quicktime |
| Super 16mm | Betacam SP | ½” audioreel | Blu-Ray | MP4 | Real video |
| 8mm | 2-inch Quadruplex | ¼” audioreel | Laser Disc | MXF | SVCD |
| Super8mm | HDCAM SR | audiocassette |  | AVI | VCD |
| 9.5mm | D1 | 35mm magnetic track |  |  | Windows Media |
| 17.5mm | D5 | 16mm magnetic track |  |  |  |
| 70mm | DVCPRO HD |  |  |  |  | 

For digital files, list the physical carrier on which the file is stored. For all other materials, use this element to provide more specific information on the physical carrier.

Institutions should develop standard lists of terms to indicate the specific carrier type or refer to authoritative existing lists.

These are some of the most common terms, but not a complete or definitive list.

- LTO5
- LTO6
- T10000D
- HDD (abbreviated for “external hard drive”)
- DVD-R
- Blu-Ray 

For reasons of clarity and to avoid redundancy, optionally, institutions can decide to skip the general carrier type description, since it is already implicit in the specific carrier type.

<a id="sec-projection_characteristics_of_a_manifestation"></a>
## Projection Characteristics of a Manifestation{
The projection characteristics of a Manifestation include aspect ratio and aperture or image format.

**Aspect Ratio/Image Ratio**

The aspect ratio (also known as the image ratio or projection ratio) is the projected image area visible on screen, expressed as a value of width to height (the value of height always being “1”), for example, 2.34:1, 2.39:1.
Selection should be made from a controlled list of values.
A suggested list of examples, which is open and not exhaustive, includes:

- 1.33:1
- 1.37:1
- 1.19:1
- 2.55:1
- 2.35:1
- 1.66:1
- 1.75:1
- 1.85:1
- 2.39:1
- 4:3

Fuller details and examples of “aspect ratio” value lists can be found in the Technical Glossary of Common Audiovisual Terms (National Film and Sound Archive Australia), [The Advanced Projection Manual](https://iupress.org/9782960029611/the-advanced-projection-manual) and the PBCore essenceTrackAspect Ratio [http://metadataregistry.org/concept/list/vocabulary_id/129.html](http://metadataregistry.org/concept/list/vocabulary_id/129.html)


The aspect ratio reflects the compositional intentions of the original content makers and the intended presentation of the moving image content.[^6] If the aspect ratio of a Work/Variant is altered, moving image information is lost, creating a Manifestation/Item with different moving image content.[^7] The Manifestation should reflect the projected image of the Work/Variant that it represents, rather than that on the Item.
Institutions may record variations in projection characteristics as Item-specifics, rather than create multiple Manifestations.

**Aperture/Image Format**

The actual exposed image or picture area as it appears on the moving image itself, for example Academy, Full screen, Widescreen, etc. The image format (aperture) does not necessarily bear any relation to the preferred image ratio (projection ration or aspect ratio) of the moving image.[^8]

Selection should be made from a controlled list of terms.
A suggested list of examples, which is open and not exhaustive, includes:

- Academy 
- Widescreen 
- Cinemascope 
- Movietone 
- Flat 
- Full Height 
- Full Screen 
- Anamorphic 
- 3D 
- Pan and scan 
- Pillarbox (bars added at the sides) 
- Letterbox/Widescreen (bars added at the top and bottom) 
- Windowbox (bars added at the side and the top and bottom) 

Further examples can be found in [The Advanced Projection Manual](https://iupress.org/9782960029611/the-advanced-projection-manual/).

<a id="sec-sound_characteristics_of_a_manifestation"></a>
### Sound Characteristics of a Manifestation
Sound characteristics are technical specifications relating to the placement of sound on a Manifestation.[^9]

Its description consists of a statement about the presence or absence of sound, and optionally, in case of presence, of the description of the method with which the sound has been fixed.

Indicate the presence or absence of sound in the Manifestation. Selection should be made from a controlled list of terms, e.g.:

- Sound  
- Silent  
- Mute  
- Combined  
- Combined as Mute  
- Combined as Sound  
- Mixed  
- Temporary 

Optionally, use a flag-type value indicating if the Manifestation includes recorded sound or not (i.e.: has sound: yes/no).

<a id="sec-sound_systems"></a>
#### Sound Systems
Describes the technical or proprietary system used to record the sound on a Manifestation. Select from a controlled list, e.g.:

- Dolby SR
- Dolby Digital
- Mute
- Combined Magnetic Sound
- Combined Optical Sound
- VA RCA Duplex

<a id="sec-manifest_sound_channel_configuration"></a>
#### Sound Channel Configuration
If the Manifestation has sound, note here the track configuration (e.g., mono, stereo, etc.).
Selection should be made from a controlled list of terms.

In case of presence of sound, optionally, if considered relevant, record the name of the physical principle of sound recording. Selection should be made from a controlled list of terms, e.g.:

- Needle sound
- Optical
- Magnetic
- Analogue sound
- Digital

If the Work/Variant associated with the Manifestation in hand had sound originally, but the Manifestation lacks sound, describe it as silent (or mute) and give a note to that effect.[^10]

If the Work/Variant associated with the Manifestation in hand was silent originally, but the Manifestation has sound added, describe it as sound and make a note to that effect.

<a id="sec-colour_characteristics_of_a_manifestation"></a>
### Colour Characteristics of a Manifestation
The presence of colour(s), tone(s), etc. in a Manifestation.[^11]

Colour is also the specific colours, tones, etc. (including black and white) present in a moving image contained in a Manifestation.[^12]

It consists of a designation of the colour state and, optionally, of the description of the colour system.

Record the colour state of a Manifestation. Selection should be made from a controlled list of terms, e.g.:

- Colour
- Colour + Black & White
- Tinted
- Black and white
- Black and white (tinted)
- Black and white (toned)
- Black and white (tinted and toned)
- Sepia

Optionally, if considered relevant, describe the system or process by which colour is fixed on the carrier or as part of the digital encoding. Selection should be made from a controlled list of terms, e.g.:

- Pathécolor
- Technicolor
- Kinemacolor
- Anscocolor
- Ferraniacolor
- Fujicolor
- Kodachrome
- Eastmancolor

- RGB
- YUV

<a id="sec-extent_of_a_manifestation"></a>
## Extent of a Manifestation[^1]
The concept of extent as applied to Manifestations is the “ideal” logical, physical, or temporal (duration) units and not a description of a real physical object.
Actual objects in the collection are described at the Item level.

The extent of a Manifestation must be recorded as a reference for the completeness of all the related Items, using appropriate authoritative secondary sources where feasible.

<a id="sec-logical_extent_of_a_manifestation"></a>
### Logical Extent of a Manifestation
Logical extent is the number of discrete logical units which make up the Manifestation, both for analogue (e.g. reels, cassettes, discs) and digital (cassettes, discs, files), considering that the digital Manifestations may be bound to a physical carrier (such as DVD) or exist without a defined carrier (such as online streaming media, podcasts, etc.).

For digital Manifestations, there can be two extents: one for the number of files, and one for the extent of the carrier (e.g., 2 LTO6 tapes).

!!! example "Example"
    A home video publication: DVD in 2 discs 

    A theatrical print: in 6 reels 

    A hard-disk stored film in 3 files

Record the number of the logical units of a Manifestation in Arabic numerals, and, if necessary, specify the type of unit. Selection should be made from a controlled list of terms, e.g:

- Reel
- Roll
- Cassette
- Cartridge
- Loop
- Disc
- File
- Digital tape

If the number of the logical units of a Manifestation is uncertain, use a question mark following the unit count[^13] or record the uncertain number preceded by “approximately.”[^14]

If the number of the logical units of a Manifestation is indeterminate, record the information using a value of “unknown.”

Alternatively, provide for a distinguishing “precision” field specifying if the unit number is exact, approximate or unknown.

<a id="sec-physical_extent_of_a_manifestation"></a>
### Physical Extent of a Manifestation[^2]
Physical extent is the total “ideal” length or footage of the medium carrying the moving image Manifestation (using appropriate authoritative secondary sources where feasible such as filmographies, censorship visas, etc.).

The actual length is a characteristic of a singular Item since it can be different for multiple Items exemplifying the same Manifestation.

Record the total length in Arabic numerals, in metres or feet.

For digital Manifestations, record the total storage of all files that comprise the Manifestation.
Use Arabic numerals followed by MB, GB, or TB as appropriate.

The Unit of Measurement (feet, metres, GB, etc.) can be provided in a separate field.
This could be two separate fields side by side – one for numbers and one for size measurement.

If the length of a Manifestation is uncertain, use a question mark following the unit count or record the uncertain number preceded by “approximately.” In a note, give an explanation for the estimated footage or metre count, where known.
Estimating the total storage size for a digital Manifestation can be particularly difficult, since storage can vary depending on technical characteristics of the file(s).

If the length of a Manifestation is unknown, record the information using a value of “unknown.”

Alternatively, provide for a distinguishing “precision” field specifying if the length is exact, approximate or unknown.

<a id="sec-physical_extent_of_an_aggregate_manifestation"></a>
#### Physical Extent of an Aggregate Manifestation
For Aggregate Manifestations record the length or footage of the whole, i.e. the total in feet or metres of all the units that constitute the Aggregate.
In addition there is the option to qualify this with details of the physical extent of each individual unit in either a Notes field, or in multiple occurrences of the duration fields, depending on what systems used permit or an institution decides.

For more information about aggregates, see [Aggregates (Compilations, Multi-component productions)](/appendices/aggregates/).

<a id="sec-duration_of_a_manifestation"></a>
### Duration of a Manifestation[^3]
This is the total duration/running time under normal or specific playback conditions (e.g. a specific frame rate).
It represents the concept of “ideal” duration/running time (i.e., the duration reported on the moving image Manifestation itself – i.e., on the container, on the accompanying material, on the wrapper of metadata in a digital file or reported by authoritative secondary sources such as filmographies, censorship visas, etc.).
In cases where it is known that the time on the Manifestation is incorrect and all Items will inherit the same incorrect duration, record the accurate duration and make a note about the error/discrepancy found on the Manifestation.

The actual duration is usually considered a characteristic of a singular moving image Item, since it can differ among multiple Items exemplifying the same Manifestation.

Record, in Arabic numerals, the total duration/running time in minutes, normally rounded off to the nearest minute.
Optionally, include minutes and seconds, or, for a higher level of precision and to enable calculations, use the format HH:MM:SS.
This numeric format will help to calculate estimated digital storage in analogue-to-digital transfer projects.

If the duration/running time of a Manifestation is uncertain, use a question mark following the unit count or, if the system allows, use the qualifier “Duration Precision” and add the term “approximate.” (see [Duration Precision](/manifestations/elements_of_a_manifestation/#sec-manifest_duration_precision))

In a note, give an explanation for the estimated duration/running time, if such information applies.[^15]

If the duration/running time of a Manifestation is unknown, record the information using a value of “unknown.”

<a id="sec-duration_of_an_aggregate_manifestation"></a>
#### Duration of an Aggregate Manifestation
For Aggregate Manifestations record the duration of the whole, i.e. the total running time of all the units that constitute the Aggregate.
In addition there is the option to qualify this with details of the duration of each individual unit in either a Notes field, or in multiple occurrences of the duration fields, depending on what systems used permit or an institution decides.

!!! example "Example"
    DVD “The Audrey Hepburn Collection” contains 3 films, all with extra features. The running times for each of those 3 units are given on the container. 

    The total running time of these may be added as duration, with an additional clarifying note detailing the running times of the individual units.

For more information about Aggregates see [Aggregates (Compilations, Multi-component productions)](/appendices/aggregates/).

<a id="sec-duration_of_a_manifestation_associated"></a>
#### Duration of a Manifestation associated with a Work/Variant of the Silent Era
When recording duration of Manifestations of a Work/Variant of the silent era, take into account that the rate of frames per second varied over the years and between Variants/Manifestations.
Also take into account the so-called “stretch frame” practice, adopted after the silent era, which “increases the number of frames printed on a film to enable films shot at silent speeds to be projected at sound speed and retain the original temporal characteristics.” [^16]

In a note, indicate the frame rate on which the duration is based or if the Manifestation is the result of a “stretch frame” practice.[^17] (See also [Frame Rate](/items/elements_of_a_moving_image_item/#sec-frame_rate))

<a id="sec-duration_of_a_broadcast"></a>
#### Duration of a Broadcast Manifestation associated with a Work/Variant
When recording duration for Broadcast Manifestations there are two potential sets of data: a Slot Duration and an Actual Running Time.
If the system allows, note the type of duration in the Duration Type element (see [Duration Type](/manifestations/elements_of_a_manifestation/#sec-duration_type)).

Slot Duration relates to information from TV listings or publicity information for the programmed “slot” on the TV channel, whereas Actual Running Time relates to the exact running time of the entity when it was broadcast, excluding any inserted advertisements, etc. Thus, for example, an episode of the soap opera “Coronation Street” may have a Slot Duration of 30 minutes, but an Actual Running Time of 24 minutes.

Similarly, record the start and end time of the broadcast, ideally using 24-hour clock notation, e.g. 23:00 rather than 11:00pm.
This may also involve two potential sets of data: a whole slot start and end time, or the actual more precise start and end time of the broadcast.

It is for an institution to choose whether to record both sets of data in each instance or limit to either just slot or actual broadcast/running times.

<a id="sec-manifest_duration_precision"></a>
#### Duration Precision
In this qualifier, note whether the duration is exact, approximate, or estimated.
Items can apply the additional “stock maximum.”

<a id="sec-duration_type"></a>
#### Duration Type
Where appropriate, add the type of duration being described.
For example, broadcast materials could have “Slot Duration” and “Actual Duration.”

<a id="sec-notes_for_manifestations"></a>
## Notes for Manifestations
Notes for Manifestations are annotations providing additional information relating specifically to Manifestation attributes and relationships.[^18] See [Cataloguer’s Notes](/appendices/cataloguers-notes/).

<a id="sec-date_and_country_of_manifestation"></a>
## Date and Country of Manifestation
Dates and country of Manifestation are not elements of a Manifestation under EN 15907, as in the latter it envisages this data being on linked Publication Events. However, in some systems they may be structured as elements of a Manifestation. For further consideration of this see [Boundaries between Manifestations and Events](/boundaries/boundaries_between_manifestations_and_events)

[^1]: Partially based on EN 15907, 6.8 except for the physical components/units number, which is not provided for in the standard.
[^2]: Based on FIAF 1991, 5.3.4.1, 87.
[^3]: Based on FIAF 1991, 5.3.4.2.
[^4]: The V-ISAN represents the third segment of the ISAN number, which consists of a 96-bits number structured as follows: the first is the root, which identifies the work, the second is the episode section, which identifies the part within a multi-part work, the third is the so-called version section, which identifies variants and Manifestations (particularly as far as format changes and “media embodiments”, such as Blu-Ray, digital files, tapes, etc.., are concerned): see [http://www.isan.org/docs/isan_user_guide.pdf](http://www.isan.org/docs/isan_user_guide.pdf), Version 2.2.2. February 2012, 13/49.
[^5]: DOI (= Digital Object Identifier): see [http://www.doi.org/](http://www.doi.org/).
[^6]: This definition from Academy Film Archive in-house glossary of terms, and OLAC, Moving Image Works, Part 3a: Operational Definitions (08/09) (PDF Document), [http://olacinc.org/drupal/capc_files/MIW_3a.pdf](http://olacinc.org/drupal/capc_files/MIW_3a.pdf).
[^7]: OLAC, Moving Image Works, Part 3a: Operational Definitions (08/09) (PDF Document), [http://olacinc.org/drupal/capc_files/MIW_3a.pdf](http://olacinc.org/drupal/capc_files/MIW_3a.pdf)
[^8]: This definition from Academy Film Archive in-house glossary of terms.
[^9]: RDA 3.17. 01
[^10]: Based on AMIM2 5C3.
[^11]: RDA 7.17.3 Colour of Moving Image
[^12]: RDA 7.17.3 Colour of Moving Image
[^13]: AMIM2, 5B5, p.9
[^14]: RDA: 3.4.0.4
[^15]: Based on FIAF 1991, 5.3.4.2.
[^16]: Definition of “Stretch frame” taken from: [http://www.nfsa.gov.au/preservation/glossary/stretch-frame](http://www.nfsa.gov.au/preservation/glossary/stretch-frame).
[^17]: Adapted from FIAF 5.3.4.2.
[^18]: Based on RDA 2.20.1.Basic Instructions on Making Notes on Manifestations or Items
