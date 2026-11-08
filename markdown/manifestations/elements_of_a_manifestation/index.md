

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

If multiple titles are recorded, where allowable, associate a “Title Type” to a title for differentiation between the various [Title Types](../../titles/title_types/index.md#sec-title_types)).

The title of a Manifestation can sometimes differ, either slightly or wholly from the title of the Variant or Work to which it is linked.
This may be the case, for example, with the acquisition of an incomplete Manifestation lacking a title or with a title added by the source of the acquisition.

See [Title](../../titles/titles/index.md#sec-appendix_title) for further titling details and information.

For creating titles for untitled or unidentified entities see [Supplied/Devised Titles (i.e. Creating titles for untitled/unidentified entities or production material)](../../titles/supplied_devised_titles/index.md#sec-supplied_devised_titles)

See [Definition](../../aggregates/index.md#sec-definition) for titling of Aggregates.

For guidance on wording, order, spelling, punctuation, accentuation and capitalisation, see [Purpose](../../preliminary/purpose_scope_and_use/index.md#sec-purpose).

For sources of information for the Manifestation Title, see [Sources of Information](../../preliminary/prelim_sources_of_information/index.md#sec-prelim_sources_of_information).

<a id="sec-manifest_title_type"></a>
### Title Type
Where relevant for an institution, if the Manifestation includes multiple titles, such as a title in another language for a dubbed or subtitled variant, record the relevant titles and associate a “Title Type” to each title for differentiation between the various types of titles (see [Titles and Title Types](../../titles/titles/index.md)).

<a id="sec-manifest_language"></a>
## Language
“Language” should ideally be presented as a set of two elements: the language term, and its usage in a particular Manifestation.
Language can be present in a Manifestation as written, spoken or sung.
Its usage qualifies whether the specific language is dialogue, dubbed, subtitles, intertitles, etc.

<a id="sec-language_terms"></a>
### Language Terms
Where possible, record the language(s) using the full form of name, e.g., French, Italian, etc. rather than abbreviations or codes, by taking the most suitable value(s) from a controlled list.

This can be an in-house list but it is preferable to use a standard language list such as ISO 639 ([http://www.loc.gov/standards/iso639-2/php/code_list.php](http://www.loc.gov/standards/iso639-2/php/code_list.php)).

If no language can be determined, the information can be omitted or indicated by a value of “not known”.

<a id="sec-item_usage_type"></a>
### Usage Type
More than one language can occur in different forms, depending on how the content is expressed: the usage type of the languages defines the form with which the language is expressed, for example, spoken, sung, written, etc.

Record the usage type of a language by taking the most suitable value from a controlled list.
A suggested list, which is open and not exhaustive, can be found in [Language Usage Types](../../works/elements_of_a_work_variant/index.md#sec-languages).

If usage type(s) cannot be determined, indicate a value of “unknown”.

!!! example "Example"
    Caccia tragica (Italy, Giuseppe De Santis, 1947) 

    Not for release (archival) – 35mm – Italian (spoken), Romanian (intertitles)

!!! example "Example"
    New York stories, (United States of America, Woody Allen, Francis Ford Coppola, Martin Scorsese, 1989)  
    
    Home video publication – DVD - English (spoken); Italian, German, French, Spanish (subtitles) – Buena Vista (publisher),     2002/05/16

!!! example "Example"
    The Bridge. Episode 1 (Sweden, Denmark, Charlotte Sieling, 2011) 

    TV broadcast – United Kingdom, 2012-04-21 - Swedish (Dialogue (original)), Danish (Dialogue (original)), English             (Subtitles)

<a id="sec-multiple_language_options_for_digital_manifestions_items"></a>
### Multiple language options for Digital Manifestations/Items

The above examples of language term and usage type relate to instances of one particular manifestation or print on analogue media or a recording of a particular broadcast, where there would be multiple individual instances of different language dialogue and subtitle/dubbed combinations (i.e. an individual Manifestation and Item(s) for each). However, with digital media, including digital streaming files, DVDs, Blu Rays, etc. there are often multiple language choices all on the one entity.

There are different options for capturing this, depending on the systems used, materials acquired, and decisions made by your institution on the extent of data to be captured.

There are largely three main possible approaches:

1.	Core description: record only the principal or relevant language(s) necessary for identification and access.  
2.	Extended Manifestation/Item description: distinguish the language actually presented from additional selectable dubbed       and/or subtitled languages.  
3.	Full descriptive approach: record the complete language configuration when this is significant for an institution's          collection, users, preservation responsibilities or access requirements.  

Ideally, if desiring to capture all the language options of a digital entity, it would be best to have a further separate language section and fields within the Manifestation record. This is in order to distinguish clearly between the actual presence of particular spoken and/or subtitled languages on the soundtrack of the original moving image (or particular Manifestation of the moving image) and the selective choice options of other dubbed or subtitled alternative language(s), i.e. fields for Language and Usage and fields for alternative Selectable Language and Usage.

!!! example "Example"
    New York stories, (United States of America, Woody Allen, Francis Ford Coppola, Martin Scorsese, 1989) 

    Home video publication – DVD, English (spoken); – Selectable language alternatives Italian, German (dubbed); English,        Italian, German, French, Spanish, (subtitles) – Buena Vista (publisher), 2002/05/16

The same language field could be utilised for both, but there is a high risk of ambiguity and lack of clarity regarding what language(s) actually feature on the original release and what are selectable alternative language options chosen by the individual viewer. It could imply that all the languages indicated appeared at the same time within the moving image. If used, then some form of qualifying note on the record would also be necessary for clarity. Alternatively, an additional field to go alongside the Lanaguage and Usage field indicating original or selectable language on the Manifestation would aid clarity.

It is not necessary to create a new Variant/Manifestation for each selectable language. In systems that only allow for single parent records, or have a 2-level hierarchy, this would mean having to create multiple Item records as well for what is effectively the same Item, i.e. giving an impression of multiple Items of the moving image held in a collection, when in fact there may only be one physical Item. 

In 3-level hierarchy systems that allow one Item to link to multiple parent Manifestations then each language option could be reflected with its own Manifestation if desired, e.g.


<center><object data="/diagrams/manif_multi_lang_threelevel.drawio.svg" type="image/svg+xml" width="80%"></object></center>


Similarly, in systems where Variants are used that allow one Manifestation to link to multiple parent Variants then each language option could be reflected with its own Variant all linked to the one Manifestation and Item, if desired. This would also be the structuring that is RDA compliant (if following the RDA standard then Variants will be called Expressions), e.g.


<center><object data="/diagrams/manif_multi_lang_rda.drawio.svg" type="image/svg+xml" width="80%"></object></center>


However, a similar ambiguity to that of utilising the one language field for both actual and selectable languages could arise. So notes would be needed on the Manifestation/Item to clarify that there are selectable languages for the user to choose on the one entity, not that it is an Aggregate consisting of three versions of the film itself one after the other and all on one Blu Ray.  

If capturing Selectable language(s) information it is also important to have the same fields and fill in this same information on the Item record too, as it may sometimes be different to the Manifestation. 

An acquired digital file of a streamed moving image may be a recording of what was streamed, which is likely to default to the most appropriate language version for the streaming country in which it was recorded, and as a recording will not therefore necessarily include all the other language options as well. Equally, if acquired directly from a streaming company, then an institution's deliverable specifications in agreements with the company may only be to include one, or a few, set(s) of language subtitles, namely just those in the language(s) of the institution's own country.  

It is also possible that language(s) are added as part of digitalisation, preservation or other technological processes so it will be important to be able to specify which languages were added in relation to particular Items in those instances.  

The Item should record the actual characteristics of the material held by an institution rather than simply inherit all the possibilities of the Manifestation.  

Alternatively, an insitution may take the stance that multiple language choice options are a known integral part of any DVD, Blu Ray, and digital streaming - whether one or two dubbed/subtitled language options, or twenty plus options - and do not necessarily all need to be captured on the Manifestation/Item in their records. If the focus or interest of their users is most likely to be for accessing a moving image in their own spoken or subtitled language then an institution may decide to prioritise just that in the Language and Usage fields of their relevant Manifestation/Item records, taking the "core description" approach.  

<a id="sec-format_of_a_moving_image_manifestation"></a>
<a id="sec-physical_digital_description_of_a_manifestation"></a>
## Physical and Digital Description of a Manifestation
As previously mentioned, a Manifestation is defined on the basis of two criteria: changes in the publication context and changes in format.
Physical and digital description records technical characteristics such as format, projection, sound, and colour. For a Manifestation describing a particular release or edition, its expected characteristics can provide a reference for the associated Items, regardless of which Items are held in a collection.

This reference does not imply that every Item associated with a Manifestation has the same technical characteristics. As explained in [Moving Image Manifestations](../index.md#sec-moving_image_manifestations), a Pre-Release Manifestation may group different production materials, and institutions may associate in-house derivatives with the same Manifestation as their sources. A single “ideal” technical format need not apply to every Item in such a grouping.

Manifestation-level characteristics may be reused in Item descriptions where they apply to the object being described. Item descriptions should record the actual characteristics of each object; characteristics should not be assumed to apply solely because the Item is linked to that Manifestation.
In some databases, selection of a format or broad format category initiates provision of element fields relevant to that format at a Manifestation level, an Item level, or both, for example in a 2-Level hierarchy.
See “Shallow hierarchy model: 2 levels” found at [Elements of description across Works, Variants, Manifestations, and Items](../../preliminary/core_elements_of_description/index.md#sec-elements_of_description).

Ideally the information need only be recorded once irrespective of where in the data structure an institution must place it.
Therefore guidelines for the treatment of high-level physical and digital description elements are explained fully in the Manifestation chapter.
The Item chapter contains a detailed listing of item-specific elements.
Where Extent and Format at Manifestation level describe an expected or “ideal” release, Item-specific information records the actual material and any differences from that reference. Where the Manifestation groups varied materials, describe each Item on its own terms rather than treating its different characteristics as deviations from a single ideal object.

Differences in format can help distinguish Manifestations. Apply the criteria below together with the institutional options described in [Boundaries between Manifestations](../../boundaries/boundaries_between_manifestations/index.md), including the option of associating an in-house copy in a different format with the same Manifestation as its source.

Subject to those institutional options, record a new Manifestation of a Work/Variant when there is evidence of one or more of the following changes associated with the format:

- Changes to the physical artefact or the digital file on which it is fixed
- Changes to the display characteristics (i.e. in aspect ratio, sound or colour characteristics, etc.)
- Change in the container (i.e. cassette to cartridge as container for a tape).

In a note (See [Cataloguer’s Notes](../../appendices/cataloguers-notes/index.md)), explain the format changes used to determine the Manifestation in hand as different and “new” in comparison with any other, already identified and described Manifestation.

The physical and digital description of a Manifestation includes the following elements:

- Format
- Projection characteristics
- Sound characteristics
- Colour characteristics

<a id="sec-media_type_of_a_manifestation"></a>
<a id="sec-manifest_general_media_type"></a>
<a id="sec-manifest_specific_media_type"></a>
<a id="sec-manifestation_format"></a>
### Format

Format describes the physical or digital technical form in which content is fixed, including the physical medium, recording format, digital file format, or package format. It helps identify the technology, equipment, or software required to read, decode, reproduce, or play back that content. Other technical characteristics may be needed to establish the full playback requirements.

This develops the information addressed through Carrier type and Gauge within EN 15907's broader Format description.[^format_standard] Other technical characteristics, including aspect ratio, sound, colour, and digital codecs, are described separately in this manual.

Cataloguing systems may record format information in one field or distribute it across several fields, such as General Carrier Type and Specific Carrier Type, as used in the first edition of this manual (2016).[^format_history] Use the available structure consistently so that the technical format of the object can be identified. For digital materials, distinguish the format of the digital object from that of the physical storage media holding its copies.

Use terminology appropriate to the collection and cataloguing system, drawing on a controlled vocabulary where available. Broad format designations may support identification and searching, while named formats provide further technical information. This guidance does not require separate general and specific fields or a hierarchical vocabulary.

For film and tape, distinguish gauge—the width of the material—from format. A format designation may include its gauge, but different formats may use material of the same width. For example, Standard 8 and Super 8 share the same nominal gauge but differ in perforation and image dimensions. Gauge remains a distinct descriptive attribute and may be recorded separately, even when it is also included in the format designation.

For digital objects, distinguish container formats, image file formats, and package formats. A package may contain files in several formats; an image sequence may comprise many files in one image format. Describe the component formats where needed to make their application clear. Codecs describe the encoding of the digital content and should not be treated as interchangeable with container or package formats.

Authored audio and video disc formats should be distinguished from optical media used to store digital objects. Whether a disc is writable or commercially produced does not, by itself, identify the technical format of its contents. Where physical storage media are also recorded in the catalogue, keep their characteristics distinguishable from those of the digital objects. See [Moving Image Items](../../items/index.md#sec-moving_image_items) for the scope of this distinction.

The following terms are examples, not exhaustive lists or a prescribed classification. Audio and video carrier formats may record analogue or digital signals; file-based audio and video objects are described through their digital formats.

#### Film Formats

- Standard 8mm film
- Super 8mm film
- 16mm film
- 35mm film
- 35mm magnetic film
- 70mm film

#### Audio Formats

- Open-reel audiotape
- Audiocassette
- CD (audio)
- DAT

#### Video Formats

- 1-inch Type C
- U-matic
- Betacam SP
- Digital Betacam
- DVD-Video
- Blu-ray

#### Digital Formats

- Container formats: MOV, MXF, MKV, MP4, WAV
- Image file formats: DPX, TIFF, OpenEXR
- Package formats: DCP, DCDM, IMF

#### Sources for Format Terminology

Institutions may develop their own controlled lists or refer to existing sources. These include SMPTE standards, engineering guidelines, and recommended practices, as well as the following:

!!! example "Examples of sources"
    YEE ([http://myee.bol.ucla.edu/catrul.doc](http://myee.bol.ucla.edu/catrul.doc)) 5.3.3 (physical carriers)

    AMIM2 5D, pp. 18-19 (for gauges/width values)

    AMIM2 5B7, pp. 10-11 (including both “tape” and “disc” based video formats).

    RDA 3.20; YEE ([http://myee.bol.ucla.edu/catrul.doc](http://myee.bol.ucla.edu/catrul.doc)) 5.3.14 (for encoding formats).

    PBCore instantiationPhysical [http://metadataregistry.org/concept/list/vocabulary_id/145.html](http://metadataregistry.org/concept/list/vocabulary_id/145.html) (for physical carriers)

    PBCore instantiationDigital ([http://pbcore.org/pbcoreinstantiation/instantiationdigital/](http://pbcore.org/pbcoreinstantiation/instantiationdigital/)) (for broad digital formats)

<a id="sec-projection_characteristics_of_a_manifestation"></a>
### Projection Characteristics of a Manifestation
The projection characteristics of a Manifestation include aspect ratio and aperture or image format.

**Aspect Ratio/Image Ratio**

Aspect ratio (also known as the image ratio or projection ratio) expresses the relationship between image width and height. Film aspect ratios are conventionally expressed with the height normalised to 1, for example 1.37:1 or 2.39:1. Video aspect ratios are also commonly expressed as whole-number proportions, such as 4:3 or 16:9. State whether the value describes the recorded image area, the active image area within an encoded frame, or the intended presentation, where this distinction is relevant.
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


The intended presentation aspect ratio reflects the compositional intentions of the original content makers.[^6] Distinguish alterations to the image, such as cropping or stretching, from changes to the surrounding frame, such as letterboxing or pillarboxing. Cropping may remove image information.[^7] Adding borders does not, by itself, change the image's proportions or remove content.

Where applicable, describe the intended presentation at Manifestation level and the actual characteristics of the particular Item in its description.

Institutions may record variations in projection characteristics as Item-specifics, rather than create multiple Manifestations.

**Aperture/Image Format**

For film, describe the recorded image area and the applicable aperture or image format, for example Academy or full aperture.[^8] Distinguish the recorded image area from the area intended to be shown in projection, which may be masked.

Select terms from one or more controlled vocabularies, as appropriate to the aspects being described. The following examples are illustrative, not exhaustive, and may be used in combination.

*Aperture and recording geometry*

- Academy
- Full aperture
- Movietone

*Named image systems*

- CinemaScope
- Todd-AO

*Image characteristics*

- Anamorphic

*Broad presentation designations*

- Widescreen
- Flat
- Full Height
- Full Screen

*Image placement and reframing*

- Pan and scan (reframing the image)
- Pillarbox (bars added at the sides)
- Letterbox (bars added at the top and bottom)
- Windowbox (bars added at the sides and top and bottom)

*Stereoscopic presentation*

- 3D

Further examples can be found in [The Advanced Projection Manual](https://iupress.org/9782960029611/the-advanced-projection-manual/).

<a id="sec-sound_characteristics_of_a_manifestation"></a>
### Sound Characteristics of a Manifestation
Sound characteristics describe the presence or absence of recorded sound and, where relevant, its technical characteristics.[^9] The example lists below distinguish these aspects; they are suggested values, not exhaustive lists. Select terms from one or more controlled vocabularies appropriate to the aspects being described.

**Presence or absence of sound**

Select terms from a controlled vocabulary, for example:

- Sound
- Silent

If the associated Work/Variant originally had sound but the Manifestation lacks it, record the absence and explain it in a note.[^10]

If the associated Work/Variant was originally silent but the Manifestation includes added recorded sound, describe it as Sound and explain the addition in a note.

Optionally, also record a yes/no value indicating whether recorded sound is present.

<a id="sec-sound_systems"></a>
#### Sound System
Describe the sound system used, using a broad category or a specific system as appropriate. Select terms from a controlled vocabulary, for example:

- Needle sound
- Optical
- Magnetic
- Dolby Stereo SR
- Dolby Digital
- VA RCA Duplex

<a id="sec-noise_reduction"></a>
#### Noise Reduction
Some sound systems, such as Dolby Stereo, incorporate noise reduction; it may also be used with other recording methods, such as magnetic sound. Where relevant, describe noise reduction separately from the sound system, for example:

- Dolby A
- Dolby SR

<a id="sec-manifest_sound_channel_configuration"></a>
#### Sound Channel Configuration
If recorded sound is present, describe its channel configuration. Select terms from a controlled vocabulary, for example:

- Mono
- Stereo

These terms describe the arrangement of sound channels, not the sound system. The groupings above do not require separate database fields.

<a id="sec-colour_characteristics_of_a_manifestation"></a>
### Colour Characteristics of a Manifestation
Distinguish the colour appearance of the image from the technical means used to produce or encode it.[^11] Colour appearance describes what is visible, including black and white, colour, and the appearance of tinting or toning.[^12] The technical description identifies the colour system, process, or digital encoding used. A particular appearance does not, by itself, establish how it was produced.

**Colour appearance**

Record the colour characteristics of the image represented by the Manifestation, including black and white, tinting, toning, or combinations of colour and black and white. Where these characteristics vary between sections, describe the variation as needed. Select terms from a controlled vocabulary, for example:

- Colour
- Black and white
- Tinted
- Toned
- Tinted and toned (both present in the same image)

More specific vocabulary terms may identify particular tint colours or toning processes, such as blue tinting or sepia toning. These can support searching by the particular treatment or colour represented. Distinguish a process applied to the material from its appearance reproduced in a copy.

Tinting and toning can be described both as processes applied to film material and as colour appearances. State which meaning is intended. A film element may have undergone tinting or toning, while a photographic or digital copy may reproduce that appearance without having undergone the same process.

For digital Manifestations and Items, terms such as Tinted or Toned may describe the colour appearance reproduced in the image, rather than a physical treatment of the digital object. Make this distinction clear in the description.

**Colour systems and processes**

Where relevant, also record the colour system or process used. Record the actual tinting or toning process applied to source film material separately where known. Select terms from a controlled vocabulary, for example:

- Pathécolor
- Technicolor
- Kinemacolor
- Anscocolor
- Ferraniacolor
- Fujicolor
- Kodachrome
- Eastmancolor

**Digital colour encoding**

For digital materials, distinguish the image's colour appearance from its colour encoding. RGB and YUV describe colour models, not film colour processes, and do not, by themselves, establish that the image is in colour. Record relevant digital colour-encoding information separately where needed.

Manifestation-level information should describe characteristics applicable to the associated Items; record Item-specific characteristics and differences in the Item descriptions. These groupings do not require separate database fields.

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

For more information about aggregates, see [Aggregates (Compilations, Multi-component productions)](../../aggregates/index.md).

<a id="sec-duration_of_a_manifestation"></a>
### Duration of a Manifestation[^3]
This is the total duration/running time under normal or specific playback conditions (e.g. a specific frame rate).
It represents the concept of “ideal” duration/running time (i.e., the duration reported on the moving image Manifestation itself – i.e., on the container, on the accompanying material, on the wrapper of metadata in a digital file or reported by authoritative secondary sources such as filmographies, censorship visas, etc.).
In cases where it is known that the time on the Manifestation is incorrect and all Items will inherit the same incorrect duration, record the accurate duration and make a note about the error/discrepancy found on the Manifestation.

The actual duration is usually considered a characteristic of a singular moving image Item, since it can differ among multiple Items exemplifying the same Manifestation.

Record, in Arabic numerals, the total duration/running time in minutes, normally rounded off to the nearest minute.
Optionally, include minutes and seconds, or, for a higher level of precision and to enable calculations, use the format HH:MM:SS.
This numeric format will help to calculate estimated digital storage in analogue-to-digital transfer projects.

If the duration/running time of a Manifestation is uncertain, use a question mark following the unit count or, if the system allows, use the qualifier “Duration Precision” and add the term “approximate.” (see [Duration Precision](../../manifestations/elements_of_a_manifestation/index.md#sec-manifest_duration_precision))

In a note, give an explanation for the estimated duration/running time, if such information applies.[^15]

If the duration/running time of a Manifestation is unknown, record the information using a value of “unknown.”

<a id="sec-duration_of_an_aggregate_manifestation"></a>
#### Duration of an Aggregate Manifestation
For Aggregate Manifestations record the duration of the whole, i.e. the total running time of all the units that constitute the Aggregate.
In addition there is the option to qualify this with details of the duration of each individual unit in either a Notes field, or in multiple occurrences of the duration fields, depending on what systems used permit or an institution decides.

!!! example "Example"
    DVD “The Audrey Hepburn Collection” contains 3 films, all with extra features. The running times for each of those 3 units are given on the container. 

    The total running time of these may be added as duration, with an additional clarifying note detailing the running times of the individual units.

For more information about Aggregates see [Aggregates (Compilations, Multi-component productions)](../../aggregates/index.md).

<a id="sec-duration_of_a_manifestation_associated"></a>
#### Duration of a Manifestation associated with a Work/Variant of the Silent Era
When recording duration of Manifestations of a Work/Variant of the silent era, take into account that the rate of frames per second varied over the years and between Variants/Manifestations.
Also take into account the so-called “stretch frame” practice, adopted after the silent era, which “increases the number of frames printed on a film to enable films shot at silent speeds to be projected at sound speed and retain the original temporal characteristics.” [^16]

In a note, indicate the frame rate on which the duration is based or if the Manifestation is the result of a “stretch frame” practice.[^17] (See also [Frame Rate](../../items/elements_of_a_moving_image_item/index.md#sec-frame_rate))

<a id="sec-duration_of_a_broadcast"></a>
#### Duration of a Broadcast Manifestation associated with a Work/Variant
When recording duration for Broadcast Manifestations there are two potential sets of data: a Slot Duration and an Actual Running Time.
If the system allows, note the type of duration in the Duration Type element (see [Duration Type](../../manifestations/elements_of_a_manifestation/index.md#sec-duration_type)).

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
Notes for Manifestations are annotations providing additional information relating specifically to Manifestation attributes and relationships.[^18] See [Cataloguer’s Notes](../../appendices/cataloguers-notes/index.md).

<a id="sec-date_and_country_of_manifestation"></a>
## Date and Country of Manifestation
Dates and country of Manifestation are not elements of a Manifestation under EN 15907, as in the latter it envisages this data being on linked Publication Events. However, in some systems they may be structured as elements of a Manifestation. For further consideration of this see [Boundaries between Manifestations and Events](../../boundaries/boundaries_between_manifestations_and_events/index.md)

[^1]: Partially based on EN 15907, 6.8 except for the physical components/units number, which is not provided for in the standard.
[^2]: Based on FIAF 1991, 5.3.4.1, 87.
[^3]: Based on FIAF 1991, 5.3.4.2.
[^4]: The V-ISAN represents the third segment of the ISAN number, which consists of a 96-bits number structured as follows: the first is the root, which identifies the work, the second is the episode section, which identifies the part within a multi-part work, the third is the so-called version section, which identifies variants and Manifestations (particularly as far as format changes and “media embodiments”, such as Blu-Ray, digital files, tapes, etc.., are concerned): see [http://www.isan.org/docs/isan_user_guide.pdf](http://www.isan.org/docs/isan_user_guide.pdf), Version 2.2.2. February 2012, 13/49.
[^5]: DOI (= Digital Object Identifier): see [http://www.doi.org/](http://www.doi.org/).
[^6]: This definition from Academy Film Archive in-house glossary of terms, and OLAC, Moving Image Works, Part 3a: Operational Definitions (08/09) (PDF Document), [https://web.archive.org/web/20110702223309/http://olacinc.org/drupal/capc_files/MIW_3a.pdf](https://web.archive.org/web/20110702223309/http://olacinc.org/drupal/capc_files/MIW_3a.pdf).
[^7]: OLAC, Moving Image Works, Part 3a: Operational Definitions (08/09) (PDF Document), [https://web.archive.org/web/20110702223309/http://olacinc.org/drupal/capc_files/MIW_3a.pdf](https://web.archive.org/web/20110702223309/http://olacinc.org/drupal/capc_files/MIW_3a.pdf).
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
[^format_standard]: EN 15907:2010, §6.7, Format. Carrier type and Gauge are elements within its broader Format description, alongside aspect ratio, sound system, and colour; this is a correspondence, not an assertion of identical scope.
[^format_history]: See the first edition of [The FIAF Moving Image Cataloguing Manual (2016)](https://www.fiafnet.org/images/tinyUpload/E-Resources/Commission-And-PIP-Resources/CDC-resources/20160920_Fiaf_Manual-WEB.pdf), §§3.1.5.1.1–3.1.5.1.2, General Carrier Type and Specific Carrier Type.
