


!!! abstract "Definition"
    The physical product of a Manifestation of a Work or Variant, i.e. the physical copy of a Work or Variant.
    An Item may consist of one or more components, i.e. the whole Item may consist of 1 reel or 5 reels, 2 VHS tapes or 1 DVD.
    An Item record may contain fields or scope for separate barcodes and condition information for each component of the item (each reel for example) if required.The Item may be whole or incomplete or a fragment.
    In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.

<a id="sec-moving_image_items"></a>
# Moving Image Items

Whereas the Manifestation record describes the “ideal” of a particular format or publication, the Item record represents the actual holding in a repository’s collection.

An Item may consist of one or more components or parts (Item-parts). An Item record may contain fields or scope for separate barcodes and condition information for each Item-part of the Item (each reel/tape/file for example) and separate barcodes or other identifier for each container of those Item parts if required.

The Item may be whole or incomplete or a fragment.
In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.[^1]

Institutions may also opt to catalogue the carrier with several Items on it, e.g. an LTO tape or a Harddrive with multiple digital files (either belonging to one work or several works), because there is no other option to list digital Items under a Manifestation in their databases. However, this practice cannot be recommended in the long run for the lack of clarity and impaired search options this may result in. Ideally digital files are treated like distinct Items with Item-parts where applicable.

Here are some examples for Item-parts:
- A feature fiction film stored as a 35mm print consisting of 6 reels/6 cans. This would be 1 Item and 6 Item-parts with their own associated can identification number, barcode, or shelf number.
- A short documentary survives on one 16mm reel in one can. This would be 1 Item and 1 Item-part with an associated can identification number, barcode, or shelf number.
- A TV-documentary can be found in the archive on 2 Umatic tapes. This would be 1 Item and 2 Item-parts.
- The optical sound-track of a fiction film survives as a 35mm negative in 6 parts/6 cans. This would be 1 Item and 6 Item-parts with their own associated can identification number, barcode, or shelf number.
- The viewing file for your digital restoration has been made for streaming. This would be 1 Item and 1 Item-part.
- Your 6 rolls of a 35mm negative of a fiction film have been scanned. This would be 1 Item and 6 Item-parts, following the analogue tradition. In the same way, your sound negative would amount to 1 Item and 6 Item-parts.

<a id="sec-digital_items_examples"></a>
## Examples for Digital Items ##

How to deal with digital Items depends very much on the specific set-up. Some archives have the option to run LTO tape libraries and link their files via UUIDs (Universally Unique Identifiers) to the records database. Others store digital Items on LTO (Linear Tape-Open) tapes or Hard drives. Some institutions have a fully developed digitisation and restoration workflow in-house with many Items (and accordingly Manifestations) produced, others only store a viewing file as proRes. Many archives take on born-digital Items and have to guarantee authenticity of the data using the necessary infrastructure. For digital bitstreams, "inspection" is performed via automated fixity checks and checksum monitoring (like MD5 or SHA-256) to ensure the data has not degraded or changed.

Most film archives have modelled treating digital Items along the lines of how they catalogued their analogue Items, thus creating Items for digital files. 

Digital Items come with many more language options though, which can be chosen by the user and thus exist somewhat simultaneously. This makes cataloguing challenging because choices need to be made on the Manifestation level as well as the Item. See here for more information on [Multiple Language Options](/manifestations/elements_of_a_manifestation/#sec-multiple_language_options_for_Digital_Manifestations_Items).

Cataloguing digital Items has become a lot more important and less streamlined. Below are some examples of how institutions catalogue digital Items. 

### Example 1: Digitisation or Restoration of analogue material in-house ###

An analogue feature film with 5 reels/cans of a duplicate negative image and negative optical sound has each been scanned for a restoration project. The aim was to create a DCP for cinema screenings and a viewing file for streaming.

Question: How to catalogue these Items?

Answer: One way to do it, would be to link all the digital Items with the Manifestation associated with the source Item, and create the digital Items as:  

- Item 1: Raw Scan of the soundtrack (5 Item-parts)  
- Item 2: Raw Scan of the image (5 Item-parts)  
- Item 3: Master File (combined sound+image, made from both Raw Scans) (1 Item-part)  
- Item 4: Viewing File (combined sound+image made from Master) (1 Item-part)  
- Item 5: DSM (1 Item-part, made from both Raw Scans)  
- Item 6: DCDM (1 Item-part, made from the DSM)  
- Item 7: DCP (1 Item-part, made from the DCDM)


<br><center><object data="/diagrams/digit_item4dgrmsize.drawio.svg" type="image/svg+xml" width="100%"></object></center>

Another, and more advisable way since this relates to a restoration project, would be to link all the new digital Items with a new Restoration type Manifestation, e.g.

<br><center><object data="/diagrams/digit_item5a.drawio.svg" type="image/svg+xml" width="100%"></object></center>

Or even to create other additional new Manifestations with relevant types and linking the various digital files under these as relevant, so that five of the digital files are linked to a Restoration Manifestation, the DCP file is linked to a Theatrical release Manifestation, and the Viewing file to an Internet Manifestation, e.g.

<br><center><object data="/diagrams/digit_item7.drawio.svg" type="image/svg+xml" width="100%"></object></center> 

There are multiple ways to structure and choose relevant types of Manifestations dealing with digitised and born-digital Items, depending on the cataloguing systems and requirements of your institution and the reasons for digitisation, i.e. whether for preservation, restoration, streaming, etc. This section is primarily aimed at showing how to create digital Items. For further information see [LINK TO MANIFESTATION CHAPTER]

Each of these files has a UUID which creates the link to both the LTO-storage and, if applicable, to the server for quick access and online streaming. In every case, the LTO-tape or the Harddrive is not listed as Item, because these are considered Carriers/Containers which can contain other Items (and Item-parts) as well.
An institution may opt to create new Manifestations for digital Items, such as the streaming file or the DCP. This decision needs to be based on the institutions needs, strategy and resources.

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

There are different options. Structuring choices will very much depend on whether your institution has a database system that allows for one record to have two parent records or not, or the ability to develop new fields/elements within records. In the chapter about Manifestations, the section on [Multiple Language Options](/manifestations/elements_of_a_manifestation/#sec-multiple_language_options_for_Digital_Manifestations_Items) explores this further and gives more information, resulting from previous discussions within the international cataloguing community, and balancing aspects such as whether Variants are used or not, and different systems and levels of hierarchies used by different archives. 

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

<br><center><object data="/diagrams/item_mult-lang.drawio.svg" type="image/svg+xml" width="100%"></object></center>

Relating Items in this way is covered in [ADD LINK TO RELEVANT SECTION IN OTHER RELATIONSHIPS CHAPTER]


[^1]: Digital medium definition taken from CEN’s “Film Identification – enhancing interoperability of metadata. Element sets and structures. FprEN 15907:2010 (E)
