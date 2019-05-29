# -*- coding: utf-8 -*-

import jiagu

def extract_resume_info(resume):

    kn = jiagu.knowledge(resume)
    print(kn)
