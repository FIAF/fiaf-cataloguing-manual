# E.5.2.1 Model: Augmented Aggregate Manifestation within a one-to-many Work/Variants-Manifestations database system {#manual-E.5.2.1}

This involves creation of a new aggregating Work record.
Works link together in associative relationship “contains/contained in” and aggregate Manifestation links to aggregating Work in “part of” relationship.

```
┌────────────────┐    ┌──────────────────────────────────┐   ┌─────────────────────┐
│                │    │                                  │   │     Casablanca      │
│   Casablanca   │    │   Casablanca. Special Edition    │   │ (TV Episode, 1955)  │
│  (1943) Work   │◀──▶│    (2003) [Aggregating] Work     │◀─▶│        Work         │
│                │    │                                  │   │                     │
└────────────────┘    └──────────────────────────────────┘   └─────────────────────┘
                       ▲    ▲           ▲       ▲      ▲
             ┌─────────┘    │           │       │      │
             │              │           │       │      └─────────────────┐
             ▼              │           │       │                        │
  ┌────────────────────┐    │           │       │                        ▼
  │      You Must      │  ┌─┘           │       └───────────┐  ┌───────────────────┐
  │      Remember      │  │             │                   │  │ Bacall on Bogart  │
  │    This (1989)     │  │             │                   │  │    (1988) Work    │
  │       (Work)       │  │             │                   │  │                   │
  └────────────────────┘  │             │                   │  └───────────────────┘
                          ▼             └┐                  │
                 ┌────────────────┐      │                  ▼
                 │                │      │      ┌───────────────────────┐
                 │  Carrotblanca  │      │      │                       │
                 │  (1995) Work   │      │      │  Casablanca. Trailer  │
                 │                │      │      │      (1942) Work      │
                 └────────────────┘      │      │                       │
                                         │      └───────────────────────┘
                                         │
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │                                  │
                       │   Casablanca. Special Edition    │
                       │    (DVD Manifestation, 2003)     │
                       │      (Augmented Aggregate)       │
                       │                                  │
                       └──────────────────────────────────┘
```