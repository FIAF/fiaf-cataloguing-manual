---
title: Event Types
---
| **Work** | **Variant** | **Manifestation** | **Item** |
| --- | --- | --- | --- |
|  |  | [Manifestation Publication Types](/events/publication/#sec-publication) |  |
| [Award(s) or Nomination(s)](/events/publication/#sec-awards_or_nominations) | [Award(s) or Nomination(s)](/events/publication/#sec-awards_or_nominations) | [Award(s) or Nomination(s)](/events/publication/#sec-awards_or_nominations) |  |
| [Production](/events/publication/#sec-production) | [Production](/events/publication/#sec-production) |  |  |
| [Rights/Copyright/IPR Registration](/events/publication/#sec-values_rights_copyright_ipr_registration) | [Rights/Copyright/IPR Registration](/events/publication/#sec-values_rights_copyright_ipr_registration) | Licensing | Licensing |
|  | [Preservation](/manifestations/attributes_of_a_manifestation/#sec-preservation) | [Preservation](/manifestations/attributes_of_a_manifestation/#sec-preservation) | [Preservation](/manifestations/attributes_of_a_manifestation/#sec-preservation) |
|  | [Decision](/events/publication/#sec-decision) | [Decision](/events/publication/#sec-decision) |  |
|  |  | [Manufacture](/events/publication/#sec-manufacture) |  |
|  |  |  | [Inspection](/events/accessioning_and_source/#sec-inspection) |
|  |  |  | [Acquisition](/events/events_manifestations-2/#sec-acquisition) | 


Record one or more Event types, for example, “preservation,” “inspection,” “acquisition”, etc., to express the nature of the Event’s relationship to the Work, Variant, Manifestation, or Item. The table above demonstrates what Event Type is applicable with each of those.

<a id="sec-publication"></a>
## Publication

Record one or more Event type, for example, “decision,” “manufacture,” etc., to express the nature of the Event’s relationship to the Manifestation. Selection should be made from a controlled list of terms. A suggested list, which is open and not exhaustive, can be found in D.4 Event Types.

For Manifestations, a Publication Event corresponds to a screening, broadcast, streaming, or the release of the Manifestation of a Work/Variant on a physical distribution medium or online.

A Publication Event may be associated with instances of Agent in the role of e.g., publisher, distributor, broadcaster[^1], etc. See [Distributor (theatrical)](/agents/agents_for_manifestations/#sec-distributor_theatrical) and [sec:work_variant_agent_types](#sec-work_variant_agent_types).

A Publication Event may be associated with instances of “Other” relationship(s) (e.g., promotional material of the theatrical distribution, the advertising of the home video publication, etc.).

Record all the existing relationships of a Publication Event, if the information is known and considered of relevance.

Publication Event information consists of the following sub-elements:

  - Publication type
  - Publication date
  - Region

**Publication type**

Record the Publication type for Manifestations. Selection should be made from a controlled list of values, e.g.

- Release  
- Publication  
- Distribution  
- Broadcast  
- Online Transmission (e.g. Internet, Intranet)  
- Pre-Release  
- Theatrical distribution  
- Non-theatrical distribution  
- Not for release  
- Home video publication  
- Unknown

For Manifestations, the Publication Event that originated the embodiment of a specific Work/Variant in a Manifestation, corresponds to criteria individuated to distinguish the boundaries between Manifestations. For this reason, conceptually, and also in practice, “publication type” overlaps the main definition of “Manifestation type,” as explained in [INSERT LINK TO Boundaries between Manifestations and Events section] and, as such, is already described. Institutions have the option to decide whether to repeat this information or not.

**Publication date**

Record the date on which Work/Variant or Manifestation was released or otherwise made available. Dates should be formatted according to ISO 8601 or some other recognised standard. The date should be that of the specific event of the Manifestation publication, e.g. a moving image Manifestation may have Publication dates in separate Publication events - a Manifestation for its first theatrical release date of 1957, and then Manifestations for the broadcast date (in 1981) and streaming date (in 2020). 
 
**Region**

Record the country or other political or physical geographic entity where the Publication Event took place (e.g. first projection in the framework of a theatrical distribution) or made the Work/Variant or Manifestation available (e.g. distribution area).

If known and considered of relevance, record the name of the city or smaller geographic entity where the Publication Event took place.

For the treatment of the geographical names, see Getty Thesaurus of Geographic Names (TGN), or some other recognised standard.

If known and considered of relevance, record the name of the event that the publication was a part of (e.g., name of a film festival, distribution channel of a broadcaster, etc.)

If known and considered of relevance, record the specific restrictions for accessing the content (e.g. press-screening only, airplanes only, etc.).

<a id="sec-awards_or_nominations"></a>
## Award(s) or Nomination(s)[^1]

The bestowal of an award relating to the Work/Variant or Manifestation. This excludes awards for Agents alone (e.g. "for lifetime achievement"), but includes awards for individual achievements within the context of a Work or Variant (e.g. "Best screenplay"). Awards will usually be associated at the level of the Work, except for cases where features of a particular Variant are explicitly mentioned (e.g. "Best audio commentary for the visually impaired") or the award relates to a particular Manifestation (such as a DVD edition).

An Award(s) or Nomination(s) Event may be associated with instances of Agent in the role of e.g. publisher, distributor, broadcaster , etc. See [Distributor (theatrical)](/agents/agents_for_manifestations/#sec-distributor_theatrical) and [sec:work_variant_agent_types](#sec-work_variant_agent_types). If the award was given for the achievement of a specific Agent within the context of the Work/Variant or Manifestation, identify the Agent. Also used to identify Agents that have sponsored the award.

An Award(s) or Nomination(s) Event may be associated with instances of other Events during which award winners were selected (e.g. film festival).

Record all the existing relationships of a Publication Event, if the information is known and considered of relevance.

Award(s) or Nomination(s) Event information consists of the following sub-elements:

- Award(s)/Nomination(s) date
- Nomination only
- Award name
- Achievement

**Award(s)/Nomination(s) date**

Record the date the award was bestowed on an Agent associated with the Work, Variant or Manifestation. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

**Nomination only**

Indicate if the Work, Variant or Manifestation (or a specific achievement in the creation of it) was nominated but not among the winners.
This element can be realised in a system as a “flag.” If there was only a nomination, this element would be set to a logical value of “true.”

**Award name**

The name of the award or trophy, possibly including a numeric designation (e.g. 2nd Prize)

**Achievement**

A phrase describing a specific achievement for which the award was given, if not for the Work, Variant or Manifestation in total.

<a id="sec-production"></a>
## Production[^2]
A distinct event in the course of production of a Work or Variant, including the main production event OR events that are separated in space and/or time from the main production event, or known with a greater amount of detail. Examples are dates and locations where castings took place; dates and locations of shootings or other recordings; or dates and locations of particular post-production activities.

May include year/date of shooting of non-professional, actuality or unedited footage.

A Production Event may be associated with instances of Agent in the role of e.g. production company, location scout, etc. Selection should be made from a controlled list of values. See [sec:work_variant_agent_types](#sec-work_variant_agent_types).

Record all the existing relationships of a Production/Publication Event, if the information is known and considered of relevance.

Production Event information consists of the following sub-elements:

- Production Event type
- Location
- Region
- Year/Date
- Event details

**Production Event type**

Selection should be made from a controlled list of values, e.g.:

* Casting
* Outdoor shooting
* Indoor shooting
* Post-Production

**Location**

Any geographic name(s) or address(es) of the location(s) where the event took place

**Region**

The country or other large-scale geographic entity where the event took place

**Year/Date**

The year/date or time-span during which the event took place. Dates should be formatted according to ISO 8601 or some other recognised standard.

**Event details**

Any further information about the event either in plain textual form, or as an instance of a data type from another schema

<a id="sec-values_rights_copyright_ipr_registration"></a>
## Rights/Copyright/IPR Registration[^3]
These are optional, and it is for an institution to choose whether it has the resources or requirement to compile rights data. Further more detailed information on the subject of rights/copyright/IPR registration can be found in [Rights/Copyright/IPR Registration](/appendices/rights/).

A Copyright/IPR Registration Event is the act of registering copyright or intellectual property rights for a Work or Variant with an accredited agency.

A Copyright/IPR Registration Event may be associated with instances of Agent in the role of e.g. applicant, etc. Selection should be made from a controlled list of values.

Record all the existing relationships of a Copyright/IPR Registration Event, if the information is known and considered of relevance.

Copyright/IPR Registration Event information consists of the following sub-elements:

- Registration Date
- Registration Agency
- Regional scope
- Name of applicant
- Registration number

**Registration date**

The date on which the registration was filed or the date on which registration became effective. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

**Registration agency**

Name of the agency issuing the registration certificate (e.g. "UK Intellectual Property Office," name of a legal deposit library, etc.).

**Regional scope**

The geographic region for which copyright is claimed.

**Name of applicant**

Name of the Agent claiming copyright in the Work or Variant.

**Registration number**

The number assigned by the registration agency. 

<a id="sec-preservation_restoration"></a>
## Preservation/Restoration
A Preservation/Restoration Event is associated with a new Variant, Manifestation or Items resulting from the preservation/restoration process in which the contents of one or more Items (or fragments thereof) from Manifestations of a Work were transferred with the intention of restoring or reconstructing the content as originally intended, or safeguarding it from decay.[^5]  

This includes statements about past or future treatments scheduled for the item.  If desired and if applicable, record one or more general types of past or future treatment activities (e.g. "added leaders", "cleaned ultrasonically", "tears repair", etc.). Selection should be made from a controlled list of values. [CHECK - DO WE HAVE A LIST FOR THAT?]

A Preservation/Restoration Event has as typical Agent(s) the institution(s) or individual professionals that make preservation decisions. Selection should be made from a controlled list of values. See [sec:work_variant_agent_types](#sec-work_variant_agent_types).

A Preservation/Restoration Event can be in relationship with instances of “Other” relationships (such as technical reports, documentation material, promotional material for the specific project, etc.).

Record all the existing relationships of a Preservation/Restoration Event, if the information is known and considered of relevance.

Preservation/Restoration Event information consists of the following sub-elements:

- Preservation/Restoration type  
- Preservation/Restoration date
    

- Preservation/Restoration type
  
Record the general type of the preservation/restoration activity performed. Selection should be made from a controlled list of terms, which may include:
 
- Conservation / Repair  
- Image Digitisation  
- Sound Digitisation  
- Reconstruction  
- Image Restoration  
- Image Grading  
- Sound Restoration  
- Printing / Recording   
- Duplication   
- Transfer   


**Preservation/Restoration type**

Record the general type of the preservation activity performed, for example, duplication, transfer, etc. Selection should be made from a controlled list of terms, e.g.:

* Duplication (Printing / Recording)
* Transfer
* Reproduction
* Digitisation
* Reconstruction
* Restoration

[cHECK IN CLOSED ISSUES WHICH OF THESE TWO IS THE LIST THAT WAS FINALLY DECIDED ON]

**Preservation/Restoration Date**

Record the date or time span in which the preservation/restoration activity was performed. (Dates should be formatted according to ISO 8601 or some other recognised standard.)
Add in a note any information describing the preservation process in detail.

This can include: 

-	Genesis of the project or reason why preservation was undertaken  
-	Significant challenges  
-	Relevant research (documenting sources of information related to content or production techniques)  
-	Technical, aesthetic or ethical decisions  
-	Recommendations for further work (details concerning limitations due to source material, resources, technology, etc.)  

A Preservation/Restoration Event can be used in conjunction with Preservation or Restoration type Manifestations as relevant.

[INSERT ILLUSTRATIVE DIAGRAMS USING BOTH HERE]

[ALSO INSERT LINK - TO EXTERNAL CDC SITE HOLDING EWA'S COMPLEX PRESERVATION EVENT DIGITISATION AND PRESERVATION RESTORATION WORKFLOW DOCUMENTS]

<a id="sec-decision"></a>
## Decision[^4]
A Decision Event is an event in which a Manifestation of a certain Work/Variant is evaluated by a censorship body or an accredited rating agency.

A Decision Event may be associated with instances of Agent, e.g. in the role of the agency performing the rating or censorship, and also with instances of “Other” relationship(s) (e.g., the original censorship documents).

Record all the existing relationships for the Decision Event, if the information is known and considered of relevance.

Decision event information consists of the following sub-elements:

- Decision type  
- Decision date  
- Regional scope  
- Certificate number  
- Verdict  

**Decision type**

Record the type or status of the decision event. Usually the term adopted is "censorship" or “revision” for decisions mandated by law, "rating" for decisions under a voluntary scheme. Further types may include special forms of evaluation, e.g. for tax privileges, as long as these are distinct from awards.

Selection should be made from a controlled list of terms, including ones such as:

- Censorship  
- Revision  
- Rating  


**Decision date**

Record the date on which the verdict was announced or on which the verdict was declared valid. Dates should be formatted according to ISO 8601 or some other recognised standard.

**Regional scope**

Record the geographic region for which the verdict is (was) valid.

**Certificate number**

Record in Arabic numerals the number issued by the agency as a unique identifier of the act(s) of rating or censorship such as censorship visas or rating certificates.

**Verdict**

Record the outcome of the act of rating or censorship.

[INSERT ILLUSTRATIVE EXAMPLES HERE FROM A COUPLE OF DIFFERENT COUNTRIES]

<a id="sec-manufacture"></a>
## Manufacture
A Manufacture Event represents a “common” event within which the embodiment of a Manifestation occurs, owing to the instances of a number of physical items that bear the same characteristics.

Therefore, the manufacture event of a moving image Manifestation corresponds to the activity within which it was fixed on a physical carrier, through particular technical processes such as film printing, telecine, video copying, digitisation, mastering, etc., or where it is saved to an “immaterial” medium, such as a digital file.

A Manufacture Event may be associated with instances of Agent, e.g. a laboratory that prints all the copies for a theatrical distribution or a studio that masters the DVDs for a home video publication.

A Manufacture Event may be associated with instances of “Other” relationship(s).

Record all the existing relationships for the Manufacture Event, if the information is known and considered of relevance.

Manufacture event information consists of the following sub-elements:

- Manufacture type  
- Manufacture date  
- Manufacture region  

**Manufacture type**

Record the general type of the manufacture activity performed, for example, film printing, tele-cine, video copying, etc. Selection should be made from a controlled list of terms, including ones such as:

- Film printing  
- Telecine  
- Video copying  
- Scanning  
- Mastering  
- Uploading  

**Manufacture date**

Record the date or time span on which the Manufacture Event took place. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

**Manufacture region**

Record the country or other political or physical geographic entity where the Manufacture Event took place (e.g. the region/place where the laboratory was located).
(For the treatment of the geographical names, see Getty Thesaurus of Geographic Names (TGN), or some other recognised standard.)

If known and considered of relevance, record the name of the city or smaller geographic entity where the Manufacture Event took place.

[^1]: EN 15907, 6.12 Award, pp. 25-26.
[^2]: Adapted from EN 15907 6.11 Production Event, p. 20
[^3]: EN 15907 6.15 IPR Registration, pp. 23-24
[^4]: EN 15907, 6.13 Decision event, pp. 26-27
[^5]: There is no designated separate Restoration Event in EN 15907, and as there can often be an overlap in the types of activity associated with both preservation and restoration, we extended the definition in the 2016 FIAF Moving Image Cataloguing Manual to cover restoring and reconstruction of content too. We have also now referred to it as a Preservation/Restoration Event to increase clarity.


[^1]: Some institutions specifically dealing with TV material may wish to use an actual “TV Transmission Manifestation” for this data.

