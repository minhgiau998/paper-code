# NPM Publishing Guide

Instructions for publishing PAPER-CODE templates package to npm registry.

## Overview

The `@paper-code/templates` package provides reusable Jinja2 documentation templates that can be:

- Used with PAPER-CODE CLI
- Installed and customized in any project
- Extended with organization-specific templates

## Prerequisites

You need:

- npm account (https://www.npmjs.com/signup)
- npm CLI installed locally
- Access to publish under `@paper-code` organization (or create your own scope)

### Generate NPM Token

1. Go to https://www.npmjs.com/settings/tokens
2. Click "Generate New Token"
3. Select "Classic Token" or "Granular Access Token"
4. For automation: Use "Automation" type
5. Copy the token

### Granular Access Token (Recommended)

For enhanced security:

1. Select "Granular Access Token"
2. Permissions:
   - "Publish packages"
   - "Read and write organization packages"
3. Expiration: 1 year (or custom)

### Add NPM Token to GitHub Secrets

1. Go to repository Settings → Secrets and variables → Actions
2. Add `NPM_TOKEN` with your npm token value
3. Verify it's available in Actions

## Publishing Process

### 1. Update Version & Changelog

```bash
cd docs-templates

# Update version in package.json
# Follow semantic versioning: 0.5.0 → 0.5.1, 0.6.0, 1.0.0, etc.

# Option 1: Manual update
nano package.json
# Change "version": "0.5.0" to "0.5.1"

# Option 2: npm version (recommended)
npm version patch      # 0.5.0 → 0.5.1 (patch)
npm version minor      # 0.5.0 → 0.6.0 (minor feature)
npm version major      # 0.5.0 → 1.0.0 (breaking change)
```

This automatically creates a git tag!

### 2. Test Package Locally

```bash
# Validate package.json
npm pack --dry-run

# Check what will be published
npm pack

# Inspect the tarball
tar -tzf paper-code-templates-0.5.1.tgz | head -20
```

### 3. Publish to NPM

#### Option A: Automated (Recommended)

Create a GitHub release:

```bash
git push origin main
# Go to https://github.com/minhgiau998/paper-code/releases
# Click "Draft a new release"
# Select tag: v0.5.1 (created by npm version)
# Add release notes
# Click "Publish release"
```

The GitHub Actions workflow automatically publishes to npm!

#### Option B: Manual from CLI

```bash
cd docs-templates

# Login to npm
npm login

# Publish package
npm publish

# Verify
npm view @paper-code/templates
```

#### Option C: Manual Dry Run

Test before publishing:

```bash
npm publish --dry-run
```

Shows what would be published without actually publishing.

### 4. Verify Published Package

```bash
# Wait 2-3 minutes for npm to index

# Check package
npm view @paper-code/templates

# Install fresh
npm install @paper-code/templates

# Test in Node
node -e "const pkg = require('@paper-code/templates'); console.log(pkg.getTemplatesInfo())"
```

## Version Management

### Semantic Versioning

Follow [semver](https://semver.org/):

```
MAJOR.MINOR.PATCH
0.5.1

0 = MAJOR (breaking changes)
5 = MINOR (new features)
1 = PATCH (bug fixes)
```

### Release Types

| Bump  | Command             | Example       | When                   |
| ----- | ------------------- | ------------- | ---------------------- |
| Patch | `npm version patch` | 0.5.0 → 0.5.1 | Bug fixes only         |
| Minor | `npm version minor` | 0.5.0 → 0.6.0 | New templates/features |
| Major | `npm version major` | 0.5.0 → 1.0.0 | Breaking changes       |

### Pre-release Versions

For beta/alpha releases:

```bash
npm version prerelease --preid=alpha
npm version prerelease --preid=beta
npm version prerelease --preid=rc

# Examples:
# 0.5.0-alpha.0
# 0.5.0-beta.1
# 0.5.0-rc.1
```

Then publish:

```bash
npm publish --tag alpha
npm publish --tag beta
```

## Package Structure

Ensure these files/folders are included:

```
docs-templates/
├── core/              ✅ Core templates
├── ai/                ✅ AI templates
├── stacks/            ✅ Framework templates
├── libs/              ✅ Library templates
├── github/            ✅ GitHub templates
├── package.json       ✅ Package metadata
├── index.js           ✅ Node.js entry point
├── README.md          ✅ Documentation
├── LICENSE            ✅ MIT license
└── .npmignore         ✅ Exclude from npm
```

Excluded files (in `.npmignore`):

```
node_modules/
.github/
.env
.DS_Store
test/
coverage/
```

## GitHub Actions Workflow

### Automatic Publishing (Recommended)

Triggered by GitHub release:

```yaml
on:
  release:
    types: [published]
```

When you create a release with tag `v0.5.1`, it automatically:

1. ✅ Publishes to npm
2. ✅ Verifies package installation
3. ✅ Posts summary

### Manual Trigger

Go to **Actions** → **Publish NPM Package**:

1. Click "Run workflow"
2. Select environment:
   - **npm-dry-run**: Test without publishing
   - **npm**: Publish to npm
3. Click "Run workflow"

## Troubleshooting

### "401 Unauthorized"

```bash
# Check npm token
npm token list

# Verify token in GitHub secrets
# Settings → Secrets and variables → Actions

# Re-authenticate
npm logout
npm login
npm publish
```

### "Package already published"

Same version can't be published twice. Update version:

```bash
npm version patch
npm publish
```

### "No access to organization"

Need org permissions:

```bash
# Check current user
npm whoami

# Request access to @paper-code org
# Contact: minhgiau04041998@gmail.com
```

### "Package not found after publish"

npm caches for 5-10 minutes:

```bash
# Wait and retry
npm cache clean --force
npm view @paper-code/templates
```

### Files missing from tarball

Check `.npmignore`:

```bash
# Verify included files
npm pack --dry-run

# Too much excluded?
# Review .npmignore file
cat .npmignore
```

## Testing Published Package

### Full Integration Test

```bash
# Create test directory
mkdir test-paper-code-templates
cd test-paper-code-templates

# Install from npm
npm init -y
npm install @paper-code/templates

# Test with PAPER-CODE CLI
npm install -g paper-code
paper-code init --template-dir ./node_modules/@paper-code/templates

# Verify templates loaded
ls node_modules/@paper-code/templates/
```

## Best Practices

1. **Tag Releases:** Always tag releases in git

   ```bash
   git tag v0.5.1
   git push origin --tags
   ```

2. **Update Changelog:** Document changes

   ```bash
   # docs-templates/CHANGELOG.md
   ## 0.5.1 (2024-01-13)
   - Fix template rendering issue
   - Add new library templates
   ```

3. **Test Before Publishing:** Use `--dry-run`

   ```bash
   npm publish --dry-run
   ```

4. **Use Semantic Versioning:** Follow semver strictly

5. **Keep Files Minimal:** Use `.npmignore` to reduce package size

6. **Add Keywords:** Helps discoverability
   ```json
   "keywords": ["documentation", "templates", "paper-code"]
   ```

## Release Checklist

Before publishing:

- [ ] Update version in `package.json`
- [ ] Update `CHANGELOG.md`
- [ ] Update `README.md` if needed
- [ ] Run validation: `npm pack --dry-run`
- [ ] Create/update git tag
- [ ] Push to GitHub
- [ ] Create GitHub release (auto-triggers CI)
- [ ] Wait 5 minutes and verify on npm

## Monitoring

### Check Package Stats

- **NPM Package:** https://www.npmjs.com/package/@paper-code/templates
- **Download Stats:** https://npm-stat.com/@paper-code/templates
- **Trending:** https://www.npmtrends.com/@paper-code/templates

### Monitor Issues

- GitHub Issues: https://github.com/minhgiau998/paper-code/issues
- npm Discussions: Check package page

## Security

### Token Best Practices

1. **Never commit tokens** to git
2. **Use GitHub Secrets** for CI/CD
3. **Rotate tokens** annually
4. **Use scoped tokens** with limited permissions
5. **Monitor token usage** in npm dashboard

### Package Integrity

npm automatically verifies:

- Package signatures
- Security audits
- Dependency checks

Run locally:

```bash
npm audit
npm audit fix
```

## Resources

- [npm Publishing Guide](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry)
- [npm Semantic Versioning](https://docs.npmjs.com/about-semantic-versioning)
- [npm Security](https://docs.npmjs.com/about-security)
- [Scoped Packages](https://docs.npmjs.com/about-scoped-packages)

## Next Steps

1. **Set up npm token** in GitHub Secrets
2. **Test the workflow** with dry-run
3. **Publish first release** to npm
4. **Monitor package usage** on npm stats
5. **Keep templates updated** with new features

---

For PyPI publishing, see [PUBLISHING.md](./PUBLISHING.md).

For overall roadmap, see [ROADMAP.md](./ROADMAP.md).
