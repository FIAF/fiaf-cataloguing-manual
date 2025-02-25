\subsection{E.5.1.1 Model: Collection Aggregate Manifestation within a one-to-many Works/Variants-Manifestations database system}
\label{sec:manual-E.5.1.1}

This model involves creation of a new aggregating Work record.
Works link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship.

```pikchr
B1: box rad 5px "Sabrina" "(1954) (Work)" fit at (0,3) 

B2: box rad 5px "Funny Face" "(1956) (Work)" fit at (4,3) 

B3: box rad 5px "Breakfast at Tiffanys" "(1961) (Work)" fit at (0,2) 

B4: box rad 5px "The Audrey Hepburn Collection" "(DVD Manifestation, 2008)" "(Collection Aggregate)" fit at (2,1) 

B5: box rad 5px "The Audrey Hepburn Collection" "(DVD Item)" fit at (2,0) 

B6: box rad 5px "The Audrey Hepburn Collection" "(2008) (Work)" fit at (2,3) 

arrow <-> from B1.e to B6.w

arrow <-> from B6.e to B2.w

arrow <-> from B6.s to B4.n

arrow <-> from B4.s to B5.n

arrow <-> right 0.2 from B3.e then up until even with B6 then right to B6.w
```