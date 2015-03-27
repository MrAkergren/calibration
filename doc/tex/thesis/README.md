#How to:

To compile the document, run 

```
pdflatex thesis
biber thesis
pdflatex thesis
pdflatex thesis
```

The different `.tex` files should include the section they are named after, and necessary settings should be added to `thesis.tex`, as it is the main file. 

Subsections should be added in the section files to begin with, unless they grow to large.

References should be added to `ref.bib`, and should be referred by `\cite{}` or `\cite[s.~X]{}` where X is the page number or page interval 
