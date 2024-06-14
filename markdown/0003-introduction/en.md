# Introduction {#manual-introduction}

\setcounter{page}{27}
\pagenumbering{arabic}

The archival moving image field has changed dramatically in recent years, with technological advances revolutionising cataloguing, preservation, and access practices. To help cataloguers and archivists respond to these changes, FIAF presents the _FIAF Moving Image Cataloguing Manual (FIAF Manual)_, a revision of the 1991 *FIAF Cataloguing Rules for Film Archives (FIAF Rules)*. These new guidelines, created by the FIAF Cataloguing and Documentation Commission and the FIAF Cataloguing Rules Revision Working Group, will help cataloguers create cataloguing or metadata records that will meet requirements of new database technologies and new metadata standards while remaining compatible
with older methods and standards.

Hello paul!

The Manual offers primarily descriptive cataloguing rules rather than a schema of data elements. However, it is difficult to discuss rules without mentioning data elements where the rules would be applied (e.g., Title, Date, etc.). Thus, the Manual by default provides both a metadata structure (fields or elements) and rules in how to input the values the fields contain. It reflects current and recommended cataloguing practices at international film archives represented on the Commission with the goal of interoperability with related cataloguing and metadata standards.

The cataloguing of moving images encompasses the complex, professional tasks of gathering and arranging data within systems upon which an institution depends. Indeed, accurate, well-organised descriptions of both filmographic and technical information about an institution’s collection serve as the basis for informed internal use such as preservation, collections development, and outreach or exhibition. They further constitute the key to accessing collections by external users such as scholars, researchers and the general public – both now and for future generations.[^1]

Cataloguing archival moving images combines general archival processing methodologies and traditional library cataloguing. The process of archiving moving images applies practices held in common with archiving other materials such as papers and manuscripts. The materials’ origin or provenance is a key element to understanding their significance. Their historical context shows their relationship(s) to other works and, in cases of works with multiple manifestations, the development of individual works. Knowledge of this historical context and development of materials can be useful in their preservation.[^2] An attempt has been made throughout the guidelines to address capturing provenance and preservation information.

This manual is intended to address some of the limitations moving image archives face when using guidelines and systems developed primarily for general libraries.

General library catalogues are built to support the discovery of a specific publication and its various editions. This discovery is facilitated by a focus on the creation of access points to author, title and/or subject. Many libraries catalogue through bibliographic utilities to pool effort by sharing records of these single publications. While this shared bibliographic model works well for libraries, since many will have exact copies of the same publication, it does not  provide all the functions that moving image archives need. Because moving image archives’ collections often include unique or rare holdings, such as pre-print elements, master prints, and unreleased material in addition to viewing copies, they need catalogues that go beyond the functions of a library catalogue to meet many of the collection management needs of archives. The FIAF Manual is intended to provide guidance in creating metadata or cataloguing records that fulfill these collection management functions.

This revision of the 1991 guidelines recognises that institutions use a variety of systems and data structures and may find it difficult to implement far-ranging changes in their cataloguing practices. The revisions suggested in this manual will help archives harmonise their practices with related standards, models, and schema, including:

1. The conceptual model Functional Requirements for Bibliographic Records (FRBR), published in 1998 by the International Federation of Libraries Association. FRBR is one of the models underlying RDA: Resource Description and Access[^3], and it provides “a framework that identifies and clearly defines the entities of interest to users of bibliographic records, the attributes of each entity, and the types of relationships that operate between entities.”[^4]
    
2. RDA: Resource Description and Access (RDA), co-published in 2010 by the American Library Association, the Canadian Library Association, and Chartered Institute of Library and Information Professionals. RDA was developed as a new standard for resource description and access designed for the digital world, and applies FRBR concepts and terminologies. It is intended to eventually supplant Anglo-American Cataloguing Rules (AACR2), which has been the descriptive cataloguing standard in English-speaking communities since the 1960s. Like AACR2, RDA covers all types of content and media.[^5]

3. The European Standards Committee (CEN) Cinematographic Works Standard (CWS) (EN 15744 and EN 15907). This two-part standard defines the metadata essential for facilitating data exchange between databases and consistent identification of moving images. The metadata schema (EN 15907), which is based in part upon the FRBR conceptual model, was approved in 2010 and disseminated through four workshops held from October 2010 – June 2011. Brief definitions of key elements in the FRBR-based CEN model are at the end of the Introduction.

For further information about the relationship of this set of guidelines to FRBR, RDA and EN 15907, see [Appendix F.3](#manual-F.3). Although these guidelines are structured to correspond closely with the above standards/models/schema, and use associated terminology, note that neither they nor these guidelines are system-specific. They cover the fundamentals for cataloguers for the construction and management of data and records in whatever system or standards used by an institution.

While these guidelines are intended to be applicable to all forms of moving image materials, archives with extensive broadcasting collections may wish to look to broadcasting-specific metadata schemas such as EBUCore[^6] and PBCore[^7] for additional guidance. 

<u>**FRBR-based CEN Terms in Brief**</u>

These guidelines use the terminology of CEN Cinematographic Works Standards for terms reflecting the core structuring of moving image records - namely Work, Variant, Manifestation and Item. It is worthwhile providing brief definitions for preliminary guidance here (whilst FRBR is discussed in more depth in [Appendix F.3 Relationship of FIAF Cataloguing Rules to Functional Requirements of Bibliographic Records](#manual-F.3))

**Work**

An entity comprising the intellectual or artistic content and the process of realisation in a cinematographic medium, e.g., what the moving image is called, when it was made, who made it, who was in it, what it is about, etc. This core information usually does not change throughout any Variant or Manifestation.

**Variant**

An entity that may be used to indicate any change to content-related characteristics that do not significantly change the overall content of a Work as a whole. This is similar to a Work since it does not yet describe physical or digital embodiments of the content. For example: A film edited for television broadcast will contain most of the content of the original Work, but have some parts edited out.

**Manifestation**

The embodiment of a moving image Work/Variant. Manifestations include all analogue, digital and online media. Manifestation information can include a description of what the particular Manifestation should ideally contain, regardless of the Items held in the archive. For example: The original release time of a film is 1:30:00, but the Manifestation held at the archive is missing footage so is shorter.

**Item**

The physical product of a Manifestation of a Work or Variant, i.e. the physical copy of a Work or Variant. An Item may consist of one or more components, i.e. the whole Item may consist of 1 reel or 5 reels, 2 VHS tapes or 1 DVD. An Item record may contain fields or scope for separate barcodes and condition information for each component of the item (each reel for example) if required.The Item may be whole or incomplete or a fragment. In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.[^8]

\newpage

[^1]: FIAF, 1991, p. ix.
[^2]: Adapted from AMIM2, p.1.
[^3]: The other two conceptual models are FRAD (Functional Requirements for Authority Data), [http://www.ifla.org/node/7923](http://www.ifla.org/node/7923) and FRSAD Functional Requirements for Subject Authority Data, [http://www.ifla.org/node/1297](http://www.ifla.org/node/1297).
[^4]: FRBR Final Reports, p. 3.
[^5]: RDA 0.0 and 0.1, p. 0-1.
[^6]: [https://tech.ebu.ch/MetadataEbuCore](https://tech.ebu.ch/MetadataEbuCore)
[^7]: [http://pbcore.org/](http://pbcore.org/)
[^8]: Taken from EN15907. Item – Definition from the standard. [http://filmstandards.org/fsc/index.php/EN_15907_Item](http://filmstandards.org/fsc/index.php/EN_15907_Item)
