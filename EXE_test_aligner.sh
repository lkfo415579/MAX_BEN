work_dir=zh-en
source=fast/Bi-Subtitle.tok.zh
target=fast/Bi-Subtitle.tok.en
#source=fast/5k.zh
#target=fast/5k.en
lex_e2f=$work_dir/en_lex.e2f_f
model=$work_dir/model/500w.zhen.model.p
output_name=$work_dir/output/Bi-Subtitle

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
--tc 44 \
--to 0.95 \
--tw 0.95 \
--t_lower \
--tf $output_name
