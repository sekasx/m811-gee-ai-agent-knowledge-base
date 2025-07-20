# M811 Google Earth Engine AI Agent - Knowledge-Base

**Course:** M811 – Space Image Processing  
**Programme:** MSc *Space Technologies, Applications and seRvices* (STAR)  
**Author:** **Chris Sekas**  

---

## TL;DR

A repo that **scrapes every dataset page from Google Earth Engine, converts them to Markdown, and packages them so an AI agent (built with [Gendox](https://gendox.dev/)) can answer natural‑language questions like “Which sensors give 10m NIR coverage over Greece in winter 2019‑2020?”—plus a handful of tiny helper scripts for quickly exploring dataset availability and token sizes.

---

## The Problem

Google Earth Engine (GEE) hosts **~730 remote‑sensing datasets**. Discovering the right one is painful:

- GEE’s search only works if you already know a dataset’s name.
- Students therefore reuse the same handful of satellites.
- Valuable, lesser‑known collections stay invisible.

---

## Goal

Make GEE’s catalogue **searchable in plain English** so students and specialists can immediately see which datasets (and bands) fit their scientific questions.

---

## Objectives

1. **AI Agent** – Build a knowledge base from every dataset page and deploy it on **Gendox**. The agent:
    - Accepts natural‑language queries.
    - Asks clarifying follow‑ups.
    - Recommends datasets and spectral bands.

2. **Getting‑started scripts** – A mini toolbox that lets researchers:
    - Scrape and convert GEE catalogue pages to Markdown.
    - Inspect token counts to stay within LLM context limits.
    - List or prune dataset files by size.

---

## Repository Layout

```
resources/
 ├─ GEE-all-datasets.<date>.html     # raw catalogue page
 ├─ datasets.json                    # list of dataset URLs
 └─ markdown/                        # *.md files (one per dataset)

src/dataset-extraction/
 ├─ html-href-extraction.py          # pulls dataset links from catalogue HTML
 ├─ url-to-md.py                     # calls Gendox /web-scrape → Markdown
 └─ md-token-stats.py                # token analytics + outlier stats

environment.yml                      # Conda spec
README.md
```

---

## 1. Set‑Up

### Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda (Python 3.12)
- Docker Desktop if you want to run Gendox locally
- macOS / Linux shell (or Windows WSL)

### Create the Conda Environment

```bash
conda env create -f environment.yml
conda activate M811-GEE-AI-Agent-Knowledge-Base
```

### (Optional) Run Gendox Locally

```bash
git clone https://github.com/ctrl-space-labs/gendox-core
cd gendox-core/gendox-compose-scripts/dev-ci-installation
docker-compose up -d
```

Gendox will be available at: http://localhost:8000

---

## 2. Data Preparation Workflow

### Step 1 – Extract Dataset URLs

Save the [GEE catalogue page](https://developers.google.com/earth-engine/datasets/catalog) as `resources/GEE-all-datasets.<date>.html` (e.g., `GEE-all-datasets.2025-07-19.html`).
```bash
python src/dataset-extraction/html-href-extraction.py \
  resources/GEE-all-datasets.2025-07-19.html \
  --selector "td.ee-dataset > a" \
  --base-url "https://developers.google.com/" \
  --output resources/datasets.json \
  --unique --pretty
```

Result: `resources/datasets.json` – a deduplicated list of dataset page URLs.

---

### Step 2 – Fetch and Convert Pages to Markdown

```bash
python src/dataset-extraction/url-to-md.py \
  resources/datasets.json \
  resources/markdown \
  --gendox-url http://localhost:8000 \
  --elements main \
  --delay 0.3
```

Each dataset page is saved as a Markdown file in `resources/markdown`.

---

### Step 3 – Inspect Token Stats

```bash
python src/dataset-extraction/md-token-stats.py \
  resources/markdown \
  --model text-embedding-3-small \
  --csv resources/markdown/token_stats.csv
```

Example output:

```
Scanned 730 Markdown file(s)
  Total tokens : 3,550,111
  Average      : 7,289.76
  Median       : 2,303.00
  Std dev      : 53,439.75
  Max file     : …/LANDFIRE_Vegetation_ESP_v1_2_0_HI.md (742,604)
  Min file     : …/AHN_AHN2_05M_RUW.md                  (907)

Stats for bottom 99% of files (723 files):
  Average      : 2,561.12
  ...
```

This is usefule to ensure that the dataset pages fit within the context limits of your LLM/Embedding models (e.g., text-embedding-3-small has a 8K token limit).
---

## 3. Building the Agent (in Gendox)

1. **Create a new Knowledge Base** and upload `resources/markdown/`
2. **Enable semantic indexing**
3. **Create a new Agent**, link it to the KB, and use this prompt:

   > You are a remote-sensing expert. Ask clarifying questions when a user query is vague, then recommend suitable Google Earth Engine datasets and spectral bands.

4. **Publish the Agent** and share the URL with students and researchers.

---

## 4. Getting‑Started Examples

| Script                          | Purpose                                      |
|---------------------------------|----------------------------------------------|
| `html-href-extraction.py`       | Extract dataset links from GEE catalogue     |
| `url-to-md.py`                  | Convert dataset pages to Markdown (via API)  |
| `md-token-stats.py`             | Analyze token usage per dataset              |

---

## 5. How to Cite

> **Chris Sekas** (2025). *M811‑GEE‑AI‑Agent‑Knowledge‑Base: Preparing Google Earth Engine datasets for natural-language search.* GitHub repository, MIT License. https://github.com/your-org/M811-GEE-AI-Agent-Knowledge-Base

---

## Licence Notice

- **Source code, build scripts, and documentation in `/src`, `/tests`, `environment.yml`, and this `README.md`**  
  © 2025 Chris Sekas — released under the **MIT Licence** *(see `LICENSE`)*.

- **Content inside `resources/markdown/`**  
  These Markdown files are scraped verbatim from the Google Earth Engine Data Catalog.  
  Except where otherwise noted, that original text is licensed by Google under the  
  **Creative Commons Attribution 4.0 International (CC BY 4.0)** licence  
  (<https://creativecommons.org/licenses/by/4.0/>).  
  When redistributing those files you **must** retain the CC BY 4.0 notice and attribute Google by linking back to each dataset’s source page.


