"""Small dependency-free command line interface."""

from __future__ import annotations

import argparse
import json

from polititrace.catalog import load_families, load_sources, validate_catalogues


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="polititrace")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list-families", help="List the political families in the MVP")
    subparsers.add_parser("list-sources", help="List registered source catalogues")
    subparsers.add_parser("validate", help="Validate project catalogues")
    return parser


def main() -> None:
    args = _build_parser().parse_args()

    if args.command == "list-families":
        for family in load_families():
            print(f"{family['id']}: {family['display_name']}")
        return

    if args.command == "list-sources":
        for source in load_sources():
            print(f"{source['id']}: {source['name']} — {source['url']}")
        return

    issues = validate_catalogues()
    if issues:
        print(json.dumps([issue.__dict__ for issue in issues], ensure_ascii=False, indent=2))
        raise SystemExit(1)
    print("Catalogues valides.")


if __name__ == "__main__":
    main()
