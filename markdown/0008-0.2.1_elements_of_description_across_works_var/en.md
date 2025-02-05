# 0.2.1 Elements of description across Works, Variants, Manifestations, and Items {#manual-0.2.1}

This section includes sample structures for how the elements can be applied across Works, Variants, Manifestations, and Items.
Four models are provided, beginning with the more complete four-level model and ending with a simple one-level model.
Models should be applied according to an institution’s system and also determined by the amount of information known about an Item.

The full list of elements of description for each entity is set out in the following charts and diagrams, and in Chapters 1-3.
See Appendix I, Examples of records containing core elements in the different levels of hierarchy for examples of real records which contain these core elements (as well as others) across the hierarchies.

\newpage
```pikchr
$line_width = 3.5
$line_height = 0.2

$work_y = -2
$variant_y = -6
$manifestation_y = -10
$item_y = -14
$text_x = 3.75

# LABEL

box ht 0.5 wid 8.5 rad 5px "Extended hierarchy model: 4 levels" bold fill lightgreen at (2.5, 0.5)

# WORK

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightgreen at ($text_x-1, $work_y)

B2: box ht $line_height wid $line_width rad 5px \
"- Type - Whole conditions (serial / standalone / component part)" \ 
ljust color none fill lightgreen at ($text_x, $work_y+0.8)

B2: box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill lightgreen at ($text_x, $work_y+0.6)

B2: box ht $line_height wid $line_width rad 5px \
"- Titles (original, alternative, series/serial)" \ 
ljust color none fill lightgreen at ($text_x, $work_y+0.4)

B2: box ht $line_height wid $line_width rad 5px \
"- Country (production country/countries)" \ 
ljust color none fill lightgreen at ($text_x, $work_y+0.2)

B2: box ht $line_height wid $line_width rad 5px \
"- Dates (copyright / production)" \ 
ljust color none fill lightgreen at ($text_x, $work_y)

B2: box ht $line_height wid $line_width rad 5px \
"- Language(s): original language of conception/presentation" \ 
ljust color none fill lightgreen at ($text_x, $work_y-0.2)

B2: box ht $line_height wid $line_width rad 5px \
"- Notes/History" \ 
ljust color none fill lightgreen at ($text_x, $work_y-0.4)

B2: box ht $line_height wid $line_width rad 5px \
"- Content: Synopsis, Genre, Form, Subject" \ 
ljust color none fill lightgreen at ($text_x, $work_y-0.6)

B2: box ht $line_height wid $line_width rad 5px \
"- Agents: Cast, Credits, Rights holders " \ 
ljust color none fill lightgreen at ($text_x, $work_y-0.8)

box ht 3.5 wid 3.5 rad 5px "WORK" "abstract entity" fill lightgreen at (0, $work_y)

# VARIANT

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightgreen at ($text_x-1, $variant_y)

box ht $line_height wid $line_width rad 5px \
"- Type - Whole conditions (serial / standalone / component part)" \ 
ljust color none fill lightgreen at ($text_x, $variant_y+0.8)

box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill lightgreen at ($text_x, $variant_y+0.6)

box ht $line_height wid $line_width rad 5px \
"- Titles (original, alternative, series/serial)" \ 
ljust color none fill lightgreen at ($text_x, $variant_y+0.4)

box ht $line_height wid $line_width rad 5px \
"- Country (production country/countries)" \ 
ljust color none fill lightgreen at ($text_x, $variant_y+0.2)

box ht $line_height wid $line_width rad 5px \
"- Dates (copyright / production)" \ 
ljust color none fill lightgreen at ($text_x, $variant_y)

box ht $line_height wid $line_width rad 5px \
"- Language(s)" \ 
ljust color none fill lightgreen at ($text_x, $variant_y-0.2)

box ht $line_height wid $line_width rad 5px \
"- Notes/History" \ 
ljust color none fill lightgreen at ($text_x, $variant_y-0.4)

box ht $line_height wid $line_width rad 5px \
"- Content: Synopsis, Genre, Form, Subject" \ 
ljust color none fill lightgreen at ($text_x, $variant_y-0.6)

box ht $line_height wid $line_width rad 5px \
"- Agents: Cast, Credits, Rights holders " \ 
ljust color none fill lightgreen at ($text_x, $variant_y-0.8)

box ht 3.5 wid 3.5 rad 5px "VARIANT" "abstract entity" "optional" fill lightgreen at (0, $variant_y)

# MANIFESTATION

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightgreen at ($text_x-1, $manifestation_y)

box ht $line_height wid $line_width rad 5px "- Type - pre-release, theatrical, non-theatrical," \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y+0.9)

box ht $line_height wid $line_width rad 5px  \
"  transmission, home-viewing, internet, restoration, not-for-release, etc" \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y+0.7)

box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y+0.5)

box ht $line_height wid $line_width rad 5px \
"- Titles" \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y+0.3)

box ht $line_height wid $line_width rad 5px \
"- Language(s): language of dialogue, subtitles, dubbing, intertitles, etc. " \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y+0.1)

box ht $line_height wid $line_width rad 5px \
"- Format: 35mm film, Digital Cinema Package (DCP), Blu-ray, etc" \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y-0.1)

box ht $line_height wid $line_width rad 5px \
"- Extent: physical, logical, temporal, e.g. duration, running time, length, etc." \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y-0.3)

box ht $line_height wid $line_width rad 5px \
"- Event: release, transmission, distribution, creation, dates" \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y-0.5)

box ht $line_height wid $line_width rad 5px \
"- Rights context: platforms, territories, dates  " \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y-0.7)

box ht $line_height wid $line_width rad 5px \
"- Agents: Creator, Broadcaster, Distributor, Publisher" \ 
ljust color none fill lightgreen at ($text_x, $manifestation_y-0.9)

box ht 3.5 wid 3.5 rad 5px "MANIFESTATION" "realisation, release, exhibition" "or distribution entity " fill lightgreen at (0, $manifestation_y)

# ITEM

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightgreen at ($text_x-1, $item_y)

box ht $line_height wid $line_width rad 5px \
"- Identifier (inventory numbers) " \ 
ljust color none fill lightgreen at ($text_x,$item_y+1.5)

box ht $line_height wid $line_width rad 5px \
"- Element Type : instantiation type, e.g. original negative," \ 
ljust color none fill lightgreen at ($text_x,$item_y+1.3)

box ht $line_height wid $line_width rad 5px \
"  dupe positive, Lavender, sound negative" \ 
ljust color none fill lightgreen at ($text_x,$item_y+1.1)

box ht $line_height wid $line_width rad 5px \
"- Item specifics: carrier, base, gauge, format, digital file type," \ 
ljust color none fill lightgreen at ($text_x,$item_y+0.9)

box ht $line_height wid $line_width rad 5px \
" sound, sound systems, colour standards etc" \ 
ljust color none fill lightgreen at ($text_x,$item_y+0.7)

box ht $line_height wid $line_width rad 5px \
"- Extent: physical, temporal, e.g. footage, file size, duration" \ 
ljust color none fill lightgreen at ($text_x,$item_y+0.5)

box ht $line_height wid $line_width rad 5px \
"- Access conditions: Condition report - pristine, not for projection," \ 
ljust color none fill lightgreen at ($text_x, $item_y+0.3)

box ht $line_height wid $line_width rad 5px \
"heavy scratch- es, etc; storage location - home location, current location;" \ 
ljust color none fill lightgreen at ($text_x, $item_y+0.1)

box ht $line_height wid $line_width rad 5px \
"- Conservation recom-   mendations: urgent transfer required,"  \ 
ljust color none fill lightgreen at ($text_x, $item_y-0.1)

box ht $line_height wid $line_width rad 5px \
"relocate to sub-zero,  etc " \ 
ljust color none fill lightgreen at ($text_x, $item_y-0.3)

box ht $line_height wid $line_width rad 5px \
"- Event(s) (with Dates): creation, acquisition, accession, " \ 
ljust color none fill lightgreen at ($text_x, $item_y-0.5)

box ht $line_height wid $line_width rad 5px \
" de-accession, loan, transport  " \ 
ljust color none fill lightgreen at ($text_x, $item_y-0.7)

box ht $line_height wid $line_width rad 5px \
"- Acquisition: source, method, funding context, " \ 
ljust color none fill lightgreen at ($text_x, $item_y-0.9)

box ht $line_height wid $line_width rad 5px \
"conditions of access, dates" \ 
ljust color none fill lightgreen at ($text_x, $item_y-1.1)

box ht $line_height wid $line_width rad 5px \
"- Agents: donors, archive technicians/conservationists, etc." \ 
ljust color none fill lightgreen at ($text_x, $item_y-1.3)

box ht $line_height wid $line_width rad 5px \
"- Holding institution: name of the Item holde" \ 
ljust color none fill lightgreen at ($text_x, $item_y-1.5)

box ht 3.5 wid 3.5 rad 5px "ITEM" "physical or digital" "object" fill lightgreen at (0, $item_y)
```

\newpage
```pikchr

$line_width = 3.5
$line_height = 0.2

$work_y = -2
$manifestation_y = -6
$item_y = -10
$text_x = 3.75

# LABEL

box ht 0.5 wid 8.5 rad 5px "Full hierarchy model: 3 levels" bold fill lightblue at (2.5, 0.5)

# WORK

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightblue at ($text_x-1, $work_y)

B2: box ht $line_height wid $line_width rad 5px \
"- Type - Whole conditions (serial / standalone / component part)" \ 
ljust color none fill lightblue at ($text_x, $work_y+0.6)

B2: box ht $line_height wid $line_width rad 5px \
"- Titles (original, alternative, series/serial)" \ 
ljust color none fill lightblue at ($text_x, $work_y+0.4)


B2: box ht $line_height wid $line_width rad 5px \
"- Dates (copyright / production)" \ 
ljust color none fill lightblue at ($text_x, $work_y+0.2)


B2: box ht $line_height wid $line_width rad 5px \
"- Language(s): original language of conception/presentation" \ 
ljust color none fill lightblue at ($text_x, $work_y)


B2: box ht $line_height wid $line_width rad 5px \
"- Content: Synopsis, Genre, Form, Subject" \ 
ljust color none fill lightblue at ($text_x, $work_y-0.2)


B2: box ht $line_height wid $line_width rad 5px \
"- Agents: Cast, Credits, Rights holders " \ 
ljust color none fill lightblue at ($text_x, $work_y-0.4)


B2: box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill lightblue at ($text_x, $work_y-0.6)


box ht 3.5 wid 3.5 rad 5px "WORK" "abstract entity" fill lightblue at (0, $work_y)

# MANIFESTATION

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightblue at ($text_x-1, $manifestation_y)


box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill lightblue at ($text_x, $manifestation_y+0.9)


box ht $line_height wid $line_width rad 5px \
"- Titles" \ 
ljust color none fill lightblue at ($text_x, $manifestation_y+0.7)

box ht $line_height wid $line_width rad 5px "- Type - pre-release, theatrical, non-theatrical," \ 
ljust color none fill lightblue at ($text_x, $manifestation_y+0.5)

box ht $line_height wid $line_width rad 5px  \
"  transmission, home-viewing, internet, restoration, not-for-release, etc" \ 
ljust color none fill lightblue at ($text_x, $manifestation_y+0.3)

box ht $line_height wid $line_width rad 5px \
"- Language(s): language of dialogue, subtitles, dubbing, intertitles, etc. " \ 
ljust color none fill lightblue at ($text_x, $manifestation_y+0.1)

box ht $line_height wid $line_width rad 5px \
"- Format: 35mm film, Digital Cinema Package (DCP), Blu-ray, etc" \ 
ljust color none fill lightblue at ($text_x, $manifestation_y-0.1)

box ht $line_height wid $line_width rad 5px \
"- Extent: physical, logical, temporal, e.g. duration, running time, length, etc." \ 
ljust color none fill lightblue at ($text_x, $manifestation_y-0.3)

box ht $line_height wid $line_width rad 5px \
"- Event: release, transmission, distribution, creation, dates" \ 
ljust color none fill lightblue at ($text_x, $manifestation_y-0.5)

box ht $line_height wid $line_width rad 5px \
"- Rights context: platforms, territories, dates  " \ 
ljust color none fill lightblue at ($text_x, $manifestation_y-0.7)

box ht $line_height wid $line_width rad 5px \
"- Agents: Creator, Broadcaster, Distributor, Publisher" \ 
ljust color none fill lightblue at ($text_x, $manifestation_y-0.9)

box ht 3.5 wid 3.5 rad 5px "MANIFESTATION" "realisation, release, exhibition" "or distribution entity " fill lightblue at (0, $manifestation_y)

# ITEM

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightblue at ($text_x-1, $item_y)

box ht $line_height wid $line_width rad 5px \
"- Identifier (inventory numbers) " \ 
ljust color none fill lightblue at ($text_x,$item_y+1.6)

box ht $line_height wid $line_width rad 5px \
"- Titles (original, alternative) " \ 
ljust color none fill lightblue at ($text_x,$item_y+1.4)

box ht $line_height wid $line_width rad 5px \
"- Element Type : instantiation type, e.g. original negative," \ 
ljust color none fill lightblue at ($text_x,$item_y+1.2)

box ht $line_height wid $line_width rad 5px \
"  dupe positive, Lavender, sound negative" \ 
ljust color none fill lightblue at ($text_x,$item_y+1)

box ht $line_height wid $line_width rad 5px \
"- Item specifics: carrier, base, gauge, format, digital file type," \ 
ljust color none fill lightblue at ($text_x,$item_y+0.8)

box ht $line_height wid $line_width rad 5px \
" sound, sound systems, colour standards etc" \ 
ljust color none fill lightblue at ($text_x,$item_y+0.6)

box ht $line_height wid $line_width rad 5px \
"- Extent: physical, temporal, e.g. footage, file size, duration" \ 
ljust color none fill lightblue at ($text_x,$item_y+0.4)

box ht $line_height wid $line_width rad 5px \
"- Access conditions: Condition report - pristine, not for projection," \ 
ljust color none fill lightblue at ($text_x, $item_y+0.2)

box ht $line_height wid $line_width rad 5px \
"heavy scratch- es, etc; storage location - home location, current location;" \ 
ljust color none fill lightblue at ($text_x, $item_y+0)

box ht $line_height wid $line_width rad 5px \
"- Conservation recom-   mendations: urgent transfer required,"  \ 
ljust color none fill lightblue at ($text_x, $item_y-0.2)

box ht $line_height wid $line_width rad 5px \
"relocate to sub-zero,  etc " \ 
ljust color none fill lightblue at ($text_x, $item_y-0.4)

box ht $line_height wid $line_width rad 5px \
"- Event(s) (with Dates): creation, acquisition, accession, " \ 
ljust color none fill lightblue at ($text_x, $item_y-0.6)

box ht $line_height wid $line_width rad 5px \
" de-accession, loan, transport  " \ 
ljust color none fill lightblue at ($text_x, $item_y-0.8)

box ht $line_height wid $line_width rad 5px \
"- Acquisition: source, method, funding context, " \ 
ljust color none fill lightblue at ($text_x, $item_y-1)

box ht $line_height wid $line_width rad 5px \
"conditions of access, dates" \ 
ljust color none fill lightblue at ($text_x, $item_y-1.2)

box ht $line_height wid $line_width rad 5px \
"- Agents: donors, archive technicians/conservationists, etc." \ 
ljust color none fill lightblue at ($text_x, $item_y-1.4)

box ht $line_height wid $line_width rad 5px \
"- Holding institution: name of the Item holde" \ 
ljust color none fill lightblue at ($text_x, $item_y-1.6)

box ht 3.5 wid 3.5 rad 5px "ITEM" "physical or digital" "object" fill lightblue at (0, $item_y)
```

\newpage

```pikchr

$line_width = 3.5
$line_height = 0.2

$work_y = -2
$manifestation_y = -6
$item_y = -10
$text_x = 3.75

# LABEL

box ht 0.5 wid 8.5 rad 5px "Shallow hierarchy model: 2 levels" bold fill lightpink at (2.5, 0.5)

# WORK

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightpink at ($text_x-1, $work_y)

B2: box ht $line_height wid $line_width rad 5px \
"- Type - Whole conditions (serial / standalone / component part)" \ 
ljust color none fill lightpink at ($text_x, $work_y+0.6)

B2: box ht $line_height wid $line_width rad 5px \
"- Titles (original, alternative, series/serial)" \ 
ljust color none fill lightpink at ($text_x, $work_y+0.4)


B2: box ht $line_height wid $line_width rad 5px \
"- Dates (copyright / production)" \ 
ljust color none fill lightpink at ($text_x, $work_y+0.2)


B2: box ht $line_height wid $line_width rad 5px \
"- Language(s): original language of conception/presentation" \ 
ljust color none fill lightpink at ($text_x, $work_y)


B2: box ht $line_height wid $line_width rad 5px \
"- Content: Synopsis, Genre, Form, Subject" \ 
ljust color none fill lightpink at ($text_x, $work_y-0.2)


B2: box ht $line_height wid $line_width rad 5px \
"- Agents: Cast, Credits, Rights holders " \ 
ljust color none fill lightpink at ($text_x, $work_y-0.4)


B2: box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill lightpink at ($text_x, $work_y-0.6)

box ht 3.5 wid 3.5 rad 5px "WORK-like" "abstract entity," "with some context" fill lightpink at (0, $work_y)

# MANIFESTATION

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightpink at ($text_x-1, $manifestation_y)


box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill lightpink at ($text_x, $manifestation_y+0.9)


box ht $line_height wid $line_width rad 5px \
"- Titles" \ 
ljust color none fill lightpink at ($text_x, $manifestation_y+0.7)

box ht $line_height wid $line_width rad 5px "- Type - pre-release, theatrical, non-theatrical," \ 
ljust color none fill lightpink at ($text_x, $manifestation_y+0.5)

box ht $line_height wid $line_width rad 5px  \
"  transmission, home-viewing, internet, restoration, not-for-release, etc" \ 
ljust color none fill lightpink at ($text_x, $manifestation_y+0.3)

box ht $line_height wid $line_width rad 5px \
"- Language(s): language of dialogue, subtitles, dubbing, intertitles, etc. " \ 
ljust color none fill lightpink at ($text_x, $manifestation_y+0.1)

box ht $line_height wid $line_width rad 5px \
"- Format: 35mm film, Digital Cinema Package (DCP), Blu-ray, etc" \ 
ljust color none fill lightpink at ($text_x, $manifestation_y-0.1)

box ht $line_height wid $line_width rad 5px \
"- Extent: physical, logical, temporal, e.g. duration, running time, length, etc." \ 
ljust color none fill lightpink at ($text_x, $manifestation_y-0.3)

box ht $line_height wid $line_width rad 5px \
"- Event: release, transmission, distribution, creation, dates" \ 
ljust color none fill lightpink at ($text_x, $manifestation_y-0.5)

box ht $line_height wid $line_width rad 5px \
"- Rights context: platforms, territories, dates  " \ 
ljust color none fill lightpink at ($text_x, $manifestation_y-0.7)

box ht $line_height wid $line_width rad 5px \
"- Agents: Creator, Broadcaster, Distributor, Publisher" \ 
ljust color none fill lightpink at ($text_x, $manifestation_y-0.9)

box ht 3.5 wid 3.5 rad 5px "Crossover data" "held in either level" "or both levels" fill lightpink at (0, $manifestation_y)

# ITEM

box ht 3.5 wid 8 rad 5px "" ljust color none fill lightpink at ($text_x-1, $item_y)

box ht $line_height wid $line_width rad 5px \
"- Identifier (inventory numbers) " \ 
ljust color none fill lightpink at ($text_x,$item_y+1.6)

box ht $line_height wid $line_width rad 5px \
"- Titles (original, alternative) " \ 
ljust color none fill lightpink at ($text_x,$item_y+1.4)

box ht $line_height wid $line_width rad 5px \
"- Element Type : instantiation type, e.g. original negative," \ 
ljust color none fill lightpink at ($text_x,$item_y+1.2)

box ht $line_height wid $line_width rad 5px \
"  dupe positive, Lavender, sound negative" \ 
ljust color none fill lightpink at ($text_x,$item_y+1)

box ht $line_height wid $line_width rad 5px \
"- Item specifics: carrier, base, gauge, format, digital file type," \ 
ljust color none fill lightpink at ($text_x,$item_y+0.8)

box ht $line_height wid $line_width rad 5px \
" sound, sound systems, colour standards etc" \ 
ljust color none fill lightpink at ($text_x,$item_y+0.6)

box ht $line_height wid $line_width rad 5px \
"- Extent: physical, temporal, e.g. footage, file size, duration" \ 
ljust color none fill lightpink at ($text_x,$item_y+0.4)

box ht $line_height wid $line_width rad 5px \
"- Access conditions: Condition report - pristine, not for projection," \ 
ljust color none fill lightpink at ($text_x, $item_y+0.2)

box ht $line_height wid $line_width rad 5px \
"heavy scratch- es, etc; storage location - home location, current location;" \ 
ljust color none fill lightpink at ($text_x, $item_y+0)

box ht $line_height wid $line_width rad 5px \
"- Conservation recom-   mendations: urgent transfer required,"  \ 
ljust color none fill lightpink at ($text_x, $item_y-0.2)

box ht $line_height wid $line_width rad 5px \
"relocate to sub-zero,  etc " \ 
ljust color none fill lightpink at ($text_x, $item_y-0.4)

box ht $line_height wid $line_width rad 5px \
"- Event(s) (with Dates): creation, acquisition, accession, " \ 
ljust color none fill lightpink at ($text_x, $item_y-0.6)

box ht $line_height wid $line_width rad 5px \
" de-accession, loan, transport  " \ 
ljust color none fill lightpink at ($text_x, $item_y-0.8)

box ht $line_height wid $line_width rad 5px \
"- Acquisition: source, method, funding context, " \ 
ljust color none fill lightpink at ($text_x, $item_y-1)

box ht $line_height wid $line_width rad 5px \
"conditions of access, dates" \ 
ljust color none fill lightpink at ($text_x, $item_y-1.2)

box ht $line_height wid $line_width rad 5px \
"- Agents: donors, archive technicians/conservationists, etc." \ 
ljust color none fill lightpink at ($text_x, $item_y-1.4)

box ht $line_height wid $line_width rad 5px \
"- Holding institution: name of the Item holde" \ 
ljust color none fill lightpink at ($text_x, $item_y-1.6)

box ht 3.5 wid 3.5 rad 5px "ITEM-like" "physical or digital" "object, with some" "context" fill lightpink at (0, $item_y)


```



\newpage
```pikchr


$line_width = 3.5
$line_height = 0.2

$item_y = -2.75
$text_x = 3.75

# LABEL

box ht 0.5 wid 8.5 rad 5px "No hierarchy model: 1 level" bold fill 0xcbc3e3 at (2.5, 0.5)

# ITEM

box ht 5 wid 8 rad 5px "" ljust color none fill 0xcbc3e3 at ($text_x-1, $item_y)

box ht $line_height wid $line_width rad 5px \
"- Identifier (international, in-house unique identifier number)" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+2.3)

box ht $line_height wid $line_width rad 5px \
"- Type - Whole conditions (serial / standalone / component part)" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+2.1)

box ht $line_height wid $line_width rad 5px \
"- Titles (original, alternative, series/serial)" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+1.9)

box ht $line_height wid $line_width rad 5px \
"- Dates: copyright, production, release, object creation, object acquisition" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+1.7)

box ht $line_height wid $line_width rad 5px \
" accession, de-accession, loan, transport" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+1.5)

box ht $line_height wid $line_width rad 5px \
"- Content: Synopsis, Genre, Form, Subject" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+1.3)

box ht $line_height wid $line_width rad 5px \
"- Agents: Cast, Credits, Rights holders " \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+1.1)

box ht $line_height wid $line_width rad 5px "- Type - pre-release, theatrical, non-theatrical," \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+0.9)

box ht $line_height wid $line_width rad 5px  \
"  transmission, home-viewing, internet, restoration, not-for-release, etc" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+0.7)

box ht $line_height wid $line_width rad 5px \
"- Language(s): original language of conception/presentation" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y+0.5)

box ht $line_height wid $line_width rad 5px \
"- Instantiation type, e.g. original negative," \ 
ljust color none fill 0xcbc3e3 at ($text_x,$item_y+0.3)

box ht $line_height wid $line_width rad 5px \
"  dupe positive, Lavender, sound negative" \ 
ljust color none fill 0xcbc3e3 at ($text_x,$item_y+0.1)

box ht $line_height wid $line_width rad 5px \
"- Format/Item specifics: 35mm film, Digital Cinema Package (DCP), " \ 
ljust color none fill 0xcbc3e3 at ($text_x,$item_y-0.1)

box ht $line_height wid $line_width rad 5px \
" Blu-ray, etc; carrier, base, gauge, format, digital file type," \ 
ljust color none fill 0xcbc3e3 at ($text_x,$item_y-0.3)

box ht $line_height wid $line_width rad 5px \
" sound, sound systems, colour standards, etc" \ 
ljust color none fill 0xcbc3e3 at ($text_x,$item_y-0.5)

box ht $line_height wid $line_width rad 5px \
"- Extent: physical, temporal, e.g. footage, file size, duration" \ 
ljust color none fill 0xcbc3e3 at ($text_x,$item_y-0.7)

box ht $line_height wid $line_width rad 5px \
"- Event(s) (with Dates): release, transmission, distribution, creation, " \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-0.9)

box ht $line_height wid $line_width rad 5px \
" acquisition, accession, de-accession, loan, transport, dates " \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-1.1)

box ht $line_height wid $line_width rad 5px \
"- Rights context: platforms, territories, dates, transfer of ownership" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-1.3)

box ht $line_height wid $line_width rad 5px \
"- Agents: Creator, Broadcaster, Distributor, Publisher, Donor, Institution" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-1.5)

box ht $line_height wid $line_width rad 5px \
"technicians/conservationists, etc." \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-1.7)

box ht $line_height wid $line_width rad 5px \
"- Acquisition: source, method, funding context, " \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-1.9)

box ht $line_height wid $line_width rad 5px \
"conditions of access, dates" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-2.1)

box ht $line_height wid $line_width rad 5px \
"- Holding institution: name of the Item holde" \ 
ljust color none fill 0xcbc3e3 at ($text_x, $item_y-2.3)


box ht 5.5 wid 3.5 rad 5px \
"WORK / MANIFESTATION / ITEM" \
"properties expressed in one record," \
"with abstract, contextual and object data" \
"stored on a single hierarchy level" \
fill 0xcbc3e3 at (0, $item_y)


```

\newpage

**Work/Manifestation/Item.
Properties expressed in one record, with abstracts, contextual and object data stored in a single level hierarchy Distribution of the elements of description according to the four entities order**

| Properties | (Work) | (Manifestation) | (Item) |
| -- | -- | -- | -- |
| Titles | Uniform, Preferred, Other Title information, Alternative, Supplied/Devised | Title proper | Title proper |
| Part | Monographic, Analytic, Serial, Collection | | |
| Content | Categories: fiction/non fiction; genre, synopsis, subject, etc. | | |
| Dates/Events | Creation, Production, Censorship, Copyright | Release, manufacture, transmission, distribution, etc. | Object creation, acquisition, accession, de-accession, loan, transport, etc. |
| Agents | Cast, credits, rights holders, creator, etc. | Distributor, broadcaster, publisher | Donor, Archive/archivist, technician, restorer, etc. |
| Rights context | Copyright holder and date | Platforms, territories, dates. Agents (distributors, license holder) | Transfer of ownership |
| Event types | Awards Censorship Production IPR registration | Pre-release, theatrical, non-theatrical, transmission, home viewing, internet, not for release, censorship etc. | Acquisition Reproductions Disposal |
| Format general | | 35mm film, digital cinema, blu ray, etc. | |
| Format specific | | | 16mm film pos, 35mm lavender separation, ProRes422 HQ, etc. |
| Condition report | | | Pristine, not for projection, heavy scratches, etc. |
| Storage location | | | Home location, current location, previous location || 
| Conservation recommendations | | | Urgent transfer required, relocate sub-zero, etc. |


[^11]: Form = Fiction, Non-fiction, etc. Some institutions may incorporate these as a genre term, whilst others
may have them as a separate category to genre.

