# AI_PROTOCOL.md — How to Work with AI on This Project
## Read this before starting any AI session. No exceptions.

---

## THE SINGLE MOST IMPORTANT RULE

**One task. One prompt. One verification. Then next task.**

Never give the AI two things to do in one message.
Never move to the next task until you have verified the previous one in the browser.

---

## MANDATORY FIRST MESSAGE — PASTE THIS AT THE START OF EVERY SESSION

```
Before you do anything, you MUST:
1. Read CLAUDE.md fully
2. Read STYLE_GUIDE.md fully
3. Read PATTERNS.md fully
4. Read TASKS.md and find the first unchecked task in the current phase
5. Run code-review-graph list_graph_stats_tool — confirm the graph is fresh
6. Run code-review-graph get_impact_radius_tool on the file you plan to change
7. Tell me which task you are about to do and wait for my confirmation before starting

Do not write a single line of code until you have done all 6 steps above.
```

---

## THE EXACT PROMPT TEMPLATE

Copy this for every single task:

```
Task: [Copy the exact task text from TASKS.md]
File to change: [exact filename, e.g. Home.html or exellar-backend/app/routes/projects.py]
Pattern to use: [Pattern name from PATTERNS.md, e.g. "Pattern #6 — Project Card"]
Do NOT:
- Create any new CSS classes
- Add any <style> blocks
- Restructure existing HTML sections
- Change anything outside the specified file
- Do more than this one task

After making the change, show me exactly what you changed (diff format if possible).
Stop and wait for my confirmation before doing anything else.
```

---

## GOOD PROMPT EXAMPLES

✅ **Good:**
```
Task: Create js/home-featured.js that fetches GET /api/projects?is_featured=true
and renders 3 cards into the div#home-projects-grid container.
File: js/home-featured.js (new file)
Pattern: Pattern #16 — Dynamic JS Boilerplate + Pattern #6 — Project Card
Do NOT modify Home.html. Do NOT add new CSS.
```

✅ **Good:**
```
Task: Replace the placeholder text "1964" stat in Home.html About section
with the correct text "Est. 1964"
File: Home.html, line ~690 (search for "Year of Incorporation")
Do NOT change any CSS classes. Do NOT touch any other section.
```

✅ **Good:**
```
Task: Create exellar-backend/app/models/project.py with the Project model.
Fields: id (UUID), title, slug (auto-generated from title, unique), category,
status (enum: ongoing/completed), location, scope, size, client_name,
services, partners, story_headline, story_body, client_testimonial,
thumbnail (filename string), gallery (JSON), is_featured (bool),
created_at, updated_at.
Do NOT create any other files. Just this one model.
```

---

## BAD PROMPT EXAMPLES — NEVER DO THESE

❌ **Bad (too vague):**
```
Make the home page look better
```

❌ **Bad (too many things):**
```
Fix the nav, update the about section, and also build the backend
```

❌ **Bad (no constraints):**
```
Add a projects section to the home page
```

❌ **Bad (invites redesign):**
```
The about section needs to be improved, do whatever you think is best
```

---

## HOW TO HANDLE AI MISTAKES

If the AI breaks something or does something wrong:

1. **Do not ask it to "fix it"** — this makes things worse
2. Say exactly what is wrong: "The image is missing the `b-lazy` class"
3. Or: "The card div is missing `inline_block col-d-33`"
4. Reference the correct pattern: "Use Pattern #6 from PATTERNS.md exactly"
5. If the damage is bad: `git restore FILENAME` to revert and start over

---

## HOW TO VERIFY AFTER EVERY CHANGE

Before marking a task complete in TASKS.md:

```
[ ] Open browser preview (http://localhost:8080/PAGENAME.html)
[ ] Check the specific thing that was changed
[ ] Check nothing else broke (scroll the whole page)
[ ] Check browser console — zero red errors
[ ] Check mobile view (resize to 375px)
[ ] THEN mark the task ✅ in TASKS.md
```

---

## USING CODE-REVIEW-GRAPH EFFECTIVELY

Ask the AI to run these BEFORE making any change:

```
# Check graph is up to date
code-review-graph list_graph_stats_tool

# Find what's in the file you're about to change
code-review-graph query_graph_tool pattern=file_summary target=FILENAME

# Check what would break if you change something
code-review-graph get_impact_radius_tool target=FILENAME

# Find where a function is called
code-review-graph query_graph_tool pattern=callers_of target=FUNCTION_NAME
```

If the graph is stale (not updated today):
```
code-review-graph build_or_update_graph_tool
```

---

## WHICH AI TOOL FOR WHICH TASK

| Task Type | Best Tool | Notes |
|---|---|---|
| HTML content changes | Claude Code | Reads CLAUDE.md automatically |
| CSS class lookup | Claude Code | Use Grep on style.css |
| Backend Python code | Claude Code or Cursor | Must read CLAUDE.md first |
| React admin panel | Claude Code or Cursor | Plain CSS Modules only |
| Dynamic JS files | Claude Code | Follow Pattern #16 |
| Deployment/Server | Claude Code | Follow DEPLOYMENT.md exactly |
| Image editing | External tool | Not an AI code task |

---

## FILE REFERENCE CARD

Keep this open while working:

```
CLAUDE.md          → Rules for AI. Auto-read by Claude Code.
TASKS.md           → Master checklist. One task at a time.
STYLE_GUIDE.md     → Tech stack, CSS classes, patterns reference.
PATTERNS.md        → Copy-paste HTML snippets. Never invent new ones.
DEPLOYMENT.md      → VPS deployment. Read fully before touching server.
AI_PROTOCOL.md     → This file. How to prompt correctly.

Project files:
css/style.css          → READ ONLY. Never modify. 371KB Turner original.
js/app.js              → READ ONLY. Never modify.
js/vendor.js           → READ ONLY. Never modify.
js/projects-dynamic.js → Modifiable. Dynamic project cards.
js/project-detail.js   → Modifiable. Project detail hydration.
js/careers-dynamic.js  → Modifiable. Jobs + apply modal.
Home.html              → Modifiable. Main homepage.
exellar-backend/       → Backend — build from scratch.
exellar-admin/src/     → Admin panel — build from scratch.
```

---

## SESSION CHECKLIST (run through this every time)

```
Before session:
[ ] Opened TASKS.md — know which task I'm doing next
[ ] Prepared the exact prompt using the template above
[ ] NOT planning to do more than one task

During session:
[ ] AI confirmed it read CLAUDE.md, STYLE_GUIDE.md, PATTERNS.md
[ ] AI confirmed code-review-graph is fresh
[ ] AI told me what it's about to do before doing it
[ ] I confirmed the plan before AI wrote any code

After session:
[ ] Verified in browser — no errors
[ ] No new CSS classes were added
[ ] No existing HTML sections were restructured
[ ] Checked browser console — zero red errors
[ ] Marked task ✅ in TASKS.md
[ ] Committed changes to git
```

---

## GIT WORKFLOW

After every verified task:

```bash
cd "C:/Users/Shabbir Shaikh/Downloads/Proj"
git add [specific files changed]
git commit -m "Task: [description of what was done]"
```

Never use `git add .` — always add specific files to avoid accidentally committing `.env`, `*.db`, etc.

---

## EMERGENCY CONTACTS & REFERENCES

- Project: Exellar Construction LLP website
- Server: Hostinger VPS (details in .env — DO NOT commit)
- Domains: exellar.co.in, api.exellar.com, admin.exellar.com
- Admin default: admin@exellar.co.in / Admin@123 (change immediately after deployment)
- Full deployment guide: DEPLOYMENT.md
- Design rules: STYLE_GUIDE.md
