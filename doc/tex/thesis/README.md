#How to:

To compile the document, run 

```
pdflatex thesis
biber thesis
pdflatex thesis
pdflatex thesis
```

The different .tex files should include the section they are named after, and necessary settings should be added to thesis.tex, as it is the main file.

References should be added to `ref.bib`