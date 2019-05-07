.PHONY: all clean doc examples help

PYTHON := python3

.DEFAULT: help
help:
	@echo "make all"
	@echo "	builds documentation and examples"
	@echo ""
	@echo "make doc"
	@echo "	builds HTML documentation"
	@echo ""
	@echo "make examples"
	@echo "	builds PDFs and PNGs of example graphs"
	@echo ""
	@echo "make help"
	@echo "	prints this help message (default)"

%.pdf: %.py
	$(PYTHON) $<

examples: $(patsubst %.py,%.pdf,$(wildcard example*.py))

local_mpl_config.html: local_mpl_config.py
	pydoc -w local_mpl_config

doc: local_mpl_config.html

all: examples doc

clean:
	$(RM) local_mpl_config.html
	$(RM) *.pdf *.png

# vim: set noexpandtab ts=2 sw=2 tw=72:
