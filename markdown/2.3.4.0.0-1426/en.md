2.3.4 Format of a moving image Manifestation

As  previously  mentioned,  a  Manifestation  is  defined  on  the  basis  of  two  criteria:
changes in the publication context and changes in format. The format of a Manifesta-
tion is the description of the physical artefact or the digital file on which it is fixed. The
concept of format as applied to Manifestations is the “ideal” representation of all the
physical items or computer files that bear the same characteristics and descend from a
common Work/Variant, regardless of what is actually held in a collection.

A  majority  of  the  physical  and  digital  description  elements  of  moving  im-
age  Manifestations  are  intended  to  be  inherited  by  the  Items,  as  they  serve  as
the  exemplars  of  Manifestations.  In  some  databases,  selection  of  a  physical  car-
rier  type  initiates  provision  of  element  fields  relevant  to  that  type  at  a  Man-
ifestation  level,  or  an  Item  level,  or  both  (e.g.  in  a  2-Level  hierarchy.  See  “Shal-
low  hierarchy  model:  2  levels”  found  at  0.2.1  Elements  of  description  across  Works,
Variants, Manifestations, and Items).

Ideally the information need only be recorded once irrespective of where in the data
structure an institution must place it. Therefore guidelines for the treatment of high-level
physical and digital description elements are explained fully in the Manifestation chap-
ter. The Item chapter contains a detailed listing of item-specific elements. Physical prop-
erties such as Extent and Format at the Manifestation level represent the “ideal,” and
item-specific elements will capture where it differs from this “ideal” at the Item level.

The information about the format of a Manifestation plays a relevant role because any
change in format represents a criterion to determine the boundaries between one Man-
ifestation and another (see 2.1 Boundaries between Manifestations).




Record a new Manifestation of a Work/Variant when there is evidence of at least one,

or more than one, of the following changes associated with the format:

•	 Changes to the physical artefact or the digital file on which it is fixed
•	 Changes to the display characteristics (i.e. in aspect ratio, sound or colour

characteristics, etc.)

•	 Change in the container (i.e. cassette to cartridge as container for a tape).

In  a  note  (See  Appendix  B,  Cataloguer’s  Notes),  explain  the  format  changes  used  to
determine  the  Manifestation  in  hand  as  different  and  “new”  in  comparison  with  any
other, already identified and described Manifestation.

The description of the format of a Manifestation is articulated in the following elements:

•	 Carrier type
•
Projection characteristics
•
Sound characteristics
•	 Colour characteristics

2.3.4.1 Carrier type of a Manifestation

Carrier type is the medium on or the encoding format in which the Manifestation is fixed.

Its description consists of a general carrier type, which describes the basic properties
of  the  Manifestation’s  physical  format,  for  example,  film,  video  tape,  digital  file,  etc.,
and a specific carrier type, which corresponds to the gauge, in case of films and tapes,
and for digital files, to the physical carrier on which the file is stored.

2.3.4.1.1 General Carrier Type

The broad media type of the Manifestation (e.g., film, video, audio, optical, digital
file). Recording this high-level information will enable simple searching for only film, vid-
eo, digital, etc. elements rather than searching by all possible formats and carriers.

A suggested list, which is open and not exhaustive, can be found in D.7.2 Manifesta-

tion/Item Specific Carrier Type.

For reasons of clarity and to avoid redundancy, optionally, institutions can decide to skip

the general carrier type description, since it is already implicit in the specific carrier type.

2.3.4.1.2 Specific Carrier Type

Record the specific carrier type, by indicating

1)   For film and video: the width of the film stock or of the magnetic tape on which

the Manifestation is fixed;

2)  For digital files: The physical carrier storing the digital file.



For digital files, it is most important for users to immediately identify the file contain-
er or wrapper (MXF, MOV, DPX, etc.) rather than the physical media on which it is stored.
Physical media storing a file can change, but that does not necessarily mean that the file
format has changed. For purposes of distinguishing the format change that constitutes
a  new  Manifestation,  it  is  the  digital  file  format  that  is  the  important  distinguishing
factor. Information on the specific codecs and resolution are captured in Item elements.

For optical media, only add commercially produced media here. If the optical media
is “writable” and is being used to store a digital file, put the digital file format in the gen-
eral carrrier type, and the optical storage media in specific media type.

Select the value from a suitable controlled list. A suggested list, which is open and not

exhaustive, can be found in D.7.2 Manifestation/Item Specific Carrier Type.

2.3.4.2 Projection characteristics of a Manifestation

The projection characteristics of a Manifestation include aspect ratio and aperture

or image format.

Aspect Ratio

The aspect ratio (also known as projection ratio) is the projected image area visible
on screen, expressed as a value of width to height (the value of height always being “1”),
for example, 2.34:1, 2.39:1. Selection should be made from a controlled list of values. A
suggested list, which is open and not exhaustive, can be found in D.7.14 Aspect Ratio.

The aspect ratio reflects the compositional intentions of the original content makers
and the intended presentation of the moving image content.89 If the aspect ratio of a
Work/Variant  is  altered,  moving  image  information  is  lost,  creating  a  Manifestation/
Item with different moving image content.90 The Manifestation should reflect the pro-
jected image of the Work/Variant that it represents, rather than that on the Item. Insti-
tutions may record variations in projection characteristics as Item-specifics, rather than
create multiple Manifestations.

Aperture/Image Format

The actual exposed image or picture area as it appears on the moving image itself, for
example Academy, Full screen, Widescreen, etc. The image format does not necessarily
bear any relation to the preferred projection ratio (aspect ratio) of the moving image.91
Selection should be made from a controlled list of terms. A suggested list, which is open
and not exhaustive, can be found in D.7.15 Aperture.

89  This definition from Academy Film Archive in-house glossary of terms, and OLAC, Moving Image Works,
Part 3a: Operational Definitions (08/09) (PDF Document), http://olacinc.org/drupal/capc_files/MIW_3a.pdf.
90  OLAC, Moving Image Works, Part 3a: Operational Definitions (08/09) (PDF Document), http://olacinc.org/
drupal/capc_files/MIW_3a.pdf
91  This definition from Academy Film Archive in-house glossary of terms.



2.3.4.3 Sound characteristics of a Manifestation

Sound characteristics are technical specifications relating to the placement of sound

on a Manifestation.92

Its description consists of a statement about the presence or absence of sound, and
optionally, in case of presence, of the description of the method with which the sound
has been fixed.

Indicate the presence or absence of sound in the Manifestation, i.e. “sound,” “silent,”
“mute”. Selection should be made from a controlled list of terms. A suggested list, which
is open and not exhaustive, can be found in D.7.4 Manifestation/Item Sound Type.

Optionally,  use  a  flag-type  value  indicating  if  the  Manifestation  includes  recorded

sound or not (i.e.: has sound: yes/no).

2.3.4.3.1 Sound systems

Describes the technical or proprietary system used to record the sound on a Manifes-
tation/Item, for example, Dolby SR, Dolby Digital, etc. Select from a controlled list. A sug-
gested list, which is open and not exhaustive, can be found in D.7.13 Item Sound System.

2.3.4.3.2 Sound Channel Configuration

If the Manifestation has sound, note here the track configuration (e.g., mono, ste-

reo, etc.). Selection should be made from a controlled list of terms.

In case of presence of sound, optionally, if considered relevant, record the name of
the physical principle of sound recording, for example, “Needle,”, “Optical,” “Magnetic,”
etc. Selection should be made from a controlled list of terms. A suggested list, which is
open and not exhaustive, can be found in D.7.5 Manifestation/Item Sound Fixation Type.

If the Work/Variant associated with the Manifestation in hand had sound originally, but
the Manifestation lacks sound, describe it as silent (or mute) and give a note to that effect.93

If the Work/Variant associated with the Manifestation in hand was silent originally, but

the Manifestation has sound added, describe it as sound and make a note to that effect.

2.3.4.4 Colour characteristics of a Manifestation

The presence of colour(s), tone(s), etc. in a Manifestation.94

Colour is also the specific colours, tones, etc. (including black and white) present in a

moving image contained in a Manifestation.95

92  RDA 3.17. 01
93  Based on AMIM2 5C3.
94  RDA 7.17.3 Colour of Moving Image
95  RDA 7.17.3 Colour of Moving Image



It consists of a designation of the colour state and, optionally, of the description of

the colour system.

Record the colour state of a Manifestation, for example, Black and white (tinted), Colour,
Colour + Black & White, etc. Selection should be made from a controlled list of terms. A suggest-
ed list, which is open and not exhaustive, can be found in D.7.11 Manifestation/Item Colour Type.

Optionally,  if  considered  relevant,  describe  the  system  or  process  by  which  colour  is
fixed on the carrier or as part of the digital encoding, for example, Pathécolor, Technicolor,
RGB, , etc. Selection should be made from a controlled list of terms. A suggested list, which
is open and not exhaustive, can be found in D.7.12 Manifestation/Item Colour Standard.
