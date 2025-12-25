
\newpage
\section{Moving Image Carriers} 
\label{sec:moving_image_carriers} 

\subsection{Definitions} 
\label{sec:moving_image_carriers_definition} 

Carriers are not mentioned in the EN15907 standard, and historically these have often been referenced, or data added in fields, within an Item or holdings record itself. They are referenced as being amongst the "Item specifics".

However, it is recognised that since 2011 developments in standards such as RDA [add footnote to https://www.rdaregistry.info/Elements/i/#P40009], and in some moving image database systems in response to client needs have meant that some institutions require this additional level of record, linked to a relevant Item as either an associated related record or even child record. 

The same logic and structures of EN15907 can be applied to Carrier records of an Item, i.e. that they too can be linked to Agents (e.g. names of individual technicians doing preservation work on a reel), Events (e.g. Preservation Event), etc. If not structured as a child record of an Item then they could equally constitute an "Other relation" relationship - again, this is not specified in the Other relation section of EN15907 standard itself regarding Items, but is logically implicit.

Institutions use carriers and their relationship to item differently.

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
