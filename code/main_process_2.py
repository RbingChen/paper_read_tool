# coding:utf-8
import re
import json
from util_pdf import extract_text_pdfplumber, extract_text_pypdf

from util_llm import llm_api_response, prompt
from util_json import extract_json_from_string, extract_json_simple, string_find_json,extract_and_repair_html


name =  "RankerMixer"
pdf_path = "../input_data/" +name+".pdf"

texts = extract_text_pypdf(pdf_path)

output_path = "../output_data/"+name+"/"
for ind, text in enumerate(texts):
    page = f"第{ind}页/{len(texts)}页"

    print(page)
    try_cnt = 0
    while try_cnt < 2:
        try:
            ret = llm_api_response(prompt + text)
            ret_ = extract_json_simple(ret)
            if ret_ is None:
                ret_ = extract_and_repair_html(ret)
            if ret_ is not None:
                print(ret_)
                with open(output_path + str(ind) + ".html", "w", encoding="utf-8") as f:
                   if isinstance(ret_, str):
                       ret_= ret_.replace("\\n", "\n")
                       ret_= ret_.replace('\\"', '\"')
                       f.write(ret_)
                   else:
                      f.write(ret_["output"])
                break
        except Exception as e:
            print(repr(e))
            print("error in " + page)
            try_cnt += 1

