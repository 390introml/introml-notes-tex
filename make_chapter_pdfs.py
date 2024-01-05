#!/usr/local/bin/python3

"""
Split top.pdf into individual PDFs and copy to chapter_pdfs/chapter_TITLE.pdf
"""

import os
import re
import json

tfn = "top.toc"
dfn = "lecture_note_chapters.json"

cinfo = []

for k in open(tfn):
    if k.startswith("%"):
        continue

    # See if regular chapter
    m = re.search("{chapter}{\\\\numberline {([0-9A-Z]+)}(.*?)}{([0-9]+)}{", k)
    if m:
        # print("Found chapter:", k) #debug
        cnum = m.group(1)
        title = m.group(2)
        page = int(m.group(3)) + 1
        print("%s. %s: %s" % (cnum, title, page))
        cinfo.append({"cnum": cnum, "title": title, "page": page})
        continue

    # else see if Index
    m = re.search("{chapter}{Index}{([0-9]+)}{", k)
    if m:
        # print("Found Index:", k) #debug
        cnum = "Index"
        title = "Index"
        page = int(m.group(1)) + 1
        print("%s. %s: %s" % (cnum, title, page))
        cinfo.append({"cnum": cnum, "title": title, "page": page})
        continue


for idx, cdat in enumerate(cinfo):
    # ofn = "../mitx/static/notes/chapter_%s.pdf" % cdat['title'].replace(' ', '_')
    # ofn = "../catsoop/__STATIC__/LectureNotes/chapter_%s.pdf" % cdat['title'].replace(' ', '_')
    ofn = "chapter_pdfs/chapter_%s.pdf" % cdat["title"].replace(" ", "_")
    cdat["filename"] = ofn
    pstart = cdat["page"]
    if idx + 1 < len(cinfo):
        pend = int(cinfo[idx + 1]["page"]) - 1
    else:
        pend = 9999
    print("Extracting pages %s to %s -> %s" % (pstart, pend, ofn))
    if pend > 999:
        eop = ""
    else:
        eop = pend
    ofnx = ofn[:-4] + "_%d.pdf"
    # cmd = "pdfseparate -f %s %s top.pdf %s" % (pstart, eop, ofnx)
    cmd = "pdfjam top.pdf %s-%s -o  %s" % (pstart, eop, ofn)
    print(cmd)
    os.system(cmd)

with open(dfn, "w") as fp:
    fp.write(json.dumps(cinfo, indent=4))

print("Wrote chapter info to %s" % dfn)
