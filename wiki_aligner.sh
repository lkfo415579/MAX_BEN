work_dir=zh-pt
source=$work_dir/wiki_zh.8055
#source=$work_dir/zh_wiki.delete.gb.segment.re
target=$work_dir/wiki_pt.8055
#target=$work_dir/pt_wiki.tok.re
#source=$work_dir/test/junk.zh
#target=$work_dir/test/junk.pt
lex_e2f=$work_dir/lex/lex.e2f_f
model=$work_dir/model/law2_t.model.p
output_name=$work_dir/match/anson3.match

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

#--m_sort 
python wiki_Alinger.py -m \
--mm $model \
--mlm $lex_e2f \
--ms $source \
--mt $target \
--mh 0.95 \
--mc 16 --mo $output_name

