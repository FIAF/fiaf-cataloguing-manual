\newpage
# E.5.1.2 Model: Collection Aggregate Manifestation within a many-to-many Works/Variants-Manifestation database system {#manual-E.5.1.2}

A single Aggregate Manifestation links to the many individual Works/Variants in “part of” relationship.

```
┌────────────────┐              ┌────────────────┐    ┌───────────────────────┐
│                │              │                │    │                       │
│    Sabrina     │              │   Funny Face   │    │ Breakfast at Tiffanys │
│ (1954) (Work)  │              │ (1956) (Work)  │    │     (1961) (Work)     │
│                │              │                │    │                       │
└────────────────┘              └────────────────┘    └───────────────────────┘
         ▲                               ▲                        ▲
         │                               │                        │
         │                               │                        │
         └────────────────────┐          │          ┌─────────────┘
                              │          │          │
                              │          │          │
                              │          │          │
                              ▼          ▼          ▼
                    ┌────────────────────────────────────────┐
                    │                                        │
                    │     The Audrey Hepburn Collection      │
                    │       (DVD Manifestation, 2008)        │
                    │         (Collection Aggregate)         │
                    │                                        │
                    └────────────────────────────────────────┘
                                         ▲
                                         │
                                         ▼
                    ┌────────────────────────────────────────┐
                    │                                        │
                    │     The Audrey Hepburn Collection      │
                    │               (DVD Item)               │
                    │                                        │
                    └────────────────────────────────────────┘
```
