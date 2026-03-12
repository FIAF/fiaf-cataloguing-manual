---
title: Dedication
---
![](/diagrams/front.png)

This manual is dedicated to Christian Dimitriu (1945-2016), whose contributions to the field of moving image archiving and FIAF, are immeasurable; and to Ronny Loewy (1946-2012), whose knowledge of moving image metadata standards was a primary and crucial source of information during the development of this publication; and to Laurent Bismuth (1965-2021), a passionate advocate of CEN 15907 standard whose extensive cataloguing knowledge and expertise and contributions in discussions during the compilation of this publication were invaluable.

<a id="sec-acknowledgements"></a>
## Acknowledgements
This manual is a result of the combined efforts of many professionals to whom we owe our gratitude.

Contributors to early, formative discussions that informed the basis for our approach include Anna Bohn, Marco Rendina, Rosario López de Prado, Anne-Marie Grapton, Andrea Leigh, and Kelley McGrath.

Many professionals from the FIAF Cataloguing Rules Revision Working Group graciously volunteered their knowledge and experience to the review of this manual.
A special thanks to Laurent Bismuth, Georg Eckes, and Detlev Balzer for their thoughtful suggestions for improvement.
We also appreciate Detlev for hosting the FIAF Cataloguing and Documentation Commission (CDC) wiki on his filmstandards.org website.

Several of the illuminating charts and examples, and other formatting needs (such as URLs) were kindly handled by Marian Hausner, Mats Skärstrand, and Miriam Campos-Quinn.
Marian Hausner also did a painstaking job constructing the bibliography.

This work could not have been done without the support and guidance of the British Film Institute who contributed institutional policies and documents for our use.
In particular, we want to mention Gabriele Popp, who encouraged and supported BFI staff involvement, and Stephen McConnachie, who generously contributed content and freely gave of his time and knowledge.

We thank current and former members of the CDC, the members of the FIAF Executive Committee, and the FIAF Senior Administrator for their support, especially Christophe Dupin, Rachael Stoeltje, and Olga Futemma.

A very special thank you is owed to Nancy Goldman, who managed numerous steps of the project, such as convening and chairing meetings and guiding the project’s development.
She also contributed to the authoring of the manual and invested many hours in providing valuable insight and constructive criticism.

Lastly, we are indebted to Linda Tadic, who did a superb job of editing the manual and offered us the wisdom of her expertise, especially in the realm of digital media; and also to designer Lara Denil for all her hard work in improving and transforming the final layout of the manual for publication.

Natasha Fairbairn (Co-author)     
Maria Assunta Pimpinelli (Co-author ; co-Chair, FIAF Rules Revision)     
Thelma Ross (Co-author ; co-Chair, FIAF Rules Revision)

<a id="sec-introduction"></a>
## Introduction
The archival moving image field has changed dramatically in recent years, with technological advances revolutionising cataloguing, preservation, and access practices.
To help cataloguers and archivists respond to these changes, FIAF presents the *FIAF Moving Image Cataloguing Manual (FIAF Manual)*, a revision of the 1991 *FIAF Cataloguing Rules for Film Archives (FIAF Rules)*.
These new guidelines, created by the FIAF Cataloguing and Documentation Commission and the FIAF Cataloguing Rules Revision Working Group, will help cataloguers create cataloguing or metadata records that will meet requirements of new database technologies and new metadata standards while remaining compatible with older methods and standards.

The Manual offers primarily descriptive cataloguing rules rather than a schema of data elements.
However, it is difficult to discuss rules without mentioning data elements where the rules would be applied (e.g., Title, Date, etc.).
Thus, the Manual by default provides both a metadata structure (fields or elements) and rules in how to input the values the fields contain.
It reflects current and recommended cataloguing practices at international film archives represented on the Commission with the goal of interoperability with related cataloguing and metadata standards.

The cataloguing of moving images encompasses the complex, professional tasks of gathering and arranging data within systems upon which an institution depends.
Indeed, accurate, well-organised descriptions of both filmographic and technical information about an institution’s collection serve as the basis for informed internal use such as preservation, collections development, and outreach or exhibition.
They further constitute the key to accessing collections by external users such as scholars, researchers and the general public – both now and for future generations.[^fn1]

Cataloguing archival moving images combines general archival processing methodologies and traditional library cataloguing.
The process of archiving moving images applies practices held in common with archiving other materials such as papers and manuscripts.
The materials’ origin or provenance is a key element to understanding their significance.
Their historical context shows their relationship(s) to other works and, in cases of works with multiple manifestations, the development of individual works.
Knowledge of this historical context and development of materials can be useful in their preservation.[^fn2] An attempt has been made throughout the guidelines to address capturing provenance and preservation information.

This manual is intended to address some of the limitations moving image archives face when using guidelines and systems developed primarily for general libraries.

General library catalogues are built to support the discovery of a specific publication and its various editions.
This discovery is facilitated by a focus on the creation of access points to author, title and/or subject.
Many libraries catalogue through bibliographic utilities to pool effort by sharing records of these single publications.
While this shared bibliographic model works well for libraries, since many will have exact copies of the same publication, it does not  provide all the functions that moving image archives need.
Because moving image archives’ collections often include unique or rare holdings, such as pre-print elements, master prints, and unreleased material in addition to viewing copies, they need catalogues that go beyond the functions of a library catalogue to meet many of the collection management needs of archives.
The FIAF Manual is intended to provide guidance in creating metadata or cataloguing records that fulfill these collection management functions.

This revision of the 1991 guidelines recognises that institutions use a variety of systems and data structures and may find it difficult to implement far-ranging changes in their cataloguing practices.
The revisions suggested in this manual will help archives harmonise their practices with related standards, models, and schema, including:

1. The conceptual model Functional Requirements for Bibliographic Records (FRBR), published in 1998 by the International Federation of Libraries Association. FRBR is one of the models underlying RDA: Resource Description and Access[^fn3], and it provides “a framework that identifies and clearly defines the entities of interest to users of bibliographic records, the attributes of each entity, and the types of relationships that operate between entities.”[^fn4]
    
2. RDA: Resource Description and Access (RDA), co-published in 2010 by the American Library Association, the Canadian Library Association, and Chartered Institute of Library and Information Professionals. RDA was developed as a new standard for resource description and access designed for the digital world, and applies FRBR concepts and terminologies. It is intended to eventually supplant Anglo-American Cataloguing Rules (AACR2), which has been the descriptive cataloguing standard in English-speaking communities since the 1960s. Like AACR2, RDA covers all types of content and media.[^fn5]

3. The European Standards Committee (CEN) Cinematographic Works Standard (CWS) (EN 15744 and EN 15907). This two-part standard defines the metadata essential for facilitating data exchange between databases and consistent identification of moving images. The metadata schema (EN 15907), which is based in part upon the FRBR conceptual model, was approved in 2010 and disseminated through four workshops held from October 2010 – June 2011. Brief definitions of key elements in the FRBR-based CEN model are at the end of the Introduction.

For further information about the relationship of this set of guidelines to FRBR, RDA and EN 15907, see [Appendix F.3](#manual-F.3).
Although these guidelines are structured to correspond closely with the above standards/models/schema, and use associated terminology, note that neither they nor these guidelines are system-specific.
They cover the fundamentals for cataloguers for the construction and management of data and records in whatever system or standards used by an institution.

While these guidelines are intended to be applicable to all forms of moving image materials, archives with extensive broadcasting collections may wish to look to broadcasting-specific metadata schemas such as EBUCore[^fn6] and PBCore[^fn7] for additional guidance.

**FRBR-based CEN Terms in Brief**

These guidelines use the terminology of CEN Cinematographic Works Standards for terms reflecting the core structuring of moving image records - namely Work, Variant, Manifestation and Item.
It is worthwhile providing brief definitions for preliminary guidance here (whilst FRBR is discussed in more depth in [Appendix F.3 Relationship of FIAF Cataloguing Rules to Functional Requirements of Bibliographic Records](#manual-F.3))

*Work*

An entity comprising the intellectual or artistic content and the process of realisation in a cinematographic medium, e.g., what the moving image is called, when it was made, who made it, who was in it, what it is about, etc. This core information usually does not change throughout any Variant or Manifestation.

*Variant*

An entity that may be used to indicate any change to content-related characteristics that do not significantly change the overall content of a Work as a whole.
This is similar to a Work since it does not yet describe physical or digital embodiments of the content.
For example: A film edited for television broadcast will contain most of the content of the original Work, but have some parts edited out.

*Manifestation*

The embodiment of a moving image Work/Variant.
Manifestations include all analogue, digital and online media.
Manifestation information can include a description of what the particular Manifestation should ideally contain, regardless of the Items held in the archive.
For example: The original release running time of a film is 1:30:00, but the Item held at the archive is missing footage so is shorter.

*Item*

The physical product of a Manifestation of a Work or Variant, i.e. the physical copy of a Work or Variant.
An Item may consist of one or more components, i.e. the whole Item may consist of 1 reel or 5 reels, 2 VHS tapes or 1 DVD.
An Item record may contain fields or scope for separate barcodes and condition information for each component of the item (each reel for example) if required.The Item may be whole or incomplete or a fragment.
In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.[^fn8]

<a id="sec-preliminary_notes"></a>
## Preliminary Notes
<a id="sec-purpose_scope_and_use"></a>
## Purpose, scope, and use
<a id="sec-purpose"></a>
### Purpose
The primary purposes of the FIAF Manual are to suggest recommendations for the description and identification of moving images (with an emphasis on archival moving images), and to define the elements of description to facilitate the exchange of information.

<a id="sec-scope"></a>
### Scope
The manual is designed for use by institutions with moving image collections and cataloguers of moving images as a guide in the preparation of cataloguing records or descriptive metadata.
The recommendations apply to generalised film and television collections, and may require elaboration in more specialised institutions whose holdings are exclusively of a single format or type, e.g., commercials, newsfilm, television, unedited footage, etc. For example, those with television collections should additionally consider more specific standards such as EBUcore or PBcore,

Moving images include a range of materials upon which sequences of visual images have been recorded or registered and which create the illusion of movement when projected, broadcast, or played back (by means of a projector, television set, computer, software or equivalent devices).
Such images may or may not be accompanied by sound.
The definition includes moving images of all types, e.g., features, shorts, news footage, trailers, outtakes, screen tests, educational and training documentaries, experimental or independent productions, study films or video, home movies, unedited materials, television broadcasts, commercials, spot announcements, recorded performances of concerts, ballets, plays, and CCTV footage etc. It encompasses both live action and animation and includes all analogue and digital formats.

While many moving image archives also have audio materials in their collections, this manual does not offer detailed guidance for describing audio media.
However, the Manual does provide ways to describe physical and technical characteristics of analogue and digital audio Items to assist with collection and preservation management.

<a id="sec-use"></a>
### Use
Instead of defining levels of cataloguing, this manual outlines core elements for moving image description.
The core elements provide the basis for identification of a resource and for facilitating the exchange of data from one system to another.
These are not “core” elements in the sense of a Dublin Core, EBUCore, or PBCore schema, but are rather intended to illustrate common elements that are used in describing moving images and are referenced in the rules outlined in this manual.
The elements are largely drawn from EN 15744 and 15907.
For a comparison of elements described in this Manual and EN 15907, please see [Elements of Description comparison](/docs/16_appendix_08/).

This manual also provides a list of all the data elements associated with the entities described.
Thus, this approach provides a framework for the minimum and maximum amount of descriptive information allowed in a range of moving image cataloguing activities existing in a large variety of environments.

Institutions are encouraged to include as many of the non-core elements as goals and circumstances permit.
None are considered mandatory by these guidelines, but an institution may require that some are mandatory for internal purposes.

[^fn1]: FIAF, 1991, p. ix.
[^fn2]: Adapted from AMIM2, p.1.
[^fn3]: The other two conceptual models are FRAD (Functional Requirements for Authority Data), [http://www.ifla.org/node/7923](http://www.ifla.org/node/7923) and FRSAD Functional Requirements for Subject Authority Data, [http://www.ifla.org/node/1297](http://www.ifla.org/node/1297).
[^fn4]: FRBR Final Reports, p. 3.
[^fn5]: RDA 0.0 and 0.1, p. 0-1.
[^fn6]: [https://tech.ebu.ch/MetadataEbuCore](https://tech.ebu.ch/MetadataEbuCore)
[^fn7]: [http://pbcore.org/](http://pbcore.org/)
[^fn8]: Taken from EN15907. Item – Definition from the standard. [http://filmstandards.org/fsc/index.php/EN_15907_Item](http://filmstandards.org/fsc/index.php/EN_15907_Item)

