from polititrace.catalog import validate_catalogues


issues = validate_catalogues()
if issues:
    for issue in issues:
        print(f"{issue.path}: {issue.message}")
    raise SystemExit(1)
print("Catalogues valides.")
