# LLM Safety Probe: Refusal Consistency Under Rephrasing

## Overview
This project explores how large language models vary in refusal behavior when the same unsafe intent is framed in different ways.

## Motivation
Consistency in refusal behavior is important for evaluating the robustness of LLM safety mechanisms.

## Method
I designed multiple prompt variants expressing the same disallowed intent and queried a language model using a Python script. Model responses are logged for analysis.

## Analysis Plan
Responses will be manually categorized as:
- refusal
- partial_refusal
- compliance

## Limitations
- Small prompt set
- Manual labeling
- Single model
  
## Preliminary Observations
Rephrased prompts using fictional or academic framing were more likely to elicit partial or full compliance than direct requests.
