
\newpage \tableofcontents

\newpage
\section[Preliminary Notes]{Preliminary Notes 
    \label{sec:preliminary_notes}
    } 

\newpage
\subsection[Purpose, scope, and use]{Purpose, scope, and use 
    \label{sec:purpose_scope_and_use}
    } 

\subsubsection[Purpose]{Purpose 
    \label{sec:purpose}
    } 

The primary purposes of the FIAF Manual are to suggest recommendations for the description and identification of moving images (with an emphasis on archival moving images), and to define the elements of description to facilitate the exchange of information.

\subsubsection[Scope]{Scope 
    \label{sec:scope}
    } 

The manual is designed for use by institutions with moving image collections and cataloguers of moving images as a guide in the preparation of cataloguing records or descriptive metadata.
The recommendations apply to generalised film and television collections, and may require elaboration in more specialised institutions whose holdings are exclusively of a single format or type, e.g., commercials, newsfilm, television, unedited footage, etc. For example, those with television collections should additionally consider more specific standards such as EBUcore or PBcore,

Moving images include a range of materials upon which sequences of visual images have been recorded or registered and which create the illusion of movement when projected, broadcast, or played back (by means of a projector, television set, computer, software or equivalent devices).
Such images may or may not be accompanied by sound.
The definition includes moving images of all types, e.g., features, shorts, news footage, trailers, outtakes, screen tests, educational and training documentaries, experimental or independent productions, study films or video, home movies, unedited materials, television broadcasts, commercials, spot announcements, recorded performances of concerts, ballets, plays, and CCTV footage etc. It encompasses both live action and animation and includes all analogue and digital formats.

While many moving image archives also have audio materials in their collections, this manual does not offer detailed guidance for describing audio media.
However, the Manual does provide ways to describe physical and technical characteristics of analogue and digital audio Items to assist with collection and preservation management.

\subsubsection[Use]{Use 
    \label{sec:use}
    } 

Instead of defining levels of cataloguing, this manual outlines core elements for moving image description.
The core elements provide the basis for identification of a resource and for facilitating the exchange of data from one system to another.
These are not “core” elements in the sense of a Dublin Core, EBUCore, or PBCore schema, but are rather intended to illustrate common elements that are used in describing moving images and are referenced in the rules outlined in this manual.
The elements are largely drawn from EN 15744 and 15907.
For a comparison of elements described in this Manual and EN 15907, please see [Appendix G, Elements of Description comparison](#manual-G).

This manual also provides a list of all the data elements associated with the entities described.
Thus, this approach provides a framework for the minimum and maximum amount of descriptive information allowed in a range of moving image cataloguing activities existing in a large variety of environments.

Institutions are encouraged to include as many of the non-core elements as goals and circumstances permit.
None are considered mandatory by these guidelines, but an institution may require that some are mandatory for internal purposes.

\subsection[Core elements of description]{Core elements of description 
    \footnote {Adapted from CEN TC 372 EN 15744 element set} 
    \label{sec:core_elements_of_description}
    } 

These core points of description are listed with their corresponding terms as presented in the manual.
They represent an ideal minimum set of metadata for moving image cataloguing.

| CORE CONCEPT | TOP-LEVEL ELEMENT | SUB-ELEMENT|
| -- | -- | -- |
|Title | 1.3.2 Title [Work] | -- |
| Series / Serial^[EN15744 definitions “A series is a group of separate items related to one another by the fact that each item bears, in addition to its own title, a collective title applying to the group as a whole. A serial is a type of “short subject” work which is characterized principally by the episodic development of a story”. This Core Concept is referencing the name of another Work that a Work may be “part of”, where the latter has been conceived within the context/intention of being an element of a Series or Serial. It is not being used here as a Work/Variant Description Type. (See D.1 Work/Variant Description Types)] | 1.3.2 Title [Work] | 1.3.2.1 Title Type = Series/Serial [Work] |
| Cast | 1.4.1 Agents (e.g. Cast, Credits, Person, Organisation, etc.) [Work] | 1.4.1.1 Agent Activity = Cast [Work] |
| Credits (including Production Companies) | 1.4.1 Agents [Work] | 1.4.1.1 Agent Activity = Credit (use term for actual role) [Work] |
| Country of Reference | 1.3.3 Country of reference [Work] | |
| *Original Format | 2.3.4 Format of a moving image Manifestation [Manifestation] | 2.3.4.1.2 Specific Carrier Type: [Manifestation] |
| *Original Length | 2.3.5 Extent of a Manifestation [Manifestation] | 2.3.5.2 Physical extent of a Manifestation |
| *Original Duration | 2.3.5 Extent of a Manifestation [Manifestation] | 2.3.5.3 Duration of a Manifestation |
| *Original Language | 1.3.5 Language(s) [Work] | 1.3.5.1 Language Term + 1.3.5.2 Usage type [Work] |
| Year of Reference | 1.3.4 Year/Date of reference [Work] | 1.3.4.1 Date Type [Work] |
| Identifier | As appropriate: 1.3.1 Work/Variant Identifier [Work/Variant] &/OR 2.3.1 Identifier [Manifestation] &/OR 3.1.1 Identifier [Item] | As appropriate: 1.3.1.1 Identifier Type [Work/Variant] &/OR 2.3.1.1 Identifier Type [Manifestation] &/OR 3.1.1.1 Identifier Type [Item] |
| Subject/Genre/Form^[Form = Fiction, Non-fiction, etc. Some institutions may incorporate these as a genre term, whilst others may have them as a separate category to genre.] | 1.4.3 Subject/Genre/Form terms [Work] | |
| Content Description | 1.3.6 Content description (synopses, shotlists, etc) | |

The concept of “original” in this manual indicates the first known manifestation of the Work, which is not determined by its release status.
The concept of “original” must be flexible enough to be applied to released and unreleased Works.
For a released Work, we tend to refer to the “original” Work as the first known release of the first known manifestation.
For Works that are not released (e.g., a home movie), the “original” Work is simply the first known manifestation.

See [Appendix I.1 Example 1. Feature film in 3-level, 2-level and 1-level hierarchies](#manual-I.1) as an illustration.

Please see [Appendix G, Elements of Description](#manual-G) comparison for a list of all elements described in this manual.

NOTE: For exchanging data, indicating the origin of the record is important (i.e., name of the institution supplying the record).
This data is typically located in a dedicated field at the Work level and automatically generated by electronic systems.
This corresponds to CEN EN 15907, 6.2 – Record Source.

\subsection[Elements of description across Works, Variants, Manifestations, and Items]{Elements of description across Works, Variants, Manifestations, and Items 
    \label{sec:elements_of_description}
    } 

This section includes sample structures for how the elements can be applied across Works, Variants, Manifestations, and Items.
Four models are provided, beginning with the more complete four-level model and ending with a simple one-level model.
Models should be applied according to an institution’s system and also determined by the amount of information known about an Item.

The full list of elements of description for each entity is set out in the following charts and diagrams, and in Chapters 1-3.
See Appendix I, Examples of records containing core elements in the different levels of hierarchy for examples of real records which contain these core elements (as well as others) across the hierarchies.

TODO insert new diagrams here

**Work/Manifestation/Item.
Properties expressed in one record, with abstracts, contextual and object data stored in a single level hierarchy Distribution of the elements of description according to the four entities order**

| Properties | (Work) | (Manifestation) | (Item) |
| -- | -- | -- | -- |
| Titles | Uniform, Preferred, Other Title information, Alternative, Supplied/Devised | Title proper | Title proper |
| Part | Monographic, Analytic, Serial, Collection | | |
| Content | Categories: fiction/non fiction; genre, synopsis, subject, etc. | | |
| Dates/Events | Creation, Production, Censorship, Copyright | Release, manufacture, transmission, distribution, etc. | Object creation, acquisition, accession, de-accession, loan, transport, etc. |
| Agents | Cast, credits, rights holders, creator, etc. | Distributor, broadcaster, publisher | Donor, Archive/archivist, technician, restorer, etc. |
| Rights context | Copyright holder and date | Platforms, territories, dates. Agents (distributors, license holder) | Transfer of ownership |
| Event types | Awards Censorship Production IPR registration | Pre-release, theatrical, non-theatrical, transmission, home viewing, internet, not for release, censorship etc. | Acquisition Reproductions Disposal |
| Format general | | 35mm film, digital cinema, blu ray, etc. | |
| Format specific | | | 16mm film pos, 35mm lavender separation, ProRes422 HQ, etc. |
| Condition report | | | Pristine, not for projection, heavy scratches, etc. |
| Storage location | | | Home location, current location, previous location || 
| Conservation recommendations | | | Urgent transfer required, relocate sub-zero, etc. |

\subsection[Sources of Information]{Sources of Information
    \label{sec:sources_of_information}
    } 

Information entered in a record must be derived from a source.
Acceptable sources of information for moving image Works, Variants, Manifestations and Items include primary and secondary sources.

Primary sources include information on the actual Item itself.
For example, for film materials, titles and main production credits are transcribed from the frames usually in the opening credits.
Secondary sources include information written on containers and reference materials.

Although primary sources are generally preferred, this manual allows for the use of secondary sources no matter the entity, attribute or relationship described in recognition that there may be constraints on the amount of research or viewing a cataloguer can do.

Whether information is taken from primary and/or secondary sources as listed in the following, indicate that fact either by means of a note or by some other means (e.g., through coding or the use of square brackets, specific fields, or links to other databases).^[Based on RDA 2.2.4 Other Sources of Information] Add the source of the information in a Note field and include the element name.
Cite each individual source of information using an agreed upon, consistently applied citation style, such as The Chicago Manual of Style, or other style guide.

Primary source information can be derived from:

a) the title frame(s) or title screen(s)^[RDA 2.20.2.3 Title Source]

b) embedded metadata in textual form that contains a title (e.g., metadata embedded in an MPEG video file)^[Ibid.]

c) an eye-readable label bearing a title that is permanently printed on or affixed to the resource (excluding accompanying textual material or a container)^[Adapted from RDA 2.2.2.3 Resources Consisting of Moving Images]

d) accompanying material or a container issued as part of the resource itself^[Based on RDA 2.2.4 Other Sources of Information]

e) a container that is not issued as part of the resource itself (e.g., a box, case made by the owner)^[RDA 2.2.4 Other Sources of Information]

f) other published descriptions of the resource ^[Ibid.]

g) any other available source (e.g., a reference source)^[Ibid.]

Examples:

```{=latex}
\begin{tcolorbox}
Credit information derived from: \\
AFI Catalog of Feature Films: 1930-1939.
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Title derived from film opening credits.
\end{tcolorbox}
```

\subsection[Display issues]{Display issues
    \label{sec:display_issues}
    } 

Although these guidelines are primarily focused on content, many users may also welcome some guidance in data presentation.
Section 0.4 gathers some of the common display questions with recommendations.

\subsubsection[Punctuation]{Punctuation
    \label{sec:punctuation}
    } 

These guidelines do not mandate the use of any particular data presentation standard, such as ISBD punctuation.
However, ISBD punctuation is recommended if punctuation guidance is desired.
Please consult ISBD^[[http://www.ifla.org/files/assets/cataloguing/isbd/isbd-cons_20110321.pdf](http://www.ifla.org/files/assets/cataloguing/isbd/isbd-cons_20110321.pdf)] for general guidance and examples, or the FIAF Cataloguing Rules for Film Archives (1991)^[[http://www.fiafnet.org/~fiafnet/uk/publications/fep_cataloguingRules.html](http://www.fiafnet.org/~fiafnet/uk/publications/fep_cataloguingRules.html)].

These guidelines do advocate consistent usage where punctuation is needed as a cataloguing construction, for example, to separate Form elements in the creation of Partially or Fully Supplied/Devised Titles e.g.

Example:

```{=latex}
\begin{tcolorbox}
Jaws. Rushes
\end{tcolorbox}
```

For transcribed elements, record punctuation as found.
For all other elements, record punctuation as found on the source(s) of information.

\subsubsection[Capitalisation and Articles]{Capitalisation and Articles
    \label{sec:capitalisation_and_articles}
    } 

Some institutions render Work titles in capitals – all upper-case – as a simple typographical method of identifying these key items of information, while others only capitalise the first letter of a title, in accordance with ISBD.
Either usage is permitted by these guidelines, although institutions may prefer to retain the conventional practice of capitalising only the first letter of a title and any proper names as dictated by the usage of the language in which the information is given.

Users should recognise that using all capitals may create problems in the future when reformatting to mixed case if preferred in a new system, or when reformatting to mixed caps for display in a web platform where mixed caps is increasingly preferred.
Although it is possible to automate the conversion of upper case to mixed caps, that automation cannot easily manage linguistic complexities or semantic rules and exceptions such as proper nouns, or place names.
Therefore, it is recommended that an institution transition to ISBD capitalisation when and where possible.

When an “all capitals” practice is followed, institutions have the additional option of reducing to lower case words which are of minor importance to the substantive title (for filing purposes, etc.), such as sub-titles, a definite or indefinite article appearing as the first word of a title, etc. Experience has shown that this practice can make it easier for staff in institutions handling multi-lingual material to recognise, for filing purposes and interpretation, the different significance of words that are articles in one language but not in others.

While the guidelines permit both cases, it is recommended where permitted now or in the future, to use the conventional practice of capitalising only the first letter of a title and other letters as dictated by the usage of the language in which the information is given.
Leading articles should ideally be placed in separate fields in keeping with the way systems are being developed for alphabetical sorting.
Alternatively some systems (for example, those containing MARC21 records) indicate the number of non-filing characters to skip in alphabetization.

Examples:

```{=latex}
\begin{tcolorbox}
Alternative practices | ISBD practice:   \\ 
Die Hard | Die hard    \\
Die DREIGROSCHENOPER | Die Dreigroschenoper    \\
LES PATTERSON SAVES THE WORLD | Les Patterson saves the world     \\
Les MISERABLES | Les miserables    \\
American in Paris, An | An American in Paris 
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
MARC21 tag example:\\
245 03 An American in Paris
\end{tcolorbox}
```

\subsection[Language and script of the description]{Language and script of the description
    \label{sec:language_and_script_of_the_description}
    } 

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

Example:

```{=latex}
\begin{tcolorbox}
Original Chinese Title: 精武英雄    \\
Transliterated Pinyin Title: Jīng wǔ yīngxióng    \\
English Translated Title: Fist of Legend 
\end{tcolorbox}
```

\subsection[Abbreviations]{Abbreviations 
    \label{sec:abbreviations}
    } 

For transcribed data elements, transcribe abbreviations as found.
For all other elements, generally do not abbreviate words.
Optionally, additional non-preferred title types may also be added to assist in user searching and accessibility (see [Appendix A, Titles and Title Types](#manual-A)).

\subsection[Examples]{Examples 
    \label{sec:examples}
    } 

The examples given throughout the guidelines are illustrative and not prescriptive (unless stated otherwise).
They follow The Chicago manual of style^[University of Chicago. 2003. The Chicago manual of style. Chicago, Ill: University of Chicago Press.] for the sake of consistency.
They are intended to illuminate the provisions of the guidelines to which they are attached, rather than to extend those provisions.
Therefore, neither the examples nor the form in which they are presented should be taken as instructions, unless the accompanying text specifically states that they should.
Most examples are from actual titles; in the few made-up examples an attempt has been made to formulate realistic data.
Examples of complete entries may be found in [Appendix I, Examples of records containing core elements in the different levels of hierarchy](#manual-I).
Examples of the elements of description in different data structures are shown in [Appendix G, Elements of Description comparison](#manual-G).
The bibliography follows ISO 690.

\subsection[Errors]{Errors 
    \label{sec:errors}
    } 

As these guidelines recognise the importance of researched information in the catalogue entry, unintentional errors or inaccuracies from the Item should not be reproduced at the Work or Variant levels.

Begin with what the source of information says and correct it only when it is known to be ambiguous or erroneous.
Correction must be done in such a way that the resource remains recognisable to the users unaware of the error.^[YCR, Principle 3, p.4.] For example, AACR2 recommends transcribing the error followed by “sic” and sometimes the correct text in square brackets.

Example:

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

In RDA, the title is provided as transcribed without a recognition of the misspelling, with the correct title added in a secondary set of Title and Title Type fields (see [A.2.4.1 Alternative title types](#manual-A.2.4.1)) and a Note explaining the misspelling.

Example:

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

Example:

```{=latex}
\begin{tcolorbox}
Title (Work): Inglorious Basterds
\end{tcolorbox}
```

\subsection[Alternatives and options]{Alternatives and options 
    \label{sec:alternatives_and_options}
    } 

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

