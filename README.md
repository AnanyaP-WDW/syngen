# Syngen

Create finetuning/distillation data fast! Multi-model support to de-risk against single model biases.

- Multi-model support through Anyscale endpoints [Anyscale endpoint key required](https://www.anyscale.com/endpoints)
- Structured JSON output

## Work in Progress (WIP)

## Rationale

1. Create finetuning/distillation data fast and inexpensively.
2. Focus on using multiple models (e.g., meta-llama/Llama-2-7b-chat-hf, mistralai/Mistral-7B-Instruct-v0.1 etc.) to mitigate single model biases while generating new data.
3. Includes JSON repair mechanisms for outputting structured data.
4. Can work on top of rationale-based step-by-step and curriculum learning finetuning methods:
   - [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://arxiv.org/pdf/2305.02301.pdf)
   - [Orca: Progressive Learning from Complex Explanation Traces of GPT-4](https://arxiv.org/pdf/2306.02707.pdf)

## Example Usage

```bash
python -m venv venv  # Create a new virtual environment
source venv/bin/activate  # Activate the virtual environment
git clone https://github.com/AnanyaP-WDW/syngen.git
cd syngen
pip install .
```
#### check for correct installation
```bash
python -c "import syngen"
```

```python
USE_CASE = "customer review"
intro_prompt = f"""You are a helpful, intelligent chatbot. Create labeled data in json format using the given {USE_CASE}. For the {USE_CASE} output NPS score, ticket description, sentiment, customer insights, class of customer insights, class of ticket description and reasoning"""

json_prompt = """\n\nDesired JSON output format:
{
    "NPS score": "on a scale of 1 to 10 how likely would the customer recommend the product",
    "ticket description": "describe the review in few words",
    "sentiment": "sentiment of the review",
    "customer insights": "insights from the review in few words",
    "class of customer insights": "broad class in which the customer insights belong",
    "class of ticket description": "broad class in which the ticket description belong",
    "rationale": "describe in few words the rationale behind the choices"
}


Output:
```json"""

iter_list = ["The chess is, well, chess. You can choose different themes for your board (which I think is cool). There are also different types of games you can start: chess 960 (all pieces behind pawns are in random spots), rated (takes pieces away from the opponent who has a higher elo), and standard (self explanatory). My only problems with the app are that you need to buy premium to get unlimited lessons, game review, and puzzles.",
             "This is a great chess app especially for beginners. The reason I rate four stars is there is one large problem with the lessons, as far as I can tell there's no transcript and no subtitles. Which can be a big problem for the hearing impared, people with audio processing issues, or people that are in an environment that they can't turn the sound on their phone.",
             "Overall a great app and has led me to become a much better Chess player, and I actually won a Chess tournament in my middle school because of it. It does annoy me that there is a lot of stuff locked behind a subscription. But that is to be expected. EDIT: My trophies are working now. Thank you for the fix. But now I getting matched in leagues with tryhards grinding to 500 trophies when top 3 used to be like 175 trophies. But I guess it can't be helped. Still gets five stars for trophies working."]

request = GenRequest(seed_data = iter_list)
generator = SynGen(anyscale_API_KEY = "YOUR ANYSCALE API KEY",
                   intro_prompt = intro_prompt,
                   json_prompt = json_prompt
                   )
generator.run(iter_list)
```
##### expected output
```bash


({0: {'NPS score': '8',
   'ticket description': 'Mixed feelings about the chess app',
   'sentiment': 'Positive',
   'customer insights': 'Premium features are behind a paywall',
   'class of customer insights': 'Product Feature',
   'class of ticket description': 'Feature Request / Feedback',
   'rationale': 'The customer has given a high NPS score of 8, indicating a positive sentiment towards the app. They appreciate the different themes and game types. However, they have mentioned that premium features are behind a paywall, indicating a request for free access to these features or a feature request for more flexibility in accessing lessons, game review, and puzzles.'},
  1: {'NPS score': '8',
   'ticket description': 'Great chess app for beginners, but lacks transcript and subtitles',
   'sentiment': 'Positive',
   'customer insights': 'App is good for beginners, but needs improvements for accessibility',
   'class of customer insights': 'Accessibility',
   'class of ticket description': 'App features',
   'rationale': 'The reviewer gave 4 stars because the app is great for beginners, but it lacks transcript and subtitles, which can be a big problem for some users.'},
  2: {'NPS score': '9',
   'ticket description': 'Positive review with some minor complaints',
   'sentiment': 'Positive',
   'customer insights': 'App helped improve Chess skills and won a tournament',
   'class of customer insights': 'User Experience',
   'class of ticket description': 'Product Review',
   'rationale': 'The review is mostly positive with a few minor complaints about locked features and matchmaking. The user still gives the app five stars.'}},
 {})
```

## Requirements
- Anyscale endpoint API key required
- Only JSON output format from LLM's