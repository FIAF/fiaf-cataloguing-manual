---
title: Rights in an Item
weight: 2
---
<a id="sec-rights_in_an_item"></a>
### Rights in an Item
The rights in a moving image Item typically refer to the ownership (or transfer of ownership) of an object, either on a physical / analogue carrier such as a 35mm film print, or a digital file such as a DCP / DCDM or ProRes.
The transfer of ownership (sometimes referred to in legal terms as ‘transfer of title’) is important for an archive to document, as it establishes legal ownership of the collection.

Typically, the transfer involves a contract, deed or agreement signed by both parties to certify that ownership of the object is transferred to the archive, and often this is a complex legal document.
It is recommended therefore that the cataloguer capture the essential metadata elements below, and where feasible they should associate the catalogue record with an electronic version of the contract, by capturing filename / link to that document.

It should be understood that ownership of the Item does not imply any rights to exploit the Work, as outlined in the Manifestation section (for example, to digitise the object and display online, or distribute to cinemas); and it certainly does not imply any change in the intellectual property rights in the work itself.
However, often during acquisition decision-making, an archive will undertake research into the broader rights context: is the work in or out of copyright?; if it is, who owns that copyright?; if they are unknown can it be considered an orphan work?; has it been registered as such?; if it is not an orphan work?, who owns the exploitation rights in the relevant territories, platforms?
Cataloguers should therefore consider capturing details of this rights check activity when documenting the transfer of ownership of the item.

Particular acquisition agreements between object owner and archive may enforce restrictions on the archive, preventing them from undertaking certain activities on the item (for example, preventing them from digitising the item for preservation, or preventing them from exhibiting the item in internal cinema).
Any such restrictions should be captured in a ‘Provisos of acquisition’, ‘Conditions of access’ or ‘Conditions of reproduction’ set of fields, as outlined below.
In addition, the acquisition agreement may enforce a protocol for disposal of any objects which are not ultimately accessioned into the archive’s permanent collection: for example, disposal may require approval by acquisition source.

However, it is important to note that any acquisition agreement or contract must not undermine the archive’s rights under law.
For example, in the UK, under recent legislative changes (Copyright Exceptions) a moving image archive has the right to ‘copy works for archiving and preservation reasons if they are part of a permanent collection and it is not reasonably practicable to purchase a replacement’ (from https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/375956/Libraries_Archives_and_Museums.pdf).
Therefore a specific acquisition agreement could not attempt to prevent
that right to copy for preservation.

In the United States, an archive’s right to copy for access and preservation is covered under Section 108.
However, this section only applies to archives and libraries with specific qualifications.[^fn1] The current Register of Copyrights has set revising Section 108 as one of her priorities.[^fn2]

In Italy, since 2004, the Cineteca Nazionale can legally use the copies acquired by legal deposit (3 years after the deposit), or by copying/printing for cultural and non-profit purposes by way of derogation from copyright law.

Below, a set of properties are recommended for describing the rights around the Acquisition, and separately around the Loan, of moving image items.

<a id="sec-recommended_properties_to_capture3"></a>
#### Recommended properties to capture in describing the rights context of a moving image Item
<a id="sec-copyright_acquisition"></a>
##### Acquisition
See also [Acquisition](/docs/12_appendix_04/event_type/#sec-acquisition)

This section is drawn from BFI policies.

1. Internal staff contact name: Captures the name of the staff member responsible for progressing and completing the agreement.

2. Agreement status: Captures the current stage in the completion of the agreement.

  a. In progress

  b. Hardcopy agreement sent

  c. Signed hardcopy agreement received

  d. Completed

3. Agreement completion date: Captures the date from which the agreement is considered as having legally come into effect e.g. the latest date recorded on a signed hardcopy of an Acquisition agreement.

4. Acquisition method: Denotes the form of acquisition represented by the record, e.g. a donation, a bequest left in the will of a benefactor, or an internally produced off-air recording.

  a. Bequest

  b. Commission

  c. Donation

  d. Off-air recording

  e. Purchase

  f. Unknown

5. Acquisition source: Represents the person or institution through which the BFI is receiving the acquisition. Where possible, this should take the form of a link to a record within the archive’s Persons and Institutions authority dataset.

6. Acquisition source type: Qualifies the relationship between the Acquisition and the Acquisition source – i.e. is the acquisition source the legal owner of the item, or are they the authorised agent of the owner acting on their behalf such as in the case of a bequest or purchase through auction.

  a. Item Owner

  b. Agent

7. Acquisition source contact details: Captures the contact details of the acquisition source, primarily their postal address. Alternatively, where possible, this could be captured in the associated Person and Institution record.

8. Acquisition purchase price: Captures the price paid for the purchase of the complete acquisition as a integer.

9. Acquisition funding source: Captures the source of acquisition funding. This could represent funding secured through an external organisation, benefactor, or an internal budget.

10. Acquisition purchase currency: Qualifies the content of the Acquisition purchase price field with the currency of the purchase. Suggest using 3-character ISO 4217 codes.

11. Initial rights check status: Indicates the status of initial rights checks required as part of the acquisition process.

  a. Rights holder(s) recorded in Work record

  b. Rights holder is Acquisition source

  c. Rights holder could not be identified

12. Acquisition date: Captures the date on which the agreement was signed – this is the date on which the agreement becomes legally binding. In some context, instead of this signature date, archives capture the date on which the Item physically entered the premises / infrastructure of the archive. Using this ‘entry date’ can be problematic, as items can arrive onsite before agreement is signed, or can arrive without any form of signature or indeed knowledge that it is in transit i.e. receipt of an unsolicited deposit. Therefore it is recommended to use the signature date.

13. Accession date: Captures the date on which the Item formally entered the collection of the archive. Often this definition is dependent on formal documentation within the archive’s collections management system, with a unique accession reference / identifier assigned.

14. Acquisition rationale: Text field or controlled field allowing the staff responsible for the acquisition to capture the rationale behind the acquisition in relation to the archive’s published collecting policy or other formal governance model.

15. Acquisition authoriser: Captures the name of the senior member of staff who approves the acquisition in question.

16. Acquisition authorisation date: Captures the date that the acquisition was approved by a senior member of staff.

17. Acquisition provisos: Captures any provisos or clauses agreed with the acquisition source e.g any form of access/publication embargo. Note that this should not undermine the archive’s rights under law. This may be captured using a text field, or it may be controlled. And if required, it may be broken out into specific proviso areas as in 18 and 19 below.

18. Conditions governing reproduction: Text field or controlled field to capture specific restrictions on the archive’s ability to copy the item in the analogue or digital domain, for preservation or other purposes. Note that this should not undermine the archive’s rights under law.

19. Conditions governing access: Text field or controlled field to capture specific restrictions on the archive’s ability to offer internal or external access to the item, for research or commercial purposes. Note that this should not undermine the archive’s rights under law.

20. Provisos expiry date: Captures the date upon which the associated proviso expires, if at all – e.g. the end of a publication embargo.

21. Item reproduction requested: Captures whether the supply of a duplicate copy to the acquisition source is one of the terms of acquisition agreed with the acquisition source.

22. Item reproduction terms: Captures the terms under which reproduction of the acquired material will be supplied to the Acquisition source.

  a. Reproduction at Acquisition source expense

  b. Reproduction at mutually agreed expense

  c. Reproduction at archive’s expense

23. Item reproduction notes: Field to allow the terms of reproduction to be further qualified, e.g. the exact division of mutually agreed expense for reproduction.

24. Terms of disposal for unaccessioned items: Records the agreed method of disposal for material not being accessioned into the archive’s permanent collections, as authorised by the Acquisition source.

  a. Return to acquisition source

  b. Transfer to another institution

  c. Archive authorised to dispose

25. Filename of agreement: Capture the filename of an electronic version of the Acquisition agreement, or where possible a link to the file in a persistent, available directory within the organisation’s infrastructure.

<a id="sec-loan"></a>
##### Loan
1. This section outlines the properties that are specific to Loan agreements, distinct from Acquisitions

2. Lender: Represents the person or institution from which the archive is receiving the loan. Where possible, this should take the form of a link to a record within the archive’s Persons and Institutions authority dataset.

3. Lender type: Qualifies the relationship between the Lender and the Acquisition source – i.e. is the lender the legal owner of the item, or are they the authorised agent of the owner acting on their behalf.

  a. Item Owner

  b. Agent

4. Lender contact details: Captures the contact details of the lender, primarily their postal address. Alternatively, where possible, this could be captured in the associated Person and Institution record.

5. Loan start date: Captures the agreed date from which the loan commences.

6. Loan end date: Captures the end date of the loan, as defined prior to the commencement of the loan.

7. Item reproduction requested: Captures whether the supply of a duplicate copy to the lender is one of the terms of loan agreed with the lender.

8. Item reproduction terms: Captures the terms under which reproduction of the loaned material will be supplied to the lender.

  a. Reproduction at Lender expense

  b. Reproduction at mutually agreed expense

  c. Reproduction at archive’s expense

9. Item reproduction notes: Field to allow the terms of reproduction to be further qualified, e.g. the exact division of mutually agreed expense for reproduction.

10. Filename of agreement: Capture the filename of an electronic version of the Loan agreement, or where possible a link to the file in a persistent, available directory within the organisation’s infrastructure.

[^fn1]: http://www.copyright.gov/title17/92chap1.html#108
[^fn2]: http://search.copyright.gov/search?utf8=%E2%9C%93&affiliate=copyright&query=section+108

