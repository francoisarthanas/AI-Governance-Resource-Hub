# Essential research and evidence

[← Resource hub](../README.md) · [Start here](START-HERE.md)

Read the research that helps explain what governance needs to measure and prove. Distinguish empirical findings from proposals, benchmarks, and the authors' interpretations.

**5 selected resources · Catalog reviewed 2026-09-12.**

<!-- Generated from catalog/resources.json. Edit the catalog, then run python scripts/generate_catalog.py. -->

- [MIT AI Risk Repository](#mit-risk-repository)
- [AI Incident Database](#ai-incident-database)
- [Closing the AI Accountability Gap](#internal-algorithmic-auditing)
- [Model Cards for Model Reporting](#model-cards)
- [Datasheets for Datasets](#datasheets-for-datasets)

<a id="mit-risk-repository"></a>

### [MIT AI Risk Repository](<https://airisk.mit.edu/risks>)

**Publisher:** MIT AI Risk Initiative / MIT FutureTech and collaborators  
**Format:** Living database, taxonomies and research · **Access:** Free; data licensed CC BY 4.0  
**For:** Risk assessors, researchers, evaluators and educators

**Why it earns a place:** Provides a searchable inventory of AI risks tied to source literature, with causal and domain classifications that expose gaps in narrow risk registers.

**Use it to:** Filter risks relevant to your use case, inspect the source evidence, and convert applicable risks into contextual risk statements.

**Version / status:** Living resource; research first published 2024  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official repository page inspected on 2026-09-12. Page lists a seven-domain taxonomy and current multi-agent risk subdomain. Counts vary within page sections, so omit headline counts. It explicitly does not supply risk likelihood or severity scores.

</details>

<a id="ai-incident-database"></a>

### [AI Incident Database](<https://incidentdatabase.ai/>)

**Publisher:** Responsible AI Collaborative  
**Format:** Searchable incident reports and taxonomies · **Access:** Free to browse  
**For:** Governance, risk, assurance and incident-response teams; educators

**Why it earns a place:** Makes governance concrete through reported real-world failures, with linked reports that can inform risk workshops and incident exercises.

**Use it to:** Select a relevant case, review its underlying reporting, and identify the failed decision, control, ownership and evidence assumptions.

**Version / status:** Living database  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Official homepage and about page inspected on 2026-09-12; publisher and search applications verified. Entries are reported incidents, not uniformly adjudicated findings or a representative dataset of all AI deployments.

</details>

<a id="internal-algorithmic-auditing"></a>

### [Closing the AI Accountability Gap](<https://arxiv.org/abs/2001.00973>)

**Publisher:** Inioluwa Deborah Raji et al. / ACM FAT* 2020  
**Format:** Research paper and linked audit templates · **Access:** Free author manuscript  
**For:** Governance leads, internal auditors and assurance reviewers

**Why it earns a place:** Connects lifecycle decisions to a documented internal audit process, including the evidence an audit must leave behind.

**Use it to:** Use the SMACTR stages to plan one internal AI audit; identify the documents needed at each stage before testing begins.

**Version / status:** 2020 conference paper; foundational method, not a current legal standard.  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Author manuscript record, abstract, conference acceptance and linked template reference reviewed. Linked templates were not separately inspected.

</details>

<a id="model-cards"></a>

### [Model Cards for Model Reporting](<https://arxiv.org/abs/1810.03993>)

**Publisher:** Margaret Mitchell et al. / ACM FAT* 2019  
**Format:** Research paper · **Access:** Free author manuscript  
**For:** Model reviewers, procurement teams and technical owners

**Why it earns a place:** Establishes a practical model documentation format covering intended use, evaluation conditions and performance across relevant groups.

**Use it to:** Ask a supplier for intended uses, exclusions, evaluation methods and disaggregated results; record which facts still need independent evidence. Use the current [Hugging Face model-card guide](https://huggingface.co/docs/hub/model-cards) for implementation.

**Version / status:** 2019 conference paper; arXiv v2, 14 January 2019.  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Author manuscript, version, conference record and documentation scope reviewed, along with the current Hugging Face implementation guide. A model card does not document the entire deployed agent.

</details>

<a id="datasheets-for-datasets"></a>

### [Datasheets for Datasets](<https://arxiv.org/abs/1803.09010>)

**Publisher:** Timnit Gebru et al. / Communications of the ACM  
**Format:** Research paper and documentation questions · **Access:** Free author manuscript  
**For:** Data owners, privacy teams and governance reviewers

**Why it earns a place:** Makes data provenance, collection choices, intended uses and limitations visible before a dataset is reused.

**Use it to:** Apply its questions to one training or evaluation dataset, then adapt them to a retrieval corpus and identify missing provenance. See the practical [dataset-card guide](https://huggingface.co/docs/hub/datasets-cards).

**Version / status:** 2021 published paper; arXiv v8, 1 December 2021.  
**Reviewed:** 2026-09-12

<details>
<summary>Source review notes</summary>

Author manuscript record, publication note and dataset documentation scope reviewed. Applying it to retrieval corpora is this hub's suggested adaptation.

</details>
