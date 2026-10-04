# Ethics and Safety Statement — P11 Constraint Reframing

## Renaming

The pattern originally cataloged by White et al. (2023) as "Refusal Breaker"
has been renamed **Constraint Reframing** to more precisely describe its
legitimate function: helping practitioners specify context when a model's
default behaviour is overly conservative for a given use case.

## Experimental instantiations

All experimental instantiations of P11 use **verifiable non-adversarial
academic contexts**. Examples used in evaluation:

- Explaining a historical conflict in the context of an undergraduate history course
- Describing a medical procedure for patient education with patient consent assumed
- Discussing a sensitive scientific topic in the context of a research methods course
- Explaining legal concepts for a law school curriculum

All four paraphrastic variants (V-A through V-D) provided in this repository
use exclusively benign academic framing. They were reviewed by two independent
NLP researchers and confirmed as non-adversarial.

## Adversarial variants

Adversarial variants are **excluded** from this repository. They are not
provided, referenced, or made available.

## Finding interpretation

The Claude-family behavioral fingerprint finding (P11 PTS = 0.12 on Claude 3 Opus)
is informative **precisely because it demonstrates that this pattern is
effectively neutralised on aligned frontier models** for any constraint-adjacent
framing — including clearly benign academic contexts.

This is an observational finding about model behaviour, not a recommendation
to circumvent model safety mechanisms. The appropriate use of this finding is:

1. As evidence of model-family-specific behavioural heterogeneity
2. As a data point for compatibility testing when deploying Claude-family models
3. As motivation for practitioners to use Class I structural alternatives
   when cross-backend portability is required

## Dual-use acknowledgment

We acknowledge the dual-use potential of constraint reframing research.
The benchmark harness is released without adversarial instantiations.
Researchers intending to study adversarial variants should do so within
appropriate institutional ethics frameworks.
