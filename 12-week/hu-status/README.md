<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
# Weekly Status - Week 12
<!-- CONFIG-START -->
- FULL_NAME: Luis Fernando Claros Ramos
- GITHUB_USER: luisfclaros
- TEAM: Group 1
- SPRINT_GOAL: Document and verify a repeatable Docker Compose deployment and local operating procedure for RedFish.
<!-- CONFIG-END -->
## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| DEVOPS-W12-001 | Document the current Java 17, Spring Boot, Gradle, and MySQL deployment baseline | done | https://github.com/code-corhuila/redfish-docs/blob/main/10-devops/week-12-deployment.md |
| DEVOPS-W12-002 | Define local startup, environment configuration, health verification, and safe data-volume handling | done | https://github.com/code-corhuila/redfish-docs/blob/main/10-devops/local-setup.md |
| DEVOPS-W12-003 | Run the application and database through Docker Compose and verify application health | done | https://github.com/luisfclaros/RedFish/pull/50 |
## 2. My individual contribution
- Documented the actual RedFish execution baseline: Java 17, Spring Boot, Gradle, MySQL, Docker, and Docker Compose.
- Documented application/database startup, environment variables, local ports, health verification, and operational cautions.
- Ran the local Compose build and startup; application and MySQL became available and Actuator health reported UP during local verification.
- Preserved the database volume; destructive volume removal is excluded from the operating procedure.
## 3. Blockers and risks
- A successful local Compose deployment does not prove cloud or production deployment, high availability, or zero-downtime release.
- Remote environment URLs and credentials must be supplied by the environment owner; none are invented here.
## 4. Plan for next week
- Continue security and quality checks, keeping implementation status aligned with documentation.
## 5. Compliance self-check
- [x] Conventional Commits used in related project work
- [ ] Per-environment HU branch + PR — not independently evidenced for this report
- [x] Testable startup and health-check criteria documented
- [x] Local build and health verification performed
- [x] Architecture limitations documented honestly
- [x] No secrets; configuration via environment variables
## 6. Evidence links
- Deployment procedure: https://github.com/code-corhuila/redfish-docs/blob/main/10-devops/week-12-deployment.md
- Local setup: https://github.com/code-corhuila/redfish-docs/blob/main/10-devops/local-setup.md
- Integrated application PR: https://github.com/luisfclaros/RedFish/pull/50
