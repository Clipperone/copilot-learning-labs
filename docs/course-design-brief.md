Act as a senior instructor and curriculum architect specialized in GitHub Copilot Pro+ and Visual Studio Code, with the perspective of a solution architect, engineering manager, developer productivity coach, and open-source course designer.

Your mission is to design for me a complete, practical, progressive, and publication-ready learning program to master GitHub Copilot Pro+ inside Visual Studio Code, from beginner to advanced/professional level.

The final result must be structured as a professional public GitHub repository for an open course, including documentation, learning modules, exercises, labs, templates, and reusable assets so that anyone can clone it and follow the training independently.

## Course and repository goals
The course must help learners:
- use GitHub Copilot Pro+ seriously and productively inside VS Code
- configure it properly
- optimize token / premium request consumption
- keep projects efficient, maintainable, scalable, and AI-friendly
- move from basic prompting to advanced workflows
- understand built-in modes, custom instructions, agents, handoffs, and advanced features
- learn through real labs, not only theory
- use the repository as an open learning resource and a repeatable training framework

The course repository must be designed to look professional and credible when published publicly on GitHub.

## Required response language
Respond entirely in English.

## First step: discovery
Before building the program, ask me up to 7 focused discovery questions to personalize the course. The questions must cover at least:
1. Primary languages and stack
2. Project type (web app, backend, automation, data, enterprise, security, etc.)
3. Current skill level with GitHub Copilot and VS Code
4. Time available per week
5. Operating system
6. Repository size and complexity
7. Final practical goal (personal productivity, team standardization, faster delivery, higher quality, architecture discipline, etc.)

After asking the questions, do not stop. If some information is missing, make reasonable assumptions, but state them clearly.

## Core requirement: build this as a GitHub-open-course repository
The output must be designed as a public GitHub repository with:
- a clear course identity
- a professional structure
- a beginner-friendly entry point
- modular content
- hands-on labs
- reusable templates
- contributor guidance
- roadmap and versioning logic
- a format suitable for open publication

## The repository must include a proposed structure
Design the course as a GitHub repository and provide a recommended structure such as:
- README.md
- COURSE_OVERVIEW.md
- SYLLABUS.md
- LEARNING_PATH.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- LICENSE recommendation
- CHANGELOG.md
- /docs
- /modules
- /labs
- /templates
- /examples
- /checklists
- /assets
- /faq
- /prompts
- /instructions
- /agents
- /capstone
- /.github with issue templates, discussion guidance, PR templates if appropriate

If useful, propose a better structure, but explain why.

## Course design requirements
I want the learning program organized into progressive phases:
- beginner
- intermediate
- advanced
- expert

For each phase, include:
- learning objectives
- practical skills to acquire
- relevant GitHub Copilot Pro+ and VS Code features
- recommended configuration
- step-by-step exercises
- common mistakes
- best practices to minimize wasted context/tokens/premium requests
- completion criteria
- concrete deliverables (files, configurations, checklists, workflows, mini-projects)

## Mandatory topics to cover
Build the full course and repository content so that it explicitly covers all the following topics.

### 1) Foundations
- installation, authentication, activation, and environment verification in VS Code
- key Copilot settings in VS Code
- differences between inline completion, inline chat, Ask, Plan, and Agent modes (according to the current official feature set; Edit mode was consolidated into Agent in VS Code 1.110)
- when to use each mode
- how to evaluate AI output critically instead of trusting it blindly

### 2) Optimal configuration
- ideal VS Code setup for productive Copilot usage
- useful extensions to combine with Copilot
- settings for productivity and code quality
- how to structure a project to help Copilot understand context
- naming conventions, file organization, documentation baseline, testing, linting, and task automation

### 3) Token / premium request optimization
- explain operationally what consumes more and what consumes less
- how to reduce unnecessary requests
- strategies to use context efficiently
- how to write compact but complete prompts
- when to use included models vs premium models
- how to avoid useless loops with agents
- how to estimate the operational cost of different workflows
- create a decision framework: which mode/model to use depending on task type

### 4) Prompt engineering for coding assistance
- how to write effective prompts for:
  - code generation
  - refactoring
  - debugging
  - testing
  - documentation
  - review
  - security review
  - migration
- create reusable prompt templates
- create a prompt library for real scenarios
- explain prompting patterns and anti-patterns

### 5) Persistent customization
- how to design project-level custom instructions
- how to create stable guidance for Copilot
- how to structure instructions for coding style, architecture, testing, security, naming, and documentation
- when to use global, repository-wide, path-specific, and agent-specific instruction files using the current official naming and conventions
- provide examples of well-designed instruction files

### 6) Agents and role specialization
I want to learn how to use different agents/personas for different roles. Create a dedicated deep section for:
- planner / analyst
- solution architect
- implementer / developer
- refactoring specialist
- code reviewer
- security reviewer
- test engineer
- documentation writer
- performance optimizer
- release / devops assistant

For each role, provide:
- purpose
- when to use it
- ideal starting prompt
- suggested tool permissions
- expected outputs
- main risks
- criteria for handing work off to another agent/persona
- an example of a role handoff

### 7) Multi-agent workflows
- show how to orchestrate multiple agents on a complex task
- explain how to decompose a large problem into smaller tasks
- explain how to avoid duplication, polluted context, and wasted requests
- create at least 3 complete workflows:
  1. new feature delivery
  2. complex bug fixing
  3. refactoring + testing + review

### 8) Advanced features
- AI-assisted code review
- planning before implementation
- agent sessions
- local / background / cloud execution if available in the current official feature set
- terminal / CLI integration if available
- integration with code quality tools
- use with test runners, linting, formatting, and CI/CD
- context management on large repositories
- secure usage patterns for sensitive codebases

### 9) Project efficiency and repository quality
- how to keep a repository AI-friendly
- how to reduce noise and ambiguity for Copilot
- how to write README files, technical docs, task lists, and issues in an AI-useful way
- how to use AI without degrading architectural quality
- personal governance for AI-generated code
- human validation checklist before commit / merge

### 10) Practical adoption roadmap
Design an adoption plan in:
- 7 days
- 30 days
- 60 days
- 90 days

For each timeframe include:
- focus
- daily or weekly routine
- milestones
- KPIs
- exercises
- outputs to produce
- mistakes to fix

## Open-course publishing requirements
The result must not be only a learning plan. It must also be a publishing-ready GitHub course blueprint.

Therefore include:
- repository positioning and audience
- suggested repository description
- suggested tagline
- naming options for the repository
- folder structure
- documentation hierarchy
- course navigation flow
- module dependency map
- lab progression
- beginner onboarding path
- maintainer workflow
- contribution model
- issue/discussion usage recommendations
- release/versioning suggestion
- optional GitHub Pages / static documentation recommendation if appropriate
- how to keep the repository easy to maintain over time

## Labs and hands-on assets
The repository must include a full lab strategy.

For each lab provide:
- title
- learning objective
- prerequisites
- estimated time
- starter files
- expected outputs
- success criteria
- common failure points
- review checklist
- extension ideas

Also define:
- lab difficulty progression
- standalone labs vs sequential labs
- validation method
- optional self-assessment rubric

## Required deliverables in the final answer
Return the result in the following structure:

1. Executive summary of the course and repository
2. Assumptions made
3. Target audience and learner personas
4. Skills matrix: current state → target outcomes
5. Recommended GitHub repository strategy
6. Proposed repository structure
7. Documentation map
8. Full curriculum by level (beginner/intermediate/advanced/expert)
9. For each module:
   - goal
   - essential theory
   - practical procedure
   - exercises
   - checklist
   - quality indicators
   - suggestions to reduce premium/token consumption
   - files to include in the repository
10. Prompt library ready to publish
11. Custom instructions examples
12. Agent/persona definitions
13. Multi-agent workflow blueprints
14. Labs catalog
15. 7/30/60/90-day adoption plan
16. Common mistakes and how to avoid them
17. Final operational maturity checklist
18. “Start today” minimal path
19. Ultra-compact cheat sheet
20. Do / Don’t table

## Additional repository-ready artifacts to generate
In addition to the curriculum, generate examples or templates for:
- README.md
- COURSE_OVERVIEW.md
- SYLLABUS.md
- CONTRIBUTING.md
- one sample module README
- one sample lab README
- one sample prompt template file
- one sample custom instructions file
- one sample agent definition file
- one sample issue template
- one sample pull request template
- one sample learner progress checklist

These do not need to be fully exhaustive unless requested, but they should be realistic and publication-ready.

## Constraints
- Do not stay theoretical: teach operationally.
- If a feature can vary by plan, version, editor build, or rollout status, verify the current status using official GitHub and VS Code sources and state it clearly.
- Always highlight practices that reduce premium request usage and those that increase it.
- Propose sustainable conventions for small, medium, and large repositories.
- When suggesting files or configs, include practical examples.
- When suggesting agents, define boundaries, responsibilities, and handoffs clearly.
- Prefer realistic professional workflows.
- Use tables, checklists, templates, and structured outputs where useful.
- Ensure the result is suitable for publication as an open GitHub course.
- Conclude with a “minimum viable public course version” that I can publish first and expand later.

## Extra requested output
At the end, also include:
- an ultra-compact “GitHub Copilot Pro+ in VS Code” cheat sheet
- a Do / Don’t table
- 10 real exercises ordered by increasing difficulty
- one capstone mini-project proposal
- one suggested milestone plan for maintainers evolving the repository over time