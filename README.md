# Pydantic Learning

A hands-on Python project for learning **Pydantic v2** — from basic models to advanced validation, serialization, and nested structures.

## Overview

This repo walks through Pydantic's core features step by step, using a `Patient` data model as a consistent example throughout. Each file builds on the previous one, introducing new concepts in a progressive, easy-to-follow manner.

## Project Structure

```
pydantic-learning/
├── 01_concept.py                  # Basic model definition and instantiation
├── 02_concept.py                  # Complex field types (List, Dict, bool, float)
├── 03_concept.py                  # Field constraints, EmailStr, AnyUrl, Annotated
├── 04_concept_field_validator.py  # Custom field-level validators
├── 05_concept_model_validator.py  # Cross-field model-level validators
├── 06_concept_computed_fields.py  # Computed/derived fields (e.g., BMI)
├── 07_concept_nested_models.py    # Nested Pydantic models
├── 08_concept_serialization.py    # Serialization to dict/JSON with filtering
├── pyproject.toml
└── uv.lock
```

## Concepts Covered

| File | Concept |
|------|---------|
| `01_concept.py` | Basic `BaseModel`, instantiation via dict unpacking |
| `02_concept.py` | `List`, `Dict`, `bool`, `float` field types |
| `03_concept.py` | `Field()` constraints, `EmailStr`, `AnyUrl`, `Annotated`, `Optional`, strict mode |
| `04_concept_field_validator.py` | `@field_validator` for domain checks, name transforms, and age validation |
| `05_concept_model_validator.py` | `@model_validator` for cross-field validation (e.g., emergency contact rule) |
| `06_concept_computed_fields.py` | `@computed_field` to auto-calculate BMI from weight and height |
| `07_concept_nested_models.py` | Composing models (`Address` inside `Patient`) for better organization |
| `08_concept_serialization.py` | `model_dump()`, `model_dump_json()`, `include`, `exclude`, `exclude_unset` |

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run any example
uv run python 01_concept.py
```

**Requirements:** Python >= 3.11

## Dependencies

- [`pydantic`](https://docs.pydantic.dev/) >= 2.13.3
- [`email-validator`](https://github.com/JoshData/python-email-validator) >= 2.3.0
