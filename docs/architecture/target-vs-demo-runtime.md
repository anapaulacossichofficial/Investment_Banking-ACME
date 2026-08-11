# Demo Runtime vs Target Runtime

## Purpose

This document separates the current local demo implementation from the final target enterprise runtime.

## Demo runtime

The demo runtime is the current Streamlit-based working build.

Characteristics:
- local and deterministic;
- easy to inspect during development;
- suitable for screenshots, regression tests, and evidence logs;
- uses fixtures and controlled data sources;
- optimized for validation and narrative clarity.

What it should prove:
- the solution is grounded;
- the supervisor routes correctly;
- citations are retained;
- fallback behavior works;
- the architecture can support more than one capability.

## Target runtime

The target runtime is the Salesforce/Agentforce implementation.

Characteristics:
- enterprise-grade;
- reusable across agent capabilities;
- integrated with platform-native trust, guardrails, and retrieval patterns;
- ready for production workflows and organizational reuse.

What it should add:
- stronger platform orchestration;
- enterprise data source integration;
- prompt template management;
- richer observability;
- broader reuse across future agent capabilities.

## What must stay the same

These behaviors should remain consistent between demo and target:
- account and contact scoping;
- evidence-grounded generation;
- citation discipline;
- fallback when evidence is missing;
- clear separation between facts and interpretation.

## What can change

These elements can evolve from demo to target:
- data source implementation;
- orchestration runtime;
- prompt storage and management;
- platform-specific observability;
- enterprise authentication and access patterns.

## Guidance for the project

The demo runtime should be stable enough to validate the product story, while the target runtime should be documented as the scalable platform direction. The two are related, but they should not be described as identical.