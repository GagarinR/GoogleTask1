# coding: utf-8

import re
import math

def answer1(n):
    n = '2357111317192329313741434753596167717379838997101103107109113127131137139149151157163167173179181191193197199'
    primal_num = n  # string
    matched_list = []




    for i in range(0, 11):

        print '~~~~~~ %d ~~~~~~' % i
        print i
        if i == 0:
            print '23571'
        else:
            prefix_num = 5 - len(str(i))

            pattern = re.compile(r'\d{%d}%d' % (prefix_num, i))
            match = pattern.findall(primal_num)

            if match:
                print 'match: ', match, i

                locals()
                primal_num = primal_num.replace(match[0], '')
                matched_list.extend(match)

                return match[0]

            else:
                return -1

                # print matched_list

def answer(n):
    #pnum = '2357111317192329313741434753596167717379838997101103107109113127131137139149151157163167173179181191193197199'
    count = 2
    pnum=""
    while count<= 10007:
        prime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                prime = False
                break

        if prime:
            #count += count
            #print count
            pnum += str(count)
        count += 1


    print pnum


    print pnum[n:5+n]




print answer(3)




def main():
    count = 3
    n=""
    while count<= 10007:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            #count += count
            #print count
            n += str(count)
        count += 1


    print n
#main()