.PHONY: validate validate-proposal pdf release clean

validate:
	./scripts/validate

validate-proposal:
	./scripts/validate --proposal-only

pdf:
	./scripts/build-pdf

release:
	./scripts/release

clean:
	rm -rf build dist
