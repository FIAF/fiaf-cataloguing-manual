


!!! abstract "Definition"
    An Item is a particular physical or digital object associated with a Manifestation of a Work or Variant. It may comprise one or more components and may be whole, incomplete, or a fragment.
    A digital Item may comprise a single file or a related group of files managed and described as a unit. Backup copies maintained for that object represent the same digital object, rather than additional Items.

<a id="sec-moving_image_items"></a>
## Moving Image Items

The Item description identifies a particular object and its actual characteristics. A Manifestation description provides the context in which that object is associated with the Work or Variant. Where the Manifestation describes a particular release, its expected content, format, and extent may provide a reference for describing the Item, including its completeness.

Items associated with the same Manifestation are not necessarily identical copies or materials of the same kind. A [Pre-Release Manifestation](../manifestations/attributes_of_a_manifestation/index.md#sec-pre_release) may bring together camera negatives, sound negatives, trims, and other production materials, each described as a distinct Item. Depending on institutional cataloguing practice, a Manifestation may also associate source materials with derivatives made from them, including derivatives in different technical formats (see [Boundaries between Manifestations](../boundaries/boundaries_between_manifestations/index.md#sec-changes_in_the_format)). Each Item's description should identify what it comprises, its intended function, and its technical characteristics. Association with a Manifestation should follow the guidance on Manifestation types and boundaries, rather than being based solely on a relationship to the same Work.

An Item may consist of one or more components or parts (Item-parts).[^1] These may include individual film reels, tapes, or digital components such as reel-length image sequences. A digital Item-part may itself comprise several files. An Item record may contain identifiers, extent, technical characteristics, and condition information for its components, with separate identifiers for their physical containers where required.

The Item may be whole or incomplete or a fragment.
A digital Item represents a particular digital object. In this manual, a digital object is the file or related group of files that an institution manages and describes as a unit, such as a single audiovisual file, an image sequence with its sound files, or a DCP. A component is a part of that object described within it, such as the image sequence for one reel; it may itself comprise several files. A storage copy is one of the copies of the object's files, wherever it is held, whether on storage the institution manages itself or in remote or cloud storage. The storage holding these copies need not be described in the catalogue.

A digital object's [Element Type](elements_of_a_moving_image_item/index.md#sec-item_item_element_type) records its intended function within a production, duplication, preservation, or access workflow, independently of its file or package formats and physical storage media. Backup copies maintained for the same digital object are storage copies of that object, rather than additional Items. Their number and storage locations do not, by themselves, change the identity of the Item.[^2]

Processing may produce a distinct digital object, such as a differently encoded access copy or a restored master. Where the resulting object is retained and managed separately, describe it as a separate Item and identify its source. The source need not remain in the collection.

Not every modification to an existing digital object requires another Item. Changes made in maintaining that object may be documented in its description or associated history. Consider the nature of the changes, particularly changes to content or encoding, and whether the result is treated as a distinct object.

Whether a resulting Item requires a different Manifestation is a separate decision; see [Boundaries between Manifestations](../boundaries/boundaries_between_manifestations/index.md#sec-changes_in_the_format).

Description of a digital object should be distinguished from description of the physical storage media on which copies are held. A physical storage medium may hold several digital objects or only part of one. Some institutions also record these physical storage media in their catalogues. The management of storage inventory, replication, and storage systems is outside the scope of this guidance. Use of a digital preservation system or digital asset management system does not itself determine what constitutes a digital object.

Cataloguing systems and practices vary, including paper-based catalogues and systems in which holdings can only be described through their shared carrier or container. Such arrangements should still allow the individual contents to be identified and located. Grouping otherwise distinct Items solely because they share a physical storage container or medium can obscure their relationships to Works and Manifestations and reduce search accuracy. Where the system does not support separate Item descriptions, identify the contents through entries, notes, indexes, or references appropriate to that system.

In systems using an Item-part level, an Item consisting of a single component may still have one Item-part below it. The Item and Item-part descriptions may hold different attributes. Other systems describe these attributes within the Item record without a separate Item-part level.

The following examples illustrate descriptions of Items and their components in systems using an Item-part level:

- A feature fiction film stored as a 35mm print consisting of 6 reels/6 cans. This would be 1 Item and 6 Item-parts with their own associated can identification number, barcode, or shelf number.  
- A short documentary survives on one 16mm reel in one can. This would be 1 Item and 1 Item-part with an associated can identification number, barcode, or shelf number.
- A TV-documentary can be found in the archive on 2 Umatic tapes. This would be 1 Item and 2 Item-parts.  
- The optical sound-track of a fiction film survives as a 35mm negative in 6 parts/6 cans. This would be 1 Item and 6 Item-parts with their own associated can identification number, barcode, or shelf number.  
- A digital access copy made for streaming comprises a single file. This would be 1 Item and 1 Item-part.
- Six reels of a 35mm image negative and six corresponding sound reels have been digitised. The image output may be described as 1 Item with 6 Item-parts, each comprising the image sequence for one source reel. The sound output may be described as a separate, associated Item with 6 Item-parts. This mirrors the source elements without assuming that each digitised reel produces only one file.
- Alternatively, the image and sound outputs may be managed and described together as 1 digital Item with 6 Item-parts, each representing the corresponding image and sound for one digitised reel. Each Item-part may comprise a single audiovisual file or related image and sound files. The description should make clear what each component comprises.

Depending on the system used, Item-part data may be detailed within the Item record itself or in separate records linked to the Item. In some systems, Item-part records form an additional parent-child level below Items. While this is not part of EN 15907 standard structuring, it has evolved in some institutions for practical internal access and navigation reasons. Item-parts can equally be linked through associative relationships in other systems. Where Item-part descriptions are used, they may contain information specific to each component and, where supported, inherit or display shared information from the Item record; information describing the Item as a whole should remain distinguishable.

File counts and component counts are not necessarily the same, and a common folder, physical storage medium, or Element Type does not by itself establish that several files constitute one Item.

<a id="sec-digital_items_examples"></a>
## Examples for Digital Items ##

Digital Items may be acquired as born-digital materials or produced through digitisation, restoration, duplication, or preparation for access. A digital object may be a single audiovisual file, an image sequence with associated sound, or a multi-file package such as a DCP. The catalogue should identify the object, explain what it comprises, and distinguish its intended function from its technical formats and current status.

Identifiers and links may connect the catalogue description to technical metadata and to the corresponding object in other systems. Description may be maintained within the catalogue, in linked systems, or through a combination of both. The following examples do not prescribe a storage architecture or require file-by-file cataloguing.

Digital Items come with many more language options though, which can be chosen by the user and thus exist somewhat simultaneously. This makes cataloguing challenging because choices need to be made on the Manifestation level as well as the Item. See here for more information on [Multiple Language Options](../manifestations/elements_of_a_manifestation/index.md#sec-multiple_language_options_for_digital_manifestions_items).

Fixity information can support the assessment of the integrity of an object's files. Automated fixity checks can compare newly calculated file checksums with previously recorded values to detect changes in file data. Such information, together with technical inspection and provenance, may be recorded in or linked to the catalogue. Fixity checks alone do not establish authenticity, completeness, or successful playback.

### Example 1: Digitisation or Restoration of analogue material in-house ###

An analogue feature film with 5 reels/cans of duplicate negative image and 5 corresponding reels/cans of negative optical sound has been digitised for a restoration project. The aim was to create a DCP for cinema screenings and a digital access copy for streaming.

For a more detailed discussion of the term "restoration" see also the [Appendix](../restorations/index.md).

Question: How to catalogue these Items?

- Item 1: Raw digitisation output of the soundtrack, described in 5 Item-parts corresponding to the source reels where the system uses an Item-part level.
- Item 2: Raw scan of the image, described in 5 Item-parts, each comprising a reel-length image sequence, where the system uses an Item-part level.
- Item 3: Digital master (combined sound and image, made from both raw outputs).
- Item 4: Digital access copy for streaming (combined sound and image, made from the master).
- Item 5: DSM (Digital Source Master, made from both raw outputs).
- Item 6: DCDM (Digital Cinema Distribution Master, made from the DSM).
- Item 7: DCP (Digital Cinema Package, made from the DCDM).

These descriptions distinguish objects in this particular workflow; they are not all Element Types. Record each object's [Element Type](elements_of_a_moving_image_item/index.md#sec-item_item_element_type) according to its intended function, and its file, image, or package formats separately. For example, the streaming copy has Element Type Digital access copy. DCP identifies a package format; the DCP's Element Type depends on what it was made for, for example Digital access copy if it was made for the archive's own screenings, or Digital release if the restoration was made for distribution to cinemas. A raw scan is not automatically a preservation master solely because of its resolution or other technical characteristics.

The DCDM and DCP are multi-file digital objects, not single files. The other Items may also comprise several files. Item-part descriptions follow the structure of the cataloguing system: a system using this level may describe even a single component in an Item-part record, while another system records the same information within the Item. This does not imply a record for every constituent file. The image and sound outputs may alternatively be described together as one Item where they are managed as a unit.

Whereby:  

-  the 5 reels of 35mm negative sound are the source for the 5 reel-length components of the raw soundtrack Item
-  the 5 reels of 35mm negative image are the source for the 5 reel-length image sequences of the raw image Item
-  both raw Items were used to create the digital master
-  the digital master is the source for the digital access copy
-  both raw Items were used to create a DSM
-  the DSM is the source for the DCDM
-  the DCDM is the source for the DCP

Answer: One way to do it would be to link all the digital Items with the Manifestation associated with the source Item, and create the digital Items as shown below. The diagrams illustrate alternative associations with Manifestations. Their existing "file" labels should be read in conjunction with the object and component descriptions above: a reel-length image sequence or a digital package need not be a single file, and the use of Item-part records depends on the cataloguing system.


<br><center><object data="/diagrams/digit_item4dgrmsize.drawio.svg" type="image/svg+xml" width="100%"></object></center>

Another, and more advisable way since this relates to a restoration project, would be to link all the new digital Items with a new Restoration type Manifestation, e.g.

<br><center><object data="/diagrams/digit_item5a.drawio.svg" type="image/svg+xml" width="100%"></object></center>

Or even to create other additional new Manifestations with relevant types and link the various digital Items under these as appropriate, so that five Items are linked to a Restoration Manifestation, the DCP Item is linked to a Theatrical release Manifestation, and the digital access copy to an Internet Manifestation, e.g.

<br><center><object data="/diagrams/digit_item7.drawio.svg" type="image/svg+xml" width="100%"></object></center>

There are multiple ways to structure and choose relevant types of Manifestations dealing with digitised and born-digital Items, depending on the cataloguing systems and requirements of your institution and the reasons for digitisation, i.e. whether for preservation, restoration, streaming, etc. This section is primarily aimed at showing how to create digital Items. For further information see [Manifestation Types](../manifestations/attributes_of_a_manifestation/index.md#sec-manifestation_type).

Each digital object should have an identifier that connects its catalogue description to the object and, where applicable, to descriptions in linked systems. Identifiers may also be recorded for components and files as needed. These identifiers should not depend solely on filenames or storage locations. The physical storage media are not the objects being catalogued in this example.
An institution may opt to create new Manifestations for digital Items, such as the streaming copy or the DCP. This decision needs to be based on the institution's needs, strategy and resources.

### Example 2: Legal Deposit: Born-Digital Streaming File with multiple soundtrack options ###

By Legal deposit, an institution receives 1 Apple Quicktime ProRes 4444 file (file extension .mov). The file is the only embodiment of a digital-born feature film, whose original language is English. The file contains multiple bitstreams, which can be played (or disabled) according to the viewer’s needs and preferences. The bitstreams are the following:
- Video
- Audio 5.1 original version (English)
- Audio 5.1 dubbed version (French)
- Subtitles (English for hearing-impaired)
- Subtitles (French)
  
Question: How to manage the language options best? Should a Variant record or Manifestation record be created for every possible playback configuration (e.g. French dubbed version, original English version with English hearing-impaired subtitles, original English version with French subtitles, French dubbed version with French subtitles, etc.)?

Answer: 
The main issue is how to handle these with the usual fields/elements often found in a Variant/Manifestation, whereby Language traditionally means the main language(s) on the soundtrack, e.g. a film with both English and French dialogue in it. In those instances, two languages can be added, along with any subtitles language to reflect what is on the acquired Item. But as with the example given above, with digital Items you often have multiple selectable language options.

There are different options. Structuring choices will very much depend on whether your institution has a database system that allows for one record to have two parent records or not, or the ability to develop new fields/elements within records. In the chapter about Manifestations, the section on [Multiple Language Options](../manifestations/elements_of_a_manifestation/index.md#sec-multiple_language_options_for_digital_manifestions_items) explores this further and gives more information, resulting from previous discussions within the international cataloguing community, and balancing aspects such as whether Variants are used or not, and different systems and levels of hierarchies used by different archives. 

The most pragmatic way would be this one: A Work and a Manifestation (Variant optional) record is created, e.g. Manifestation Type "Internet" .
An Item record is created, including all the technical metadata available. You might use tools like Media Info to analyse the file and extract technical metadata. Some systems can pull information directly from the file when the item is created and stored in the long term storage.
The language options are added as language(s) on the Manifestation and Item level, maybe using a notes' field if necessary to clarify what are the original main language(s) on the print itself and what are the selectable languages in bit streams on the same file. Since the film is originally in English, English would be catalogued at the Manifestation level and other languages at the Item level.

### Example 3: Legal Deposit: DCDM Package and Streaming File with multiple soundtrack options ###

By Legal deposit, an institution receives 1 DCDM package, 1 Apple QuickTime ProRes 422 file and 2 srt standalone files. These items represent the only embodiments of a digital-born feature film whose original version is English. The 2 srt files contain respectively French and German subtitles.

Question: Should the srt files be catalogued as separate items? If not, should they be included within the DCDM’s Item record or within the ProRes’ item record? Also, should a “French subtitled” Variant (or Manifestation) and a “German subtitled” Variant (or Manifestations) be created and how should the relationships between Items, Manifestations and Variants be managed? 

Answer:
First of all, the decision needs to be made if one or two Manifestations are created, e.g. Type "Theatrical Distribution" if there is a DCP too, or is made, and "Internet" for the streaming file. Your institutions should have rules about that. The original language is English, so that needs to be catalogued at Manifestation level.
Depending on that, you create Item records (either linked to the same Manifestation or separate ones). 

If an institution uses Variants, a Variant record could be created for the French language version and one for the German language version, plus Manifestations, and each srt file Item under the relevant one could be linked.

Option 1: A pragmatic decision would be to record the language options at the Item level, either in the respective field for languages or in a notes field. The srt file stored in the LTO tape library would have the srt file within the bag of the digital Item.
That way you have two Items: the DCDM and the ProRes, each with language information rather than the srt files as separate Items.

Option 2: Another, more granular option would be to catalogue the srt files as separate Items too; so there should be 4 Item records in total.
As the srt files are literally just the subtitles for the film and do not include the film itself, but are designed for use in conjunction with a different Item containing the film, the Items could be linked together in an associative relationship potentially (if the system allows that) which means that each srt file could be linked to the DCDM or ProRes Items (or both), as relevant, something like e.g.:

<br><center><object data="/diagrams/item_mult-lang.drawio.svg" type="image/svg+xml" width="75%"></object></center>

Relating Items in this way is covered in [ADD LINK TO RELEVANT SECTION IN OTHER RELATIONSHIPS CHAPTER]

[^1]: Institutions use terms such as Carriers, Components, Parts, and Containers with varying meanings. This manual uses Item-parts for components of an Item, distinguishing these from physical storage containers. A digital component may comprise a single file or a related group of files; it is not defined by the internal streams or tracks within a file.
[^2]: EN 15907:2010 defines a digital Item in terms of the availability of a computer file, irrespective of backup copies. This manual develops that guidance to accommodate multi-file digital objects as well as single files.
