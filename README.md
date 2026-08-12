## Executive Summary: ACME Banking Application

- What the ACME working build demonstrates
- How to run the demo
- Which account scenarios to use
- How grounding, citations, and fallback behave
- Link to validation matrix
- Link to architecture
- Link to prompt evolution


## Enterprise Visual Preview

The application includes an executive banking interface designed for
institutional coverage workflows and competitive intelligence analysis.

### Main Intelligence Hub

![ACME_Banking Intelligence Hub](docs/screenshots/home-dashboard.png)

![Competitive Intelligence](docs/screenshots/competitive-intelligence.png)

![Executive Briefing](docs/screenshots/executive-briefing.png)

![Peer Benchmarking](docs/screenshots/executive-briefing_peer-benchmarking.png)

![Strategic Insights](docs/screenshots/executive-briefing_strategicinsights.png)

## Prompt Templates:
>> The single source of truth for prompt templates is the `src/prompts/` directory.

>> Legacy prompt files were archived in `docs/templates/legacy-prompts/`.


### Demo Execution Tests:
python -m pytest -q
python -m pytest -v
streamlit run streamlit_app.py