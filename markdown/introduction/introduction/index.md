
## Introduction

<a id="sec-introduction"></a>

The archival moving image field has changed dramatically in recent years, with technological advances revolutionising cataloguing, preservation, and access practices.
To help cataloguers and archivists respond to these changes, FIAF presents the *FIAF Moving Image Cataloguing Manual (FIAF Manual)*, a revision of the 1991 *FIAF Cataloguing Rules for Film Archives (FIAF Rules)*.
These new guidelines, created by the FIAF Cataloguing and Documentation Commission and the FIAF Cataloguing Rules Revision Working Group, will help cataloguers create cataloguing or metadata records that will meet requirements of new database technologies and new metadata standards while remaining compatible with older methods and standards.

The Manual offers primarily descriptive cataloguing rules rather than a schema of data elements.
However, it is difficult to discuss rules without mentioning data elements where the rules would be applied (e.g., Title, Date, etc.).
Thus, the Manual by default provides both a metadata structure (fields or elements) and rules in how to input the values the fields contain.
It reflects current and recommended cataloguing practices at international film archives represented on the Commission with the goal of interoperability with related cataloguing and metadata standards.

The cataloguing of moving images encompasses the complex, professional tasks of gathering and arranging data within systems upon which an institution depends.
Indeed, accurate, well-organised descriptions of both filmographic and technical information about an institution’s collection serve as the basis for informed internal use such as preservation, collections development, and outreach or exhibition.
They further constitute the key to accessing collections by external users such as scholars, researchers and the general public – both now and for future generations.[^1]

Cataloguing archival moving images combines general archival processing methodologies and traditional library cataloguing.
The process of archiving moving images applies practices held in common with archiving other materials such as papers and manuscripts.
The materials’ origin or provenance is a key element to understanding their significance.
Their historical context shows their relationship(s) to other works and, in cases of works with multiple manifestations, the development of individual works.
Knowledge of this historical context and development of materials can be useful in their preservation.[^2] An attempt has been made throughout the guidelines to address capturing provenance and preservation information.

This manual is intended to address some of the limitations moving image archives face when using guidelines and systems developed primarily for general libraries.

General library catalogues are built to support the discovery of a specific publication and its various editions.
This discovery is facilitated by a focus on the creation of access points to author, title and/or subject.
Many libraries catalogue through bibliographic utilities to pool effort by sharing records of these single publications.
While this shared bibliographic model works well for libraries, since many will have exact copies of the same publication, it does not  provide all the functions that moving image archives need.
Because moving image archives’ collections often include unique or rare holdings, such as pre-print elements, master prints, and unreleased material in addition to viewing copies, they need catalogues that go beyond the functions of a library catalogue to meet many of the collection management needs of archives.
The FIAF Manual is intended to provide guidance in creating metadata or cataloguing records that fulfill these collection management functions.

It is recognised that institutions use a variety of systems and data structures and may find it difficult to implement far-ranging changes in their cataloguing practices. The revisions suggested in this manual will help archives harmonise their practices with related standards, models, and schema as far as possible.

<a id="sec-relationship_of_fiaf_cataloguing_rules_to_functional_requirements"></a>
### Relationship of FIAF Cataloguing Rules to Functional Requirements of Bibliographic Records (FRBR), Resource Description and Access (RDA) and The European Standards Committee (CEN) Cinematographic Works Standard EN 15907
The authors of this manual have chosen to focus on current standards and practices, such as those outlined in FRBR, RDA, and EN 15907, while expanding them to be more specific and granular regarding the particular needs of moving image cataloguing. Listed below are some of the key attributes of these standards and their relationship to recommendations in the FIAF Cataloguing Manual.


1. The conceptual model Functional Requirements for Bibliographic Records (FRBR), published in 1998 by the International Federation of Libraries Association. FRBR is one of the models underlying RDA: Resource Description and Access[^3], and it provides “a framework that identifies and clearly defines the entities of interest to users of bibliographic records, the attributes of each entity, and the types of relationships that operate between entities.”[^4]
    
2. RDA: Resource Description and Access (RDA), co-published in 2010 by the American Library Association, the Canadian Library Association, and Chartered Institute of Library and Information Professionals. RDA was developed as a new standard for resource description and access designed for the digital world, and applies FRBR concepts and terminologies. It is intended to eventually supplant Anglo-American Cataloguing Rules (AACR2), which has been the descriptive cataloguing standard in English-speaking communities since the 1960s. Like AACR2, RDA covers all types of content and media.[^5]

3. The European Standards Committee (CEN) Cinematographic Works Standard (CWS) (EN 15744 and EN 15907). This two-part standard defines the metadata essential for facilitating data exchange between databases and consistent identification of moving images. The metadata schema (EN 15907), which is based in part upon the FRBR conceptual model, was approved in 2010 and disseminated through four workshops held from October 2010 – June 2011. Brief definitions of key elements in the FRBR-based CEN model are at the end of the Introduction.

Although these guidelines are structured to correspond closely with the above standards/models/schema, and use associated terminology, note that neither they nor these guidelines are system-specific.
They cover the fundamentals for cataloguers for the construction and management of data and records in whatever system or standards used by an institution.

While these guidelines are intended to be applicable to all forms of moving image materials, archives with extensive broadcasting collections may wish to look to broadcasting-specific metadata schemas such as EBUCore[^6] and PBCore[^7] for additional guidance.

**FRBR-based CEN Terms in Brief**

These guidelines use the terminology of CEN Cinematographic Works Standards for terms reflecting the core structuring of moving image records - namely Work, Variant, Manifestation and Item.

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
In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.[^8]

<a id="sec-entities"></a>
### Entities
Functional Requirements for Bibliographic Records (FRBR) was published in 1998 by the International Federation of Libraries Association. It is based on the entity-attribute-relationship model of analysis, and has been incorporated into the structure of both RDA and EN 15907.

FRBR identifies and defines three groups of entities:[^9]

- Group 1 (products of intellectual or artistic endeavor)

    - Work     
    - Expression     
    - Manifestation     
    - Item 

- Group 2 (responsible for content, production, or custodianship of Group 1 entities)

    - Person     
    - Corporate Body     

- Group 3 (may serve as subjects of Group 1 entities)

    - Group 1 and 2 entities
    - Concept
    - Object
    - Event
    - Place
    
This manual focuses almost exclusively on the Group 1 entities, their attributes and relationships. Although it also briefly provides guidelines for the description of the Group 2 and Group 3 entities, we recommend the use of other manuals and appropriate existing national or international standards for more detail in these areas.

<a id="sec-existing_standards_for_describing_entities"></a>
#### Existing standards for describing Entities
Existing standards for describing Entities include:

- RDA

    - Section 3: Person, Family, & Corporate Body (Chapters 8-11)
    - Section 4: Concept, Object, Event & Place (Chapters 12-16)
    - Appendix F: Additional Instructions on Names of Persons
    
- ISAAR (CPF): International Standard Archival Authority Record for Corporate Bodies, Persons and Families, 2nd Edition ([http://www.ica.org/10203/standards/isaar-cpf-international-standard-archival-authority-record-for-corporate-bodies-persons-and-families-2nd-edition.html](http://www.ica.org/10203/standards/isaar-cpf-international-standard-archival-authority-record-for-corporate-bodies-persons-and-families-2nd-edition.html)) - International Council of Archives);

- EFG Metadata Schema & Vocabularies – 3.6 Agent ([http://www.efgproject.eu/guidelines_and_standards.php](http://www.efgproject.eu/guidelines_and_standards.php))

Authority files

- VIAF (The Virtual International Authority File)

- ISNI (International Standard Name Identifier (ISO 27729) – [http://www.isni.org/](http://www.isni.org/)

- IdREf (Identifiants et Référentiels) – [http://www.icacds.org.uk/eng/ISAAR(CPF)2ed.pdf](http://www.icacds.org.uk/eng/ISAAR(CPF)2ed.pdf)

- Library of Congress Subject Headings (LCSH) and the Library of Congress Genre-Form Thesaurus (LCGFT)

<a id="sec-definitions_of_the_work_and_variant_entities"></a>
#### Definitions of the “Work” and ”Variant” Entities
The FIAF Cataloguing and Documentation Commission has chosen to model this manual on definitions of “Work” and “Variant” adopted by the European Standards Committee, rather than the FRBR and RDA definitions of “Work” and “Expression,” to make these concepts more practical for describing moving images. FRBR and RDA consider “works” and “expressions” to be abstract entities that only acquire physical characteristics at the “manifestation or “item” level. However, moving image “works” are more easily conceptualized as concrete entities. This is because a moving image work only becomes such through a complex process involving multiple contributors. This process results in a “fixed” or “expressed” object (whether analogue or digital) that typically combines a visual part (the moving image), and a textual part (the soundtrack or intertitles).[^10] Therefore, the concept of a moving image work comprises both the content and the process of realisation in a moving image medium.[^11]

Further, this manual continues to follow the precepts already outlined in Film Cataloguing and FIAF Cataloguing Rules for Film Archives by including the concept of “original.” The FIAF Cataloguing Rules for Film Archives recommend using the “original release title or broadcast title in the country of origin, i.e., the country of the principal offices of the production company or individual by whom the moving image work was made”[^12] to identify a Work. “Owing to the complex interrelationships of persons and corporate bodies in the creation of a moving image work, the original release or broadcast title is chosen as the single element which can provide the level of consistency and standardisation requisite for any national and international networking or sharing of cataloguing data.”[^13]

Likewise, the “original” defined here contains characteristics that persist across any variation or output of a moving image work and that reflect the original intentions of its realisation, including: circumstances of the creation process such as date(s) and place(s) of production, most contributions by agents such as directors, screenwriters, production companies and cast members, as well as certain statements about the contents.[^14]

In this way, a moving image work as a concept is closer to a combining of FRBR and RDA’s work and expression entities. This definition also aligns closely with the concept of “work primary expression” formulated by the Online Audiovisual Catalogers (OLAC) Cataloging Policy Committee (CAPC) Moving Image Work-Level Records Task Force and the CEN’s EN 15907. A primary difference here is that EN 15907 specifies for the concept of “original” to be expressed in association with an instance of a Manifestation that embodies the original Work.

The use of the term “variant” is not a mere substitute for the term “expression.” In the context of moving images, variants and expressions cannot be considered equivalent concepts because moving image works are already their own expressions.[^15] As explained above, a moving image work has by definition taken a form (been expressed) and contains specific attributes that correspond to the concept of an “original” or “primary expression.” The variants correspond to all other “expressions.” For example, a colorized version of The asphalt jungle (1950) does not express the original work; it contains a variation from the original idea conceived by John Huston and put into form. If there is no variation from the work as originally conceived, there is no “variant,” but under FRBR there would always be an “expression.” This exemplifies why these concepts are not equal: that is, there may not always be a variant but there must always be an expression.[^16]

<a id="sec-definitions_of_the_manifestation_and_item_entities"></a>
#### Definitions of the Manifestation and Item Entities
A Manifestation is the embodiment of a Work/Variant and includes all the analogue or digital forms that are derived from a Work/Variant and bear common characteristics with respect to shared intellectual content and physical format. It may be whole or incomplete or a fragment.

An Item is the physical product of a Manifestation of a Work or Variant, i.e. the physical copy of a Work or Variant. It may be whole or incomplete or a fragment. In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist[^17].

<a id="sec-boundaries_between_entities"></a>
#### Boundaries between entities
The traditional practice within moving image archives of incorporating variation information into a record enabled this one record to carry within it all the details relative to the differing components of a whole.[^18] Within the framework of the FRBR and RDA models, and the EN 15907 schema, the work record represents this “one record,” incorporating certain descriptive details, but the placement of the variation information changes. Different editions, versions, or variations are represented by the variant and manifestation entities, and the differences are recorded at the appropriate level or on the particular entity record, or designated in some way as belonging to the specific entity. The treatment of an “information resource” by using the four-tier hierarchy to express the concept allows it to be described and viewed at each of the four levels: for example, a documentary is, simultaneously, a particular copy or component pieces (item(s)), a particular publication (manifestation), a particular edition (variant), and a particular piece of work (work).

It remains essential to users of archival moving image material that information describing the original work and information describing the item in hand are presented in a manner that clearly delineates this relationship. The relationship in library terms is described as the concept of “edition” and it includes any changes in content or changes in carrier. Separate editions of printed library material are catalogued separately, and usually no attempt is made to determine whether edition statements always indicate major changes in content.[^19] “Publication,” in the context of a moving image archive, is used interchangeably with “distribution” and means “making the resource available.”[^20] For moving image materials, the terms most analogous to this concept of edition are “versions with major changes” and “variations with minor changes.”[^21] (see [http://www.fiafnet.org/images/tinyUpload/E-Resources/Commission-And-PIP-Resources/CDC-resources/FIAF_Cat_Rules.pdf](http://www.fiafnet.org/images/tinyUpload/E-Resources/Commission-And-PIP-Resources/CDC-resources/FIAF_Cat_Rules.pdf))

In moving image archives, both the occurrence of a change in the content and the extent of the change are important. In most cases, for moving image materials, the changes in content are a function of some form of editing.

The treatment of the concepts of “versions with major changes” and “variations with minor changes” in this revision shift to a focus on changes in content and changes to carrier and correlate to the boundaries between the variants (changes in content) of a work and its manifestations (changes in carrier). This does not replace the need to create a version with major changes as a new Work where this is necessary and appropriate [Boundaries between Works and Variants](/boundaries/boundaries_between_works_and_variants/).

<a id="sec-attributes"></a>
### Attributes
This manual provides a granular nomenclature for describing the attributes of the moving image entities, Work, Variant, Manifestation and Item (WVMI). The guidelines do not specify the attributes for entities related to the WVMI entities, for example, Agents (i.e., Persons, Families, Corporate Bodies, etc.). For recording the attributes of Agents (e.g. first name, last name, nationality, etc.), refer to authoritative sources such as Functional requirements for authority data: a conceptual model or tools such as the Library of Congress Name Authority File.[^22]

<a id="sec-user_tasks"></a>
### User Tasks
FRBR and RDA have defined and adopted the following tasks reflecting the traditional core functions of the catalogue:[^23]

find—i.e., to find resources that correspond to the user’s stated search criteria

identify—i.e., to confirm that the resource described corresponds to the resource sought, or to distinguish between two or more resources with similar characteristics

select—i.e., to select a resource that is appropriate to the user’s needs

obtain—i.e., to acquire or access the resource described.

RDA added an additional set of user tasks based on those defined in IFLA’s Working Group on Functional Requirements and Numbering of Authority Records (FRANAR), and describe an entity associated with a resource:

find—i.e., to find information on that entity and on resources associated with the entity

identify—i.e., to confirm that the entity described corresponds to the entity sought, or to distinguish between two or more entities with similar names, etc.

clarify—i.e., to clarify the relationship between two or more such entities, or to clarify the relationship between the entity described and a name by which that entity is known

understand—i.e., to understand why a particular name or title, or form of name or title, has been chosen as the preferred name or title for the entity.

These user tasks are listed because they are pertinent to moving image cataloguing and can be adapted to cover many of the search and discovery needs of those who might seek moving images. For example, Martha Yee (2007) provides one adaptation of the functions of the library catalogue for moving images:

To find, identify, select, and acquire: [^24]

- All the versions (Variants) of a sought Work (for example the various “director’s cuts” of Blade runner as well as the original release version), specified by its title, or by its title in conjunction with the name of one of its creators or by date, that are held by your collection or to which you license access.

- All the copies (Manifestations or Items) of a particular version (Variant) of a Work (for example, all the copies you hold of the studio’s director’s cut) that are held by your collection or to which you license access.

- All the Works of a particular person (for example, director, actor, costume designer) or corporate body (for example, studio) that are held by your collection or to which you license access.

- All the Works on a subject (for example, the Vietnam War) that are held by your collection or to which you license access.

- All the Works in a particular form or genre (for example, animation, gangster films) that are held by your collection or to which you license access.

### Representation (or, principle of transcription)

The basic principle of transcription is an area in which archival moving image cataloguing frequently deviates from traditional library cataloguing. Whereas traditional library cataloguers typically transcribe descriptive data directly from the physical item, this is not always the case in archival moving image cataloguing. Because of this, earlier moving image cataloguing rules and standards (FIAF, AMIM) have suggested the term “preferred” rather than “chief” source of filmographic information for representing moving images. The importance of reflecting the original details of a moving image work is a primary principle of organisation for moving image archives. This underlies another practice of moving image cataloguing, which was also recommended in the 1991 FIAF Rules, namely choosing the original release title in country of origin as the preferred title for a work. Other titles (e.g., translated titles, re-release or reissue titles, titles on the item or accompanying material, etc.), are recorded at the appropriate entity level, or designated as belonging to the appropriate entity, and linking mechanisms from other titles to the original release title should be utilised.

Because, however, it is not always possible for a cataloguer to determine an original release title, guidelines are also provided for choice of the preferred title of the work when either: 1) the concept of original release title is not applicable (as in the case of unedited footage), or when 2) a cataloguer is unable, through research, to determine the original release title.

[^1]: FIAF, 1991, p. ix.
[^2]: Adapted from AMIM2, p.1.
[^3]: The other two conceptual models are FRAD (Functional Requirements for Authority Data), [http://www.ifla.org/node/7923](http://www.ifla.org/node/7923) and FRSAD Functional Requirements for Subject Authority Data, [http://www.ifla.org/node/1297](http://www.ifla.org/node/1297).
[^4]: FRBR Final Reports, p. 3.
[^5]: RDA 0.0 and 0.1, p. 0-1.
[^6]: [https://tech.ebu.ch/MetadataEbuCore](https://tech.ebu.ch/MetadataEbuCore)
[^7]: [http://pbcore.org/](http://pbcore.org/)
[^8]: Taken from EN 15907. Item – Definition from the standard. [http://filmstandards.org/fsc/index.php/EN_15907_Item](http://filmstandards.org/fsc/index.php/EN_15907_Item)
[^9]: FRBR Final Report, pp. 12-16; Taylor, p. 4.
[^10]: Yee. “The Concept of Work for Moving Image Materials, p. 33.
[^11]: EN 15907, 4.1.1, p. 8.
[^12]: FIAF, 1991, p. xiii
[^13]: FIAF, 1991, p. xiii
[^14]: Adapted from the definition of a Cinematographic Work in EN 15907, 4.1.1, p.8.
[^15]: Journal of Digital Media Management Vol. 2, 3, 00–00 © Henry Stewart Publications 2047- 1300 (2013) The EN 15907 moving image metadata schema standard and its role in a digital asset management infrastructure, by Detlev Balzar, Stephen McConnachie, Thelma Ross.
[^16]: Laurent Bismuth (personal communication, May 08, 2011)
[^17]: Digital medium definition taken from CEN’s “Film Identification – enhancing interoperability of metadata. Element sets and structures. FprEN 15907:2010 (E)
[^18]: FIAF, 1991, p. xii
[^19]: FIAF, 1991, p. xii
[^20]: Andrea Leigh, (drawn from personal communication, May 05, 2011)
[^21]: FIAF, 1991, p. xii-xiii. They are defined as following in the 1991 rules: Versions with major changes. If the cataloging agency has determined that the item in hand differs significantly from the original work, i.e., major editing has been done, the item is described in a separate cataloging record. The item in hand is designated a version of the original work with major changes, e.g., short version, classroom version, etc., and the distribution information for the separate version is recorded. The relationship to the original work is indicated in the edition/version statement, and, in most instances, in a note. Distribution information relating to the original work may also be indicated in a note. Variations with minor changes. When the cataloging agency determines that an item, although designated as being re-edited, e.g., a “new edition,” has not indeed been changed significantly, it may express this relationship by recording the statement of responsibility for the original in area one, the variation and statement of responsibility for the variation in area two, and the production, distribution information for both the original and variation copies in area three. Multiple edition/version/variation statements may be given when cataloging multiple variations with minor changes.
[^22]: Patton, Glenn E. 2009. Functional requirements for authority data: a conceptual model. München: K.G. Saur.
[^23]: FRBR Final Report, p. 82; RDA, 0.0, Purpose and Scope
[^24]: Yee, 2007, p. 16.
