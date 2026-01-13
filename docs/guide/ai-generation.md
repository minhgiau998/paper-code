# AI-Powered Generation

Generate intelligent project descriptions using OpenAI's GPT models.

## Overview

Instead of manually writing project descriptions, PAPER-CODE can analyze your tech stack and generate contextual descriptions using AI.

## Setup

### 1. Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Create an account or sign in
3. Navigate to [API keys](https://platform.openai.com/account/api-keys)
4. Create a new API key
5. Copy the key

### 2. Set Environment Variable

```bash
# Create .env file in project root
echo "OPENAI_API_KEY=sk-..." > .env
```

Or export as environment variable:

```bash
export OPENAI_API_KEY=sk-...
```

## Basic Usage

Generate documentation with AI-powered descriptions:

```bash
paper-code init --ai-generate
```

The wizard will:

1. Ask for your project configuration
2. Connect to OpenAI API
3. Generate a contextual description
4. Generate all documentation with the AI description

## Advanced Usage

### With Custom Context

Provide additional context for more accurate descriptions:

```bash
paper-code init \
  --ai-generate \
  --ai-hint "E-commerce platform with real-time inventory management"
```

### Batch Mode

Use AI generation in batch mode:

```json
{
  "projects": [
    {
      "name": "Frontend App",
      "type": "frontend",
      "stack": "React",
      "libraries": ["TypeScript", "TailwindCSS"],
      "aiGenerate": true,
      "aiHint": "Interactive dashboard for analytics"
    }
  ]
}
```

## How It Works

### Model Selection

PAPER-CODE uses GPT-4 (or GPT-3.5 as fallback) to generate descriptions with the context:

```
Given:
- Project Type: Frontend
- Tech Stack: React
- Libraries: TypeScript, TailwindCSS, TanStack Query
- Optional Hint: Dashboard for analytics

Generate: A 2-3 sentence project description suitable for a README
```

### Example Prompt

```
Create a concise, engaging project description (2-3 sentences) for:
- Project Name: My Analytics Dashboard
- Type: Frontend Application
- Tech Stack: React with TypeScript
- Libraries: TailwindCSS for styling, TanStack Query for data fetching
- Additional Context: Real-time analytics dashboard with interactive charts

The description should:
1. Be written for the project README
2. Clearly explain the purpose
3. Highlight key technologies if relevant
4. Be professional but accessible
```

### Generated Example

```
My Analytics Dashboard is a modern web application built with React and
TypeScript for real-time data visualization and analysis. Using TailwindCSS
for elegant styling and TanStack Query for efficient data fetching, it provides
an interactive interface for exploring complex analytics data with responsive
design for all devices.
```

## Cost Estimation

### Pricing

- **GPT-4**: ~$0.03 per description
- **GPT-3.5**: ~$0.001 per description

### Monthly Budget

| Descriptions | GPT-4  | GPT-3.5 |
| ------------ | ------ | ------- |
| 10           | $0.30  | $0.01   |
| 100          | $3.00  | $0.10   |
| 1,000        | $30.00 | $1.00   |

## Best Practices

### 1. Use Meaningful Hints

```bash
# ✅ Good
paper-code init --ai-hint "ML pipeline for image classification with model deployment"

# ❌ Vague
paper-code init --ai-hint "ML project"
```

### 2. Verify Generated Content

Always review the AI-generated description:

```bash
# Generated: My Analytics Dashboard is a modern...

# Validate against your project:
# ✅ Accurate tech stack representation
# ✅ Clear project purpose
# ❌ Mentions feature X that doesn't exist yet (edit manually)
```

### 3. Customize After Generation

The AI-generated description is a starting point. Always customize:

```markdown
# My Analytics Dashboard

<!-- AI Generated Start -->

My Analytics Dashboard is a modern web application built with React and
TypeScript for real-time data visualization and analysis.

<!-- AI Generated End -->

## Key Features

- Real-time data updates
- Interactive charts and visualizations
- User authentication and authorization
- Export data to CSV/PDF

## Getting Started

...
```

## Fallback Behavior

If the API call fails, you'll be prompted to enter a description manually:

```
🤖 Generating AI description...
⚠️  API call failed. Please enter a project description manually:
> My awesome project that does amazing things
```

## Cost Control

### Set API Spending Limits

1. Go to [OpenAI Billing](https://platform.openai.com/account/billing/overview)
2. Set "Hard limit" in Usage limits
3. AI generation will fail gracefully if limit reached

### Use Budget-Friendly Model

```bash
# Environment variable to use GPT-3.5 instead of GPT-4
export OPENAI_MODEL=gpt-3.5-turbo
paper-code init --ai-generate
```

## Troubleshooting

### "API key not found"

```bash
# Check if .env file exists
cat .env

# Or check environment variable
echo $OPENAI_API_KEY

# Set it again
export OPENAI_API_KEY=sk-...
```

### "Rate limit exceeded"

Wait a few moments and try again. OpenAI enforces rate limits on API usage.

### "Invalid API key"

Verify your API key is correct:

```bash
# Check first 20 characters (should not include 'sk-' prefix issues)
echo $OPENAI_API_KEY | cut -c1-20
```

### "Connection timeout"

Check your internet connection and OpenAI API status.

## Privacy & Security

- **Local Processing**: Only the final description is stored locally
- **API Calls**: Project type/stack are sent to OpenAI API
- **Encryption**: Use HTTPS for API calls
- **No Training**: OpenAI doesn't train on your API calls (with API usage tier)

## Disabling AI Generation

If you prefer manual descriptions:

```bash
paper-code init  # Omit --ai-generate flag
```

You'll be prompted to enter description manually.

## Custom AI Provider

To use a different LLM provider (Claude, Cohere, etc.), modify:

```python
# src/ai_service.py
class AIService:
    def __init__(self, provider='openai'):
        if provider == 'claude':
            self.client = anthropic.Anthropic()
        else:
            self.client = openai.OpenAI()
```

---

For more information, see the [Quick Start guide](./quick-start.md) or [CLI Usage](./cli-usage.md).
