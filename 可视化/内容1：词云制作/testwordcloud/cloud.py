import jieba
from wordcloud import WordCloud
import matplotlib.pyplot  as plt
from imageio import imread
from matplotlib.font_manager import FontProperties
import json
def eng_wordcloud():
    with open('economy_goals.txt','r') as f:
        text = f.read()
    mask = imread('chinamap.png')
    wc = WordCloud(background_color='white',mask=mask).generate(text=text)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file("eng_cloud.png")
def chn_wordcloud():
    with open("2023.txt",'r',encoding='utf-8') as f:
        data=f.read()
    words=list(jieba.cut(data))
    words = [word.strip() for word in words]
    with open('stopword.txt','r',encoding='utf-8') as f:
        stopwords=f.readlines()
    stopwords = [word.strip() for word in stopwords]
    while '\n' in words:
        words.remove('\n')
    filtered_words = [word for word in words if word not in stopwords]
    print(words)
    word_dict={}
    for key in filtered_words :
        word_dict[key]=word_dict.get(key,0)+1
    mask = imread('chinamap.png')
    wc = WordCloud(font_path='HarmonyOS.ttf',background_color='white',mask=mask)
    wc.generate_from_frequencies(word_dict)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    font_set =  FontProperties(fname="HarmonyOS.ttf",size=30)
    plt.title('2023新春贺词',fontproperties=font_set)
    plt.show()
    wc.to_file('chn_wordcloud.png')
if __name__ == '__main__':
    eng_wordcloud()
    chn_wordcloud()