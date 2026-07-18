import json
from urllib import response
from app.prompts.validation_prompt import validation_prompt
from app.rag.chain import chain
from app.rag.context_formatter import format_docs
from app .rag.retriever import retriever
from app.rag.llm import llm
from app.rag.retriever import vector_store
def evaluate():
    with open("app/evaluation/test_questions.json","r",encoding="utf-8")as f:
        questions=json.load(f)

    results=[]
    
    for item in questions:
        question=item["question"]
        docs_with_score=vector_store.similarity_search_with_relevance_scores(question,k=5)
        context=format_docs([doc for doc, score in docs_with_score])
        answer=chain.invoke(question).content
        validation_chain=validation_prompt | llm
        evaluation=validation_chain.invoke({"question":question,
                                            "context":context,
                                            "answer":answer})
        

        response = (
        evaluation.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
        )

        evaluation_json = json.loads(response)
        

        results.append({
            "question":question,
            "retrieved_documents": [
                {
                    "question":doc.metadata["question"],
                    "category":doc.metadata["category"],
                    "similarity_score":round(float(score),4),
                
                }
                for doc, score in docs_with_score
            ],
            "answer":answer,
            "evaluation":evaluation_json
        })

    with open("app/evaluation/results.json","w",encoding="utf-8")as f:
        json.dump(results,f,ensure_ascii=False,indent=4)

if __name__=="__main__":
    evaluate()
