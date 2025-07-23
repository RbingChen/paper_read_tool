# coding:utf-8
import json
import requests
import logging

APP_ID = "1913043036402708564"
ds_r1 = ["Doubao-deepseek-r1", "deepseek-r1-friday", "deepseek-v3-friday", "deepseek-chat"]
Qwq = ["QwQ-32B-Friday"]


def llm_api_response(user_inputs, system_prompt="", app_id="1913043036402708564", model='deepseek-r1-friday'):
    api_base = 'https://aigc.sankuai.com/v1/openai/native/chat/completions'
    header = {'Content-type': 'application/json', 'Authorization': 'Bearer {appid}'.format(appid=app_id)}
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_inputs}]
    try:
        data = json.dumps({
            "messages": messages,
            "stream": "false",
            "temperature": 0.6,
            'model': model,
            'top_p':0.85,
            'frequency_penalty':0.2,
            'presence_penalty':0.2,
            'top_k':5,
            'max_tokens': 8192
        })
        res = requests.post(url=api_base, headers=header, data=data)
        result = json.loads(res.text)
        print(result)
        ret = result['choices'][0]['message']['content']

        # logger.info("[GPT4响应] completion response : {}".format(json.dumps(result, ensure_ascii=False)))
        return ret
    except Exception as e:
        # logger.exception( "[GPT4请求异常]: " + repr(e)
        #                  + "\t\t[GPT4请求参数]" + json.dumps(messages, ensure_ascii=False)
        #                  + "\t\t[GPT4响应结果]")

        return None


prompt= """
1、角色设定：你是一个算法专家，非常擅长阅读各种语言的论文阅读。现在需要完成一下任务。  
2、核心任务：
  a、内容理解：请输出对文本给出理解、解释、认知。
  b、内容翻译：把文本翻译成中文，注意区分标题、段落标题、图片、数学公式定义等。
  c、摘要总结：请对文本做一个摘要总结，概括核心内容
  d、术语识别：识别文本中提到的关键术语，并给出详细解释 
3、输出要求：
  a、翻译的输出，要英文与中文对照，做好分段落，不要一句一对照。
  b、4个任务整合成html格式输出，确保前端可以渲染。 
  c、渲染样式要求。视觉层次：使用不同颜色区分原文和翻译内容；专业排版：原文使用浅灰色背景+灰色边框，翻译使用浅绿色背景+绿色边框，图示使用黄色背景突出显示
   公式居中展示并添加编号说明；术语高亮：所有关键技术术语使用红色粗体显示，并包含英文原文；数学公式支持：通过MathJax完美渲染LaTeX公式；语义化结构：使用恰当的HTML标签组织内容层次
4、输出格式：{"output": "可渲染为html网页的文本"}  
5、输入文本如下：  
"""



