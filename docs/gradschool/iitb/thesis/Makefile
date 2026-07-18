all: report.tex report.bib titlepage.tex
	latex report.tex
	bibtex report
	latex report.tex
	latex report.tex
	dvips report.dvi
	ps2pdf report.ps
