<!-- Short, focused guidance for AI coding agents working in this repository -->
# Copilot / AI agent instructions — leetcode/Two Sum

Purpose
- This repository contains a single LeetCode problem workspace (primary file: `TwoSum.dib`). Use minimal, targeted edits. The goal is to produce a correct, idiomatic solution for the user's requested language without adding unrelated scaffolding.

Big picture (what matters)
- Single-problem repo: don't assume a larger app. The main artifact is `TwoSum.dib` — review it for the user's intent and any constraints before editing.
- Preferred output: a single solution file named after the problem (examples below) and a tiny README note if the user asks for instructions.

Repository-specific conventions
- Keep changes small and reversible. Users often expect short PRs focused on one solution.
- Suggested solution filenames (pick one matching the language):
  - Python: `TwoSum.py`
  - JavaScript/Node: `TwoSum.js`
  - TypeScript: `TwoSum.ts`
  - Java: `TwoSum.java`
  - C++: `TwoSum.cpp`
- Do NOT rename or delete `TwoSum.dib`. Treat it as the canonical problem file.

How to act when implementing
- If the user hasn't specified a language, ask a clarifying question: "Which language should I implement: Python, Java, C++, JS, or TS?"
- Produce a single-file solution unless the user asks for a project scaffold (do not add package.json, pyproject, etc., unless requested).
- Include a brief comment header in the solution file describing input/output expectations and complexity (one- or two-line).

Testing & running
- This repo has no test runner by default. If the user requests runnable tests, create a minimal test harness (few lines) and explain how to run it.
- When adding a test harness, prefer language-native minimal commands (e.g., `python TwoSum.py`, `node TwoSum.js`) and document them in a one-line README update.

PR / commit guidance
- Keep the commit message succinct: e.g., `feat: solve Two Sum in Python` or `fix: improve Two Sum complexity`.
- In PR descriptions, include the chosen language and a short explanation of algorithm and complexity.

Integration & dependencies
- Avoid adding external dependencies for single-problem solutions. If a dependency is necessary, ask the user first and document why.

Examples (explicit patterns from this repo)
- If implementing Python solution: create `TwoSum.py` with a small `if __name__ == '__main__':` block demonstrating usage.
- If user asks to convert or refactor a solution already present in another language, preserve original file and add the new one (do not overwrite) unless asked to replace.

Guardrails
- Do not add unrelated files or complex project setup unless the user requests it.
- Avoid heavy refactors or style-only changes; keep the focus on solving or clarifying the problem.

Questions for the user (if unspecified)
- Which language should I implement in?
- Should I add a runnable test harness and instructions for running locally?

If anything in this file is unclear, ask the user before making large or irreversible changes.
