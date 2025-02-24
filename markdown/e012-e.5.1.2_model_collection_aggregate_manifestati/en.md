\newpage
# E.5.1.2 Model: Collection Aggregate Manifestation within a many-to-many Works/Variants-Manifestation database system {#manual-E.5.1.2}

A single Aggregate Manifestation links to the many individual Works/Variants in “part of” relationship.

```pikchr
B1: box rad 5px "Sabrina" "(1954) (Work)" fit at (0,2) 

B2: box rad 5px "Funny Face" "(1956) (Work)" fit at (1.5,2) 

B3: box rad 5px "Breakfast at Tiffanys" "(1961) (Work)" fit at (3,2) 

B4: box rad 5px "The Audrey Hepburn Collection" "(DVD Manifestation, 2008)" "(Collection Aggregate)" fit at (1.5,1) 

B5: box rad 5px "The Audrey Hepburn Collection" "(DVD Item)" fit at (1.5,0) 

arrow <-> down 0.2 from B1.s then right until even with B4 then down to B4.n

arrow <-> from B2.s to B4.n

arrow <-> down 0.2 from B3.s then left until even with B4 then down to B4.n

arrow <-> from B4.s to B5.n
```