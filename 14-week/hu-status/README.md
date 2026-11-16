<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
# Weekly Status - Week 14
<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Luis Fernando Claros Ramos
- GITHUB_USER: luisfclaros
- TEAM: Group 1
- SPRINT_GOAL: Establish automated CI/CD quality gates and expand automated test coverage for RedFish.
<!-- CONFIG-END -->
## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| CI-W14-001 | Add GitHub Actions build and test workflow using Java 17 and Gradle | doing | https://github.com/luisfclaros/RedFish/pull/48 |
| CI-W14-002 | Generate JaCoCo coverage reports and add static analysis with CodeQL | doing | https://github.com/luisfclaros/RedFish/pull/48 |
| CI-W14-003 | Add vulnerability, configuration, and secret scanning with Trivy | doing | https://github.com/luisfclaros/RedFish/pull/48 |
| TEST-W14-001 | Expand domain and JPA adapter tests for users, roles, vehicles, products, and customers | done | https://github.com/luisfclaros/RedFish/pull/49 |
## 2. My individual contribution
- Prepared CI/CD quality gates: Java 17 / Gradle build and test workflow, JaCoCo reporting, CodeQL static analysis, and Trivy scanning.
- Added tests covering User and Role domain behavior, Vehicle validation and assignment, Product and Customer JPA mappings, and Spring Data adapter operations.
- Documented limitations of the current monolith and quality gates requiring environment configuration or additional verification.
- Kept the work in feature branches and pull requests rather than claiming direct promotion to protected environments.
## 3. Blockers and risks
- PR #48 remains open and unmerged; branch protection, QA smoke tests, and image publication still require configuration and verification.
- PR #49 is closed but not merged; it is based on the Week 14 feature branch and is not integrated into main.
- Spring context testing requiring Docker/Testcontainers was identified as a separate validation limitation.
## 4. Plan for next week
- Prepare controlled load and resilience experiments against the real running application.
- Record actual execution evidence and distinguish proposed thresholds from approved SLOs.
## 5. Compliance self-check
- [x] Conventional Commits used
- [x] Work separated into feature/test branches and PRs
- [x] Test coverage added for domain and persistence adapter behavior
- [x] CI/CD and quality gates documented
- [x] DDD / hexagonal boundaries considered in test scope
- [x] No secrets committed
## 6. Evidence links
- CI/CD quality gates PR: https://github.com/luisfclaros/RedFish/pull/48
- Additional tests PR: https://github.com/luisfclaros/RedFish/pull/49
