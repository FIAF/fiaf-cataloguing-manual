---
title: Event Type
weight: 2
---
<a id="sec-event_type"></a>
### Event Type
| **Work** | **Variant** | **Manifestation** | **Item** |
| --- | --- | --- | --- |
| [Publication](/docs/12_appendix_04/event_type/#sec-publication) | [Publication](/docs/12_appendix_04/event_type/#sec-publication) | [Publication](/docs/12_appendix_04/event_type/#sec-publication) |  |
| [Award(s) or Nomination(s)](/docs/12_appendix_04/event_type/#sec-awards_or_nominations) | [Award(s) or Nomination(s)](/docs/12_appendix_04/event_type/#sec-awards_or_nominations) | [Award(s) or Nomination(s)](/docs/12_appendix_04/event_type/#sec-awards_or_nominations) |  |
| [Production](/docs/12_appendix_04/event_type/#sec-production) | [Production](/docs/12_appendix_04/event_type/#sec-production) |  |  |
| [Rights/Copyright/IPR Registration](/docs/12_appendix_04/event_type/#sec-values_rights_copyright_ipr_registration) | [Rights/Copyright/IPR Registration](/docs/12_appendix_04/event_type/#sec-values_rights_copyright_ipr_registration) | Licensing | Licensing |
|  | [Preservation](/docs/12_appendix_04/theatrical_distribution/#sec-preservation) | [Preservation](/docs/12_appendix_04/theatrical_distribution/#sec-preservation) | [Preservation](/docs/12_appendix_04/theatrical_distribution/#sec-preservation) |
|  | [Decision](/docs/12_appendix_04/event_type/#sec-decision) | [Decision](/docs/12_appendix_04/event_type/#sec-decision) |  |
|  |  | [Manufacture](/docs/12_appendix_04/event_type/#sec-manufacture) |  |
|  |  |  | [Inspection](/docs/12_appendix_04/event_type/#sec-inspection) |
|  |  |  | [Acquisition](/docs/12_appendix_04/event_type/#sec-acquisition) | 

<a id="sec-publication"></a>
#### Publication
For Works/Variants, a Publication Event corresponds to the first verified release or availability of the Work or Variant, whether theatrical, straight-to-video, broadcast or online transmission, etc.

For Manifestations, a Publication Event corresponds to a screening, broadcast or the release of the Manifestation of a Work/Variant on a physical distribution medium or online.

A Publication Event may be associated with instances of Agent in the role of e.g., publisher, distributor, broadcaster[^fn6], etc. See [Distributor (theatrical)](/docs/12_appendix_04/manifestation_agent_types/#sec-distributor_theatrical) and [Work/Variant Agent Types](/docs/12_appendix_04/work_variant_agent_types/#sec-work_variant_agent_types).

A Publication Event may be associated with instances of “Other” relationship(s) (e.g., promotional material of the theatrical distribution, the advertising of the home video publication, etc.).

Record all the existing relationships of a Publication Event, if the information is known and considered of relevance.

Publication Event information consists of the following sub-elements:

  - Publication type
  - Publication date
  - Region

- Publication type

For Works/Variants, record the type of Publication Event for Works/Variants, for example, publication, release, distribution, broadcast, online transmission.
Selection should be made from a controlled list of values.
See [Manifestation Publication Types](/docs/12_appendix_04/manifestation_publication_types/#sec-manifestation_publication_types).

Record the Publication type for Manifestations, for example, “pre-release,” “theatrical distribution,” etc. Selection should be made from a controlled list of terms.
See [Manifestation Publication Types](/docs/12_appendix_04/manifestation_publication_types/#sec-manifestation_publication_types).

For Manifestations, the Publication Event that originated the embodiment of a specific Work/Variant in a Manifestation, corresponds to criteria individuated to distinguish the boundaries between Manifestations.
For this reason, conceptually, and also in practice, “publication type” overlaps the main definition of “Manifestation type,” as explained in [Boundaries between Manifestations](/docs/03_moving_image_manifestations/boundaries_between_manifestations/#sec-boundaries_between_manifestations) and, as such, is already described.
Institutions have the option to decide whether to repeat this information or not.

- Publication date

Record the date on which Work/Variant or Manifestation was released or otherwise made available.
Dates should be formatted according to ISO 8601 or some other recognised standard.

- Region

Record the country or other political or physical geographic entity where the Publication Event took place (e.g. first projection in the framework of a theatrical distribution) or made the Work/Variant or Manifestation available (e.g. distribution area).

If known and considered of relevance, record the name of the city or smaller geographic entity where the Publication Event took place.

For the treatment of the geographical names, see Getty Thesaurus of Geographic Names (TGN), or some other recognised standard.

If known and considered of relevance, record the name of the event that the publication was a part of (e.g., name of a film festival, distribution channel of a broadcaster, etc.)

If known and considered of relevance, record the specific restrictions for accessing the content (e.g. press-screening only, airplanes only, etc.).

<a id="sec-awards_or_nominations"></a>
#### Award(s) or Nomination(s)[^fn1]
The bestowal of an award relating to the Work/Variant or Manifestation.
This excludes awards for Agents alone (e.g. “for lifetime achievement”), but includes awards for individual achievements within the context of a Work or Variant (e.g. “Best screenplay”).
Awards will usually be associated at the level of the Work, except for cases where features of a particular Variant are explicitly mentioned (e.g. “Best audio commentary for the visually impaired”) or the award relates to a particular Manifestation (such as a DVD edition).

An Award(s) or Nomination(s) Event may be associated with instances of Agent in the role of e.g. publisher, distributor, broadcaster[^fn7], etc. See [Distributor (theatrical)](/docs/12_appendix_04/manifestation_agent_types/#sec-distributor_theatrical) and [Work/Variant Agent Types](/docs/12_appendix_04/work_variant_agent_types/#sec-work_variant_agent_types).
If the award was given for the achievement of a specific Agent within the context of the Work/Variant or Manifestation, identify the Agent. Also used to identify Agents that have sponsored the award.

An Award(s) or Nomination(s) Event may be associated with instances of other Events during which award winners were selected (e.g. film festival).

Record all the existing relationships of a Publication Event, if the information is known and considered of relevance.

Award(s) or Nomination(s) Event information consists of the following sub-elements:

  - Award(s)/Nomination(s) date
  - Nomination only
  - Award name
  - Achievement

- Award(s)/Nomination(s) date

Record the date the award was bestowed on an Agent associated with the Work, Variant or Manifestation.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Nomination only

Indicate if the Work, Variant or Manifestation (or a specific achievement in the creation of it) was nominated but not among the winners.
This element can be realised in a system as a “flag.” If there was only a nomination, this element would be set to a logical value of “true.”

- Award name

The name of the award or trophy, possibly including a numeric designation (e.g. 2nd Prize)

- Achievement

A phrase describing a specific achievement for which the award was given, if not for the Work, Variant or Manifestation in total.

<a id="sec-production"></a>
#### Production[^fn2]
A distinct event in the course of production of a Work or Variant, including the main production event OR events that are separated in space and/or time from the main production event, or known with a greater amount of detail.
Examples are dates and locations where castings took place; dates and locations of shootings or other recordings; or dates and locations of particular post-production activities.

May include year/date of shooting of non-professional, actuality or unedited footage.

A Production Event may be associated with instances of Agent in the role of e.g. production company, location scout, etc. Selection should be made from a controlled list of values. See [Distributor (theatrical)](/docs/12_appendix_04/manifestation_agent_types/#sec-distributor_theatrical) and [Work/Variant Agent Types](/docs/12_appendix_04/work_variant_agent_types/#sec-work_variant_agent_types).

Record all the existing relationships of a Production Event, if the information is known and considered of relevance.

Production Event information consists of the following sub-elements:

  - Production Event type
  - Location
  - Region
  - Year/Date
  - Event details

- Production Event type

Selection should be made from a controlled list of values. See [Production Event Types](/docs/12_appendix_04/production_event_types/#sec-production_event_types).

- Location

Any geographic name(s) or address(es) of the location(s) where the event took place

- Region

The country or other large-scale geographic entity where the event took place

- Year/Date

The year/date or time-span during which the event took place. Dates should be formatted according to ISO 8601 or some other recognised standard.

- Event details

Any further information about the event either in plain textual form, or as an instance of a data type from another schema

<a id="sec-values_rights_copyright_ipr_registration"></a>
#### Rights/Copyright/IPR Registration[^fn3]
These are optional, and it is for an institution to choose whether it has the resources or requirement to compile rights data.
Further more detailed information on the subject of rights/copyright/IPR registration can be found in [Rights/Copyright/IPR Registration](/docs/17_appendix_09/).

A Copyright/IPR Registration Event is the act of registering copyright or intellectual property rights for a Work or Variant with an accredited agency.

A Copyright/IPR Registration Event may be associated with instances of Agent in the role of e.g. applicant, etc. Selection should be made from a controlled list of values.

Record all the existing relationships of a Copyright/IPR Registration Event, if the information is known and considered of relevance.

Copyright/IPR Registration Event information consists of the following sub-elements:

  - Registration Date
  - Registration Agency
  - Regional scope
  - Name of applicant
  - Registration number

- Registration date

The date on which the registration was filed or the date on which registration became effective.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Registration agency

Name of the agency issuing the registration certificate (e.g. “UK Intellectual Property Office,” name of a legal deposit library, etc.).

- Regional scope

The geographic region for which copyright is claimed.

- Name of applicant

Name of the Agent claiming copyright in the Work or Variant.

- Registration number

The number assigned by the registration agency.

<a id="sec-preservation"></a>
#### Preservation[^fn4]
A Preservation Event is associated with a new Variant, Manifestation or Items resulting from the preservation process in which the contents of one or more Items (or fragments thereof) from Manifestations of a Work were transferred with the intention of restoring or reconstructing the content as originally intended, or safeguarding it from decay.

This includes statements about past or future treatments scheduled for the item.[^fn8] If desired and if applicable, record one or more general types of past or future treatment activities (e.g. “added leaders”, “cleaned ultrasonically”, “tears repair”, etc.).
Selection should be made from a controlled list of values.

A Preservation Event has as typical Agent(s) the institution(s) or individual professionals that make preservation decisions.
Selection should be made from a controlled list of values. See [Distributor (theatrical)](/docs/12_appendix_04/manifestation_agent_types/#sec-distributor_theatrical) and [Work/Variant Agent Types](/docs/12_appendix_04/work_variant_agent_types/#sec-work_variant_agent_types).

A Preservation Event can be in relationship with instances of “Other” relationships (such as technical reports, documentation material, promotional material for the specific project, etc.).

Record all the existing relationships of a Preservation Event, if the information is known and considered of relevance.

Preservation Event information consists of the following sub-elements:

  - Preservation type
  - Preservation Date

- Preservation type

Record the general type of the preservation activity performed, for example, duplication, transfer, etc. Selection should be made from a controlled list of terms. See [Manifestation Preservation Types](/docs/12_appendix_04/manifestation_preservation_types/#sec-manifestation_preservation_types).

- Preservation Date

Record the date or time span in which the preservation activity was performed.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

Add in a note any information describing the preservation process in detail.

This can include:[^fn9]

  - Genesis of the project or reason why preservation was undertaken
  - Significant challenges
  - Relevant research (documenting sources of information related to content or production techniques)
  - Technical, aesthetic or ethical decisions
  - Recommendations for further work (details concerning limitations due to source material, resources, technology, etc.)

<a id="sec-decision"></a>
#### Decision[^fn5]
A Decision Event is an event in which a Manifestation of a certain Work/Variant is evaluated by a censorship body or an accredited rating agency.

A Decision Event may be associated with instances of Agent, e.g. in the role of the agency performing the rating or censorship.

A Decision Event may be associated with instances of “Other” relationship(s) (e.g., the original censorship documents).

Record all the existing relationships for the Decision Event, if the information is known and considered of relevance.

Decision event information consists of the following sub-elements:

  - Decision type
  - Decision date
  - Regional scope
  - Certificate number
  - Verdict
  - Decision type

- Decision type

Record the type or status of the decision event.
Usually the term adopted is “censorship” or “revision” for decisions mandated by law, “rating” for decisions under a voluntary scheme.
Further types may include special forms of evaluation, e.g. for tax privileges, as long as these are distinct from awards.

Selection should be made from a controlled list of terms. See [Manifestation Decision Types](/docs/12_appendix_04/manifestation_decision_types/#sec-manifestation_decision_types).

- Decision date

Record the date on which the verdict was announced or on which the verdict was declared valid. Dates should be formatted according to ISO 8601 or some other recognised standard.

- Regional scope

Record the geographic region for which the verdict is (was) valid.

- Certificate number

Record in Arabic numerals the number issued by the agency as a unique identifier of the act(s) of rating or censorship such as censorship visas or rating certificates.

- Verdict

Record the outcome of the act of rating or censorship.

<a id="sec-manufacture"></a>
#### Manufacture
A Manufacture Event represents a “common” event within which the embodiment of a Manifestation occurs, owing to the instances of a number of physical items that bear the same characteristics.

Therefore, the manufacture event of a moving image Manifestation corresponds to the activity within which it was fixed on a physical carrier, through particular technical processes such as film printing, telecine, video copying, digitisation, mastering, etc., or where it is saved to an “immaterial” medium, such as a digital file.

A Manufacture Event may be associated with instances of Agent, e.g. a laboratory that prints all the copies for a theatrical distribution or a studio that masters the DVDs for a home video publication.

A Manufacture Event may be associated with instances of “Other” relationship(s).

Record all the existing relationships for the Manufacture Event, if the information is known and considered of relevance.

Manufacture event information consists of the following sub-elements:

  - Manufacture type
  - Manufacture date
  - Manufacture region

- Manufacture type

Record the general type of the manufacture activity performed, for example, film printing, tele-cine, video copying, etc. Selection should be made from a controlled list of terms. See [Manifestation Manufacture Types](/docs/12_appendix_04/manifestation_manufacture_types/#sec-manifestation_manufacture_types).

- Date of Manufacture

Record the date or time span on which the Manufacture Event took place. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Region of Manufacture/embodiment

Record the country or other political or physical geographic entity where the Manufacture Event took place (e.g. the region/place where the laboratory was located).
(For the treatment of the geographical names, see Getty Thesaurus of Geographic Names (TGN), or some other recognised standard.)

If known and considered of relevance, record the name of the city or smaller geographic entity where the Manufacture Event took place.

<a id="sec-inspection"></a>
#### Inspection
The inspection of a particular Item for the purposes of assessing and recording the condition or treatment of the Item.

An Inspection Event may be associated with instances of Agent in the role of e.g. inventory archivist, projectionist, etc.

An Inspection Event may be associated with instances of “Other” relationship(s).

Record all the existing relationships for the Inspection Event, if the information is known and considered of relevance.

Inspection Event information consists of the following sub-elements:

  - Inspection type
  - Inspection date
  - Inspection detail

- Inspection type

The general type of inspection activity performed.

If desired and if applicable, record one or more general type(s) of the inspection activity performed (e.g. projection prep, inventory). Selection should be made from a controlled list of terms. This includes statements about past or future inspections scheduled for the item.[^fn10]

- Inspection date

The date or time span in which the inspection activity was performed. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Inspection detail

Information describing the condition of the Item in greater detail.

If desired and if applicable, record information about the condition of the Item, including nature and extent of damage. Selection should be made from a controlled list of terms. (See [Item Copy Condition Base/Emulsion – Film and Video](/docs/12_appendix_04/manifestation_item_condition_preservation_and_restoration/#sec-item_copy_condition_base_emulsion_film_and_video))

<a id="sec-acquisition"></a>
#### Acquisition
The acquisition of a particular Item for an institution’s collection.

An Acquisition Event may be associated with instances of Agent in the role of e.g. the institution or a person or set of persons in charge of acquisitions for the institution, etc.

An Acquisition Event may be associated with instances of “Other” relationship(s).

Record all the existing relationships for the Acquisition Event, if the information is known and considered of relevance.

An Acquisition Event information consists of the following sub-elements:

  - Acquisition type
  - Acquisition date
  - Acquisition source
  - Accession date
  - Acquisition detail

- Acquisition type

Describes the means by which the Item was acquired, for example, donation, exchange, loan, etc. Select from a controlled list of terms. See, [Item Acquisition type](/docs/12_appendix_04/manifestation_item_acquisition_accessioning_and_source/#sec-item_acquisition_type).

- Acquisition date

The date on which the Item was physically acquired. This date is distinct from an Accession date, which should be entered only once any required assessment has been completed, and the Item has been formally added to the inventory of the collection. (Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Acquisition source

The name of the person or organisation from which the Item was obtained, indicating whether the acquisition was direct from, for example, the donor or via an intermediary or agent. Select from a controlled list of terms. See [Item Acquisition type](/docs/12_appendix_04/manifestation_item_acquisition_accessioning_and_source/#sec-item_acquisition_type).

- Accession date

The date on which the Item was formally added to the inventory of the collection.
(Dates should be formatted according to ISO 8601 or some other recognised standard.)

- Acquisition detail

Information describing the acquisition of the Item in greater detail.

[^fn1]: EN 15907, 6.12 Award, pp. 25-26.
[^fn2]: Adapted from EN 15907 6.11 Production Event, p. 20
[^fn3]: EN 15907 6.15 IPR Registration, pp. 23-24
[^fn4]: EN 15907, 6.15 Preservation event, pp. 28-29
[^fn5]: EN 15907, 6.13 Decision event, pp. 26-27
[^fn6]: Some institutions specifically dealing with TV material may wish to use an actual “TV Transmission Manifestation” for this data.
[^fn7]: Some institutions specifically dealing with TV material may wish to use an actual “TV Transmission Manifestation” for this data.
[^fn8]: YCR 6.5, 6.6
[^fn9]: Based on in-house Academy Film Archive preservation documentation.
[^fn10]: YCR 6.5, 6.6

