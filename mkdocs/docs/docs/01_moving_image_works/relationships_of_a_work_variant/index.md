---
title: Relationships of a Work/Variant (links/associations with other entities/records)
---
<a id="sec-relationships_of_a_work_variant"></a>
### Relationships of a Work/Variant (links/associations with other entities/records)
A relationship associates an instance of a Work/Variant with another instance of an entity.
Entities are described in subsequent sections, but examples of entities are people or companies associated with a Work/Variant (eg, studio, director, cast), events (copyright registration), subjects (other Works/Variants are about the same subject), and records.

Relationships can be implemented in many ways, depending on the purpose, the modelling paradigm, or architectural constraints of the chosen platform.
These guidelines are intended to be data structure neutral.[^fn3] Therefore, these guidelines cannot prescribe exactly how to demonstrate relationships.
Instead they recommend that certain relationships be established without instruction on how precisely those links be made manifest, i.e., whether by physical associative record linking or “see also” text conventions.

A Work may have relationships with the following:

- Agent(s)
- Event(s)
- Subject(s)/Genre(s)/Form(s)
- Variant(s)
- Manifestation(s)
- Other (including other Works)

A Variant may have relationships with the following:

- Agent(s)
- Event(s)
- Subject(s)/Genre(s)/Form(s)
- Work(s)
- Manifestation(s)
- Other (including other Variants)

<a id="sec-work_events"></a>
#### Events (e.g., IPR registration, screenings, awards, etc.)[^fn1]
An Event characterises occurrences in the lifecycle of a moving image Work or its Variants.
Instances of any Event type can have Agent and “Other” relationships.

Record one or more Event type, for example, “publication,” “copyright/IPR registration,” “festival showing,” etc., to express the nature of the Event’s relationship to the Work/Variant.
Selection should be made from a controlled list of terms.
A suggested list, which is open and not exhaustive, can be found in [Event Type](/docs/12_appendix_04/event_type/#sec-event_type).

<a id="sec-subject_genre_form_terms"></a>
#### Subject/Genre/Form Terms
Provide access to the Work by means of subjects (or subject identifiers) that describe the content of the Work, and additionally by genre(s) and/or form(s) (or identifiers) of which the Work is an example (i.e. what the Work is). Works should ideally have at least one Genre (and/or Form) and one Subject term as a minimum.

Genre - reflects what the Work is (i.e. in terms of categories of Works characterised by similar plots, themes, settings, situations, and characters, e.g. Horror, Science-fiction, Crime, Westerns, Thrillers, Comedy, etc.)

Form - a further categorisation term relating to what the Work is and the form it takes, descriptive of the characteristics of its format and/or purpose, e.g. Fiction, Non-fiction, Short, Animation, Video Essay, etc. which some systems may have as a separate category whilst others incorporate them within their Genre terms.

Subject - reflects the content of the Work, what it features and what it is about.

There are no rules as to how many genre and subject terms can be associated with a Work. It will be different from moving image to moving image and down to the assessment of the individual cataloguer within the levels of subject cataloguing decided by their institution.

!!! example "Example"
    **Main title** <br/> 
    A trip down Market Street before the fire / [Miles Brothers]. <br/> <br/>
    **Published/Created**  <br/>
    United States. [United States : Miles Brothers, 1906]. <br/> <br/>
    **Summary**  <br/>
    The following is a scene-by-scene description of the film: [Frame: 0300 (part 1)] The film begins looking northeast on Market Street just west of the intersection of Hyde, Grove and 8th streets. The dark building at right is the Odd Fellows Hall and the grey building beyond (across 8th St.) is the Grant Building (1905). A white postal service automobile is at left center. The three large buildings receding down Market Street at left are [0319 (part 1)] the Murphy Building (1889), [0353 (part 1)] the Donohoe Building (1890), and the Flood Building (1905). [etc.; this is an excerpt from the full record.] <br/> <br/>
    **Subjects** <br/>
    Market Street (San Francisco, Calif.) <br/>
    Street-railroads--California--San Francisco. <br/>
    Horse-drawn vehicles--California--San Francisco. <br/>
    City traffic--California--San Francisco. <br/>
    Pedestrians--California--San Francisco. <br/>
    Automobiles--California--San Francisco. <br/> <br/>
    **Form/Genre** <br/>
    Actualities (Motion pictures) <br/>
    Short films. <br/>
    Silent films. <br/>
    Nonfiction films.

!!! example "Example"
    **Main title**  <br/>
    Mardi Gras parade -- US : Thomas A. Edison, Inc. [producer, distributor], [190-?].  <br/> <br/>
    **Summary**  <br/>
    Early actuality footage, shot from a single location on a street in New Orleans, showing a Mardi Gras parade. Mule drawn floats, children and adults in costumes, and brass bands march down the street, as crowds of spectators mill about the sidewalks, sometimes spilling into the street. <br/> <br/>
    **Subjects**  <br/>
    1. Carnival -- Louisiana -- New Orleans. 2. Parades -- Louisiana – New Orleans. 3. Holidays. <br/> <br/>
    **Genres**  <br/>
    1. Actualities. 2. Shorts.

!!! example "Example"
    **Main title**  <br/>
    British Canadian Pathe news. No. 83A / L.E. Ouimet presents. -- CA : British Canadian Pathe News [producer], 1919 ; CA : Specialty Film Ltd. [distributor], 1919. <br/> <br/>
    **Contents**  <br/>
    London: Ilford Municipal Market proves great success (43 ft.) -- Yarmouth, Eng.: Happy hours by the sea (46 ft.) -- Lauzon, Que.: World’s largest drydock (84 ft.) -- Toronto: Cycle racing at Exhibition Park (218 ft.) -- Kingston: [Geo. Vernot, Canadian swimmer, demonstrates strokes] (140 ft.) -- Fresno, Cal.: [Staged train wreck at fair] (69 ft.) -- Gary, Ind.: [Federal troops in big steel centers as result of recent riots] (150 ft.) -- Getting together, an animated cartoon by Bert Green (65 ft.) – A Review of events in Great Britain: Yarmouth: Deutschland, German Navy ship, now tourist attraction; London: “Pussy-foot” Johnson trying to make Britain “dry;” Doncaster: horse racing; Manchester: statue of Abraham Lincoln unveiled, gift of the U.S. to England’s great Cotton City (123 ft.). <br/> <br/>
    **Subjects**  <br/>
    1. Markets -- England -- London. 2. London (England) -- Description. 3. Seaside resorts -- England. 4. Yarmouth (Isle of Wight) -- Description. 5. Drydocks -- Canada. 6. Saint Henri (Quebec) -- Description. 7. Bicycle racing -- Canada. 8. Swimming -- Canada. 9. Strikes and lockouts -- Steel industry -- United States. 10. Prohibition -- England. 11. Horse-racing -- England. 12. Doncaster (South Yorkshire) -- Description.13. Lincoln, Abraham, 1809-1865 -- Statues. 14. Manchester (Greater Manchester) -- Description. <br/> <br/>
    **Genre**  <br/>
    1. Newsreels.

!!! example "Example"
    **Main title**  <br/>
    O Beijo da mulher aranha = Kiss of the spider woman / director, Hector Babenco ; producer, David Weisman ; screenplay, Leonard Schrader. -- BR : HB Filmes [producer], 1895 ; US Sugarloaf Films [producer], 1985 ; US : Island Alive [distributor], 1985. <br/> <br/>
    **Summary**  <br/>
    Molina, a homosexual window-trimmer convicted on a morals charge, shares a dreary prison cell with Valentin, a clandestinely-held politically active journalist who has been endlessly tortured by prison authorities in a vain attempt to extract information about his activities. Both men could not be farthe apart in personal attitudes, lifestyles, and emotional makeup: Molina is a glib raconteur, who dwells in a fantasy world of glamorous movies from yesteryear, of romantic screen heroes and tragic heroines. Valentin is a self-disciplined intellectual who is devoted to the cause of human rights and his political concerns. [etc. ; this is an excerpt from the full record] <br/> <br/>
    **Subjects**  <br/>
    1. Prisoners -- Drama. 2. Interpersonal relations -- Drama. 3. Homosexuality, Male -- Drama. 4. Political prisoners -- Drama. 5. Torture -- Drama. <br/> <br/>
    **Genres**  <br/>
    1. Drama. 2. Features.

<a id="sec-assigning_subject_terms"></a>
##### Assigning Subject terms
When considering the assigning of subject terms to a moving image Work record there are two main components to consider in making an intellectual assessment; the contexts of "about" and "of":

**Of** is straightforwardly, explicitly what is seen and visible in the shots and scenes that make up the moving image. 

**About** is the elements and themes of a moving image that are implicit from the unfolding and combining of different images, or more explicit from interviews, commentary, or narration on the soundtrack.

EN15744 advocates that all Works should have at least one subject term as a minimum.

But it is up to each institution to decide the depth and level of subject indexing, and whether it catalogues according to the principle of capturing just what is seen, or just what it is about. The ideal is to have both elements:

“one must try to capture what is seen onscreen as well as what the images are about conceptually.” (NB.Olwen Terris - cite source in footnote

Decisions will depend on resources, technologies, an institution’s requirements and user needs, etc.  Some may choose to apply different levels and balances of these two **of** and **about** elements depending on whether the moving image is fiction or non-fiction. Footage libraries, for example, may be more likely to concentrate on **of** elements, but other archives may prefer to focus on **about** subjects. 

[ADD IN FURTHER EXAMPLES FROM OTHER ARCHIVES TO BOURNE ONE BELOW]

For example, one practice for fiction moving images may be to assess what they are mainly about and apply  2-3 core subject terms reflecting the central themes or the nub of what they are about, plus any extra ones deemed necessary or relevant, e.g.:

!!! example "Example"
    The Bourne Identity (USA, 2002) <br/>
    Form = Fiction <br/>
    Genre(s) = Thriller, Crime, Action and Adventure <br/>
    Subject(s) = Identity, Black ops, Political assassinations

Subject terms *Car chases*, *Paris*, *Motorways*, *Guns*, *Fights*, *Surveillance*, etc. all feature within the film, but are not what it is about. However, if your institution uses wide keyword ranges in cataloguing, similar to IMDB's multiple "plot keywords" on Work records, then they would be relevant to apply.

The content description/synopsis of a Work can be used to highlight factors that may be prominent but not core in the storyline. 

Similarly, The Bourne Ultimatum (USA, 2007)could have the same subjects as above, plus *Manhunts* since a central part of the storyline of this film is the government agency's hunt for Jason Bourne to try and eliminate him. It could also possibly include *CIA* as well as the thread running through the film is that CIA personnel are both hunting Bourne and trying to find out about the earlier covert operations/organisations.

It is for the Cataloguer to assess and judge whether to include place as a subject term in the record.
In order to establish whether place is a core subject to include in subject cataloguing or not you would need to assess the significance of place within the storyline and themes of the moving image and whether it is integral to these or incidental.

For example, in the film Brighton Rock (UK, 1948) the place of Brighton is integral to the story – it is about gangsters in the English seaside town of Brighton and that is where the whole story is set. However, in the comedy film  Carry On at Your Convenience (UK, 1971), which contains scenes of a works outing to the seaside (which just happens to be Brighton) it is not integral – it simply features in one bit of the storyline. 

Place is more likely to be a core subject term in cataloguing non-fiction moving images. For example, Bunkar: The Last of the Varanasi Weavers (India, 2018) is a documentary that focuses on the lives of the weavers of Varanasi in Uttar Pradesh. Gulabi Gang (India, 2014) is about a women’s movement standing against gender violence and caste oppression, but the geographical place Bundelkhand is also relevant to add as a subject term both for context and because there are shots of the area in the film.

With fiction moving images, care is needed not to confuse place within the storyline of the moving image with shooting location during filming, e.g. the early Alfred Hitchcock film The Manxman (Uk, 1926) is set in a fishing village in the Isle of Man, but was actually filmed on location in Cornwall, England.

If adding place as a subject it would not therefore be Cornwall but the Isle of Man, since that is what the film is actually about and where it is set.

Actual filming locations data can be added in a different field (in the EN15907 structure locations and production information can be added to a linked Production Event).

<a id="sec-work_other_relationships"></a>
#### Other relationships[^fn2]
If desired or appropriate, express relationships that are not covered by the Agent, Subject, and Event relationships, including all kinds of aggregation and re-use of Works and their Variants.
(See [Aggregates (Compilations, Multi-component productions)](/docs/13_appendix_05/).)

Commonly-occurring relationships include:[^fn4]

*Work(s) that the moving image Work is based on (e.g. moving images adapted from novels, plays, etc.)*

!!! example "Example"
    The grapes of wrath (United States of America, 1940, John Ford), based on the homonymous novel by John Steinbeck (1939).

*Work(s) that the moving image Work is a performance of (moving image recordings made of live stage presentations of music, plays, dance, etc.)*

!!! example "Example"
    Pink Floyd: live at Pompeii (Belgium,West Germany, France, 1972, Adrian Maben ), concert filmed in the old Pompeii amphitheatre.

*Work(s) that the moving image Work forms part of (e.g. series/serials, aggregations/compilations)*

!!! example "Example"
    Fantômas contre Fantômas (Serial in 5 episodes, Louis Feuillade 1914, production Société des Etablissements Gaumont).

!!! example "Example"
    Fiddlesticks, Ub Iwerks, 1930, episode of the animation series Flip the Frog (Celebrity Pictures, distr. Metro Goldwyn-Mayer, 1930-1933 (38 issues).

*Work(s) that the moving image Work has a sequential relationship with (e.g. sequels, prequels, serials)*

!!! example "Example"
    The Godfather Part I <br/>
    The Godfather Part II <br/>
    The Godfather Part III Francis Ford Coppola (United States of America, 1972- 1974-1990)

*Work(s) about the moving image Work (e.g. documentary about the making of a feature film or TV programme)*

!!! example "Example"
    La ciociara quarant’anni dopo (Italy, 2001, Stefano Landini), documentary on the restoration of La ciociara (Italy, 1960, Vittorio De Sica).

!!! example "Example"
    Reise nach Metropoli (Germany, 2009, Artem Demenok), documentary on the restoration of Metropolis (Fritz Lang, 1927).

*Work(s) that are promotional material of the moving image Work (e.g. Trailers)*

!!! example "Example"
    Wuthering Heights (Film Trailer) (United States of America, 1939) is the trailer for Wuthering Heights (United States of America, 1939, William Wyler)

*Non-moving image Works that the moving image Work has a relationship with (e.g. Books, articles, scripts, posters, documents, etc)*

!!! example "Example"
    Kes (United Kingdom, 1969, Ken Loach), book “Life after Kes: an anthology of the film Kes”, by Simon W. Golding. GET Publishing, 2005. ISBN. 0954879333

!!! example "Example"
    Land and freedom (United Kingdom, 1995, Ken Loach), script Land and freedom (c.1993) (script for ‘Land and freedom’, with opening sequence different from earlier scripts).

!!! example "Example"
    Carry on camping (United Kingdom, 1969, Gerald Thomas), archival documents - general production correspondence including notes from the pre-production meeting, studio agreement, final screen credits, and draft trailer script).

!!! example "Example"
    The wicked lady (United Kingdom, 1945, Leslie Arliss), costume

Record one or more “Other” relationship type terms to express the nature of the relationship to the Work/Variant, choosing the most specific term possible from a controlled list of values , for example, “based on,” “contained in,” etc. .
A suggested list, which is open and not exhaustive, can be found in [Other Relationships for Works, Variants, Manifestations, Items](/docs/12_appendix_04/other_relationships_for_works_variants_manifestations_items/#sec-other_relationships_for_works_variants_manifestations_items).

Or, compose a term to describe the relationship between the Work being catalogued and the related Work.

In a note, add any additional information concerning the relationship considered relevant.

Describe or demonstrate Work-to-Work relationships through linking to the Work identifier of the related Work, through the usage of relator terms, or according to the confines of the institution’s data structure.

Remember, a Work based on a pre-existing Work should be identified as a Variant of the same Work unless it has been so significantly changed as to have become a new related Work.[^fn5] See [Boundaries between Works](/docs/14_appendix_06/#sec-boundaries_between_works) and [Boundaries between Works and Variants](/docs/14_appendix_06/#sec-boundaries_between_works_and_variants) for determining when a Work should be identified as a new, but related Work and when it should be identified as a Variant of the original Work.

<a id="sec-variants"></a>
#### Variants
Express the relationship between a moving image Work and a moving image Variant (e.g., Part/part of).
Describe or demonstrate Work-to-Variant relationships through linking to the Work identifier, through the usage of relator terms, or according to the confines of your data structure.

<a id="sec-manifestations"></a>
#### Manifestations
Express the relationship between a moving image Work or Variant and a moving image Manifestation (e.g., Part/part of).
Describe or demonstrate Work-to-Manifestation relationships through linking to the Work identifier, through the usage of relator terms, or according to the confines of your data structure.

[^fn1]: EN 15907 5.2 Event
[^fn2]: EN 15907 8.5 HasAsSubject; YCR, 1.2.7 Relationships With Other Moving Image Works or Other Kinds of Works
[^fn3]: EN 15907 8.1 Relationships. General
[^fn4]: OLAC TF, Part I, Moving Image Work Definition and Boundaries, Commonly-Occurring Relationships, p. 16.
[^fn5]: YCR, 1.1.7 Works based on previous works, pp. 24-25.

