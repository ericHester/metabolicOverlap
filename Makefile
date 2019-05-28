all: install

clean:
	rm -rf ./.local ./sourcedata

install: sourcedata/ModelSEEDDatabase .local/lib/python2.7/site-packages/PyFBA

.local:
	virtualenv ./.local

sourcedata/ModelSEEDDatabase:
	mkdir -p sourcedata;\
	cd sourcedata;\
	git clone https://github.com/ModelSEED/ModelSEEDDatabase.git

.local/lib/python2.7/site-packages/PyFBA: .local sourcedata/ModelSEEDDatabase 
	. ./startsession.sh;\
	cd ./.local;\
	git clone https://github.com/bradfordboyle/pyglpk.git;\
	cd pyglpk;\
	make install test;\
	cd ..;\
	pip install python-libsbml-experimental lxml beautifulsoup4;\
	pip install pyfba;\

.PHONY: install all
