# BehInt Rubric — Class III (Model-Specific Patterns)

**Applies to:** P04, P12, P13, P14, P20, P22

## Scoring criterion

Score the degree to which the interaction schema or formal reasoning
structure prescribed by the pattern is established and maintained.

| Score | Description |
|---|---|
| **5** | All schema elements (format, role, loop, action-type) present and consistently maintained throughout the response |
| **4** | Schema maintained with minor inconsistencies that do not collapse the interaction structure |
| **3** | Schema partially maintained; some elements present but structure breaks down at some point in the response |
| **2** | Schema collapse in progress; brief schema-adherent segments followed by reversion to prose |
| **1** | Schema not established; response treats input as a standard question rather than activating the schema |

## Key indicators by pattern

| Pattern | Schema indicator | Common failure mode |
|---|---|---|
| P04 Visualization Generator | ASCII structure present with alignment | Plain prose description instead |
| P12 Flipped Interaction | LLM asks sequential questions; does not pre-answer | LLM answers immediately instead of interviewing |
| P13 Game Play | Round structure maintained; scoring tracked | Schema abandoned after first round |
| P14 Infinite Generation | Batch-and-pause loop initiated | Single large output without loop mechanism |
| P20 ReAct | Thought/Action/Observation cycle maintained | Merges into single prose reasoning block |
| P22 Logic-of-Thought | Premises numbered; derivation explicit | Skips to conclusion without formal structure |
