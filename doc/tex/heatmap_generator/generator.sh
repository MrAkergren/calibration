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

dt="$(date +%y-%m-%d_%k.%M)"
rawfile=raw_result_$panelname"_"$dt.txt
reformfile=reform_result_$panelname"_"$dt.txt

mv -v test_results.txt $docpath/$rawfile && cd $docpath

#Change panel_array... to $rawfile when panel and luxmeter are available
./$regex_script $square_size panel_array_test.txt $reformfile

start="$(less a.tex)"
end="$(less b.tex)"

cp a.tex ga.tex

printf '{'$reformfile'}\n' >> ga.tex && echo $end >> ga.tex


pdflatex ga
mv ga.pdf heatmap_of_$panelname.pdf 
rm ga.tex
rm *.log
rm *.aux
mkdir -p output
mv heatmap_of_$panelname.pdf $rawfile $reformfile ./output
clear
printf '\a'
echo "If you see this, then the script is finished. The pdf-file is located in the output folder"
echo ""
