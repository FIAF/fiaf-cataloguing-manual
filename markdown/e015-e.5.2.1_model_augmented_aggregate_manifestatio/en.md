# E.5.2.1 Model: Augmented Aggregate Manifestation within a one-to-many Work/Variants-Manifestations database system {#manual-E.5.2.1}

This involves creation of a new aggregating Work record.
Works link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship.

```pikchr
C1: box rad 5px "Casablanca" "(1943) Work" fit at (0,3) 

C2: box rad 5px "Casablanca. Special Edition" "(2003) [Aggregating] Work" fit at (2,3) 

C3: box rad 5px "Casablanca" "(TV Episode, 1955) Work" fit at (4,3) 
 
C4: box rad 5px "You Must Remember This" "(1989) (Work)" fit at (0,2) 

C5: box rad 5px "Bacall on Bogart" "(1988) Work" fit at (4,2) 

C6: box rad 5px "Carrotblanca" "(1995) Work" fit at (1,1) 

C7: box rad 5px "Casablanca. Trailer" "(1942) Work" fit at (3,1) 

C8: box rad 5px "Casablanca. Special Edition" "(DVD Manifestation, 2003)" "(Augmented Aggregate)" fit at (2,0)

arrow <-> from C1.e to C2.w 

arrow <-> from C2.e to C3.w 

arrow down 0.2 from C2.s then left until even with C4 then down to C4.n

arrow down 0.2 from C2.s then right until even with C5 then down to C5.n

arrow down 0.2 from C2.s then left until even with C6 then down to C6.n

arrow down 0.2 from C2.s then right until even with C7 then down to C7.n

arrow from C2.s to C8.n
```