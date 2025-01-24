\newpage
# E.5.1.1 Model: Collection Aggregate Manifestation within a one-to-many Works/Variants-Manifestations database system {#manual-E.5.1.1}

This model involves creation of a new aggregating Work record.
Works link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship.

```
┌────────────────┐      ┌────────────────────────────────┐     ┌────────────────┐
│                │      │                                │     │                │
│    Sabrina     │      │ The Audrey Hepburn Collection  │     │   Funny Face   │
│ (1954) (Work)  │◀────▶│         (2008) (Work)          │◀───▶│ (1956) (Work)  │
│                │  ┌──▶│                                │     │                │
└────────────────┘  │   └────────────────────────────────┘     └────────────────┘
                    │                    ▲
                    │                    │
┌────────────────┐  │                    │
│                │  │                    │
│  Breakfast at  │  │                    │
│    Tiffanys    │◀─┘                    │
│ (1961) (Work)  │                       │
│                │                       ▼
└────────────────┘  ┌────────────────────────────────────────┐
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
