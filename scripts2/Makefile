all: install

PREFIX = /usr/local
ModelSEEDDatabase ?= ${PREFIX}/share/ModelSEEDDatabase
PYSRC = connection_add_weight.py rxn_to_connections.py lists_to_matrix.py \
	rxn_expandinfo.py map_name.py
PYTGT = ${PYSRC:%.py=${PREFIX}/bin/%}
SHSRC = fna_to_rxn.sh
SHTGT = ${SHSRC:%.sh=${PREFIX}/bin/%}

${PYTGT}: ${PYSRC}
	@mkdir -p "${PREFIX}/bin"
	@cp -f "$(@F).py" $@
	@chmod 755 $@

${SHTGT}: ${SHSRC}
	@mkdir -p "${PREFIX}/bin"
	@cp -f "$(@F).sh" $@
	@chmod 755 $@

${ModelSEEDDatabase}:
	@cd "$ModelSEEDDatabase" 2>/dev/null \
		&& git rev-parse --git-dir 2>/dev/null \
		|| git clone https://github.com/ModelSEED/ModelSEEDDatabase.git \
			"${ModelSEEDDatabase}"

${PREFIX}/share/sas:
	@mkdir -p "${PREFIX}/share/sas";
	@curl http://blog.theseed.org/downloads/sas.tgz \
		| tar -zxC"${PREFIX}/share/sas"
	@"${PREFIX}/share/sas/modules/BUILD_MODULES"

install: ${PYTGT} ${SHTGT} ${ModelSEEDDatabase} ${PREFIX}/share/sas

uninstall:
	rm -rf "${PREFIX}/share/ModelSEEDDatabase"
	rm -rf "${PREFIX}/share/sas"
	rm -rf ${PYTGT}

.PHONY: install all
.SECONDARY:
