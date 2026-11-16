<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
# Weekly Status - Week 15
<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Luis Fernando Claros Ramos
- GITHUB_USER: luisfclaros
- TEAM: Group 1
- SPRINT_GOAL: Prepare controlled load and resilience experiments for the running RedFish application and document their safe execution.
<!-- CONFIG-END -->
## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| OPS-W15-001 | Prepare a read-only k6 load test for health and optional product endpoints | doing | https://github.com/luisfclaros/RedFish/pull/51 |
| OPS-W15-002 | Document a controlled MySQL interruption and recovery procedure for an isolated local/QA environment | doing | https://github.com/luisfclaros/RedFish/pull/51 |
| OPS-W15-003 | Define measurable acceptance thresholds for latency and error rate without presenting provisional values as approved SLOs | doing | https://github.com/luisfclaros/RedFish/pull/51 |
## 2. My individual contribution
- Prepared a k6 script for read-only load checks against /actuator/health and optionally /api/v1/products using a test account.
- Added configurable p95 latency and error-rate thresholds, explicitly identified as provisional defaults.
- Prepared a runbook for interrupting and restoring MySQL in an isolated local/QA environment without deleting persistent volumes.
- Documented that the experiment targets a dependency of the current modular monolith and does not pretend to simulate unavailable microservices.
## 3. Blockers and risks
- The k6 experiment has not been recorded as executed with a result and commit SHA.
- The controlled failure/recovery procedure still requires execution in a disposable environment and evidence of recovery and data consistency.
- The related pull request remains open and in draft; no successful experiment or approved SLO is claimed.
## 4. Plan for next week
- Complete the integrated MVP 3 demonstration and delivery package.
- Run the prepared experiments only in a safe isolated environment and attach actual results.
## 5. Compliance self-check
- [x] Conventional Commits used
- [x] Experiment scripts and runbook prepared in a feature branch / PR
- [x] Acceptance thresholds are configurable and explicitly provisional
- [ ] Load experiment executed and results recorded
- [ ] Failure/recovery experiment executed and results recorded
- [x] No destructive volume deletion; no secrets committed
## 6. Evidence links
- Week 15 load and resilience PR: https://github.com/luisfclaros/RedFish/pull/51
