# Contributing to African Native Oral LLM

Thank you for your interest in contributing to this project! We welcome contributions from researchers, developers, linguists, and community members.

## Ways to Contribute

### 1. Data Contributions

#### Oral Tradition Recordings
- Record elders and knowledge keepers (with consent)
- Submit existing recordings (with proper permissions)
- Help with transcription and translation

#### Language Resources
- Share dictionaries and word lists
- Contribute grammar documentation
- Provide example sentences and texts

**Process:**
1. Review [ethical guidelines](docs/ethical_guidelines.md)
2. Complete consent process (Notebook 01)
3. Submit via data collection interface
4. Community review and approval

### 2. Code Contributions

#### Development Setup

```bash
# Clone repository
git clone https://github.com/muchiriTimdev/ngumzo.ai.git
cd African-Native-Oral-LLM

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

#### Contribution Areas

| Area | Skills Needed | Priority |
|------|--------------|----------|
| Audio processing | Python, DSP, librosa | High |
| Tokenizer training | NLP, linguistics | High |
| Model training | PyTorch, transformers | High |
| Web interface | React, TypeScript | Medium |
| Documentation | Writing, research | Medium |
| Community outreach | Communication, cultural knowledge | High |

#### Coding Standards

- Follow PEP 8 for Python code
- Add docstrings to all functions
- Include type hints
- Write tests for new features
- Update documentation

### 3. Language-Specific Contributions

#### Adding a New Language

1. **Create language directory**:
   ```
   docs/language_specific/swahili/
   ├── phonology.md
   ├── grammar.md
   ├── orthography.md
   └── resources.md
   ```

2. **Document features**:
   - Phonemic inventory
   - Tone system (if applicable)
   - Writing system
   - Special characters/Unicode range

3. **Add tokenizer config**:
   - Special tokens
   - Normalization rules
   - Pre-tokenization patterns

4. **Submit PR** with:
   - Language documentation
   - Example text samples
   - Test cases

### 4. Documentation

#### Areas Needing Documentation
- [ ] Language-specific guides
- [ ] API documentation
- [ ] Tutorial videos
- [ ] Best practices guides
- [ ] Ethical case studies

## Pull Request Process

1. **Fork** the repository
2. **Create branch**: `git checkout -b feature/your-feature`
3. **Make changes** with clear commits
4. **Add tests** for new functionality
5. **Update documentation**
6. **Submit PR** with description:
   - What problem it solves
   - How you tested it
   - Any breaking changes

### PR Review Criteria

- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Ethical review (for data)
- [ ] Community approval (for language content)

## Ethical Requirements

All contributions must comply with our ethical framework:

### For Data
- Explicit informed consent documented
- Community ownership acknowledged
- Benefit sharing agreement in place
- Cultural sensitivity reviewed

### For Code
- No bias amplification
- Privacy-preserving design
- Transparent algorithmic decisions
- Community-controlled features

## Community Guidelines

### Code of Conduct
- Respect all contributors
- Welcome newcomers
- Assume good intent
- Focus on constructive feedback
- Prioritize community needs

### Communication Channels
- GitHub Issues: Bug reports, feature requests
- GitHub Discussions: General questions
- Email: ethics@african-native-oral-llm.org (ethical concerns)
- Community meetings: Monthly (announced in Discussions)

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Acknowledged in release notes
- Cited in academic publications (with permission)
- Invited to community events

## Questions?

- Technical: Open a GitHub Discussion
- Ethical: See [ethical guidelines](docs/ethical_guidelines.md)
- General: Email project@african-native-oral-llm.org

---

Thank you for helping build AI that serves African communities!
