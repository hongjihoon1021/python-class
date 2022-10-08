scores={'김채린':85,'박수정':98,'함소희':94,'안예림':90,'연수진':93}
sum_=0
for key in scores:
    score=scores[key]
    print(key,':',score)
    sum_+=score
print('합계:',sum_,'평균:',sum_/len(scores))
