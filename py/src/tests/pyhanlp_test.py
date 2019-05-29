# -*- coding: utf-8 -*-

from pyhanlp import HanLP
import pkuseg
import stanfordnlp



resume = '''
姚波先生,非执行董事候选人。1971年出生,北美精算师协会会员(FSA),并获得美国纽约大学工商管理硕士学位。自2009年6月起出任中国平安执行董事,自2010年4月和2009年6月起分别出任中国平安首席财务官和副总经理,于2012年10月起出任中国平安总精算师,于2016年1月起出任中国平安常务副总经理。2010年6月至今,任平安银行(原深圳发展银行)董事。姚波先生于2001年5月加入中国平安,2009年6月至2016年1月任中国平安副总经理,2008年3月至2010年4月任中国平安财务负责人,2007年1月至2010年6月任中国平安总精算师,2004年2月至2007年1月任中国平安财务副总监,2004年2月至2012年2月期间兼任中国平安企划部总经理,2002年12月至2007年1月任中国平安副总精算师,2001年至2002年曾任中国平安产品中心副总经理。自2016年5月30日起担任平安健康医疗科技有限公司非执行董事。
'''

resume1 = '''姚波先生,非执行董事候选人。1971年出生,北美精算师协会会员(FSA),并获得美国纽约大学工商管理硕士学位。'''
resume2 = '姚波先生是非执行董事候选人'

def stanfordseg():
    nlp = stanfordnlp.Pipeline(lang='zh', use_gpu=True)
    doc = nlp(resume2)
    # help(doc.sentences[0])
    for sec in doc.sentences:
        print(sec.text)
    # print(doc.sentences[0].print_dependencies())

def hanseg(resume):
    # segment = HanLP.newSegment("CRF").enableAllNamedEntityRecognize(True)
    # print(segment.seg(resume2))
    # sentence = HanLP.parseDependency('姚波先生是非执行董事候选人')
    # for word in sentence.iterator():  # 通过dir()可以查看sentence的方法
    #     print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))

    # segment = HanLP.newSegment().enableAllNamedEntityRecognize(True)
    # print(segment.seg(resume))
    # segment = HanLP.newSegment().enableOrganizationRecognize(True)
    # print(segment.seg(resume))

    # nlp = StanfordCoreNLP("/Users/eamon/dev/quant/kg/py/corpus/stanford-corenlp-full-2018-02-27",lang='zh')
    print(nlp.ner(resume2))

# hanseg(resume)
# seg = pkuseg.pkuseg(postag=True)
# print(seg.cut(resume))
stanfordseg()