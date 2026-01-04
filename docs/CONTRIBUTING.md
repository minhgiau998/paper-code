# Contributing to PAPER-CODE

We love pull requests! Here is how you can add support for new Tech Stacks or Libraries.

## 🚀 Adding a New Tech Stack

Example: Adding **"SvelteKit"**.

1.  **Update Config:**
    Open `src/config.py` and add "SvelteKit" to `TECH_STACKS["Frontend"]`.

2.  **Create Templates:**
    Go to `src/templates/stacks/frontend/` and create two files:
    - `sveltekit_arch.md.j2` (Architecture)
    - `sveltekit_standards.md.j2` (Coding Standards)
    
    *Note: The filename must be the sanitized version of the stack name (lowercase, underscores).*

3.  **Verify:**
    Run the tool locally to verify the generation:
    ```bash
    python src/main.py --template SvelteKit --output ./test-output
    ```

## 📚 Adding a New Library

Example: Adding **"Prisma"**.

1.  **Update Config:**
    Open `src/config.py` and add "Prisma" to the relevant `LIBRARIES` list (e.g., under Node.js, Next.js).

2.  **Create Template:**
    Create `src/templates/libs/prisma.md.j2`.
    
3.  **Use Conditional Logic:**
    Inside the template, you can handle framework differences:
    ```jinja
    {% if "NestJS" in tech_stack %}
      // NestJS specific setup...
    {% else %}
      // Standard setup...
    {% endif %}
    ```