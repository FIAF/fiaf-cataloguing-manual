

The manual generally envisages recording shared physical and digital characteristics once at Manifestation level for use in Item descriptions. Institutions may also record these characteristics directly at Item level. In either approach, the Item description should reflect the actual object and identify its specific characteristics and differences.

In applying this principle, account should be taken of the nature of the associated materials. A Manifestation may describe copies of a particular release, but it may also bring together varied production materials or, according to institutional practice, source materials and derivatives in different formats. Item descriptions should therefore identify characteristics specific to each object and make clear which Manifestation-level information applies. Information describing some associated Items should not inadvertently be presented as a characteristic of every Item linked to that Manifestation (see [Moving Image Manifestations](../../manifestations/index.md#sec-moving_image_manifestations)).

In some databases, selection of a format or broad format category initiates provision of element fields relevant to that format at a Manifestation level, an Item level, or both, for example in a 2-Level hierarchy.
See “Shallow hierarchy model: 2 levels” in [Elements of description across Works, Variants, Manifestations, and Items](../../preliminary/core_elements_of_description/index.md#sec-elements_of_description).

Physical and digital description is covered in both the Manifestation and Item chapters. The detailed Item guidance begins at [Item Specifics/Extent](../../items/elements_of_a_moving_image_item/index.md#sec-item_specifics_extent), with cross-references to relevant Manifestation guidance.

Where properties such as Extent and Format at Manifestation level describe an expected or “ideal” release, Item-specific information records the actual material and any differences from that reference. Where the Manifestation groups varied materials, each Item should be described on its own terms rather than as a deviation from a single ideal object.

Further data relating to the condition, preservation, location, and, [acquisition](../../events/further_event_types/index.md#sec-acquisition), accessioning, and source of the Item are also recommended elements for the Item (see [Access Conditions](../../items/elements_of_a_moving_image_item/index.md#sec-access_conditions)). 

These may be either added to the Item description itself or, where this is not possible, related to other separate files or databases, via physical link or text indication.

A useful collection of technical metadata on digital Items as well as data collected during digitisation, can be found [here](https://docs.google.com/spreadsheets/d/1cm4KBG_e-bdMppKOcYsFTck7vv5rJDwRI9z0RYX5bNM/edit?gid=646006523#gid=646006523). This spreadsheet was created by a Task Force in the CDC, headed by Elzbieta Wysocka.

<a id="sec-item_identifier"></a>
## Identifier
Create an unambiguous numerical or alphanumerical reference to the moving image Item, such as a call number, barcode, shelf mark, UUID or similar, to uniquely identify the copy.[^3] This may be in addition to separate Acquisition and Accession number(s) or identifier(s). More information on [Acquisition](../../events/further_event_types/index.md#sec-acquisition).

For digital objects, assign an identifier to the object being described, whether it comprises one file or several. Do not rely solely on a filename or directory path: names and locations may change, and different files may share the same name. Retain filenames as technical metadata and record identifiers for components or individual files where needed. An object-level identifier does not require a separate catalogue record for every file.

Digital systems may use UUIDs (Universally Unique Identifiers), internal database identifiers, or persistent identifiers. Record the identifier scheme or namespace where necessary to make the reference unambiguous. Identifiers and links should connect the Item description to the corresponding digital object and, where applicable, to metadata held in linked systems, independently of its current storage location.

As with Work, Variant and Manifestation Identifiers, besides its one unique identifier an Item can have more than one Identifier.

For example, a film Item (and the Item-parts) may have a barcode for the cans and a shelf number for its location.
Note the type of Identifier using Identifier Type.

<a id="sec-item_identifier_type"></a>
### Identifier Type
If an institution’s system allows, a “Type” can be applied with an Identifier to define the source of the Identifier.
Examples: Barcode, Shelf mark, Accession number, UUID (Universally Unique Identifiers), Persistent Identifiers (PID), Internal Database IDs.

<a id="sec-item_title"></a>
## Title
Record at least one title, identifying phrase, or name for the moving image Item Title.

If multiple titles are recorded, where allowable, associate a “Title Type” to a title for differentiation between the various types of titles (see [Title Types](../../titles/title_types/index.md#sec-title_types)).

In most cases the title of an Item will be the same as that of the Manifestation to which it pertains.

The title of an Item can sometimes differ, either slightly or wholly from the title of the Manifestation, and/or Work/Variant to which it is linked.
In particular, this may be the case where an incomplete physical product of the Manifestation has been acquired.
For example, if a film in the collection is missing the first reel where opening title credits usually appear, the Item will not have a title to be transcribed.

For creating titles for untitled or unidentified entities see [Supplied/Devised Titles](../../titles/supplied_devised_titles/index.md#sec-supplied_devised_titles).

For the treatment of Aggregates (e.g. compilations of whole Manifestations) as applied to Items, see the appendix concerning 
[Titling of Aggregates](../../aggregates/titling_of_aggregates/index.md)

For guidance on wording, order, spelling, punctuation, accentuation and capitalisation, see [Purpose](../../preliminary/purpose_scope_and_use/index.md#sec-purpose).

For sources of information for the Item Title, see [Sources of Information](../../preliminary/prelim_sources_of_information/index.md#sec-prelim_sources_of_information).

<a id="sec-item_title_type"></a>
### Title Type
Items can have more than just the title transcribed from the opening credits.
There can be title information written on leader, cans, and video containers.
Sometimes this information is different to what is in the credits; sometimes it is the only source of information to help identify an Item’s content.

Note the source of title information.
For Items where the only title information is found on a can or leader, use an Acquisition Title Type(s) (see [Alternative title types](../../titles/title_types/index.md#sec-alternative_title_types)) or descriptive words such as “Title on can” or “Title on leader.”

<a id="sec-holding_institution"></a>
## Holding Institution[^1]
Record the name of the institution possessing the moving image Item or authorised to make it available.

Optionally, if available, record a suitable repository identifier or a registered namespace identifier for the institution.

<a id="sec-item_location"></a>
<a id="sec-item-location"></a>
### Item Location
Record location information sufficient to locate and retrieve the Item. Where locations have identifiers, record these as part of the location information.

Keep the Item’s identifier distinguishable from its location information, even where a shelf mark or other location-based reference also serves as an identifier.

Record movements and changes of location so that the current location of the Item or its parts can be established. Location information may be recorded directly or provided through linked records or systems, according to institutional practice. Barcodes may identify containers or storage locations and support the tracking of movements.

Where copies of a digital object are held in multiple storage locations, location information may refer to those copies without treating each as a separate Item. For digital Items, persistent identifiers may link to current access or storage information without making the location itself the Item’s identifier (see [Identifier](#sec-item_identifier)).

<a id="sec-item_acquisition type"></a>
### Item Acquisition Type
Moving image items change location during their life cycle in the archive and before or after. They are acquired, loaned, removed or not acquired.
Nowadays it becomes more and more important to have information about the provenance of Items in an institution's collection. 
In every one of these actions it is useful to record the agents involved (e.g. donor, recipient), location, and type of acquisition (e.g. donation). Ideally record the person/institution by linking to internal authority records as well as the date when the Item entered the collection.
The transfer of ownership is important for an archive to document, as it establishes legal ownership of the collection.

Typically, the transfer involves a contract, deed or agreement signed by both parties to certify that ownership of the object is transferred to the archive, and often this is a complex legal document. It is recommended therefore that the cataloguer capture the essential metadata elements below, and where feasible they should associate the catalogue record with an electronic version of the contract, by capturing filename / link to that document.

Particular acquisition agreements between object owner and archive may enforce restrictions on the archive, preventing them from undertaking certain activities on the item (for example, preventing them from digitising the item for preservation, or preventing them from exhibiting the item in internal cinemas). Any such restrictions should be captured in a ‘Provisos of acquisition’, ‘Conditions of access’ or ‘Conditions of reproduction’ set of fields, as outlined below. In addition, the acquisition agreement may enforce a protocol for disposal of any objects which are not ultimately accessioned into the archive’s permanent collection: for example, disposal may require approval by the acquisition source.

Record the acquisistion Type at Item level as a value list (e.g. bequest, commission, donation, off-air recording, purchase, unknown) as well as where it came from. 

<a id="sec-item_ownership"></a>
### Item Ownership
If possible, record who currently has ownership of the Item, ideally also tracking the history of the ownership. For example, the Item could have been deposited 20 years ago and has now changed ownership by contract to the holding institution. Many times, preservation decisions might be influenced by ownership status. Ideally record the person/institution by linking to internal authority records as well as the dates when changes of ownership occured. 

<a id="sec-item_item_element_type"></a>
## Item Element Type[^2]
Element Type describes the nature of an Item and its intended function within a production, duplication, preservation, or access workflow: why it was made and its place in that process. It helps distinguish, for example, a production original, an intermediate made for further copying, and a copy made for exhibition or viewing.

Element Type should be distinguished from the Item's format and its current preservation, access, or administrative status. Format describes the physical or digital technical form in which the Item exists, indicating the technology, equipment, or software required to reproduce, read, or decode its content. Element Type describes its place and intended purpose in the workflow. An institution's subsequent use or designation of an Item does not, by itself, change its Element Type. For example, a release print retained for preservation remains a release print.

Institutions should use a controlled vocabulary whose terms are consistent in scope, describing the nature and intended function of the Item. Avoid mixing Element Types with terms describing technical formats, colour processes, physical storage media, or current administrative status; record these characteristics in their respective fields.

Select an Element Type from the vocabulary used by the institution, based on the available information about the Item. Where its particular function is unknown, use an available term that accurately reflects what is known rather than assuming a function. Do not infer intended function solely from format, technical quality, storage location, or current use.

The following terms are examples, not an exhaustive vocabulary. They are arranged by format category, because the same function is named differently for different media. Audio and video Element Types describe physical tapes and discs, whether their signal is analogue or digital; file-based digital objects, including sound-only recordings, use digital Element Types. Physical storage media holding digital objects have no Element Type of their own. Select terminology appropriate to the Item being described.

| **Format** | **Element Type examples** |
| --- | --- |
| Film: picture | Original negative, Original cut negative, Duplicate negative, Film-out negative, Original reversal positive, Duplicate positive, Fine grain master positive, Work print, Answer print, Release print; Negative or Positive where generation or function is unknown |
| Film: sound | Sound negative, Sound positive, Separated magnetic sound |
| Audio tapes and discs | Original sound recording, Audio master |
| Video tapes and discs | Original video recording, Video master, Video access copy, Home video release |
| Digital files and packages | Original digital recording, Digital master, Digital mezzanine, Digital access copy, Digital release |

A digital release is made for the publication or distribution of the content, such as a distributor's theatrical or online delivery. Package and file formats do not determine Element Type: a DCP may, for example, be a digital release, an access copy made by an archive for screenings, or a master.

<a id="sec-item_specifics_extent"></a>
## Item Specifics/Extent (e.g. physical/digital description)
All moving image Item descriptions should contain details of the physical/digital characteristics of the Items, their location, treatment and condition.

Institutions with archival moving images need to describe their holdings accurately for preservation, copying and reconstruction purposes.

Often there will be physically separate Items, for example image, track, music, different colour bases, etc., which are all essential parts of a single moving image.[^4] Descriptive terminology covering all areas of physical description and attributes should be established in controlled lists of terms, to be applied in the relevant categories.
The range of these and what they are can be established in-house or utilising an established list, for example, the [FIAF Glossary of Technical Terms](https://www.fiafnet.org/pages/E-Resources/Technical-Terms.html).

Each Item should have its own description, whether the physical/digital characteristics between Items differ in one way or another, for example, in length, gauge, base, sound, etc., or, the Items acquired are duplicate identical copies.

Independently acquired digital objects may warrant separate Item descriptions even where their files are identical, for example where their provenance or acquisition conditions differ. Preserve the relevant acquisition histories and conditions whether the objects are described separately or together. Do not assume that they are backup copies of one digital object solely because their files are identical.

Institutions may record as much technical information as they wish or need, but the Physical and Digital Description elements of an Item should ideally consist of the elements listed in the sub-sections below where discernible.

A digital file may contain several streams, such as video, audio, or subtitles, including multiple audio or subtitle alternatives. A digital object comprising related files may carry these elements within individual files or across separate files. Where technical characteristics differ between streams or components of a digital Item, make clear which values belong together and which stream or component they describe. This does not require separate catalogue records.

Technical characteristics of digital objects may be obtained from embedded metadata or identified using tools such as [MediaInfo](https://mediaarea.net/en/MediaInfo). Check which stream or component each value describes.

<a id="sec-media_type"></a>
<a id="sec-item_general_media_type"></a>
<a id="sec-item_specific_media_type"></a>
<a id="sec-item_format"></a>
### Format

Format describes the physical or digital technical form in which content is fixed, including the physical medium, recording format, digital file format, or package format. It helps identify the technology, equipment, or software required to read, decode, reproduce, or play back that content. Other technical characteristics may be needed to establish the full playback requirements. Format should be distinguished from the Item's intended function, which is described through [Element Type](#sec-item_item_element_type).

Cataloguing systems may record format information in one field or distribute it across several fields, such as General Carrier Type and Specific Carrier Type, as used in the first edition of this manual (2016).[^5] Use the available structure consistently so that the technical format of the object can be identified. For digital materials, distinguish the format of the digital object from that of the physical storage media holding its copies.

Record the format of the actual Item. Reuse applicable Manifestation-level information and record Item-specific differences. Broad format designations may support searching, but separate general and specific fields or a hierarchical vocabulary are not required by this guidance. For common recording guidance, illustrative format terms, and the relationship to EN 15907, see [Format](../../manifestations/elements_of_a_manifestation/index.md#sec-manifestation_format).

For digital objects, identify the relevant container, image, or package format. A package may contain files in several formats, and an image sequence may comprise many files in the same image format. Record component formats where necessary to make the description unambiguous, without requiring a separate catalogue record for each file. Information on codecs and resolution is recorded in the corresponding technical properties.

Distinguish an authored audio or video disc from an optical disc used to store digital objects. The fact that a disc is writable or commercially produced does not, by itself, determine the function or technical format of its contents. For the distinction between digital objects and physical storage media, see [Moving Image Items](../index.md#sec-moving_image_items).

<a id="sec-item_status"></a>
### Item Status
Description of the current preservation, access, or administrative status of the Item. This is separate from [Element Type](#sec-item_item_element_type), which describes the nature and intended function of the Item in the workflow in which it was made. For example, retaining a release print for preservation does not change its Element Type.

A designation of how the Item is used, such as for preservation or for access, and its administrative status, such as whether it has been accessioned or is on loan, answer different questions. Where both are recorded, keep them distinguishable rather than mixing them in one list of values. Select terms from controlled lists, for example:

*Preservation and access designation*

- Preservation
- Access

*Administrative status*

- Accessioned
- On Loan
- Status pending
- Removed

Where local status terms such as Master or Viewing are used, make clear that they express the institution's current designation of the Item, not necessarily its original intended function.

<a id="sec-sound"></a>
### Sound
Indicate whether the Item includes recorded sound. For a digital object comprising related files, describe the object as a whole; sound may be carried within an audiovisual file or in separate associated audio files.

Select terms from a controlled vocabulary, for example:

- Sound
- Silent
- Mute

Use Silent where the moving image was made without a recorded soundtrack, as with films of the silent era. Use Mute for material whose content is intended to have recorded sound but which carries none of it, such as a picture negative of a sound film, a print with a blank soundtrack area, or a picture-only scan of a sound film. A digital object without audio need not be described as Mute, since the absence of audio in its technical description shows that no sound is carried; the term remains available where it helps distinguish such an object from silent material.

The absence of recorded sound in an Item does not, by itself, establish that its associated Manifestation lacks sound or that the Work was originally silent.

For film, distinguish a mute element with a blank soundtrack area from a silent-aperture element whose image extends into the area otherwise reserved for the soundtrack. Describe the image area under [Projection Characteristics](#sec-projection_characteristics).

Reuse applicable Manifestation-level information and record Item-specific differences. See also [Sound Characteristics of a Manifestation](../../manifestations/elements_of_a_manifestation/index.md#sec-sound_characteristics_of_a_manifestation).

<a id="sec-item_sound_channel_configuration"></a>
### Sound Channel Configuration
Record the sound channel configuration, using terms from a controlled vocabulary, for example mono, stereo, or 5.1.

Where an Item includes sound components or selectable soundtracks with different configurations, identify which configuration applies to each. Channel count alone does not establish the configuration; for example, two channels may carry stereo sound or two independent mono recordings.

<a id="sec-sound_system"></a>
### Sound System
See also [Sound Characteristics of a Manifestation](../../manifestations/elements_of_a_manifestation/index.md#sec-sound_characteristics_of_a_manifestation)

Record the sound system present on the Item, using a broad category or a specific system as appropriate. Select terms from a controlled vocabulary.

For digital objects, record the sound system that a soundtrack is made for or needs for reproduction, such as Dolby Digital, where known; record the encoding of the audio stream under [Audio Codec](#sec-audio_codec). Some names refer to both, so record each under its own attribute where both are known.

Examples of sound systems:

- Combined magnetic sound
- Optical variable area
- Dolby Stereo SR
- Dolby Digital
- VA RCA Duplex

Where relevant, record noise reduction separately; see [Noise Reduction](../../manifestations/elements_of_a_manifestation/index.md#sec-noise_reduction).

<a id="sec-colour"></a>
### Colour
For guidance on colour appearance and colour systems and processes, see [Colour Characteristics of a Manifestation](../../manifestations/elements_of_a_manifestation/index.md#sec-colour_characteristics_of_a_manifestation).

Record the colour characteristics of the image present in the Item.[^7] Where characteristics vary between components or sections, describe the variation as needed.

Distinguish the image's colour appearance from the processes used to produce it. Record tinting, toning, or another applied-colour process only for an Item that itself underwent it. A photographic or digital copy reproducing the result shares the appearance, Black and white with applied colour, without the process, as explained in the Manifestation guidance above.

Reuse applicable Manifestation-level information and record Item-specific differences.

**Digital colour encoding**

For digital materials, distinguish the image's colour appearance from its colour encoding. RGB and YUV describe colour models, not film colour processes, and do not, by themselves, establish that the image is in colour. Record relevant digital colour-encoding information separately where needed.

Where relevant, also record the colour space and transfer function. These describe different aspects of digital colour representation and should be distinguished from the colour encoding. Make clear which image stream or component the colour encoding, colour space, and transfer function describe. Select terms from controlled vocabularies appropriate to each aspect, for example:

*Colour encoding*

- RGB
- YUV

*Colour space*

- Rec. 709
- Rec. 2020

*Transfer function*

- Linear
- Log
- Gamma 2.4
- PQ
- HLG

These groupings do not require separate database fields.

<a id="sec-unit_number"></a>
### Unit Number
For full instructions see [Logical Extent of a Manifestation](../../manifestations/elements_of_a_manifestation/index.md#sec-logical_extent_of_a_manifestation)

The number of discrete logical units that make up the moving image Item. Item unit number(s) may differ from that of the associated Manifestation. The unit number in Manifestation relates to the ideal, whereas the Item unit number refers to the actual units held by the institution, e.g. an institution may have only acquired 3 reels of a 4-reel film.

<a id="sec-extent"></a>
### Extent
The actual physical/digital extent is a characteristic of a singular Item, since it can be different for multiple Items exemplifying the same moving image Manifestation.

For film, record footage for the film reel in feet or metres. 
This footage represents actual length, rather than the “ideal” length, which is recorded for Manifestations (see [Physical Extent of a Manifestation](../../manifestations/elements_of_a_manifestation/index.md#sec-physical_extent_of_a_manifestation)).
If your system allows, provide the Unit of Measurement – feet or metres – in another element.
Having separate numeric fields can facilitate calculations in determining the amount of footage that will be preserved.

For digital files, enter the numerical measurement indicating the size of the digital asset’s file(s), in KB, MB, GB, or TB.

As above, the Unit of Measurement (feet, metres, GB, etc.) may be provided in a separate field.
This could be two separate fields side by side – one for numbers and one for size measurement.

If the length of an Item is uncertain, use a question mark following the unit count or record the uncertain number preceded by “approximately.” In a note, give an explanation for the estimated footage or metre count, where known.

If the length of an Item is indeterminate, record the information using a value of “unknown.”

Alternatively, provide for a distinguishing “precision” field specifying if the length is exact, approximate or unknown.

<a id="sec-projection_characteristics"></a>
### Projection Characteristics
For full instructions, see [Projection Characteristics of a Manifestation](../../manifestations/elements_of_a_manifestation/index.md#sec-projection_characteristics_of_a_manifestation)

The projection characteristics of a Manifestation/Item include aspect ratio and aperture or image format.

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

<a id="sec-broadcast_standard_video"></a>
### Broadcast Standard - Video
Record the broadcast standard applicable to the Item, where relevant, for example NTSC, PAL, or SECAM.

<a id="sec-duration"></a>
### Duration
Duration in minutes of the moving image(s) contained in the Item, not the total duration of the Manifestation.
Optionally, include minutes and seconds, or, for a higher level of precision and to enable calculations, use the format HH:MM:SS (hours, minutes, seconds).
This numeric format will help to calculate estimated digital storage in analogue-to-digital transfer projects.

This duration represents actual temporal extent, rather than the “ideal” temporal extent, which is recorded for Manifestations (see [Duration of a Manifestation](../../manifestations/elements_of_a_manifestation/index.md#sec-duration_of_a_manifestation)).
Actual duration is a characteristic of a singular Item, since it can differ among multiple Items exemplifying the same Manifestation.

If the duration/running time of an Item is uncertain, use a question mark following the unit count or record the uncertain number preceded by “approximately.” If necessary, in a note, give an explanation for the estimated duration/running time, where known.

If the duration/running time of an Item is indeterminate, record the information using a value of “unknown.”

Alternatively, provide for a distinguishing “precision” field specifying if the duration/ running time is exact, approximate or unknown.

If the Item is a video or audio tape where the tape stock maximum duration is identified (e.g., Fuji M321-SP 30M is a Betacam SP tape of 30 minutes duration), that maximum duration can be noted in the “precision” field as “stock maximum.” This information can be helpful since it implies the Item cannot be longer than the maximum duration of the stock.

<a id="sec-item_duration_precision"></a>
#### Duration Precision
In this qualifier, note whether the duration is exact, approximate, estimated, or stock maximum.

<a id="sec-frame_rate"></a>
### Frame Rate
Frame rate is the native or preferred (if silent cinema) frame rate for the Item.
Information related to the frame rate used during a digitisation process is added to Transfer Speed (see [Transfer Speed](../../items/elements_of_a_moving_image_item/index.md#sec-transfer_speed)).

Frame Rate and Transfer Speed can sometimes be the same thing, and at other times different, depending on whether it is an Item that is being scanned into a digital file or an Item that is a digital file to start with. For example, a silent film that was shot at a 16 fps frame rate could be transferred at 23.98 fps. In this case, the resulting digital file would have a frame rate of 23.98, even though the original film is 16 fps.

Precision can be added to this element by adding a “Type” qualifier to note if the frame rate is original, or the transfer rate.

Note that in digital cinema, a film can have Variable frame rates.

<a id="sec-base"></a>
### Base
The physical material or video format on which the Item is captured, for example, describing the flexible transparent material that supports a film items’ emulsion (e.g.  acetate, nitrate, polyester) or a magnetic track, (e.g. CTA).
Select from controlled list of terms, if possible, keep separate lists for analogue film material and analogue video.

- Acetate  
- Diacetate  
- Triacetate (aka CTA)
- Nitrate  
- Polyester  
- Magnetic tape  

<a id="sec-stock"></a>
### Stock
Describes the specific stock/brand on which the Item is captured. This element should be used for all media: film, video, audio, optical, digital tape.
Selection should be made from a controlled list of terms, e.g. Agfa, Eastman Kodak, Fujifilm, Gevaert, etc. for analogue film; Akai, BASF, Sony, TDK, etc. for Video; Ampex, Scotch, Shamrock, 3M, etc. for Audio; Maxell, Memorex, Philips, Verbatim, etc. for Optical; Fuji, HP, Oracle, Sony, etc. for Digital Tape; Hitachi, Seagate, Toshiba, Western Digital, etc. for Hard drives.

<a id="sec-stock_batch"></a>
### Stock Batch
The stock batch number of the media the Item is captured on.
This can be a video, audio, optical media, or digital tape stock.
Identifying the batch number can assist in identifying problems related to specific manufactured batches.

<a id="sec-video_codec"></a>
### Video Codec
Record the video encoding used in the digital Item. Where encodings differ between streams or components, identify which encoding applies to each.

A digital container may hold video, audio, and subtitle streams within one file. A package may instead contain separate files for image, sound, subtitles, and metadata. These are different levels of technical description, not interchangeable uses of the word file.

For example, a DCP is a package containing MXF picture and sound track files and supporting metadata, rather than a DCP contained in an MXF file. Picture encoding, such as JPEG 2000, and audio encoding, such as PCM, are described separately from the package and container formats. Internal stream descriptions do not, by themselves, create Item-parts.

Examples for value lists:

PBCore essenceTrackEncoding vocabulary:
[http://metadataregistry.org/concept/list/vocabulary_id/156.html](http://metadataregistry.org/concept/list/vocabulary_id/156.html)

EBUCore Video Compression Code: [https://web.archive.org/web/20100415174921/http://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm](https://web.archive.org/web/20100415174921/http://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm)

<a id="sec-audio_codec"></a>
### Audio Codec
The audio encoding used for the sound, whether carried as an audio stream within an audiovisual file or in a separate audio file. Record the encoding for the relevant stream or component where different encodings occur within one Item. Audio encoding may be compressed or uncompressed.

Examples for value lists:

PBCore essenceTrackEncoding vocabulary:
[http://metadataregistry.org/concept/list/vocabulary_id/156.html](http://metadataregistry.org/concept/list/vocabulary_id/156.html)

EBU Audio Compression Code vocabulary: [https://www.ebu.ch/metadata/cs/ebu_AudioCompressionCodeCS.xml](https://www.ebu.ch/metadata/cs/ebu_AudioCompressionCodeCS.xml)

This vocabulary also includes sound systems and noise-reduction terms. Select values appropriate to audio encoding; describe sound systems and noise reduction under their respective attributes.

<a id="sec-resolution"></a>
### Resolution
Record the digital image’s frame dimensions in pixels, where known. Broad designations such as Standard Definition or High Definition may also be recorded.

<a id="sec-bit_depth"></a>
### Bit Depth
Selection should be made from a controlled list of terms, e.g. 10, 16, 24, 32, etc.

Note that bit depth can be used in describing both video and audio files.

State whether the value describes image or audio samples and which stream or component it applies to. For images, distinguish bits per channel from a total bits-per-pixel value.

<a id="sec-transfer_speed"></a>
### Transfer Speed
If the Transfer Speed is the same as the Frame Rate [Frame Rate](../../items/elements_of_a_moving_image_item/index.md#sec-frame_rate), these values should be the same.
However, silent films might be transferred at a higher speed than the original frame rate.
For example, a silent film that was shot at a 16fps frame rate could be transferred at 23.98 fps.
It is important to note the transfer speed so an institution can identify how the transferred Item compares to the source Item.
If the transfer speed is faster than the source frame rate, the target Item could have a shorter duration than the source Item.

<a id="sec-access_conditions"></a>
## Access Conditions
Record any information on how and to whom the moving image Item can be made available, including details of the condition of the Item and of its treatment, preservation or restoration Events.
This creates a condition and preservation history for the Item, and is also important for assessing conservation conditions and establishing and prioritising collections care and preservation activities.

Observations about Item conditions will typically happen in the course of an Event such as inspection of an Item. These observations and updating on records should aim to be as clear and concise as possible, avoiding abbreviations and intitials, and as far as possible using controlled vocabulary. Besides consistency, this enables better searching and accessibility of data.

These actions can be recorded as an [Event](../../events/further_event_types/index.md), and the person or entity performing the action linked/added as an [Agent](../../agents/agents_for_items/index.md).

<a id="sec-item_copy_condition_base_emulsion_film_and_video"></a>
#### Item Copy Condition Base/Emulsion - Film and Video

Record information about the condition of the Item including the nature and extent of any damage to its base and/or emulsion and/or perforations, where applicable.
Selection should be made from a controlled list of terms, e.g. Brittle, Buckled, Light Scratches, Heavy Scratches, Tears, Warped, Hydrolysis.

<a id="sec-item_copy_condition_perforations_film"></a>
#### Item Copy Condition Perforations – Film
Selection should be made from a controlled list of terms, e.g. Foil Patches, Torn, Pulled, Missing.

<a id="sec-item_surface_deposit_film_and_video"></a>
#### Item Surface Deposit – Film and Video
Selection should be made from a controlled list of terms, e.g. Mould, Rust, Oil deposits, Dirt, Drying marks.

<a id="sec-image_film_and_video"></a>
#### Image – Film and Video
For film, this relates to the inherent qualities of the Emulsion rather than the physical
condition of the Emulsion.

For video, refer to AV Artifact Atlas for guidance on terms.

[https://web.archive.org/web/20160308013530/http://avaa.bavc.org/artifactatlas/index.php/A/V_Artifact_Atlas](https://web.archive.org/web/20160308013530/http://avaa.bavc.org/artifactatlas/index.php/A/V_Artifact_Atlas)

* Discolouration
* Magenta Bias
* Faded
* Print through in mould
* Drop-outs

<a id="sec-item_decomposition_film_and_video"></a>
#### Item Decomposition – Film and Video

* Powder
* Sticky
* Sticky at head

Capture the date on which the condition of the Item was recorded (using ISO standard[^8]).
The identification of the individual who carried out the technical assessment and has recorded the condition should also be given. Any names should be given in full, rather than initials or abbreviations.
As stated above, people or companies performing inspections are Agents.

Note any indication that the Item is in need of servicing prior to being accessed for use.

<a id="sec-notes_for_items"></a>
## Notes for Items
Notes for Items are an annotation providing additional information relating specifically to Item attributes and relationships.[^9] See [Cataloguer’s Notes](../../appendices/cataloguers-notes/index.md). 

Individual institutions may also choose to capture further data as required, e.g. line standard, or source device/software (used in creating in-house copies of acquired moving images), etc.

[^1]: Based on EN 15907, Holding institution
[^2]: Developed from EN 15907, Instantiation type, with practical guidance for production, duplication, preservation, and access across film, audio, video, and digital objects.
[^3]: EN 15907, “Inventory number,” p. 12
[^4]: See The FIAF Cataloguing Rules for Film Archives (1991). 5. Physical Description. Introduction
[^5]: The first edition of [The FIAF Moving Image Cataloguing Manual (2016)](https://www.fiafnet.org/images/tinyUpload/E-Resources/Commission-And-PIP-Resources/CDC-resources/20160920_Fiaf_Manual-WEB.pdf), §§3.1.5.1.1–3.1.5.1.2, uses General Carrier Type and Specific Carrier Type. These are not separately named elements in EN 15907; see the correspondence explained under Format in the Manifestation chapter.
[^7]: RDA 7.17.3 Colour of Moving Image
[^8]: ISO 8601
[^9]: Based on RDA 2.20.1.Basic Instructions on Making Notes on Manifestations or Items
