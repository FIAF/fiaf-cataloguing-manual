
\newpage
\section{Moving Image Variants} 
\label{sec:variant_moving_image_variants}
 
\subsection[Definitions]{Definitions 
\footnote {For a discussion of other definitions of the “Work” and Variant entities, see \nameref{sec:moving_image_works}.}} 
\label{sec:moving_image_variants_definition}

Brief definitions of the standard CEN terms Work/Variant/Manifestation/Item used in the Manual were provided at the end of the Introduction (see \nameref{sec:introduction}).
This section provides an in-depth definition of the term Variant.

\subsubsection[Moving Image Variant]{Moving Image Variant 
\footnote {Adapted from EN 15907, 4.2 Variant.}} 
\label{sec:moving_image_variant}
    
A moving image Variant is an entity that may be used to indicate any change to content-related characteristics that do not significantly change the overall content of a Work as a whole.
Such Variants can be produced by minor additions, deletions or substitutions to the content.
As a general guideline, changes that would result in a different content description should be treated as a separate Work rather than a Variant, particularly regarding EN 15907 standard.

Changes that could be described as Variants are detailed in \nameref{sec:boundaries_between_works_and_variants}, and may include the addition of subtitles, dubbing, and editing as a result of censorship or adjustment of duration, e.g. for TV programming.
For institutions that have made a policy decision not to use the Variant, these changes may constitute Manifestation differences.

The determination of a Variant requires human analysis, and as such is an interpretative practice.
It is not always easy to establish what the Variants may be.
For example, an institution may have a television recording of a motion picture broadcast but no way of comparing it with an original theatrical copy as to whether it has been altered in terms of subtle censorship of content or duration

**Therefore, this entity is optional.** If employed, each instance of a Variant is related to a Work and can have one-to-many relationships with instances of Manifestation(s), and many-to-many relationships with Event(s), Agent(s) and Other Relation(s). If no Variant of a Work exists or is known to exist, then this entity can be omitted, connecting an instance of a Work with one or more instances of Manifestation. The above is the case under EN 15907, but please note that the Variant (aka Expression) is an integral part of the data architecture of IFLA Library Reference Model (LRM), so if the latter standard is being used in your institution then use of Variants (Expressions) would be expected.

\subsection{Attributes of a Variant} 
\label{sec:attributes_of_a_variant}

\subsubsection[Variant Type]{Variant Type
\footnote {YCR, 2.1.1 Nature of modification (change in content) of expression}} 
\label{sec:appendix_variant_type}
     
Identify and describe the kind of change from a Work that gives rise to any instance(s) of a Variant. Selection should be made from a controlled list of values, for example:

* Censored
* Dubbed
* Subtitled
* Abridged/Condensed (e.g. for television)
* Augmented (where additional content is added, such as director’s cuts with restored scenes, or alternate endings, commentaries)
* Preservation/Restoration
* Different sound track
* Sonorized
* Colourized
* Black and white copy of work originally issued in colour

A change in colour, which is a physical property, expresses a different Manifestation according to the data model this manual follows. However, it is recognised that in practice, institutions who employ the Variant entity may consider changes to colour to provoke the creation of a Variant because the colourisation of a black and white Work represents a fundamental change to the visual aspects of the original Work.

\subsection{Elements of a Variant} 
\label{sec:elements_of_a_variant}

This section describes the metadata elements that can be used to describe a Variant.
It is up to each institution to choose which elements are most applicable to describe their collections and according to what their system can support.

This Manual recommends using the qualifier “Type” for several core elements if an institution’s system can support it.
In these cases, “Type” is used to define the source, function or purpose of the value entered in the main element.
Using a “Type” qualifier conforms to its use in Dublin Core and other Dublin Core-influenced standards such as EBUCore and PBCore.
Examples of using “Type” include the Identifier, Title, Date, and Description elements.

\subsubsection{Variant Identifier} 
\label{sec:variant_identifier} 

Create an unambiguous reference to the Variant using a unique identifier and indicate the type of identifier.
The identifier should be a numerical or alphanumerical reference.
This identifier is for the content of the Work, not for a specific Item.
Work, Manifestations and Items have their own Identifiers, discussed in other sections.
This Work Identifier is shared by all Variants, Manifestations and Items associated to the Work.

In a way, a unique Variant Identifier can have more value than a Variant’s Title.
Titles can confuse through different spellings, translations, and are not unique (i.e., King Kong).
An Identifier refers to a specific Variant and provides clear disambiguation between Works and Variants when there is confusion.

There can be more than one Variant unique identifier for the content.
This commonly occurs when institutions have content assigned identifiers by various standards or distribution agencies (ISAN, EIDR), or a government or other official body in the archive’s country has assigned an identifier to the work.
An institution will likely have its own internal Identifier as well, often auto-generated by an institution’s information or asset management system.

\subsubsection{Title}
\label{sec:work_title}
     
Record the title, an identifying phrase, or name for a Variant of applicable.
If your institution is applying the use of “Type” qualifiers, use “Title Type” to state the function of a particular title (see \nameref{sec:work_title_type} and \nameref{sec:titles_and_title_types}).

Ideally, the record should at a minimum contain the “preferred title” (also referred to as “main” or “original” title) of the Work.
It may differ from the title found on a particular manifestation of the Work; the actual title on the Manifestation is noted in the Manifestation Title element (see \nameref{sec:manifest_title}).
See \nameref{sec:title_types} for additional information.

This may be via use of a “Title type” qualifier.
See \nameref{sec:titles_of_series_serials} for other options

```{=latex}
\begin{tcolorbox}
Gone with the wind (United States of America, 1939, Victor Fleming) \\
Gone with the wind – Preferred Title of the Work \\
Via col vento – Variant title – Dubbed (Italian) \\
Gejaagd door de win – Variant title – Dubbed (Dutch) \\
Autant en emporte le vent – Variant title – Dubbed – (French) \\
風と共に去りぬ – Variant title – Dubbed (Japanese)    
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Аленький цветочек (USSR, 1952, Lev Atamanov) \\
Аленький цветочек – Title of the Work \\
Alenkiy tsvetochek: Alternative (transliterated) title of Work/ Variant (Preferred title if systems don’t use Cyrillic) \\
Feuerrotes Blümchen – Variant title – Dubbed (German) \\
The Scarlet Flower – Variant title – Dubbed (English)   
\end{tcolorbox}
```

\subsubsection{Country of Reference}
\label{sec:country_of_reference} 

Where known and applicable, record the geographic origin of the Variant.
This should be the country or countries where the principal offices or production facilities of the production company or companies are located.^[EN 15907, 6.5 Country of Reference, p. 19] 
Where an official national certificate or designation of a Work exists, use this as the authoritative source, e.g., Italian government department designates what is officially an Italian film.^[The certification of “Italian nationality” is provided by the law/decree 2004, n. 28, part. 5 (but already provided in the former law 1213/1965). 
According to the 2004 law, the biggest part of the cast and crew, the locations, and the technical facilities have to be Italian, and 30% of the budget has to be spent in Italy. There is a number of exceptions for artistic reasons and in case of co-productions.]
When more than one place is associated with a Work/Variant, choose the place(s) with primary importance.

For institutions who need or require specific ordering of country of reference then the following options are possible examples of how this may be achieved.^[The first of these was the formula followed by the British Film Institute. BFI CID Stylistics Manual – 2nd Edition. A.8.1., which subsequently changed to using a country of reference ordering based more on the on-screen ordering of production companies. CID Cataloguing Manual|Moving Image Catalogue (revised 2022). F.4 and F.4.1.]

If the Work is a multi-national production, the countries added to the record should be in order of financial involvement.
For example, an Austrian/Italian/French co-production where the Austrian production company/sponsors financed 60%, the Italian 25% and the French 15% then the order of the countries would be: Austria, Italy, France.

If it is not possible to establish clearly the financial percentages of each country’s involvement, then consider the nationality of the director of the title and/or the majority of personnel involved with the film and select that as being the main country of origin of the film.

If the production company has branches in more than one country, choose the one responsible for the production of the work.

If the Work is a multi-national production, with production company branches in multiple countries, and it is not clear which particular one was involved, then choose the predominant production company if known.

Alternatively, since it is often impossible for a cataloguer to determine with any level of accuracy the precise percentages of financial involvement of companies, assign country of origin based on the nationality of the production companies in the order that they appear on screen (for example,  copyright companies followed by production and then ‘presents’ companies). Look at which companies are named on the screen as copyright holders, production companies, and 'presents' companies, with all the attendant credits for production companies such as ‘In association with’, ‘With the participation of’, ‘Supported by’, and add the countries in which these companies are based as country of references for the Work, starting with that of the primary production company.

It is recognised that countries can lay out their credits differently, sometimes with less important companies listed first, or with a 'presents' credit as the only credit of the major production companies.

If the production company has branches in more than one country, choose the production country of the actual branch responsible for the production of the work. If the Work is a multi-national production, with a production company with branches in multiple countries and it is unclear which branch was involved, choose the predominant production company if known.

An institution should compile its own rules for ordering of country of reference depending on its preferred practice or needs.

Record the country of origin using the full form of the country name, e.g. United Kingdom rather than UK, by taking the most suitable value(s) from a controlled list. This can be an in-house list but the use of a standard list such as ISO 3166^[http://www.iso.org/iso/home/standards/country_codes.htm] is preferable. If ISO is used, apply the English Short Name that is associated to a code. Optionally, record the country code as found in ISO 3166-1-alpha 2.

If the country name has changed, record the name of the country as it was at the time of production, e.g., Czechoslovakia for a Work/Variant produced in 1970, but Czech Republic or Slovakia for one from 2012.^[ISO 3166-3 Codes for the representation of names of countries and their subdivisions -- Part 3: Code for formerly used names of countries, is available for purchase as a PDF on the ISO website: [http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=2130](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=2130)]

\subsubsection{Year/Date of Reference}
\label{sec:year_date_of_reference} 

A year or fuller date (e.g., day/month/year) is essential to identifying a moving image Work and, where applicable, its Variants.
A common use of year/date is chronological ordering of lists of Works and their Variants.^[EN 15907, 6.6 Year of Reference, p. 20] 
As explained below, these guidelines recommend, where possible, applying two qualifiers to a Date element: Date Type, and Date Precision.

There is no primary or “preferred” year or date except within the context of the type of Work and, where applicable, its Variants.
That is, typically, an original date of release or broadcast is essential for identifying a moving image Work and its Variants.
In the absence of a release or broadcast date, provide a year of creation or production.

Record any dates associated with the Work or its Variants formatted according to [ISO 8601](https://www.iso.org/standard/40874.html) or other available resources, such as [EDTF](https://www.loc.gov/standards/datetime/) (Extended Date Time Format).
ISO 8601 prescribes that dates should be formatted hierarchically as Year-Month-Day, using this convention: YYYY-MM-DD.
Example: 2015-07-04.
This structure eliminates confusion when dates can be formatted with month before day or day before month (e.g., 07/04/2015 or 04/7/2015).
Using the ISO format makes indexing and sorting more efficient.
Using words (June 11, 2004), while perhaps user-friendly in its narrative construction, are difficult to index as dates.
Mixing date formats causes confusion in data retrieval and for users!

Where full dates are not known use Year-Month YYYY-MM or just Year YYYY, as systems permit.

\paragraph{Date Type}
\label{sec:date_type} \

The year or date should be associated with an event in the life cycle of the Work or its Variants (see \nameref{sec:work_events}).
If your system supports it, apply a “Date Type” qualifier to make the date or year purpose clear.
Date Type terms should be derived from a controlled vocabulary.
For a list of initial terms, see \nameref{sec:event_type}.

For Works and Variants, the date is typically related to events such as its creation, availability (i.e. publication, release, distribution, broadcast or transmission) or registration (e.g. for copyright or intellectual property purposes), or bestowal of an award. 

More than one year or date may be associated with a Work or its Variants.
For example, in the case of a Work comprising segments produced in different years (for example, a home movie); list the years, if known, e.g., 1955, 1956, 1959.^[Irish Film Archive, p. 13.]

Similarly, a Work may have a production date of 1962, a copyright date of December 1963, and a first release date of January 1964.
Apply the Date Type qualifier to clarify the purpose of each date.

\paragraph{Date Precision}
\label{sec:date_precision} \

Where possible, provide a “Date Precision” qualifier to note if the date is precise, approximate, estimated, or a range.
EDTF also provides codes to denote precision.
For example, an uncertain or approximate date may be formatted thus: 2004-06~-11 (year and month are approximate; day known).
Using a Date Precision qualifier, this Date entry could be entered as:

Date: 2004-06-11    
Date Type: Creation    
Date Precision: Approximate

An institution may choose to use a precision qualifier for imprecise dates.

If ISO formatting and/or the Date Precision qualifier are not applied, then use consistent terms and formatting to note date approximations.^[FIAF, 3.5.4, p. 64]:

*One year or the other*

```{=latex}
\begin{tcolorbox}
1971 or 1972
\end{tcolorbox}
```

*Probable Year (with qualifying note to indicate date is probably 1969)*

```{=latex}
\begin{tcolorbox}
{[1969?]} \\
1969? \\
Circa 1969
\end{tcolorbox}
```

*Approximate Year*

```{=latex}
\begin{tcolorbox}
{[Circa 1960]} \\
Circa 1960 \\
1960 circa
\end{tcolorbox}
```

*Decade Certain*

```{=latex}
\begin{tcolorbox}
191- \\
Decade 1910 \\
1910 decade
\end{tcolorbox}
```

*Probable Decade (with qualifying note to indicate that date is probable decade date)*

```{=latex}
\begin{tcolorbox}
{[191-?]} \\
1910 decade \\
Decade 1910 
\end{tcolorbox}
```

*Use for time spans, the outside limits of which can be precisely determined*

```{=latex}
\begin{tcolorbox}
between 1906 and 1912
\end{tcolorbox}
```

*Where system has date start/ date end functionality*

```{=latex}
\begin{tcolorbox}
1906 1912
\end{tcolorbox}
```

In instances such as these, a note should be given which further explains the Date.

```{=latex}
\begin{tcolorbox}
{[Personal record. Eugene Meyer family. Family camping trip through the Canadian Rockies]}. -- US, 1926. \\
{[Note]} Year from notes accompanying item, attached to inventory, and from Merlo Pusey’s Eugene Meyer, (New York: Knopf, 1974), p.195
\end{tcolorbox}
```

\subsubsection{Language(s)}
\label{sec:languages}

A moving image Work is conceived and presented in a particular language or set of languages.
Changes to the original language(s), as in the case of dubbing, are considered minor changes and can constitute a Variant of a moving image Work.

Alternatively, such minor changes can constitute a new Manifestation of a moving image Work rather than a Variant.
Institutions using cataloguing structures that do not distinguish Variant level information (for example, those that create records primarily at the Manifestation level), should apply this alternative.
(See guidelines for language in a Manifestation: \nameref{sec:manifest_language})

Indicate the language(s) (e.g., Italian) and usage(s) (e.g., Italian intertitles) in which the moving image Variant/Manifestation is written, spoken or sung, if applicable.
More than one language can occur in different forms, depending on how the content is expressed (e.g., French dialogue and English subtitles).

\paragraph{Language Term}
\label{sec:language_term} \

Record the language(s) by taking the most suitable value(s) from a controlled list of languages.

This can be an in-house list but it is preferable to use a standard language list such as the ISO 639 codes, including ISO 639-2, 693-3 and 639-5 (http://www.loc.gov/standards/iso639-2/langhome.html).

Optionally, record the language code as found in ISO 639, where allowable.

If no language can be determined, the information can be omitted or indicated by a value of “unknown”.

\paragraph{Usage Type}
\label{sec:work_usage_type} \

Record the usage type of a language (e.g. spoken, intertitles, subtitles, etc.) by taking the most suitable term from a controlled list elaborated in-house or referring to an existing authoritative list. See \nameref{sec:language_usage_types}. [ADD LINK TO SAME LANGUAGE USAGE SECTION WITH LIST IN WORKS]

Optionally, record language usage type at the Manifestation/Item level (see \nameref{sec:manifest_language}).
A value of “original” can be added to the Language element here to indicate that statements made about the language(s) for a particular Manifestation/Item are indicative of the language(s) of the “original” Work. ^[The indication of “original” values at the Manifestation level follows EN 15907 attributes of a Manifestation, pp. 10-11]

\subsubsection[Content description (synopses, shotlists, etc)]{Content description (synopses, shotlists, etc) 
\footnote {Adapted from YCR, 1.2.16 Summary of genre, form, and subject matter of work, p. 38.}}
\label{sec:content_description} 

Write a concise, objective, non-critical summary of the content of the moving image Work and/or Variant.
Content descriptions can be synposes, brief TV guide-like one sentence description, shotlists, etc. There can be more than one type of content description in the record, e.g. it is possible to have both a shotlist and a synopsis.

The content description should be written in a style that is easy to read.
It should not include technical terms, abbreviations, or allusions significant to a specialist audience.
Avoid slang expressions and colloquialisms fashionable at the time of writing,and, where several cataloguers are viewing independently, they should, ideally, try to achieve a common written style.
Descriptions should be objective and not include subjective commentary on the quality of the content.
If acceptable summaries are already available in secondary sources, cataloguers may use these, instead of taking the time to prepare summaries of their own. If using summaries exactly as written, put the summary in quotes and note the source of the summary.^[FIAF 7.2.12. Summary]

```{=latex}
\begin{tcolorbox}
An historical drama set in 16th century England in which King Henry VIII divorces his wife, Catherine of Aragon, and marries Anne Boleyn, a former lady-in-waiting, who is in love with Sir Thomas Wyatt. After several years, Henry becomes infatuated with Lady Jane Seymour and arranges to have the innocent Anne found in a compromising situation with Sir Thomas. Anne is tried for infidelity, found guilty, and executed.
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Donald Graham, millionaire ex-convict, plans revenge on society figure John Cabin Brand, whom he blames for the death of his daughter.
\end{tcolorbox}
```

A content description may also be a shotlist or listing of the contents of an aggregate Work/Variant (see \nameref{sec:aggregates_compilations_multi_component_productions}). Shotlists are the ideal content description to have or aim to have, particularly for non-fiction moving images, but it is recognised that resources and accessibility mean this is not always possible or practical for an archive or institution.

```{=latex}
\begin{tcolorbox}
Title: Pathe News {[Excerpts No. 6]} \\
Contents: “Newest U.S. Submarine Goes into Commission,” Pathe News No. 60 {[1921]} (160 ft.) -- “Span of New Memorial Bridge to Connect N.H. and Maine,” Pathe News No. 57 {[1923]} (72 ft.) -- “Celebrate 300th Anniversary of Settling of Portsmouth,”Pathe News No. 69 {[1923]} (99 ft.) -- “World’s Largest Sub Takes First Plunge,” Pathe News No. 93 {[1927]}, (c) 21Nov27; MP4478 (134 ft.) -- “New Memorial Bridge between N.H. and Maine!” Pathe News No. 70 {[1923]} (105 ft.) -- “Launch Largest Submarine Cruiser,” Pathe Sound News No. 1 {[1930]}, (c) 29Dec29; MP1025 (80 ft.).
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Title: Victorian Cinema: 4: Bamforth/Riley/Hepworth \\
Contents: \\
Weary Willie (1898) (78ft), \\
Catching the Milk Thief (1899) (140ft) \\
The Tramp and the Baby’s Bottle (1899) (214ft), \\
Women’s Rights (1899) (289ft), \\
A Kiss in the Tunnel (1899) (367ft), \\
Boy’s Cricket Match and Fight (1900) (475ft), \\
{[… real example shortened]} \\
End
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
Title: Magnificent Reproductions of the Great Yorkshire Show in Bradford (1901) \\ \\
Mitchell \& Kenyon 641: Panning shot across a road to the Yorkshire Agricultural Society building with a diffuse crowd of people in front of the building. As the shot passes the building, a number of people can be seen sitting down, including mothers with babies and some older people (00.36). Cut to a close-up shot of the building, with a sign reading “The Yorkshire Agricultural Society. Established 1837” (00.45). Cut to a horse-drawn cart spraying some sort of liquid on the path as it moves along. Lettering on the back of the cart reads “Bradford City Council no. 30” (00.58). Cut to wide steps, with a number of smartly dressed men walking down them (presumably entering the show) (01.14). Cut to a shot of the blades of a windmill as they turn (01.23). Cut to a general shot of the show, with crowds and various stalls (02.07). A marquee in the background has the sign “R. Hornsby \& Sons Ltd., Grantham”. Another sign reads “Marshall. Sons \& Co.”. Chimneys and houses can be seen in the background (02.27min).
\end{tcolorbox}
```

The content description can be based on a viewing of the work, accompanying documentation, or secondary sources, but the source should be clearly noted.

For unedited Works, where time and resources permit, each scene should be summarized.
If there are shots of particular significance or interest – of, for example, prominent people or places – these should be recorded.
Otherwise a general description of scenes and sequences will suffice^[Irish Film Archive, p. 23.].

If applicable, add information about the content of the moving image Variant where it differs from the content of the Work.

\paragraph{Content Description Type} 
\label{sec:content_description_type} \

Include a qualifying keyword or otherwise denote the type of summary (e.g. Synopsis, Shotlist, Review).^[EN 15907, 6.17.3 Elements, Description type, p. 30.]

\subsubsection{Notes}
\label{sec:notes}

Notes for moving image Works/Variants are annotations providing additional information or clarification relating specifically to Works/Variants attributes and relationships.^[Based on RDA 2.20.1.Basic Instructions on Making Notes on Manifestations or Items] See \nameref{sec:cataloguers_notes}.

\subsubsection{History}
\label{sec:history}

Record historical information about events of interest in the creation of the original moving image Work/Variant that is of value for your users, such as censorship history, production versions, and the like.
This historical information may be recorded in association with instances of Events or Agents.

If desired, institutions may include historical information that crosses over into being about the Manifestation(s) and/or Item(s).
This may be done where there is value to the user in keeping all the information together for research or clarification purposes rather than across disparate Manifestation and Item records.
This may also be applied where no History fields exist in an institution’s system at Manifestation or Item levels, or a no hierarchy one level structure is used.

```{=latex}
\begin{tcolorbox}
Christopher Columbus (United Kingdom, 1949, David MacDonald) \\
There are three documented versions. Version one: which has the shortened reels 3A and 3B; Version two: which has the shorter ending; Version three: which has the long ending (this script is based on the full length reels 3A and 3B and on the short ending, as this is the export version.
The short ending (version two) has Columbus reinstated by the King and Queen, him leaving their presence and telling Juana he will be remembered longer than the monarchs as he walks down a corridor. The longer version (version three) has a more American feel with two sailors informing Columbus of the great nation his discovery will give rise to, complete with quotes from Jefferson, Lincoln and Roosevelt.
\end{tcolorbox}
```

\paragraph{Custodial History}
\label{sec:custodial_history} \

If desired, write a brief custodial history of the Work/Variant if known, particularly for rare and unique materials.
Indicate the current holding institution of the original or master material if known.

Information on the provenance of the specific Items in an archive’s collection should be included in the Item sections.

\paragraph{Censorship History}
\label{sec:censorship_history} \

Document information related to the censorship history of a Work/Variant, including:^[EN 15907, 6.13 Decision event, pp. 26-27.]

*Any events in which a Manifestation/Item of a Work/Variant was evaluated by a censorship body or an accredited rating agency.* 

*The geographic region for which the verdict is (was) valid.*

*Any identifier issued by the agency uniquely identifying the act of rating or censorship and associated documents such as censorship visa or rating certificates.*

*The outcome of the act of rating or censorship.*

```{=latex}
\begin{tcolorbox}
À bout de souffle (France, 1960, Jean-Luc Godard) \\
\\
In Italy, this film has three different theatrical distributions, corresponding to three different visas (“visto di censura”) from the official censorship body (Ufficio di revisione cinematografica). \\
Censored Variant: Theatrical distribution in Italy – censorship visa n. 32329 – date: 1960-07-05 – Length 2463m – original French – not for under 16 years \\
Dubbed, Censored Variant: Theatrical distribution in Italy – censorship visa n. 57609 – date: 1971-01-23 – Length 2440m. – Italian \\
Dubbed, Censored Variant: Theatrical distribution in Italy– censorship visa n. 64662 – date: 1974-05-20 – Length 2430m. – Italian dubbed
\end{tcolorbox}
```

\paragraph{Other Work/Variant History}
\label{sec:other_work_variant_history} \

Any other relevant information or clarifications pertaining to the Work/Variant.

*Any changes of director, crew, or cast part-way through production.*

```{=latex}
\begin{tcolorbox}
Tosca (Italy, 1939, Karl Koch) The film was started by Jean Renoir, but after beginning, Renoir escaped to France because of World War II. The film was completed by his assistant Karl Koch, with Luchino Visconti as assistant.
\end{tcolorbox}
```

*Any demise of members of the cast or crew associated with the production.*

```{=latex}
\begin{tcolorbox}
Foolish Wives (United States of America, 1922, Erich von Stroheim) Actor Rudolph Christians died in mid-shooting; replaced by Robert Edenson who is used mainly as a double.
\end{tcolorbox}
```

*Explanations regarding length of time between production and release, e.g., due to funding issues, an initial banning, delayed release due to sensitivity over subject matter and world events, etc.*

```{=latex}
\begin{tcolorbox}
La porta del cielo (Italy, 1945, Vittorio De Sica) The shooting of the film lasted almost one year (February – November 1944) throughout the period of Nazi occupation of Rome and served as an excuse to hide and protect Jewish people, anti-fascists, etc...
\end{tcolorbox}
```

```{=latex}
\begin{tcolorbox}
La grande illusion (France, 1937, Jean Renoir) The shooting of the film lasted two years (1935-1936) and the first projection was in 1937.
\end{tcolorbox}
```

*Any other information relevant to the history of the Work and its production.*

```{=latex}
\begin{tcolorbox}
Christopher Columbus (United Kingdom, 1949, David MacDonald) Location shooting in Barbados was fraught with difficulties. The re-created ship stuck on launch, was then later rammed, suffered mechanical failure and finally caught fire. The stand-in ship was then lost at sea twice. Location shooting was hampered by the heat and the local gaol had to be used to keep the Technicolor film cool. There was also a troublesome parrot that would shout “tea break” during a dramatic scene.
\end{tcolorbox}
```

\subsection{Relationships of a Work/Variant (links/associations with other entities/records)}
\label{sec:relationships_of_a_work_variant}

A relationship associates an instance of a Variant with another instance of an entity.
Entities are described in subsequent sections, but examples of entities are people or companies associated with a Variant (eg, studio, director, cast), events (copyright registration), subjects (other Works/Variants are about the same subject), and records.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.^[EN 15907 8.1 Relationships. General] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest, i.e., whether by physical associative record linking or “see also” text conventions.

A Variant may have relationships with the following:

- Agent(s)
- Event(s)
- Subject(s)/Genre(s)/Form(s)
- Work(s)
- Manifestation(s)
- Other (including other Variants)

\subsubsection{Works}  
\label{sec:Works}

Express the relationship between a Work and a Variant (e.g., Part/part of).
Describe or demonstrate Work-to-Variant relationships through linking to the Work identifier, through the usage of relator terms, or according to the confines of your data structure.

\subsubsection{Manifestations}  
\label{sec:manifestations}

Express the relationship between a Variant and a Manifestation (e.g., Part/part of).
Describe or demonstrate Variant-to-Manifestation relationships through linking to the Variant identifier, through the usage of relator terms, or according to the confines of your data structure.
