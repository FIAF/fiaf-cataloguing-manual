
\newpage
\section{Moving Image Item Components/Carriers (i.e. individual reels, tapes, files} 
\label{sec:moving_image_carriers} 

\subsection{Definitions} 
\label{sec:moving_image_carriers_definition} 

To avoid any confusion, "Item Components/Carriers" in this section is used to mean each individual reel, tape, or file that makes up the Item, e.g. a 4 reel film will have 4 Item Component/Carrier records associated with the one Item, one for each reel. This entity is not consistently named across institutions or systems - it is variously referred to as Carriers, Components, Units, Collect Copies, etc. 

In addition, the term "Carrier" is used by some institutions to denote the physical container (i.e. the film can, videotape box, and sometimes hard drives. Details about this can be found in the next section [ADD LINK TO Section to be headed Moving Image Carriers/Containers]

Item Components/Carriers are not mentioned in the EN15907 standard, and historically these have often been referenced, or data added in fields, within an Item or holdings record itself. That is also still the case on many holdings systems. For that reason they are not included in the hierarchy models at 0.2.1. Elements of description across Works, Variants, Manifestations, and Items. They are referenced as being amongst the "Item specifics".

However, it is recognised that since 2011 developments in standards such as RDA [add footnote to https://www.rdaregistry.info/Elements/i/#P40009], and structuring in some moving image database systems in response to needs, have meant that some institutions require this additional level of record, linked to a relevant Item as either an associated related record or even hierarchical child record. 

The same logic and structures of EN15907 can be applied to Item Component/Carrier records of an Item, i.e. that they too can be linked to Agents (e.g. names of individual technicians doing preservation work on a reel), Events (e.g. Preservation Event), etc. If not structured as a child record of an Item then they could equally constitute an "Other relation" relationship - again, this is not specified in the Other relation section of EN15907 standard itself regarding Items, but is logically implicit.

Institutions may use Item Components/Carriers and their relationship to Item differently, and may also vary in the levels of data captured, depending on an institution's requirements or cataloguing systems.

Example:
Some institutions understand carriers as each individual reel, tape, or file that makes up the Item, e.g. a four reel film will have four Carrier records associated with the one Item, one for each reel.
It is possible to record technical data at the Carrier level as it often pertains directly to a discrete barcoded physical object. 
Depending on the database and metadata structure in use, it can be collected at the Carrier level and then pulled from Carrier level to Item level for easier orientation or summarisation (e.g. total length).

Some elements which could be catalogued at Carrier level include:

1. Base, e.g. Nitrate, Acetate
2. Material type, e.g. Dup-positiv, Original-negative
3. Colour, e.g. Black & White
4. Aspect ratio, e.g. 1:1,35
5. Length of each reel or carrier, e.g. meters, minutes
6. Additional information on base type and stock if known
7.  inspection sheets
8. shelve number

Digital items are build following the same logic: one digital item can be made up from separate digital files (relating to each digitised reel), while an item can also consist of one carrier. Carrier does not equal the physical unit, where the file is stored (e.g. an LTO tape), but are linked via a UUID to the digital storage.

NEW SECTION
\section{Moving Image Containers/Carriers} 
\label{sec:moving_image_carriers} 

\subsection{Definitions} 
\label{sec:moving_image_carriers_definition} 

The individual film cans, videotape boxes, DVD boxes or sleeves, and hard drives in which the Moving Image Item Components/Carriers are stored. These usually have identification and location information physically attached, e.g. barcodes, can labels, etc.

In some institutions' systems these exist as records that are linked/associated to Item Components or Items.

As with Item Components/Carriers, depending on the database and metadata structure in use, it can be collected at the Container/Carrier level and then pulled through from that level to display within the Item level for user convenience.

It is possible to record technical data at the Container/Carrier level as it often pertains directly to a discrete barcoded physical object. 
