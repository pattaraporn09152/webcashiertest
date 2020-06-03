latexmk -g -f CS5811400000.tex

##### OR

# xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex
# bibtex MathCS-tutorial.aux
# xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex
# xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex
