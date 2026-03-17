---
title: Moving Image Agents
---
For recording the attributes of Agents (e.g. first name, last name, nationality, etc.), refer to authoritative sources such as AACR2, applicable RDA chapters for recording attributes of Persons, Families, and Corporate Bodies,[^1] Functional requirements for authority data: a conceptual model, [^2]  or tools such as the Virtual International Authority File (VIAF) (viaf.org), Library of Congress Linked Data Service (id.loc.gov), Getty Union List of Artists Names (ULAN), the [Library of Congress Name Authority File](https://authorities.loc.gov/cgi-bin/Pwebrecon.cgi?RefCodes=3&ref=1&hd=1,1&SEQ=20130523194229&Search_Arg=Ethnology-United%20States&Search_Code=SHED_&CNT=100&PID=mYzkzT0fYryqza3XpBkr08lSvjsf&SID=8), or International Standard Name Identifier (ISNI) 126.127 

It is also recommended where possible to register key Agents with any of the aforementioned authority bodies if they are not already included. 

Optionally, if the Agent is credited under a name that is not identical with the preferred name from an authority file, record the name as used in the current instance of the related entity. 
Some databases may include fields and structures to deal with various alternative or credited forms of the Agent name 

Give the Agent(s) and Agent Activity in the terms and language in which they appear, either in the sources of information or in the language of the institution, or both. 

In many relational databases Agents have their own actual records with their own identifier fields such as reference numbers, activities, nationality, alternative/credited names, birth and death dates, biographies, etc. 
In these cases, relevant name/agent fields within Works, Variants, Manifestations, and Items will link through to these Agent records. 

Agent(s) may also have relationships to an instance of a specific Event or of an “Other” relationship in connection with the Work, Variant, Manifestation or Item, e.g. cinema of a premiere screening, film classification body, film laboratory, etc. 

Because responsibility for moving image materials is most often complex and highly diverse, institutions - particularly those with special interests - should determine the number of Agents and the types of roles and activities they wish to include. 
These may vary from institution to institution according to the types of moving image material held. 

| **Work** | **Variant** | **Manifestation** | **Item** |
| --- | --- | --- | --- |
| Cast | Dubbing cast | Distributor/Publisher | Acquisition source (e.g. donor) |
| Cinematographer/ Director of photography | Additional credits | Broadcaster | Curator |
| Presenter | Additional cast | Streaming Channel | Lab technician |
| Director |  | Manufacturer | Archivist |
| Producer |  |  |  |
| Production Company |  |  |  |

<a id="sec-agents_for_works_variants"></a>
## Agents for Works/Variants (e.g. Cast, Credits, Person, Organisation, etc.)
An Agent is defined as an entity that is involved in the creation, realisation, curation or exploitation of a Work/Variant and who is considered to have major responsibility for, or be of major importance to, the Work/Variant. 
Typical distinctions between Agent types are Person, Corporate Body, Family, and Person Group.[^3] 
This includes cast and credits for the Work/Variant. 

An institution should determine the types of activities they wish to include. 
These activities may vary from institution to institution according to the types of moving image material held. 
For example, an institution holding primarily television material may consider the activity of producer more important than that of director. 
Institutions whose collections are primarily composed of motion picture material may value equally the activities of directors and producers. 
Provide access to Agents when they have made an important contribution to the particular Work or Variant, even when the type of responsibility (credit function) is one that may not be considered major in other Works/Variants or types of Works/Variants.[^4]

Agents may be described in two ways: as discrete index points, and/or merged into one field where the credits are listed in order of role importance or as transcribed from the Work.  

Optionally, if the Agent is credited under a name that is not identical with the preferred name from an authority file, record the name as used in the current instance of the related entity. 

!!! example "Example"
    Bob Robertson (pseudonym/screen name used by the director Sergio Leone at the beginning of his career)

!!! example "Example"
    Terence Hill (pseudonym/screen name used by the actor Mario Girotti in the most known part of his career)

!!! example "Example"
    Sofia Lazzaro (first pseudonym/screen name used by the actress Sophia Loren, whose birth name is Sofia Villani Scicolone).

Optionally, record multiple instances of Agent, e.g., cast and credits, associated with aggregated Works/Variants (See E.6 Credits (i.e. Agents) for Aggregates). 

Variants may include both the Agents of the original Work and of the particular Variant, or just those pertaining to the particular Variant, e.g. additional cast in reinserted scenes in a Director’s Cut, new credits relating to digital special effects in a special edition with new CGI effects, cast used for a dubbed version, etc. 

<a id="sec-agent_activity_works_variants"></a>
### Agent Activity – Works/Variants
This describes the activity or role of the Agent in relation to the moving image Work/Variant (e.g. credit terms). 

Record one or more Agent Activity terms, for example, “animator,” “cast,” “choreographer,” “production company” etc., to express the nature of the agent’s relationship to the Work or Variant. 
Choose the single most specific term, if possible. Selection should be made from a controlled list of terms, such as the [FIAF Glossary of Filmographic Terms](http://www.fiafnet.org/publications/GlossaryMasterComboMarch2015.html). 

If no suggested terms apply, compose a term to describe the relationship between the Agent and the Work/Variant being catalogued. 
If the relationship is ambiguous, use a value to indicate this, for example, “unknown” or “on-screen participant” to indicate a person appearing on screen in a capacity that is indeterminate or not covered by typical terms.[^5] 
Optionally, when the role performed by an Agent is probable but not certain, provide the function name followed by a question mark. 

Besides the principal Agent Activity suggested, institutions, particularly those with special interests, may create and apply in-house value lists of other specific Agent Types, which may vary from institution to institution. 

Record in a note any additional details that cannot be expressed through controlled terms. (e.g. “appears only in final scene”, etc.). 
If a name is known to be fictitious, or requires clarification, make a note giving the actual name. 

If more than one Agent is associated with a particular role connected with a Work/Variant or related Event, where possible or desirable, record the names in the order indicated by the sequence, layout, or typography of the names on the source of information. 
Preserving the ordering of the credited persons should be determined by the requirements of individual institutions.[^6] 

!!! example "Example"
    Les Enfants du paradis 

    réalisation, Marcel Carné 

    scenario et dialogue, Jacques Prevert 

    musique, Maurice Thiriet

OR

!!! example "Example"
    Enfants du paradis, Les 

    director, Marcel Carné 

    script and dialogue, Jacques Prevert 

    music, Maurice Thiriet
 
!!! example "Example"
    Star wars 

    Director, George Lucas 

    Executive Producer, George Lucas 

    Producer, Gary Kurtz 

    Screenplay, George Lucas

If Agents are added as index points rather than listed or described in order of importance, an organisation may choose to put the Agent Activity or role term(s) at the end of the name. 

!!! example "Example"
    Les Enfants du paradis 

    Carné, Marcel, réalisation 

    Prevert, Jacques, scenario, dialogue 

    Thiriet, Maurice, musique
 
!!! example "Example"
    Star wars  

    Lucas, George, director, executive producer, screenplay 

    Kurtz, Gary, producer

[^1]: RDA 2.20.7.3
[^2]: Patton, Glenn E. 2009. Functional requirements for authority data: a conceptual model. München: K.G. Saur.
[^3]: EN 15907, 5.1 Agent
[^4]: 1991 FIAF Cataloguing Rules for Film Archives – Statements of Responsibility, p. 35.
[^5]: ist of relator terms are a combination of those found in YCR, 1.3.2. Other creators, pp. 42-43; and, OLAC TF, Part II, Core Attributes and Relationships, Commonly-Occurring Roles, pp. 16-18.
[^6]: FIAF, 1.6.2, pp. 36-37.

