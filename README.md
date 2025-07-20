# M811 Google Earth Engine AI Agent - Knowledge-Base

**Course:** M811 – Space Image Processing  
**Programme:** MSc *Space Technologies, Applications and seRvices* (STAR)  
**Author:** **Chris Sekas**  

---

> **TL;DR**  
> Google Earth Engine (GEE) hosts 730+ datasets, but its search is name-based and unintuitive.  
> This project builds an **AI agent** using [Gendox](https://github.com/ctrl-space-labs/gendox-core) that enables **natural-language search** over GEE datasets.
>
> 🧠 Ask plain questions like *“vegetation monitoring in Crete, June 2020”* → get relevant datasets and spectral bands.
>
> 🔧 Includes scripts to:
> - Scrape and convert GEE catalogue pages to Markdown
> - Analyze token counts for LLM embedding limits
> - Build a semantic search agent using RAG + pgvector + OpenAI embeddings
>
> Perfect for researchers and students who don’t want to dig through obscure dataset names.

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

1. **Create a new project** and upload the entire `resources/markdown/` folder as the project Knowledge Base**.  
2. In the project Settings *Click “Start Training”* – Gendox will use:

   | Component | Purpose |
    |-----------|---------|
   | **PostgreSQL 16 + pgvector** | Stores dense embeddings and powers fast nearest‑neighbour search. |
   | **OpenAI Embeddings v3 small** | Transforms every dataset chunk into a 1 × 1536‑dimensional vector. |
   | **Chunking** | Each Markdown file becomes **one section** (≤ 8 000 tokens) that contains the dataset description, band list, terms of use, and GEE code sample. |


3. Setup the **Agent**.  
   Use this *System Prompt*:

   > You are a remote‑sensing expert. Ask clarifying questions when a user query is vague, then recommend suitable Google Earth Engine datasets and spectral bands.

4. **Publish the Agent** and chat with it.

---

### Under the hood: hybrid semantic search

| Phase | What happens |
|-------|--------------|
| **1. HyDE query synthesis** | When a user asks a question, the LLM first **hallucinates** an ideal answer *without external context* (Hypothetical Document Embeddings, aka HyDE). It then distills that answer into a tightly‑focused search query (e.g. “10 m NIR imagery winter 2019–2020 Greece”). |
| **2. Embedding + k‑NN** | The search query is embedded with the same OpenAI v3 model. Gendox performs a k‑nearest‑neighbour lookup (Euclidean/L2 distance) in the pgvector index of all dataset sections. |
| **3. Retrieval** | The top‑*N* matching dataset chunks (title + band list + description) are returned. |
| **4. RAG completion** | Chat history + user question + Agent prompt + the retrieved chunks are fed back into the LLM, which generates a grounded answer that cites only the supplied context. |

This pipeline lets users ask very broad or incomplete questions (e.g.  
“Need images to monitor vineyard stress in Crete last June”) and still receive precise dataset + band recommendations.

---

## 4. Results

A list of questions created and compared across the Gendox AI Agent and models like ChatGPT.
The questions results show that while ChatGPT can answer some questions with very good quality, since it does not have access to the GEE dataset, it prefers to propose widely used satellites and datasets. 
It misses composite products that have been created from multiple datasets, such as the `NASA/LANCE/SNPP_VIIRS/C2` or `JAXA/GCOM-C/L3/LAND/LAI/V3`.

### Agent Configuration
In the configuration of the agent we used:
1. Embedding Models (For both semantic index creation and semantic search) -> `text-embedding-3-small`
2. Advanced Search Model (HyDE) -> `gemini-2.0-flash`
3. Retrieval -> `kNN` with `k=7`
4. RAG Model -> `gemini-2.5-flash` with medium `thinking` effort


### Examples 
Here are example questions and answers from the Gendox AI Agent:
1. NDVI
![Q1 - ndvi.png](resources/images/readme/Q1%20-%20ndvi.png)


2. NDVI - Sentinel 2
![Q2 - ndvi - sentinel-2.png](resources/images/readme/Q2%20-%20ndvi%20-%20sentinel-2.png)


3. DEM
![Q3 - DEM.png](resources/images/readme/Q3%20-%20DEM.png)


4. Soil Moisture
![Q4 - soil moisture.png](resources/images/readme/Q4%20-%20soil%20moisture.png)


5. Flowering season
![Q5 - flowering season.png](resources/images/readme/Q5%20-%20flowering%20season.png)



---

## 5. Access & Citation

To request access to the Gendox AI Agent, email: [contact@ctrlspace.dev](mailto:contact@ctrlspace.dev)

If you use this project in your research or teaching, please cite it as:

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


