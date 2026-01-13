# Publishing Guide

Instructions for maintaining and publishing PAPER-CODE to PyPI.

## Prerequisites

You need:

- PyPI account (https://pypi.org/account/register/)
- TestPyPI account (https://test.pypi.org/account/register/)
- API tokens for both

### Generate PyPI API Tokens

1. Go to https://pypi.org/manage/account/
2. Click "Add API token"
3. Name it (e.g., "GitHub Actions PyPI")
4. Select "Entire account" scope
5. Copy the token

Do the same for TestPyPI at https://test.pypi.org/manage/account/

### Add Secrets to GitHub

1. Go to repository Settings → Secrets and variables → Actions
2. Add `PYPI_API_TOKEN` with your PyPI token
3. Add `TEST_PYPI_API_TOKEN` with your TestPyPI token

## Publishing Process

### 1. Prepare Release

Update version and changelog:

```bash
# Update version in pyproject.toml
# e.g., 0.5.0 → 0.6.0

# Update CHANGELOG.md
nano CHANGELOG.md
```

### 2. Test Build Locally

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Check for issues
twine check dist/*

# Upload to TestPyPI
twine upload -r testpypi dist/*
```

Test installation:

```bash
pip install -i https://test.pypi.org/simple/ paper-code
```

### 3. Create GitHub Release

```bash
git add -A
git commit -m "bump: version 0.5.0 → 0.6.0"
git tag v0.6.0
git push origin main --tags
```

Or create release on GitHub UI:

1. Go to https://github.com/minhgiau998/paper-code/releases
2. Click "Draft a new release"
3. Select tag: `v0.6.0`
4. Add release notes
5. Click "Publish release"

This automatically triggers the PyPI publishing workflow.

### 4. Verify Published Package

```bash
# Wait 1-2 minutes for PyPI to update
pip install --upgrade paper-code

# Verify version
paper-code --version
```

## Automated Publishing (Recommended)

The GitHub Actions workflow handles publishing automatically:

1. **On Release:** When you create a GitHub release with tag `vX.Y.Z`, it automatically publishes to PyPI
2. **Manual Trigger:** Use `workflow_dispatch` to publish to TestPyPI or PyPI manually

### Manual Trigger Steps

1. Go to https://github.com/minhgiau998/paper-code/actions
2. Click "Publish to PyPI" workflow
3. Click "Run workflow"
4. Select environment (testpypi or pypi)
5. Click "Run workflow"

## Version Management

### Semantic Versioning

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR:** Breaking changes
- **MINOR:** New features (backward compatible)
- **PATCH:** Bug fixes

### Pre-release Versions

For beta/alpha releases:

```
1.0.0a1  # Alpha 1
1.0.0b1  # Beta 1
1.0.0rc1 # Release Candidate 1
```

Example release tag: `v0.5.0-alpha.1`

## Package Contents

Ensure these files are included:

- `src/` - Source code
- `README.md` - Project description
- `LICENSE` - MIT license
- `CHANGELOG.md` - Version history
- `pyproject.toml` - Package metadata
- `requirements.txt` - Dependencies

Excluded (in setup.cfg or .gitignore):

- `.git/`
- `.github/`
- `tests/`
- `.env`
- `*.pyc`
- `__pycache__/`

## Troubleshooting

### Build Fails

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Rebuild
python -m build
```

### Upload Fails

```bash
# Verify token is valid
twine upload --repository-url https://test.pypi.org/legacy/ -u __token__ -p $TOKEN dist/*

# Check for typos in version
grep version pyproject.toml
```

### Package Not Found After Upload

- Wait 5 minutes for PyPI to index
- Check on https://pypi.org/project/paper-code/
- Verify tag format: `v0.5.0` (with 'v' prefix)

## Maintenance

### Check PyPI Stats

- **PyPI:** https://pypi.org/project/paper-code/
- **Stats:** https://pypistats.org/packages/paper-code

### Monitor Issues

- GitHub Issues: https://github.com/minhgiau998/paper-code/issues
- PyPI Discussion: Check package page comments

### Security Updates

For security fixes, publish immediately:

```bash
# Tag as patch release
git tag v0.5.1
git push origin --tags
```

## Release Checklist

Before publishing:

- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md`
- [ ] Update `README.md` if needed
- [ ] Run tests: `pytest`
- [ ] Run linting: `black . && isort .`
- [ ] Build locally: `python -m build`
- [ ] Check build: `twine check dist/*`
- [ ] Test on TestPyPI
- [ ] Create git tag
- [ ] Push to GitHub
- [ ] Create GitHub release
- [ ] Verify on PyPI after 5 minutes

## Resources

- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Setuptools Documentation](https://setuptools.pypa.io/)
- [Python Versioning](https://peps.python.org/pep-0440/)
- [PyPI Security](https://pypi.org/help/#apitoken)

---

For more information, see [ROADMAP.md](../ROADMAP.md#phase-5-package-registry-publishing).
