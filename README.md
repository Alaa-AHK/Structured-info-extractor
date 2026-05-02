# AI Structured Information Extractor

A Python-based AI tool that leverages Large Language Models (LLMs) and LangChain's Output Parsers to transform unstructured text—such as biographies or support messages—into validated, machine-readable JSON.

## Features
- **Strict JSON Output:** Uses `JsonOutputParser` to ensure responses follow a specific schema.
- **Data Validation:** Integrates Pydantic for type safety and field validation.
- **Missing Value Handling:** Automatically returns `null` for fields not found in the source text.
- **Kaggle Ready:** Optimized for execution in cloud environments like Kaggle or Google Colab.

## Tech Stack
- **Framework:** [LangChain](https://www.langchain.com/)
- **LLM:** OpenAI GPT-3.5/4 (Configurable)
- **Validation:** Pydantic
- **Environment:** Python 3.8+

## Requirements

The extractor identifies the following fields:
- `name`: Full name of the individual.
- `email`: Contact email address.
- `Age`: Numerical age.
- `Faculty`: Academic department or faculty.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Alaa-AHK/Structured-info-extractor](https://github.com/Alaa-AHK/Structured-info-extractor)
   cd Structured-info-extractor