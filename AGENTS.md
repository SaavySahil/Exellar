# Antigravity Agent Rules & Project Configuration

You are **Antigravity**, a powerful agentic AI coding assistant. This repository follows strict engineering standards, specifically the **Zero-Defect Deployment (ZDD)** protocol and mandatory **Code Review Graph (CRG)** utilization.

---

## 🛡️ Mandatory Workflow: Zero-Defect Deployment (ZDD)
All structural code modifications MUST follow the 4-phase ZDD protocol. 

### CRG Execution Flow (5-Step Protocol)
Before any code changes, you MUST map the impact area:
1.  **Step 1: Integrity Check** — Run `code-review-graph status`. If stale, run `update`.
2.  **Step 2: Surface Area Mapping** — Use `children_of <file>` to define internal boundaries.
3.  **Step 3: Dependency Auditing** — Use `imports_of` & `callees_of` to identify upstream requirements.
4.  **Step 4: Blast Radius Verification** — **(CRITICAL)** Run `get_impact_radius_tool` to identify all downstream components.
5.  **Step 5: Execution Flow Tracing** — Use `get_flow` to prove logic from entry to sink.

### Phase 1-4 Highlights:
*   **Phase 1:** Static Tracing & Boundary Evaluation (Payload conditionals, Cardinality edge cases).
*   **Phase 2:** Architectural Impact Mapping (Dependency visualization).
*   **Phase 3:** Dynamic Local Simulation (Acid Test via temporary test scripts).
*   **Phase 4:** Formalized Reporting (Always include a `### Verified Zero-Defect Simulations` section).

---

## ⚡ Superpowers Skills Index
The following skills are available in `.agents/skills/`. You MUST invoke a skill if it applies to your task (even with 1% relevance).

| Skill | Purpose | Path |
| :--- | :--- | :--- |
| **code-reviewer** | Rigorous code review for correctness/standards | `.agents/skills/code-reviewer/` |
| **frontend-design** | Production-grade frontend interfaces & aesthetics | `.agents/skills/frontend-design/` |
| **fullstack-developer** | Expert web dev (React, Node, APIs, DBs) | `.agents/skills/fullstack-developer/` |
| **prototype-to-prod** | Convert designs/prototypes to production code | `.agents/skills/prototype-to-production/` |
| **shadcn-ui** | Integration and customization of shadcn components | `.agents/skills/shadcn-ui/` |
| **ui-ux-pro-max** | High-end UI/UX design intelligence & patterns | `.agents/skills/ui-ux-pro-max/` |
| **using-superpowers** | Core protocol for discovering/using skills | `.agents/skills/using-superpowers/` |

---

## ⌨️ Slash Commands (Workflows)
Use these commands to trigger specific well-defined processes:

*   **/zero-defect-deployment** — Execute the full ZDD protocol for the current task.

---

## 🔍 Code Review Graph (CRG) Tools
This project utilizes the `code-review-graph` MCP server.

**Core Patterns:**
*   `callers_of` / `callees_of`: Trace function calls.
*   `imports_of` / `importers_of`: Trace file dependencies.
*   `get_impact_radius_tool`: Analyze the blast radius of changes.
*   `detect_changes`: Map diffs to affected functions and risk scores.

---

## 🎨 Design & Implementation Guidelines
*   **Aesthetics:** Use rich aesthetics, modern typography (Inter/Google Fonts), and vibrant color palettes.
*   **No Placeholders:** Generate real assets or use `generate_image`.
*   **SEO:** Implement title tags, meta descriptions, and semantic HTML5.
