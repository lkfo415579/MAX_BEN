print "En Checker[zh file contains english then remove it.]"
def check_eng(sentence):
    sentence = sentence.split()
    en_word_count = 0
    for word in sentence:
        if any(c.isalpha() for c in word):
            en_word_count += 1
    if en_word_count > 2:
        return True
    else:
        return False
def check_eng_byDict(sentence):
    import enchant
    sentence = sentence.split()
    d = enchant.Dict("en_US")
    en_word_count = 0
    for word in sentence:
        if d.check(word):
            en_word_count += 1
    if en_word_count > 3:
        return True
    else:
        return False

def check_eng_one(sentence):
    if any(c.isalpha() for c in sentence):
        return True
    else:
        return False

def read_corpus(dir):
    import sys
    print '########Reading Zh sentences From file "' + dir + '"###########'

    def number_file(dir):
        with open(dir) as f:
            return sum(1 for _ in f)

    # len_p = number_file(file)
    with open(dir + '.zh') as f:
        zh_lines = f.readlines()
    with open(dir + '.pt') as f:
        pt_lines = f.readlines()
    print "Len of zh,pt files : %s " % len(zh_lines)
    #check en
    en_lines = []
    output_pt_lines = []
    for line_num in range(0,len(zh_lines)):
        if line_num % 2000 == 0:
            sys.stdout.write('Index: %d\r' % line_num)
            sys.stdout.flush()
        if check_eng(zh_lines[line_num]):
            en_lines.append(zh_lines[line_num])
            output_pt_lines.append(pt_lines[line_num])
            zh_lines[line_num] = "&&&&&&"
            pt_lines[line_num] = "&&&&&&"
        #if line_num > 30000:
        #    break
    #write en_line into new file
    with open(dir + '.parallel_en.en', 'w') as file:
        file.writelines(en_lines)
    with open(dir + '.parallel_en.pt', 'w') as file:
        file.writelines(output_pt_lines)
    #original removed ver
    zh_lines = [line for line in zh_lines if line != "&&&&&&"]
    pt_lines = [line for line in pt_lines if line != "&&&&&&"]

    print "------After Removed original len (%s)------" % len(zh_lines)

    with open(dir + '.re.zh', 'w') as file:
        file.writelines(zh_lines)
    with open(dir + '.re.pt', 'w') as file:
        file.writelines(pt_lines)
    print '########End###########'
    return 1


def extract():
    import sys
    if len(sys.argv) != 2:
        print 'Usage: python', sys.argv[0], 'input-file'
        exit()
    input_file = sys.argv[1]

    read_corpus(input_file)


if __name__ == "__main__":
    extract()