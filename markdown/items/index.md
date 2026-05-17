---
title: Moving Image Items
---
<a id="sec-moving_image_items_definition"></a>
## Definitions
A moving image Item is the physical or digital product of a Manifestation of a Work or Variant.

Whereas the Manifestation record describes the “ideal” of a particular format or publication, the Item record represents the actual holding in a repository’s collection.

An Item may consist of one or more parts (Item-parts), i.e. the whole Item may consist for example of 1 reel or 5 reels of analogue film, 2 VHS tapes, 1 DVD, a separate sound and image file, or files for each reel of film when digitised.
An Item record may contain fields or scope for separate barcodes and condition information for each Item-part of the Item (each can for example) if required.

The Item may be whole or incomplete or a fragment.
In the case of purely digital media, an Item is defined as the availability of the computer file, irrespective of the number of backup copies that may exist.[^1]

Institutions may also opt to catalogue the carrier with several Items on it, e.g. an LTO tape or a Harddrive with multiple digital files (either belonging to one work or several works), because there is no other option to list digital Items under a Manifestation in their databases. However, this practice cannot be recommended in the long run for the lack of clarity and impaired search options this may result in. Ideally digital files are treated like distinct Items with Item-parts where applicable.

Some examples of how institutions catalogue digital Items:

1. A 5 reel analogue film with image and sound has been digitised in a preservation project.
Under the same Manifestation as the analogue material the following Items are listed:
- Item 1: Raw Scan of the soundtrack (5 Item-parts)
- Item 2: Raw Scan of the image (5 Item-parts)
- Item 3: Master (combined sound+image) (1 Item-part)
- Item 4: Viewing File (combined sound+image made from Master) (1 Item-part)
- Item 5: DCDM (1 Item-part)
- Item 6: DCP (1 Item-part)
- Item 7: DVD (1 Item-part)

Each of these files has a UUID which creates the link to both the LTO-storage and, if applicable, to the server for quick access and online streaming. In every case, the LTO-tape or the Harddrive is not listed as Item, because these are considered Carriers which can contain other Items (and Item-parts) as well.
An institution may opt to create new Manifestations for digital Items, such as the streaming file or the DCP. This decision needs to be based on the institutions needs, strategy and resources.


[^1]: Digital medium definition taken from CEN’s “Film Identification – enhancing interoperability of metadata. Element sets and structures. FprEN 15907:2010 (E)

