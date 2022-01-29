import os


def get_file_list(dir_name):
    return os.listdir(dir_name)


def get_contents(file_list):
    y_category = []
    x_text = []
    # 0-> baseball news
    # 1-> soccer news
    # 2-> Unknown (e.g., crawling file)
    category = {0: "2", 1: "0", 2: "0", 3: "0", 4: "0", 5: "1", 6: "1", 7: "1", 8: "1"}

    for file_name in file_list:
        try:
            f = open(file_name, "r", encoding="euc-kr")
            read_ctgy = int(file_name.split(os.sep)[1].split("_")[0])
            y_category.append(category[read_ctgy])
            x_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)

    return x_text, y_category


def get_clean_text(text):
    import re
    text = re.sub("\W+", "", text.lower())
    return text


def get_corpus_dict(text):
    text = [sen.split() for sen in text]
    clean_set = [get_clean_text(word) for words in text for word in words]
    from collections import OrderedDict
    dic = OrderedDict()
    for i, v in enumerate(set(clean_set)):
        dic[v] = i
    return dic


def get_count(text, corpus):
    text = [sen.split() for sen in text]
    word_num = [[corpus[get_clean_text(word)] for word in words] for words in text]
    x_vec = [[0 for _ in range(len(corpus))] for x in range(len(text))]

    for i, text in enumerate(word_num):
        for word_num in text:
            x_vec[i][word_num] += 1
    return x_vec


def get_similarity(v1, v2):
    import math
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x**2
        sumyy += y**2
        sumxy += x*y
    return sumxy/(math.sqrt(sumxx*sumyy))


def score(x_vec, src):
    src_vec = x_vec[src]
    sim = []
    for target in x_vec:
        sim.append(get_similarity(src_vec, target))
    return sim


def ranking(sim, n):
    import operator
    x = {i:v for i, v in enumerate(sim)}
    new_x = sorted(x.items(), key = operator.itemgetter(1))
    return list(reversed(new_x))[1:n+1]


def accurancy(sim, y_category, src):
    src_category = y_category[src]
    return sum([src_category == y_category[i[0]] for i in sim]) / len(sim)


if __name__ == "__main__":
    # Get file contents from directory.
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]

    # Generate corpus
    x_text, y_class = get_contents(file_list)
    corpus = get_corpus_dict(x_text)
    print("Number of words : {0}".format(len(corpus)))

    # Get the number of same word vectors
    x_vec = get_count(x_text, corpus)
    src_num = 10
    result = []

    # Calculate similarity
    for i in range(len(y_class)):
        src_num = i
        sim_score = score(x_vec, src_num)
        sim_news = ranking(sim_score, 10)
        if y_class[src_num] == '2':
            print("Target file:", file_list[src_num])
            for rank in sim_news:
                tgt_num, similarity = rank
                print("Similarity:", similarity * 100, file_list[tgt_num])
        acc_score = accurancy(sim_news, y_class, src_num)
        result.append(acc_score)

    print("Total average accuracy:", sum(result)/len(y_class))
