#! /bin/bash

panel_mover="panel_array_gen.py"
regex_script="reform.py"
srcpath="../../../src/python/"
docpath="../../doc/tex/heatmap_generator"

cp $panel_mover $srcpath
cd $srcpath
echo 'Which panel are you testing, give a name: '
read panelname
echo 'How large square? (number of steps): '
read square_size
echo "The starting position will be the bottom left corner of the table later generated"
echo 'X starting position? '
read x_start
echo 'Y starting position? '
read y_start

clear

./$panel_mover $square_size $x_start $y_start $panelname

rm $panel_mover

dt="$(date +%y-%m-%d_%H.%M)"
rawfile=raw_result_$panelname"_"$dt.txt
reformfile=reform_result_$panelname"_"$dt

mv -v test_results.txt $docpath/$rawfile
cd $docpath

#Change panel_array... to $rawfile when panel and luxmeter are available
./$regex_script $square_size $rawfile $reformfile.txt

template=a.tex
step_size=$(python3 -c "print ($square_size / 100)")
x_start=$(python3 -c "print('%.4f' %(float($x_start)))") 
y_start=$(python3 -c "print('%.4f' %(float($y_start)))")
x_end=$(python3 -c "print('%.4f' %($x_start + $step_size))") 
y_end=$(python3 -c "print('%.4f' %($y_start + $step_size))")

echo "$(sed -n '1,89p' < $template)" > c.txt && echo "{"$reformfile".txt}" >> c.txt && \
echo "$(sed -n '90,93p' < $template)">> c.txt && echo "" >> c.txt && \
printf "\\\textbf{Koordinater (x, y)} \\\newline Längst ner till vänster: %s, %s. Högst upp till höger: %s, %s." $x_start $y_start $x_end $y_end >> c.txt \
&& echo "$(tail -n 2 $template)" >> c.txt 

mv c.txt $reformfile.tex

pdflatex $reformfile
mv $reformfile.pdf heatmap_of_$panelname.pdf 

rm *.log
rm *.aux
mkdir -p output
mv heatmap_of_$panelname.pdf $rawfile $reformfile.* ./output
clear
printf '\a'
echo "If you see this, then the script is finished. The pdf-file is located in the output folder"
echo ""
