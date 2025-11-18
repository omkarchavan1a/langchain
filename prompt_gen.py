from langchain_core.prompts import PromptTemplate


#template
template = PromptTemplate(
    template="""
Research Paper Type: {paper_input}
Writing Style: {style_input}
Desired Length: {length_input}

Title: [Enter your research paper title here]

Abstract:
[Provide a concise summary of the research paper, outlining the key problem, approach, and findings.]

Introduction:
[Introduce the background and importance of the topic, clearly state the research question or objective.]

Literature Review / Background:
[Summarize key existing research and theories relevant to your topic. Relate past findings to your current work.]

Methodology:
[Describe the methods used for investigation, data collection, or experimentation. Explain why these methods are appropriate.]

Results / Findings:
[Present the significant results or findings of your research. Use charts, tables, or figures as needed.]

Discussion:
[Interpret and discuss the implications of your findings. Highlight limitations, challenges, or interesting patterns.]

Conclusion:
[Summarize the main points of the paper and suggest future research directions or practical applications.]

References:
[List the references, articles, or books cited in your paper in the appropriate format.]

Appendices (if applicable):
[Provide any supplementary materials, such as raw data, questionnaires, or additional images.]
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,
)

template.save('template.json')


