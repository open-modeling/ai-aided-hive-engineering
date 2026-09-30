.PHONY: validate validate-proposal validate-history pdf release clean

validate:
	./scripts/validate

validate-proposal:
	./scripts/validate --proposal-only

validate-history:
	python3 scripts/validate-history

pdf:
	./scripts/build-pdf

release:
	./scripts/release

clean:
	rm -rf build dist
