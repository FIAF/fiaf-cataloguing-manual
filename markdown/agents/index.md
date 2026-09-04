---
title: Moving Image Agents (e.g. Cast, Credits, Person, Organisation, etc.)
---
An Agent can be a Person, a Corporate body, a Collective agent, or a Family. [INSERT FOOTNOTE RDA/LRM Agent entity and subtypes]

For recording the attributes of Agents (e.g. first name, last name, nationality, etc.), refer to authoritative sources such as AACR2, applicable RDA chapters for recording attributes of Persons, Families, and Corporate Bodies,[^1] Functional requirements for authority data: a conceptual model, [^2]  or tools such as the Virtual International Authority File (VIAF) (viaf.org), Library of Congress Linked Data Service (id.loc.gov), Getty Union List of Artists Names (ULAN), the [Library of Congress Name Authority File](https://authorities.loc.gov/cgi-bin/Pwebrecon.cgi?RefCodes=3&ref=1&hd=1,1&SEQ=20130523194229&Search_Arg=Ethnology-United%20States&Search_Code=SHED_&CNT=100&PID=mYzkzT0fYryqza3XpBkr08lSvjsf&SID=8), or International Standard Name Identifier (ISNI) 126.127 

It is also recommended where possible to register key Agents with any of the aforementioned authority bodies if they are not already included. 

Optionally, if the Agent is credited under a name that is not identical with the preferred name from an authority file, record the name as used in the current instance of the related entity. 
Some databases may include fields and structures to deal with various alternative or credited forms of the Agent name. 

Give the Agent(s) and Agent Activity in the terms and language in which they appear, either in the sources of information or in the language of the institution, or both. 

In many relational databases Agents have their own actual records with their own identifier fields such as reference numbers, activities, nationality, alternative/credited names, birth and death dates, biographies, etc. 
In these cases, relevant name/agent fields within Works, Variants, Manifestations, and Items will link through to these Agent records. 

Agent records in such database systems should contain such additional important metadata to aid disambiguation and correct identification. It is important to have such other identification factors relating to any Agent records in order for clarity, especially where there are different people/organisations with identical or very similar names.
An Agent record should always include the following core information:

-  the main preferred form of name
-  reference or links to any alternative names, credited names, or pseudonyms used
-  the activity/activities of the Agent

And ideally, also include the following, as applicable and if known:

-  date of birth
-  place & country of birth
-  date of death
-  place & country of death
-  nationality

Agent records may also be related/linked to other Agent records, e.g. 

<center><object data="/images/Screenshot_agentrecordeg1.png" width="100%"></object></center>



<center><object data="/images/Screenshot_agentrecordeg4.png" width="100%"></object></center>




<center><object data="/images/Screenshot_agentrecordeg3.png" width="100%"></object></center>


Or else, additional identifying metadata can be added to a biographical or notes field, e.g.

<center><object data="/images/Screenshot_agentrecordeg2.png" width="100%"></object></center>


A relationship captured between people and/or organisation records can also act as an identifier itself.

This is important for both public users or researchers searching for relevant information, and also cataloguers adding cast and credits, distributors, etc. to moving image records and needing to identify and create links to the correct Person/Organisation Agent records.


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

For further information see 13.2.1.1 Agent Activity – Works/Variants - ADD LINK]

A more in depth look at Agents, especially within an RDA/LRM context can be found here [ADD LINK TO CIRCE'S PAPER AND DIAGRAMS - yET TO BE UPLOADED ONTO CDC WEBSITE SECTION]

[^1]: RDA 2.20.7.3
[^2]: Patton, Glenn E. 2009. Functional requirements for authority data: a conceptual model. München: K.G. Saur.
