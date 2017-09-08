work_dir=zh-en
name=doc
source=fast/$name.zh
target=fast/$name.en
lex_e2f=$work_dir/en_lex.e2f_f
model=$work_dir/model/500w.zhen.model.p
output_name=$work_dir/match/$name.match

#Load-Match(Wiki) Options:
#    -m, --match         Start Load-Test-Match.
#    --ms=SOURCEFILE_M   Sourcefile name.[default: zh-en/200.test.zh]
#    --mt=TARGETFILE_M   Targetfile name.[default: zh-en/200.test.en]
#    --mlm=LEXICAL       Lexical_Model name.[default: zh-en/zh2e_f]
#    --mm=MODEL          maximum entropy model name.[default: object/model.p]
#    --mh=OK_RATE        OK RATE greater than.[default: 0.95]
#    --mc=CORES          The amount of cores.[default: 12]
#    --mo=OUTPUTFILE_M   Outputfile name.[default: match/1000.test.match]
#    --m_sort            Disable sort the original file.[default: True]
#    --ms_text=SOURCEFILE_T_ORIGIN
#                        unprocess of sourcefile name.[default: ]
#    --mt_text=TARGETFILE_T_ORIGIN
#                        unprocess of targetfile name.[default: ]
#    --m_all=M_ALL       Output format as all source sentences to target
#                        sentences.[default: False]


#--m_sort 
python wiki_Alinger.py -m \
--mm $model \
--mlm $lex_e2f \
--ms $source \
--mt $target \
--mh 0.0 --m_sort 1 --m_lower 1 \
--mc 8 --mo $output_name

