import requests
import os
from lxml import etree
import pandas as pd
import numpy as np
import time

if __name__ == "__main__":
    if not os.path.exists('./rateMyProf'):
        os.mkdir('./rateMyProf')

    url = 'https://www.ratemyprofessors.com/professor?tid=%d'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }

    def null_transform(text):
        # if retrieved empty list, transform it into 'N/A' as a placeholder
        text_null = text
        if text_null == []:
            text_null = ['N/A']
        return text_null


    def dup_main(text, num):
        """
        @param text: retrieved content from html sources
        @param num: number of times to be repeated
        """
        dup_list = []
        if len(text) > 1:
            for _ in range(num):
                dup_list.append(text)
            return dup_list

        if text == []:
            text = ['N/A']  # null as a placeholder

        try:
            dup_list = [item for item in text for _ in range(num)]
            return dup_list
        except IndexError:
            print("Index out of range:No content is retrieved, Pass to next one")

        pass


    for pageNum in range(250000, 260000):
        # avoid IP blocking and pressure on server, sleep for random seconds
        time.sleep(np.random.randint(1, 3))
        print("Crawling Page: ", pageNum)

        new_url = format(url % pageNum)
        page_text = requests.get(url=new_url, headers=headers).text
        tree = etree.HTML(page_text)

        # retrieve professor's main page attributes
        rate = tree.xpath('/html/body/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/div[1]/div/div[1]/text()')
        firstName = tree.xpath('/html/body/div[2]/div/div/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]/text()')
        lastName = tree.xpath('/html/body/div[2]/div/div/div[4]/div[1]/div[1]/div[2]/div[1]/span[2]/text()')
        # if all empty, no enough information, skip this page
        if not all([rate, firstName, lastName]):
            print("No enough information, retrieve next page")
            continue

        name = [(firstName[0] + lastName[0]).strip()]  # remove empty space
        print(name)

        take_again = tree.xpath('/html/body/div[2]/div/div/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/text()')
        difficulty = tree.xpath('/html/body/div[2]/div/div/div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/text()')
        tags = tree.xpath('/html/body/div[2]/div/div/div[4]/div[1]/div[1]/div[5]/div[2]//text()')

        # student comments' blocks
        li_list = tree.xpath('//*[@id="ratingsList"]/li')
        n = len(li_list)  # number of comments retrieved

        # to make entries' indexes consistent, we need to duplicate main page attributes
        rate_list = dup_main(rate, n)
        name_list = dup_main(name, n)
        takeAgain_list = dup_main(take_again, n)
        diff_list = dup_main(difficulty, n)
        tags_list = dup_main(tags, n)

        # Loop to retrieve attributes from every student's comment block
        emotion_list = []
        quality_list = []
        sd_list = []
        bg_list = []
        comment_list = []
        commentTags_list = []

        for li in li_list:
            emotion = li.xpath('./div/div/div[3]/div[1]/div[1]/div[2]/text()')
            emotion_list.extend(null_transform(emotion))

            quality = li.xpath('./div/div/div[2]/div[1]/div/div[2]//text()')
            quality_list.extend(null_transform(quality))

            s_difficulty = li.xpath('./div/div/div[2]/div[2]/div/div[2]//text()')
            sd_list.extend(null_transform(s_difficulty))

            background = li.xpath('./div/div/div[3]/div[2]//text()')
            bg_list.append(null_transform(background))
            # here we use 'append()' because background will a multi-value list

            comment = li.xpath('./div/div/div[3]/div[3]//text()')
            comment_list.extend(null_transform(comment))

            comment_tags = li.xpath('./div/div/div[3]/div[4]//text()')
            commentTags_list.append(null_transform(comment_tags))

        df = pd.DataFrame({'Name': name_list,
                           'OverallRate': rate_list,
                           'TakeAgain': takeAgain_list,
                           'Overall_Difficulty': diff_list,
                           'Tags': tags_list,
                           'Emotion': emotion_list,
                           'QualityRate': quality_list,
                           'StudentDifficulty': sd_list,
                           'Background': bg_list,
                           'Comment': comment_list,
                           'CommentTags': commentTags_list})

        # print(df)
        path = './rateMyProf/' + str(name[0]) + '.csv'
        df.to_csv(path)
        print('Success!')
