"""Load and validate the project's versioned catalogues."""

from __future__ import annotations

import json
from dataclasses import dataclass
from importlib.resources import files
from typing import Any


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str


def _load_json(name: str) -> Any:
    path = files("polititrace").joinpath("catalog", name)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_families() -> list[dict[str, Any]]:
    value = _load_json("families.json")
    if not isinstance(value, list):
        raise ValueError("families.json must contain a JSON array")
    return value


def load_sources() -> list[dict[str, Any]]:
    value = _load_json("sources.json")
    if not isinstance(value, list):
        raise ValueError("sources.json must contain a JSON array")
    return value


def validate_catalogues() -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    families = load_families()
    sources = load_sources()

    ids: set[str] = set()
    for index, family in enumerate(families):
        path = f"families[{index}]"
        family_id = family.get("id")
        if not isinstance(family_id, str) or not family_id:
            issues.append(ValidationIssue(path, "missing non-empty id"))
        elif family_id in ids:
            issues.append(ValidationIssue(path, f"duplicate id: {family_id}"))
        else:
            ids.add(family_id)

        if not family.get("display_name"):
            issues.append(ValidationIssue(path, "missing display_name"))
        if family.get("verification_status") not in {
            "seed_needs_primary_sources",
            "verified",
        }:
            issues.append(ValidationIssue(path, "invalid verification_status"))
        if not isinstance(family.get("entities"), list) or not family["entities"]:
            issues.append(ValidationIssue(path, "entities must be a non-empty array"))

    source_ids: set[str] = set()
    for index, source in enumerate(sources):
        path = f"sources[{index}]"
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id:
            issues.append(ValidationIssue(path, "missing non-empty id"))
        elif source_id in source_ids:
            issues.append(ValidationIssue(path, f"duplicate id: {source_id}"))
        else:
            source_ids.add(source_id)

        if not source.get("url"):
            issues.append(ValidationIssue(path, "missing url"))
        if source.get("evidence_level") not in {1, 2, 3, 4}:
            issues.append(ValidationIssue(path, "evidence_level must be 1, 2, 3 or 4"))

    return issues
