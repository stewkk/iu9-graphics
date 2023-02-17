SUBDIRS := $(subst /,,$(wildcard */))

.PHONY: $(SUBDIRS)

$(SUBDIRS):
	@meson compile -C builddir/ && builddir/$@
