work_dir=zh-en
#source=$work_dir/5k.zh
#target=$work_dir/5k.pt
source=~/200w.en-zh.zh
target=~/200w.en-zh.en
#source=~/1000.zh
#target=~/1000.en
#source=$work_dir/test/junk.zh
#target=$work_dir/test/junk.pt
lex_e2f=$work_dir/lex.e2f_f
model=$work_dir/model/200w.model.p
output_name=$work_dir/output/output

#Prepare-Training-Save Options:
#-r, --run           Start Prepare-Training-Save.
#--rs=SOURCEFILE_R   Sourcefile name.[default: zh-en/train/ted.zh]
#--rt=TARGETFILE_R   Targetfile name.[default: zh-en/train/ted.en]
#--rlm=LEXICAL       Lexical_Model name.[default: zh-en/zh2e_f]
#--rm=OUTPUTMODEL    Output maximum entropy model name.[default: zh-
#                en/model/model.p]
#--rf=OUTPUTFEATURE  Output featuresets file name.[default: no]
#--re=TESTSET        The percentage of testset size.[default: 0.0001]
#--rc=CORES          The amount of cores.[default: 12]
#--rTFPN=TFPN        The amount of testset for TFPN.[default: 1000]
#####
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

python nAligner.py -r \
--rs $source \
--rt $target \
--rlm $lex_e2f \
--rm $model \
--rc 38 \
--rf 200w.featuresets \
--re 0.001


