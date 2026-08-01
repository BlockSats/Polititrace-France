from polititrace.catalog import load_families, load_sources, validate_catalogues


def test_four_initial_families() -> None:
    assert {item["id"] for item in load_families()} == {
        "rn",
        "lfi",
        "presidential_bloc",
        "ps",
    }


def test_sources_have_official_evidence_level() -> None:
    assert all(source["evidence_level"] == 1 for source in load_sources())


def test_catalogues_are_valid() -> None:
    assert validate_catalogues() == []
