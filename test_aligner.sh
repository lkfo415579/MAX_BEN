work_dir=zh-en
source=$work_dir/s_200w.20w.zh
target=$work_dir/s_200w.20w.en
#source=$work_dir/test/junk.zh
#target=$work_dir/test/junk.pt
lex_e2f=$work_dir/lex.e2f_f
model=$work_dir/model/200w.model.p
output_name=$work_dir/output/output

#Load-Test-Find Options:
#-t, --test          Start Load-Test-Find.
#--ts=SOURCEFILE_T   Sourcefile name.[default: zh-en/test/test.zh]
#--tt=TARGETFILE_T   Targetfile name.[default: zh-en/test/test.en]
#--tlm=LEXICAL       Lexical_Model name.[default: zh-en/zh2e_f]
#--tm=MODEL          maximum entropy model name.[default: object/model.p]
#--tw=WRONG_RATE_T   WRONG RATE greater than.[default: 0.95]
#--to=OK_RATE_T      OK RATE greater than.[default: 0.95]
#--tc=CORES          The amount of cores.[default: 12]
#--tf=OUTPUTFILE     Outputfile(ok,mid,wrong) ,total 3 files.[default: zh-en/output]
#--te=TESTSET        The percentage of testset size.[default: 0.07]
#--ts_text=SOURCEFILE_T_ORIGIN unprocess of sourcefile name.[default: ]
#--tt_text=TARGETFILE_T_ORIGIN unprocess of targetfile name.[default: ]


python nAligner.py -t \
--ts $source \
--tt $target \
--tlm $lex_e2f \
--tm $model \
--tc 26 \
--to 0.97 \
--tw 0.97 \
--tf $output_name
