# D.4.5 Preservation[^209] {#manual-D.4.5}

A Preservation Event is associated with a new Variant, Manifestation or Items resulting from the preservation process in which the contents of one or more Items (or fragments thereof) from Manifestations of a Work were transferred with the intention of restoring or reconstructing the content as originally intended, or safeguarding it from decay.

Preservation Events aim to document the decision-making process, observations, key steps and decisions, involved film elements (Items and Manifestations) and additional secondary sources, and Agents. 
The number of generated Preservation Events depends on the archive's/organization's workflow, particularly on whether they decide to store the intermediate products of the restoration project, as Preservation Events will connect the individual phases of work on the final restored manifestation. This is illustrated in the diagram below.
[DIAGRAM]

Thanks to this structure, we can:
- Track the history of film elements changes
- Verify the original format and other characteristics
- Understand the impact of operations and workflow
- Identify which film elements/objects/files were created as a result of these operations.

This includes statements about past or future treatments scheduled for the item.[^210] 
Due to the different nature/function of Preservation Event types, they collect different information. What they have in common is the presence of the following fields:
- Type of an Preservation event, 
- Name of the Project (and link) under which conservation was carried out,
- Object Name / Source material to identify the subject of the preservation activity,
- Preservation Date/Activity Start Date and/or End Date Record the date or time span in which the preservation activity was performed. (Dates should be formatted according to ISO 8601 or some other recognised standard.) 
- Source material. A film element that has undergone a preservation activity or as a step in the digital restoration process.
- Result material (Selection should be made from a controlled list of terms. See D.12 Manifestation Preservation Types).

Selection should be made from a controlled list of values.

A Preservation Event has as typical Agent(s) the institution(s), a reference to the Lab or unit in the organisation where activity was carried out or individual professionals that make preservation work or decisions. The organization may decide to extend this scope to the software used in the restoration process (in accordance with METS and PREMIS) or to the machine used – e.g., a film cleaning machine, sound follower, or scanner.
Selection should be made from a controlled list of values and linking to the defined Agents. See [D.8 Manifestation Agent Types](#manual-D.8) and [D.3 Work/Variant Agent Types](#manual-D.3).

A Preservation Event can be in relationship with instances of “Other” relationships (such as technical reports, documentation material, promotional material for the specific project, etc.).

Record all the existing relationships of a Preservation Event, if the information is known and considered of relevance.

Possible values for the elements individual for each suggested Preservation Event types: 
- Conservation / Repair
- Image Digitisation
- Sound Digitisation
- Reconstruction
- Image Restoration
- Image Grading
- Sound Restoration and Mastering
- Duplication: Printing / Recording.
have been suggested in the Annex no:... and [D.12 Manifestation Preservation Types](#manual-D.12).

Some Preservation Events types, such as Conservation or Digitisation, are recurring activities. Therefore, a single Item may be linked to more than one Conservation or Digitisation type Preservation Event. 
Add in a note any information describing the preservation process in detail.

This can include:[^211]

  - Genesis of the project or reason why preservation was undertaken
  - Significant challenges
  - Relevant research (documenting sources of information related to content or production techniques)
  - Technical, aesthetic or ethical decisions
  - Recommendations for further work (details concerning limitations due to source material, resources, technology, etc.)

Some information may be generated automatically from the Manifestation Preservation file. Possible methods of extracting/generating data can be found in Annex no: column… 

[^209]: EN 15907, 6.15 Preservation event, pp. 28-29
[^210]: YCR 6.5, 6.6
[^211]: Based on in-house Academy Film Archive preservation documentation.
