# Installation

Get PAPER-CODE up and running in minutes.

## Requirements

- **Python:** 3.10 or higher
- **pip:** Python package manager

## Install from PyPI (Recommended)

The easiest way to install PAPER-CODE is from PyPI:

```bash
pip install paper-code
```

Verify the installation:

```bash
paper-code --version
```

## Install from Source (Development)

To contribute or use the latest development version:

```bash
# Clone the repository
git clone https://github.com/minhgiau998/paper-code.git
cd paper-code

# Install in development mode
pip install -e .
```

## Upgrade

To upgrade an existing installation to the latest version:

```bash
pip install --upgrade paper-code
```

Or to a specific version:

```bash
pip install paper-code==0.5.0
```

## Optional: API Key Setup

For AI-powered description generation, set up your OpenAI API key:

```bash
# Create .env file
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
```

Or export as environment variable:

```bash
export OPENAI_API_KEY=sk-your-api-key-here
```

## Verify Installation

Test the installation with a quick sanity check:

```bash
paper-code --help
```

You should see the help menu with all available commands.

## Next Steps

Ready to create your first documentation? Check out the [Quick Start](./quick-start) guide.
