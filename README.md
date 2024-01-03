# syngen
Create finetuning/distillation data fast! 
Multi-model support to de-risk against single model biases
## WIP

## Rationale
1) Create finetuning/distillarion data fast and cheap
2) Instead of using only gpt-4, which can introduce the same biases in the data thus created, we are focusing on using multiple models (meta-llama/Llama-2-7b-chat-hf,mistralai/Mistral-7B-Instruct-v0.1 etc.). This allows to derisk against single model biases while generating new data
3) Includes non-LLM and LLM based json reapair mechanism for outputing structured data
4) Can work on top of rationale based and step by step synthetic data generation (as explained
A) Distilling Step-by-Step! Outperforming Larger Language Models
with Less Training Data and Smaller Model Sizes - https://arxiv.org/pdf/2305.02301.pdf 
 B) Orca: Progressive Learning from Complex
Explanation Traces of GPT-4 - https://arxiv.org/pdf/2306.02707.pdf)