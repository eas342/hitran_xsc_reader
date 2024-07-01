# Hitran cross section file

Simple Python function to read hitran cross section file

## Installation

	git clone https://github.com/eas342/hitran_xsc_reader.git
	cd hitran_xsc_reader
	pip install .

## Example Usage

	import read_hitran
	xsc_file = 'C3H6_600.0K-9.5Torr_2500.0-3500.0_123.xsc'
	xh,yh,mh=read_hitran.read_hitran.read_xc(xscfile)
	