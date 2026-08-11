# Demo Runtime vs Target Runtime

## Purpose
This document separates the current local demo implementation from the final target enterprise runtime.

## Demo Runtime
The demo runtime is the current Streamlit-based working build.

Characteristics:
- local and deterministic;
- suitable for screenshots and regression evidence;
- uses fixtures and controlled data sources;
- optimized for validation and narrative clarity.

What it should prove:
- the solution is grounded;
- the supervisor routes correctly;
- citations are retained;
- fallback behavior works.

## Target Runtime
The target runtime is the Salesforce/Agentforce implementation.

Characteristics:
- enterprise-grade;
- reusable across agent capabilities;
- integrated with trust, guardrails, and retrieval patterns;
- ready for production workflows.

What it should add:
- stronger platform orchestration;
- enterprise data source integration;
- prompt template management;
- richer observability;
- broader agent reuse.

## What Stays the Same
- account and contact scoping;
- evidence-grounded generation;
- citation discipline;
- fallback when evidence is missing;
- clear separation between facts and interpretation.

## What Can Change
- data source implementation;
- orchestration runtime;
- prompt storage and management;
- platform-specific observability;
- authentication and access patterns.