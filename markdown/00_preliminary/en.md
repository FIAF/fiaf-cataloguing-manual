---
colorlinks: true
linkcolor: orange
urlcolor: teal
header-includes:
  - \usepackage{xcolor}
---

![](/app/src/diagrams/front.png)

\newpage
\section*{Dedication}
\label{sec:dedication}
    
This manual is dedicated to **Christian Dimitriu** (1945-2016), whose contributions to the field of moving image archiving and FIAF, are immeasurable; and to **Ronny Loewy** (1946-2012), whose knowledge of moving image metadata standards was a primary and crucial source of information during the development of this publication; and to **Laurent Bismuth** (1965-2021), a passionate advocate of CEN 15907 standard whose extensive cataloguing knowledge and expertise and contributions in discussions during the compilation of this publication were invaluable.

\newpage
\section*{Acknowledgements}
\label{sec:acknowledgements}

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

\newpage 
\tableofcontents

\newpage
\section{Introduction}
\label{sec:introduction}

The archival moving image field has changed dramatically in recent years, with technological advances revolutionising cataloguing, preservation, and access practices.
To help cataloguers and archivists respond to these changes, FIAF presents the *FIAF Moving Image Cataloguing Manual (FIAF Manual)*, a revision of the 1991 *FIAF Cataloguing Rules for Film Archives (FIAF Rules)*.
These new guidelines, created by the FIAF Cataloguing and Documentation Commission and the FIAF Cataloguing Rules Revision Working Group, will help cataloguers create cataloguing or metadata records that will meet requirements of new database technologies and new metadata standards while remaining compatible with older methods and standards.

The Manual offers primarily descriptive cataloguing rules rather than a schema of data elements.
However, it is difficult to discuss rules without mentioning data elements where the rules would be applied (e.g., Title, Date, etc.).
Thus, the Manual by default provides both a metadata structure (fields or elements) and rules in how to input the values the fields contain.
It reflects current and recommended cataloguing practices at international film archives represented on the Commission with the goal of interoperability with related cataloguing and metadata standards.

The cataloguing of moving images encompasses the complex, professional tasks of gathering and arranging data within systems upon which an institution depends.
Indeed, accurate, well-organised descriptions of both filmographic and technical information about an institution’s collection serve as the basis for informed internal use such as preservation, collections development, and outreach or exhibition.
They further constitute the key to accessing collections by external users such as scholars, researchers and the general public – both now and for future generations.^[FIAF, 1991, p. ix.]

Cataloguing archival moving images combines general archival processing methodologies and traditional library cataloguing.
The process of archiving moving images applies practices held in common with archiving other materials such as papers and manuscripts.
The materials’ origin or provenance is a key element to understanding their significance.
Their historical context shows their relationship(s) to other works and, in cases of works with multiple manifestations, the development of individual works.
Knowledge of this historical context and development of materials can be useful in their preservation.^[Adapted from AMIM2, p.1.] An attempt has been made throughout the guidelines to address capturing provenance and preservation information.

This manual is intended to address some of the limitations moving image archives face when using guidelines and systems developed primarily for general libraries.

General library catalogues are built to support the discovery of a specific publication and its various editions.
This discovery is facilitated by a focus on the creation of access points to author, title and/or subject.
Many libraries catalogue through bibliographic utilities to pool effort by sharing records of these single publications.
While this shared bibliographic model works well for libraries, since many will have exact copies of the same publication, it does not  provide all the functions that moving image archives need.
Because moving image archives’ collections often include unique or rare holdings, such as pre-print elements, master prints, and unreleased material in addition to viewing copies, they need catalogues that go beyond the functions of a library catalogue to meet many of the collection management needs of archives.
The FIAF Manual is intended to provide guidance in creating metadata or cataloguing records that fulfill these collection management functions.

This revision of the 1991 guidelines recognises that institutions use a variety of systems and data structures and may find it difficult to implement far-ranging changes in their cataloguing practices.
The revisions suggested in this manual will help archives harmonise their practices with related standards, models, and schema, including:

1. The conceptual model Functional Requirements for Bibliographic Records (FRBR), published in 1998 by the International Federation of Libraries Association. FRBR is one of the models underlying RDA: Resource Description and Access^[The other two conceptual models are FRAD (Functional Requirements for Authority Data), [http://www.ifla.org/node/7923](http://www.ifla.org/node/7923) and FRSAD Functional Requirements for Subject Authority Data, [http://www.ifla.org/node/1297](http://www.ifla.org/node/1297).], and it provides “a framework that identifies and clearly defines the entities of interest to users of bibliographic records, the attributes of each entity, and the types of relationships that operate between entities.”^[FRBR Final Reports, p. 3.]
    
2. RDA: Resource Description and Access (RDA), co-published in 2010 by the American Library Association, the Canadian Library Association, and Chartered Institute of Library and Information Professionals. RDA was developed as a new standard for resource description and access designed for the digital world, and applies FRBR concepts and terminologies. It is intended to eventually supplant Anglo-American Cataloguing Rules (AACR2), which has been the descriptive cataloguing standard in English-speaking communities since the 1960s. Like AACR2, RDA covers all types of content and media.^[RDA 0.0 and 0.1, p. 0-1.]

3. The European Standards Committee (CEN) Cinematographic Works Standard (CWS) (EN 15744 and EN 15907). This two-part standard defines the metadata essential for facilitating data exchange between databases and consistent identification of moving images. The metadata schema (EN 15907), which is based in part upon the FRBR conceptual model, was approved in 2010 and disseminated through four workshops held from October 2010 – June 2011. Brief definitions of key elements in the FRBR-based CEN model are at the end of the Introduction.

For further information about the relationship of this set of guidelines to FRBR, RDA and EN 15907, see [Appendix F.3](#manual-F.3).
Although these guidelines are structured to correspond closely with the above standards/models/schema, and use associated terminology, note that neither they nor these guidelines are system-specific.
They cover the fundamentals for cataloguers for the construction and management of data and records in whatever system or standards used by an institution.

While these guidelines are intended to be applicable to all forms of moving image materials, archives with extensive broadcasting collections may wish to look to broadcasting-specific metadata schemas such as EBUCore^[[https://tech.ebu.ch/MetadataEbuCore](https://tech.ebu.ch/MetadataEbuCore)] and PBCore^[[http://pbcore.org/](http://pbcore.org/)] for additional guidance.

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
In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.^[Taken from EN15907. Item – Definition from the standard. [http://filmstandards.org/fsc/index.php/EN_15907_Item](http://filmstandards.org/fsc/index.php/EN_15907_Item)]

\newpage
\section{Preliminary Notes}
\label{sec:preliminary_notes}

\subsection{Purpose, scope, and use} 
\label{sec:purpose_scope_and_use}
    
\subsubsection{Purpose} 
\label{sec:purpose}

The primary purposes of the FIAF Manual are to suggest recommendations for the description and identification of moving images (with an emphasis on archival moving images), and to define the elements of description to facilitate the exchange of information.

\subsubsection{Scope} 
\label{sec:scope}

The manual is designed for use by institutions with moving image collections and cataloguers of moving images as a guide in the preparation of cataloguing records or descriptive metadata.
The recommendations apply to generalised film and television collections, and may require elaboration in more specialised institutions whose holdings are exclusively of a single format or type, e.g., commercials, newsfilm, television, unedited footage, etc. For example, those with television collections should additionally consider more specific standards such as EBUcore or PBcore,

Moving images include a range of materials upon which sequences of visual images have been recorded or registered and which create the illusion of movement when projected, broadcast, or played back (by means of a projector, television set, computer, software or equivalent devices).
Such images may or may not be accompanied by sound.
The definition includes moving images of all types, e.g., features, shorts, news footage, trailers, outtakes, screen tests, educational and training documentaries, experimental or independent productions, study films or video, home movies, unedited materials, television broadcasts, commercials, spot announcements, recorded performances of concerts, ballets, plays, and CCTV footage etc. It encompasses both live action and animation and includes all analogue and digital formats.

While many moving image archives also have audio materials in their collections, this manual does not offer detailed guidance for describing audio media.
However, the Manual does provide ways to describe physical and technical characteristics of analogue and digital audio Items to assist with collection and preservation management.

\subsubsection{Use} 
\label{sec:use}
    
Instead of defining levels of cataloguing, this manual outlines core elements for moving image description.
The core elements provide the basis for identification of a resource and for facilitating the exchange of data from one system to another.
These are not “core” elements in the sense of a Dublin Core, EBUCore, or PBCore schema, but are rather intended to illustrate common elements that are used in describing moving images and are referenced in the rules outlined in this manual.
The elements are largely drawn from EN 15744 and 15907.
For a comparison of elements described in this Manual and EN 15907, please see \nameref{sec:elements_of_description_comparison}.

This manual also provides a list of all the data elements associated with the entities described.
Thus, this approach provides a framework for the minimum and maximum amount of descriptive information allowed in a range of moving image cataloguing activities existing in a large variety of environments.

Institutions are encouraged to include as many of the non-core elements as goals and circumstances permit.
None are considered mandatory by these guidelines, but an institution may require that some are mandatory for internal purposes.

\subsection[Core elements of description]{Core elements of description 
\footnote{Adapted from CEN TC 372 EN 15744 element set}}
\label{sec:core_elements_of_description}

These core points of description are listed with their corresponding terms as presented in the manual.
They represent an ideal minimum set of metadata for moving image cataloguing.

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|L|}
\hline
\textbf{CORE CONCEPT} & 
\textbf{TOP-LEVEL ELEMENT} & 
\textbf{SUB-ELEMENT} \\
\hline
Title & 
1.3.2 Title [Work] & 
-- \\
\hline
Series / Serial \footnote{EN15744 definitions “A series is a group of separate items related to one another by the fact that each item bears, in addition to its own title, a collective title applying to the group as a whole. A serial is a type of “short subject” work which is characterized principally by the episodic development of a story”. This Core Concept is referencing the name of another Work that a Work may be “part of”, where the latter has been conceived within the context/intention of being an element of a Series or Serial. It is not being used here as a Work/Variant Description Type. (See D.1 Work/Variant Description Types)} & 
1.3.2 Title [Work] & 
1.3.2.1 Title Type = Series/Serial [Work] \\
\hline
Cast & 
1.4.1 Agents (e.g. Cast, Credits, Person, Organisation, etc.) [Work] & 
1.4.1.1 Agent Activity = Cast [Work]  \\
\hline
Credits (including Production Companies) & 
1.4.1 Agents [Work] & 
1.4.1.1 Agent Activity = Credit (use term for actual role)  [Work] \\
\hline
Country of Reference & 
1.3.3 Country of reference [Work] & 
\\
\hline
*Original Format & 
2.3.4 Format of a moving image Manifestation [Manifestation] & 
2.3.4.1.2 Specific Carrier Type: [Manifestation] \\
\hline
*Original Length & 
2.3.5 Extent of a Manifestation [Manifestation] & 
2.3.5.2 Physical extent of a Manifestation \\
\hline
*Original Duration & 
2.3.5 Extent of a Manifestation [Manifestation] & 
2.3.5.3 Duration of a Manifestation \\
\hline
*Original Language & 
1.3.5 Language(s) [Work] & 
1.3.5.1 Language Term + 1.3.5.2 Usage type [Work] \\
\hline
Year of Reference & 
1.3.4 Year/Date of reference [Work] & 
1.3.4.1 Date Type [Work] \\
\hline
Identifier & 
As appropriate: 1.3.1 Work/Variant Identifier [Work/Variant] AND/OR 2.3.1 Identifier [Manifestation] AND/OR 3.1.1 Identifier [Item] & 
As appropriate: 1.3.1.1 Identifier Type [Work/Variant] AND/OR 2.3.1.1 Identifier Type [Manifestation] AND/OR 3.1.1.1 Identifier Type [Item] \\
\hline
Subject/Genre/Form \footnote{Form = Fiction, Non-fiction, etc. Some institutions may incorporate these as a genre term, whilst others may have them as a separate category to genre.} & 
1.4.3 Subject/Genre/Form terms [Work] &  
\\
\hline
Content Description & 
1.3.6 Content description (synopses, shotlists, etc) &  
\\
\hline
\end{xltabular}

The concept of “original” in this manual indicates the first known manifestation of the Work, which is not determined by its release status.
The concept of “original” must be flexible enough to be applied to released and unreleased Works.
For a released Work, we tend to refer to the “original” Work as the first known release of the first known manifestation.
For Works that are not released (e.g., a home movie), the “original” Work is simply the first known manifestation.

See \nameref{sec:example_one} as an illustration.

Please see \nameref{sec:elements_of_description_comparison} comparison for a list of all elements described in this manual.

NOTE: For exchanging data, indicating the origin of the record is important (i.e., name of the institution supplying the record).
This data is typically located in a dedicated field at the Work level and automatically generated by electronic systems.
This corresponds to CEN EN 15907, 6.2 – Record Source.

\subsubsection{Elements of description across Works, Variants, Manifestations, and Items} 
\label{sec:elements_of_description}
    
This section includes sample structures for how the elements can be applied across Works, Variants, Manifestations, and Items.
Four models are provided, beginning with the more complete four-level model and ending with a simple one-level model.
Models should be applied according to an institution’s system and also determined by the amount of information known about an Item.

Where there is a user need or requirement, some institutions may also develop database systems that pull through some data elements sitting in fields in one hierarchical or linked level to display and be viewed within another, e.g. duration from a Manifestation being visible within a Work record, or location details sitting at the Carrier level also displaying through in the linked Item record.

The full list of elements of description for each entity is set out in the following charts and diagrams, and in Chapters 1-3.
See \nameref{sec:appendix_title} for examples of real records which contain these core elements (as well as others) across the hierarchies.

![](/app/src/diagrams/figure_01.png)
![](/app/src/diagrams/figure_02.png)
![](/app/src/diagrams/figure_03.png)
![](/app/src/diagrams/figure_04.png)

\newpage
*Work/Manifestation/Item.
Properties expressed in one record, with abstracts, contextual and object data stored in a single level hierarchy Distribution of the elements of description according to the four entities order.*

\setlength\extrarowheight{2pt} 
\begin{xltabular}{\textwidth}{|L|L|L|L|}
\hline
\textbf{Properties} & 
\textbf{(Work)} & 
\textbf{(Manifestation)} & 
\textbf{(Item)} \\
\hline
Titles & 
Uniform, Preferred, Other Title information, Alternative, Supplied/Devised & 
Title proper & 
Title proper \\
\hline
Part & 
Monographic, Analytic, Serial, Collection & 
& 
\\
\hline
Content & 
Categories: fiction/non fiction; genre, synopsis, subject, etc. & 
& 
\\
\hline
Dates/Events & 
Creation, Production, Censorship, Copyright & 
Release, manufacture, transmission, distribution, etc. & 
Object creation, acquisition, accession, de-accession, loan, transport, etc. \\
\hline
Agents & 
Cast, credits, rights holders, creator, etc. & 
Distributor, broadcaster, publisher & 
Donor, Archive/archivist, technician, restorer, etc. \\
\hline
Rights context & 
Copyright holder and date & 
Platforms, territories, dates. Agents (distributors, license holder) & 
Transfer of ownership \\
\hline
Event types & 
Awards Censorship Production IPR registration & 
Pre-release, theatrical, non-theatrical, transmission, home viewing, internet, not for release, censorship etc. & 
Acquisition Reproductions Disposal \\
\hline
Format general & 
& 
35mm film, digital cinema, blu ray, etc. & 
\\
\hline
Format specific & 
& 
& 
16mm film pos, 35mm lavender separation, ProRes422 HQ, etc. \\
\hline
Condition report & 
& 
& 
Pristine, not for projection, heavy scratches, etc. \\
\hline
Storage location & 
& 
& 
Home location, current location, previous location  \\
\hline
Conservation recommendations & 
& 
& 
Urgent transfer required, relocate sub-zero, etc. \\
\hline
\end{xltabular} 

\subsection{Sources of Information}
\label{sec:prelim_sources_of_information}

Information entered in a record must be derived from a source.
Acceptable sources of information for moving image Works, Variants, Manifestations and Items include primary and secondary sources.

Primary sources include information on the actual Item itself.
For example, for moving image materials, titles and main production credits are transcribed from the frames usually in the opening credits, and other production credits from the end titles and credits.
Secondary sources include information written on containers and reference materials.
For example, credit, title, date, and other information derived from publications such as AFI Catalog of Feature Films: 1930-1939, or [Det Danske Filminstitut Filmdatabasen](https://www.dfi.dk/viden-om-film/filmdatabasen) , etc.

Although primary sources are generally preferred, this manual allows for the use of secondary sources no matter the entity, attribute or relationship described in recognition that there may be constraints on the amount of research or viewing a cataloguer can do.

Whether information is taken from primary and/or secondary sources as listed below, indicate that fact either by means of a note or by some other means (e.g., through coding or the use of square brackets, specific fields, or links to other databases).^[Based on RDA 2.2.4 Other Sources of Information] Add the source of the information in a Note field and include the element name.

Cite each individual source of information using an agreed upon, consistently applied citation style, such as The Chicago Manual of Style, or other style guide.

Primary source information can be derived from:

a) the title frame(s) or title screen(s)^[RDA 2.20.2.3 Title Source]

b) embedded metadata in textual form that contains a title (e.g., metadata embedded in an MPEG video file)^[Ibid.]

c) the director (or other crew/cast members) involved in the production of the moving image, either via verbal or written communication.

d) an eye-readable label bearing a title that is permanently printed on or affixed to the resource (excluding accompanying textual material or a container)^[Adapted from RDA 2.2.2.3 Resources Consisting of Moving Images]

```{=latex}
\begin{tcolorbox}
Title derived from film opening credits.
\end{tcolorbox}
```

Where viewing the primary source is not possible, the cataloguer is dependent on secondary sources. 

Secondary source information can be derived from:

e) accompanying material or a container issued as part of the resource itself^[Based on RDA 2.2.4 Other Sources of Information]

f) a container that is not issued as part of the resource itself (e.g., a box, case made by the owner)^[RDA 2.2.4 Other Sources of Information]

g) other published descriptions of the resource (e.g. a reference source, website, press packs, etc.)  ^[Ibid.]

h) any other available source (including family or colleagues of crew/cast members with information.)^[Ibid.]

Access to sources of information has increased massively in the 21st century, particularly with the World Wide Web.

This means it is particularly important for the cataloguer to consider the authority and context of the source before utilising information from it, e.g. whose website is it and where did their information come from?

As far as possible use authoritative secondary sources, e.g. official websites for a film, press packs, published catalogues and directories, and data from other Archives accessible databases, websites, or publications, who may have researched and created records for the moving image already. Sources may also include other non-moving image collections held by your institution, such as special collections of papers, books, newspaper cuttings, stills, posters, etc.

The number of websites stating the same “fact” is not a safe indicator. Websites copy off each other and it is easy for an erroneous fact to be perpetuated across multiple websites^[See the name note on the [BFI record for Richard Greene](https://collections-search.bfi.org.uk/web/Details/People/177651)]. The cataloguer needs to assess, balance, and judge accuracy, e.g. IMDB and Wikipedia can be good for information, but they also allow submissions and changes from the public so it is not necessarily always accurate.

When taking details and information from secondary source materials then cite those sources, either in relevant notes fields on a record as a \nameref{sec:cataloguers_notes}, or linking to a related non-moving image collection record within your institution's database systems if relevant, e.g. a related associative link to a book record or periodical article record. 

If citing websites take a note of the full title and author where relevant, not just the URL link. The latter can change or the website become defunct over time, so fuller precise details are advisable.

In instances where Primary source data relating to on-screen titles and credits, or embedded metadata is verfied as erroneous and incorrect through other Primary or authoritative Secondary sources then details of this should be added to a Work History or Notes field on the Work.

```{=latex}
\begin{tcolorbox}
Il vangelo secondo Matteo (Italy, 1964)
\end{tcolorbox}
```

Work History note: The credits in the opening titles on actual prints of the film give 'Alessandro Clerici' as playing the role of Pontius Pilate. However, he was in fact played by Alessandro Tasca (aka Alessandro Tasca di Cutò). Verified by his daughter Ama Tasca di Cutò in correspondence with the BFI (February 2020)  and further researched by the BFI in conjunction with Cineteca Bologna. Alessandro Tasca also discusses his taking on the role of Pilate in Pasolini's film, and his fee for the day's work, in correspondence with Orson Welles (housed at the University of Michigan). Distribution information from c.1964/65 from UniItalia in Rome and from other English distribution companies of the film in the 1960s also cite 'Alessandro Tasca' as the credit for Pontius Pilate.

\subsection{Display issues}
\label{sec:display_issues}
  
Although these guidelines are primarily focused on content, many users may also welcome some guidance in data presentation.
Section 0.4 gathers some of the common display questions with recommendations.

\subsubsection{Punctuation}
\label{sec:punctuation}

These guidelines do not mandate the use of any particular data presentation standard, such as ISBD punctuation.
However, ISBD punctuation is recommended if punctuation guidance is desired.
Please consult ISBD^[[http://www.ifla.org/files/assets/cataloguing/isbd/isbd-cons_20110321.pdf](http://www.ifla.org/files/assets/cataloguing/isbd/isbd-cons_20110321.pdf)] for general guidance and examples, or the FIAF Cataloguing Rules for Film Archives (1991)^[[http://www.fiafnet.org/~fiafnet/uk/publications/fep_cataloguingRules.html](http://www.fiafnet.org/~fiafnet/uk/publications/fep_cataloguingRules.html)].

These guidelines do advocate consistent usage where punctuation is needed as a cataloguing construction, for example, to separate Form elements in the creation of Partially or Fully Supplied/Devised Titles e.g.

```{=latex}
\begin{tcolorbox}
Jaws. Rushes.
\end{tcolorbox}
```

For transcribed elements, record punctuation as found.
For all other elements, record punctuation as found on the source(s) of information.

\subsubsection{Capitalisation and Articles}
\label{sec:capitalisation_and_articles}

Some institutions render Work titles in capitals – all upper-case – as a simple typographical method of identifying these key items of information, while others only capitalise the first letter of a title, in accordance with ISBD.
Either usage is permitted by these guidelines, although institutions may prefer to retain the conventional practice of capitalising only the first letter of a title and any proper names as dictated by the usage of the language in which the information is given.

Users should recognise that using all capitals may create problems in the future when reformatting to mixed case if preferred in a new system, or when reformatting to mixed caps for display in a web platform where mixed caps is increasingly preferred.
Although it is possible to automate the conversion of upper case to mixed caps, that automation cannot easily manage linguistic complexities or semantic rules and exceptions such as proper nouns, or place names.
Therefore, it is recommended that an institution transition to ISBD capitalisation when and where possible.

When an “all capitals” practice is followed, institutions have the additional option of reducing to lower case words which are of minor importance to the substantive title (for filing purposes, etc.), such as sub-titles, a definite or indefinite article appearing as the first word of a title, etc. Experience has shown that this practice can make it easier for staff in institutions handling multi-lingual material to recognise, for filing purposes and interpretation, the different significance of words that are articles in one language but not in others.

While the guidelines permit both cases, it is recommended where permitted now or in the future, to use the conventional practice of capitalising only the first letter of a title and other letters as dictated by the usage of the language in which the information is given.
Leading articles should ideally be placed in separate fields in keeping with the way systems are being developed for alphabetical sorting.
Alternatively some systems (for example, those containing MARC21 records) indicate the number of non-filing characters to skip in alphabetization.

Alternative practices | ISBD practice

```{=latex}
\begin{tcolorbox}
Die Hard | Die hard    \\
Die DREIGROSCHENOPER | Die Dreigroschenoper    \\
LES PATTERSON SAVES THE WORLD | Les Patterson saves the world     \\
Les MISERABLES | Les miserables    \\
American in Paris, An | An American in Paris 
\end{tcolorbox}
```

MARC21 tag

```{=latex}
\begin{tcolorbox}
245 03 An American in Paris
\end{tcolorbox}
```

\subsection{Language and script of the description}
\label{sec:language_and_script_of_the_description} 

The language of the original Work can be different from the language of a Manifestation or Item.
For example, the original Work title can be in the original creation language, but the item being catalogued is a Variant with the title and key credits in a different language.
Where possible, data elements in the catalogue record for the Work are recorded in the language and/or script of the original Work and may be transcribed from the Item of an original manifestation of the Work or taken from other sources.

This will primarily be for data transcribed from the screen, e.g. Title and key agents (director, producer, cast, etc.).
Do not confuse this with describing the language of the soundtrack, which is noted in specific language fields.

Data elements for the Variant, Manifestation and Item are recorded in the language that is on the Variant, Manifestation or Item and should be transcribed from the Item or from other sources in the appropriate language.
Scripts, symbols or other characters that cannot be transcribed as presented or are other than that used by the cataloguing agency or institution may, if necessary, be transliterated in the script of the institution or replaced with a cataloguer’s description.
Use a recognised standard for transliteration such as [ISO 9 for Cyrillic characters](https://www.iso.org/standard/3589.html), [Pinyin for Chinese characters](https://pinyin.info/), or [ALA-LC Romanization Tables](https://www.loc.gov/catdir/cpso/roman.html).
Give an explanatory note for the addition, if necessary.
Optionally, enclose the cataloguer’s description in square brackets.

```{=latex}
\begin{tcolorbox}
Original Chinese Title: 精武英雄    \\
Transliterated Pinyin Title: Jīng wǔ yīngxióng    \\
English Translated Title: Fist of Legend 
\end{tcolorbox}
```

\subsection{Abbreviations} 
\label{sec:abbreviations}

For transcribed data elements, transcribe abbreviations as found.
For all other elements, generally do not abbreviate words.
Optionally, additional non-preferred title types may also be added to assist in user searching and accessibility (see \nameref{sec:titles_and_title_types}).

\subsection{Examples} 
\label{sec:examples}

The examples given throughout the guidelines are illustrative and not prescriptive (unless stated otherwise).
They follow The Chicago manual of style^[University of Chicago. 2003. The Chicago manual of style. Chicago, Ill: University of Chicago Press.] for the sake of consistency.
They are intended to illuminate the provisions of the guidelines to which they are attached, rather than to extend those provisions.
Therefore, neither the examples nor the form in which they are presented should be taken as instructions, unless the accompanying text specifically states that they should.
Most examples are from actual titles; in the few made-up examples an attempt has been made to formulate realistic data.
Examples of complete entries may be found in \nameref{sec:examples_of_records}.
Examples of the elements of description in different data structures are shown in \nameref{sec:elements_of_description_comparison}.
The bibliography follows ISO 690.

\subsection{Errors} 
\label{sec:errors}

As these guidelines recognise the importance of researched information in the catalogue entry, unintentional errors or inaccuracies from the Item should not be reproduced at the Work or Variant levels.

Begin with what the source of information says and correct it only when it is known to be ambiguous or erroneous.
Correction must be done in such a way that the resource remains recognisable to the users unaware of the error.^[YCR, Principle 3, p.4.] For example, AACR2 recommends transcribing the error followed by “sic” and sometimes the correct text in square brackets.

```{=latex}
\begin{tcolorbox}
Title (Work): À bout de souffle    \\
Title (Item): À bout de souflee [sic] 
\end{tcolorbox}
```

OR

```{=latex}
\begin{tcolorbox}
Title (Work): À bout de souffle    \\
Title (Item): À bout de souflee [souffle]  
\end{tcolorbox}
```

In RDA, the title is provided as transcribed without a recognition of the misspelling, with the correct title added in a secondary set of Title and Title Type fields (see \nameref{sec:alternative_title_types}) and a Note explaining the misspelling.

```{=latex}
\begin{tcolorbox}
Title (Work): À bout de souffle    \\
Title (Item): À bout de souflee    \\
Title (Item): À bout de souffle     \\
TitleType (Item): Actual title  \\
Note: Title on item is misspelled. 
\end{tcolorbox}
```

Missing information required to understand and identify a Manifestation, Variant, or Item can be supplied in brackets.   

Record intentionally misspelled words as found.  

```{=latex}
\begin{tcolorbox}
Title (Work): Inglorious Basterds
\end{tcolorbox}
```

\subsection{Alternatives and options} 
\label{sec:alternatives_and_options} 

Certain of the individual guidelines or parts of guidelines in this manual are introduced by the words, “alternatively” or “optionally.” Optional provisions arise from the recognition that different solutions to a problem and differing levels of detail and specificity are appropriate in different contexts.
Some alternatives and options should be decided as a matter of cataloguing policy for a particular catalogue or archive and should therefore be exercised either always or never.
Other alternatives and options should be exercised case-by-case.
It is recommended that all institutions which undertake cataloguing distinguish between these two types of options and keep a record of their policy decisions and of the circumstances in which a particular option may be applied.

The necessity for judgment and interpretation by the cataloguer is recognised in these guidelines.
Such judgment and interpretation may be based on the requirements of a particular catalogue or upon the use of the items being catalogued.
The need for judgment is indicated in these guidelines by phrases such as “if appropriate,” “if important” and “if necessary.” These indicate recognition of the fact that uniform regulation of catalogues is neither possible nor desirable, and encourage the application of individual judgment based on specific local knowledge.
This statement in no way contradicts the value of standardisation.
Such judgments must be applied consistently within a particular context and must be documented by the individual archive.

In addition, adherence to these structures and standards may not be wholly appropriate or possible for some institutions, given the differences in current practice, available cataloguing tools, and other issues.
An attempt has been made to design guidelines that can be applied where feasible, but which are not meant to be prescriptive.
