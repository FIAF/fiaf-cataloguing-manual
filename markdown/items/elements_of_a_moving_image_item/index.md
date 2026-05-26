---
title: Elements of a Moving Image Item
---
A majority of the physical and digital description elements of moving image Items are intended to be inherited from the Manifestations, as they serve as the exemplars of Manifestations.
In some databases, selection of a general media type initiates provision of element fields relevant to that type at a Manifestation level, or an Item level, or both (e.g. in a 2 Level hierarchy.
See “Shallow hierarchy model: 2 levels” in [Elements of description across Works, Variants, Manifestations, and Items](/preliminary/core_elements_of_description/#sec-elements_of_description)).

Ideally the information need only be recorded once irrespective of where in the data structure an institution must place it.
Therefore guidelines for the treatment of physical/digital description elements are explained fully in the Manifestation chapter.

This chapter contains Item-specific physical/digital description elements beginning at [Item Specifics/Extent (e.g. physical/Digital description)](/items/elements_of_a_moving_image_item/#sec-item_specifics_extent).
For example, properties such as Extent and Format at the Manifestation level represent the “ideal,” and item-specific information will capture where it differs from this ideal.
Only elements that are considered Item-specific have guidelines for the recording of data.
Physical/digital description elements that are considered Manifestation-specific, but which may be repeated at the Item level, contain hyperlinks to the relevant sections in the Manifestation chapter.

Further data relating to the condition, preservation, location, and, acquisition, accessioning, and source of the Item are also recommended elements for the Item (see [Access Conditions](/items/elements_of_a_moving_image_item/#sec-access_conditions)). [ADD LINK TO ACQUISITION CHAPTER]

These may be either added to the Item description itself or, where this is not possible, related to other separate files or databases, via physical link or text indication.

<a id="sec-item_identifier"></a>
## Identifier
Create an unambiguous numerical or alphanumerical reference to the moving image Item, such as a call number, barcode, shelf mark, UUID or similar, to uniquely identify the copy.[^3] This may be in addition to separate Acquisition and Accession number(s) or identifier(s). [LINK TO Acquisition part]

For digital files, the filename is not an identifier since filenames can change. Filenames are unreliable for uniquely identifying digital objects due to several limitations: users or systems may rename files, causing loss of reference; different versions of the same files from multiple sources can share identical names; and, changing storage locations makes filenames unreliable for tracking. Moreover different systems and organisations may use varying file-naming schemes and have limited interoperability.

Digital systems use UUID (Universally Unique Identifier), Internal Database IDs and Persistent Identifiers, which, unlike UUIDs, may not be globally unique but are essential for internal collection management and control. They play a crucial role in organising and archiving digital content, ensuring unambiguous identification within asset management systems.  This means that the filename is tracked as part of the technical metadata associated with a digital item.

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

If multiple titles are recorded, where allowable, associate a “Title Type” to a title for differentiation between the various types of titles (see [Title Types](/appendices/titles/title_types/#sec-title_types)).

In most cases the title of an Item will be the same as that of the Manifestation to which it pertains.

The title of an Item can sometimes differ, either slightly or wholly from the title of the Manifestation, and/or Work/Variant to which it is linked.
In particular, this may be the case where an incomplete physical product of the Manifestation has been acquired.
For example, if a film in the collection is missing the first reel where opening title credits usually appear, the Item will not have a title to be transcribed.

For creating titles for untitled or unidentified entities see [Supplied/Devised Titles (i.e. Creating titles for untitled/unidentified entities or production material)](/appendices/titles/title_types/#sec-supplied_devised_titles)

For the treatment of Aggregates (e.g. compilations of whole Manifestations) as applied to Items, see the appendix concerning 
[Titling of Aggregates](/appendices/aggregates/titling_of_aggregates)

For guidance on wording, order, spelling, punctuation, accentuation and capitalisation, see sections within [ADD LINK TO Preliminary Notes main chapter]

For sources of information for the Title, see [Sources of Information](/preliminary/prelim_sources_of_information/#sec-prelim_sources_of_information).

<a id="sec-item_title_type"></a>
### Title Type
Items can have more than just the title transcribed from the opening credits.
There can be title information written on leader, cans, and video containers.
Sometimes this information is different to what is in the credits; sometimes it is the only source of information to help identify an Item’s content.

Note the source of title information.
For Items where the only title information is found on a can or leader, use an Acquisition Title Type(s) (see [Alternative title types](/appendices/titles/title_types/#sec-alternative_title_types)) or descriptive words such as “Title on can” or “Title on leader.”

<a id="sec-holding_institution"></a>
## Holding Institution[^1]
Record the name of the institution possessing the moving image Item or authorised to make it available.

Optionally, if available, record a suitable repository identifier or a registered namespace identifier for the institution.

<a id="sec-item_location"></a>
#### Item Location
Item descriptions should indicate a storage location number in order to provide access and retrieval.
Movements and changes of location should also be logged in order to ascertain the precise location of an Item at any given time.
If possible, use the Item Identifier and Identifier Type fields to note an Item’s location (see [Identifier](/items/elements_of_a_moving_image_item/#sec-item_identifier)).

This could be a single simple field, or could include multiple fields to reflect various electronic package or barcode numbers that may be attached to each individual can or container, shelf, or whatever is applicable to an individual institution.

<a id="sec-item_acquisition type"></a>
#### Item Acquisition Type
For more information on information which should be documented at acquisition see [LINK TO ACQUISITION CHAPTER]. Record the acquisistion Type at Item level as a value list (e.g. loan, donation) as well as where it came from. Nowadays it becomes more and more important to have information about the provenance of Items in an institutions collection. Ideally record the person/institution by linking to the internal authority records as well as the date when the Item entered the collection.

<a id="sec-item_ownership"></a>
#### Item Ownership
It possible, record who currently has ownership of the Item, ideally also tracking the history of the ownership. For example, the Item could have been deposited 20 years ago and no has changed ownership by contract to the holding institution. Many times, preservation decisions might be influenced by ownership status. Ideally record the person/institution by linking to the internal authority records as well as the dates when changes of ownership occured. 

<a id="sec-item_item_element_type"></a>
## Item Element Type[^2]
Record the nature or function of the moving image Item, describing its place in the photochemical or digital production or duplication process. Selection should be made from a controlled list of terms, e.g.:

- Colour Positive
- Colour Negative
- Copper Toned Positive
- Cyan Matrix
- Direct BW Positive
- Original negative
- Duplicate negative
- Positive
- Original positive (reversal film)
- Duplicate positive
- Lavender
- Image negative
- Sound negative
- DCP

<a id="sec-item_specifics_extent"></a>
## Item Specifics/Extent (e.g. physical/digital description)
All moving image Item descriptions should contain details of the physical/digital characteristics of the Items, their location, treatment and condition.

Institutions with archival moving images need to describe their holdings accurately for preservation, copying and reconstruction purposes.

Often there will be physically separate Items, for example image, track, music, different colour bases, etc., which are all essential parts of a single moving image.[^4] Descriptive terminology covering all areas of physical description and attributes should be established in controlled lists of terms, to be applied in the relevant categories.
The range of these and what they are can be established in-house or utilising an established list, for example, the [FIAF Glossary of Technical Terms](https://www.fiafnet.org/pages/E-Resources/Technical-Terms.html).

Each Item should have its own description, whether the physical/digital characteristics between Items differ in one way or another, for example, in length, gauge, base, sound, etc., or, the Items acquired are duplicate identical copies.

Institutions may record as much technical information as they wish or need, but the Physical and Digital Description elements of an Item should ideally consist of the elements listed in the sub-sections below where discernible.

<a id="sec-media_type"></a>
### Media Type (aka Carrier Type)

Media type is the medium on or the encoding format in which the Item is fixed.

Its description consists of a **general media** type, which describes the basic properties of the Item’s physical format, for example, film, video tape, digital file, etc., and a **specific media type**, which corresponds to the gauge, in the case of films and tapes, and for digital files, to the physical carrier on which the file is stored or containers, when carriers for files are not separately catalogued.

<a id="sec-item_general_media_type"></a>
#### General Media Type[^5] (aka General Carrier Type)
The broad media type of the Item (e.g., film, video, audio, optical, digital file).
Recording this high-level information will enable simple searching for only film, video, digital, etc. elements rather than searching by all possible formats and media types.

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

A suggested list can be found in [Manifestation General Media Type](/manifestations/elements_of_a_manifestation/#general-media-type).

For reasons of clarity and to avoid redundancy, optionally, institutions can decide to skip the general media type description for film and video, since it is already implicit in the specific media type.

<a id="sec-item_specific_media_type"></a>
#### Specific Media Type[^6] (aka Specific Carrier Type)

The specific media type for analogue film can be the width of the film stock or of the magnetic tape on which the Item is fixed.

For digital files, it is most important for users to immediately identify the file container or wrapper (MXF, MOV, DPX, etc.) rather than the physical media on which it is stored, because the physical media storing a file can change, but that does not necessarily mean that the file format has changed. It is the digital file format that is the important distinguishing factor. Information on the specific codecs and resolution are captured in other Item properties.

For optical media, only add commercially produced media here. If the optical media is “writable” and is being used to store a digital file, put the digital file format in the general media type, and the optical storage media in specific media type.

Record the specific media type, selecting from a suitable controlled list.
A suggested list, which is open and not exhaustive, can be found in [Manifestation Specific Media Type](/manifestations/elements_of_a_manifestation/#specific-media-type).

<a id="sec-item_status"></a>
### Item Status
Description of the preservation or access status of the Item. Select term from a controlled list, e.g.  

- Master   
- Viewing   
- Accessioned   
- On Loan  
- Status pending   
- Removed

<a id="sec-sound"></a>
### Sound
Technical specifications relating to the fixation of sound in a moving image Manifestation/Item (see [Sound Characteristics of a Manifestation](/manifestations/elements_of_a_manifestation/#sec-sound_characteristics_of_a_manifestation)).
This element is for high-level description of sound on the item; i.e., noting whether it has sound, is silent, etc.

Indicate the presence or absence of sound in the Item. Selection should be made from a controlled list of terms, e.g.:

- Sound  
- Silent  
- Mute  
- Combined  
- Combined as Mute  
- Combined as Sound  
- Mixed  
- Temporary 

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

<a id="sec-item_sound_channel_configuration"></a>
### Sound Channel Configuration
If the Item has sound, note here the track configuration (e.g., mono, stereo, etc.) Selection should be made from a controlled list of terms.

<a id="sec-sound_system"></a>
### Sound System
See also [Sound Characteristics of a Manifestation](/manifestations/elements_of_a_manifestation/#sec-sound_characteristics_of_a_manifestation)

Describes the technical or proprietary system used to record the sound on a Item. Select from a controlled list, e.g.:

- Dolby SR
- Dolby Digital
- Mute
- Combined Magnetic Sound
- Combined Optical Sound
- VA RCA Duplex

<a id="sec-colour"></a>
### Colour
For full instructions, see [Colour Characteristics of a Manifestation](/manifestations/elements_of_a_manifestation/#sec-colour_characteristics_of_a_manifestation).

The presence of colour(s), tone(s), etc. in an Item.[^7]

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

<a id="sec-unit_number"></a>
### Unit Number
For full instructions see [Logical Extent of a Manifestation](/manifestations/elements_of_a_manifestation/#sec-logical_extent_of_a_manifestation)

The number of discrete logical units that make up the moving image Item. Item unit number(s) may differ from that of the associated Manifestation. The unit number in Manifestation relates to the ideal, whereas the Item unit number refers to the actual units held by the institution, e.g. an institution may have only acquired 3 reels of a 4-reel film.

<a id="sec-extent"></a>
### Extent
The actual physical/digital extent is a characteristic of a singular Item, since it can be different for multiple Items exemplifying the same moving image Manifestation.

For film, record footage for the film reel in feet or metres. 
This footage represents actual length, rather than the “ideal” length, which is recorded for Manifestations (see [Physical Extent of a Manifestation(/manifestations/elements_of_a_manifestation/#sec-physical_extent_of_a_manifestation)).
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
For full instructions, see [Projection Characteristics of a Manifestation](/manifestations/elements_of_a_manifestation/#sec-projection_characteristics_of_a_manifestation)

The projection characteristics of a Manifestation/Item include aspect ratio and aperture or image format.

Record only if this information is not captured at the Manifestation level or if required at the Item level by the system in use.

<a id="sec-broadcast_standard_video"></a>
### Broadcast Standard - Video
The broadcast standard for a video or DVD/BluRay, e.g. NTSC, PAL, SECAM, etc.

<a id="sec-duration"></a>
### Duration
Duration in minutes of the moving image(s) contained in the Item, not the total duration of the Manifestation.
Optionally, include minutes and seconds, or, for a higher level of precision and to enable calculations, use the format HH:MM:SS (hours, minutes, seconds).
This numeric format will help to calculate estimated digital storage in analogue-to-digital transfer projects.

This duration represents actual temporal extent, rather than the “ideal” temporal extent, which is recorded for Manifestations (see [Duration of a Manifestation](/manifestations/elements_of_a_manifestation/#sec-duration_of_a_manifestation)).
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
Information related to the frame rate used during a digitisation process is added to Transfer Speed (see [Transfer Speed](/items/elements_of_a_moving_image_item/#sec-transfer_speed)).

Frame Rate and Transfer Speed can sometimes be the same thing, and at other times different, depending on whether it is an Item that is being scanned into a digital file or an Item that is a digital file to start with. For example, a silent film that was shot at a 16 fps frame rate could be transferred at 23.98 fps. In this case, the resulting digital file would have a frame rate of 23.98, even though the original film is 16 fps.

Precision can be added to this element by adding a “Type” qualifier to note if the frame rate is original, or the transfer rate.

Note that in digital cinema, a film can have Variable frame rates.

<a id="sec-base"></a>
### Base
The physical material or video format on which the Item is captured, for example, describing the flexible transparent material that supports a film items’ emulsion (e.g.  acetate, nitrate, polyester) or a magnetic track, (e.g. CTA).
Select from controlled list of terms, if possible, keep separate lists for analogue film material and analogue video.

Acetate
Diacetate
Triacetate (aka CTA)
Nitrate
Polyester
Magnetic tape

<a id="sec-stock"></a>
### Stock
Describes the specific stock/brand on which the Item is captured. This element should be used for all media: film, video, audio, optical, digital tape.
Selection should be made from a controlled list of terms, e.g. Eastman Kodak, Fuji, Agfa for analogue film; 3M, Agfa, Agfa Gavaert, Akai, Ampex, Ansco, BASF, Brifco, Fuji, Sony for Video; Ampex, Scotch, 3M, Shamrock for Audio; Maxell, Memorex, Philips, Verbatim for Optical; Fuji, HP, Oracle, Sony for Digital Tape; Hitachi, Seagate, Toshiba, Western Digital for Hard drives.

<a id="sec-stock_batch"></a>
### Stock Batch
The stock batch number of the media the Item is captured on.
This can be a video, audio, optical media, or digital tape stock.
Identifying the batch number can assist in identifying problems related to specific manufactured batches.

<a id="sec-video_codec"></a>
### Video Codec
The video compression standard used in the digital video Item, for example, D10, MP4, etc.

Video and digital cinema formats contained in wrappers have separate audio files contained in the format with the video file.
For example, DCPs (contained in MXF files) are comprised of a JPEG2000 video file and a WAV audio file (along with textual information in an XML file), The audio codec is described separately.

Examples for value lists:

PBCore essenceTrackEncoding vocabulary:
[http://metadataregistry.org/concept/list/vocabulary_id/156.html](http://metadataregistry.org/concept/list/vocabulary_id/156.html)

EBUCore Video Compression Code:
[https://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm](https://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm)

<a id="sec-audio_codec"></a>
### Audio Codec
The audio compression standard used in the audio file, whether it is contained in a wrapper with a video file or as a standalone audio file.

Examples for value lists:

PBCore essenceTrackEncoding vocabulary:
[http://metadataregistry.org/concept/list/vocabulary_id/156.html](http://metadataregistry.org/concept/list/vocabulary_id/156.html)

EBUCore Video Compression Code:
[https://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm](https://www.ebu.ch/metadata/cs/web/ebu_VideoCompressionCodeCS_p.xml.htm)

<a id="sec-resolution"></a>
### Resolution
Note whether the Item’s resolution is Standard Definition, High Definition, etc.

<a id="sec-bit_depth"></a>
### Bit Depth
Selection should be made from a controlled list of terms.

Note that bit depth can be used in describing both video and audio files.

<a id="sec-transfer_speed"></a>
### Transfer Speed
If the Transfer Speed is the same as the Frame Rate [Frame Rate](/items/elements_of_a_moving_image_item/#sec-frame_rate), these values should be the same.
However, silent films might be transferred at a higher speed than the original frame rate.
For example, a silent film that was shot at a 16fps frame rate could be transferred at 23.98 fps.
It is important to note the transfer speed so an institution can identify how the transferred Item compares to the source Item.
If the transfer speed is faster than the source frame rate, the target Item could have a shorter duration than the source Item.

<a id="sec-access_conditions"></a>
## Access Conditions
Record any information on how and to whom the moving image Item can be made available, including details of the condition of the Item and of its treatment, preservation or restoration Events.
This creates a condition and preservation history for the Item, and is also important for assessing conservation conditions and establishing and prioritising collections care and preservation activities.

Observations about Item conditions will typically happen in the course of an Event such as inspection of an Item. These observations and updating on records should aim to be as clear and concise as possible, avoiding abbreviations and intitials, and as far as possible using controlled vocabulary. Besides consistency, this enables better searching and accessibility of data.

These actions can be recorded as an Event [ADD LINK], and the person or entity performing the action linked/added as an Agent [ADD RELEVANT LINK]

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

[http://avaa.bavc.org/artifactatlas/index.php/A/V_Artifact_Atlas](http://avaa.bavc.org/artifactatlas/index.php/A/V_Artifact_Atlas)

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
Notes for Items are an annotation providing additional information relating specifically to Item attributes and relationships.[^9] See [Cataloguer’s Notes](/appendices/cataloguers-notes/).

[^1]: Based on EN 15907, Holding institution
[^2]: Based on EN 15907, Instantiation type
[^3]: EN 15907, “Inventory number,” p. 12
[^4]: See The FIAF Cataloguing Rules for Film Archives (1991). 5. Physical Description. Introduction
[^5] Based on EN 15907, General Carrier Type
[^6] Based on EN 15907, Specific Carrier Type
[^7]: RDA 7.17.3 Colour of Moving Image
[^8]: ISO 8601
[^7]: Based on RDA 2.20.1.Basic Instructions on Making Notes on Manifestations or Items
