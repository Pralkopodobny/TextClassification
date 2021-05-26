import pandas as pd
import enchant
def clear_file2(filename : str, output_file : str):
    y = pd.read_csv(filename, error_bad_lines=False, delimiter='cudownynapis', header=None)
    dictionary = enchant.Dict("en_US")
    i = 0
    for line in y[0]:
        words = line.split(' ')
        newline = ''
        for word in words:
            if dictionary.check(word) and word != '.':
                newline += word + ' '
        y[0][i] = newline + '\n'
        i += 1
    output_file.writelines(y[0])

if __name__ == '__main__':
    
    subj = open('.\\scale_data\\scaledata\\subj.txt', 'w')
    clear_file2('.\\scale_data\\scaledata\\James+Berardinelli\\subj.James+Berardinelli', subj)
    print('done')
    clear_file2('.\\scale_data\\scaledata\\Dennis+Schwartz\\subj.Dennis+Schwartz', subj)
    print('done')
    clear_file2('.\\scale_data\\scaledata\\Scott+Renshaw\\subj.Scott+Renshaw', subj)
    print('done')
    clear_file2('.\\scale_data\\scaledata\\Steve+Rhodes\\subj.Steve+Rhodes', subj)
    print('done')
    subj.close()

    r1 = r2 = r3 = r4 = ""
    with open('.\\scale_data\\scaledata\\Dennis+Schwartz\\rating.Dennis+Schwartz') as fp:
        r1 = fp.read()
    with open('.\\scale_data\scaledata\\James+Berardinelli\\rating.James+Berardinelli') as fp:
        r2 = fp.read()
    with open('.\\scale_data\\scaledata\\Scott+Renshaw\\rating.Scott+Renshaw') as fp:
        r3 = fp.read()
    with open('.\\scale_data\\scaledata\\Steve+Rhodes\\rating.Steve+Rhodes') as fp:
        r4 = fp.read()
    r1 += r2
    r1 += r3
    r1 += r4
    with open('.\\scale_data\\scaledata\\rating.txt', 'w') as fp:
        fp.write(r1)

    l1 = l2 = l3 = l4 = ""
    with open('.\\scale_data\\scaledata\\Dennis+Schwartz\\label.3class.Dennis+Schwartz') as fp:
        l1 = fp.read()
    with open('.\\scale_data\scaledata\\James+Berardinelli\\label.3class.James+Berardinelli') as fp:
        l2 = fp.read()
    with open('.\\scale_data\\scaledata\\Scott+Renshaw\\label.3class.Scott+Renshaw') as fp:
        l3 = fp.read()
    with open('.\\scale_data\\scaledata\\Steve+Rhodes\\label.3class.Steve+Rhodes') as fp:
        l4 = fp.read()
    l1 += l2
    l1 += l3
    l1 += l4
    with open('.\\scale_data\\scaledata\\label.3class.txt', 'w') as fp:
        fp.write(l1)